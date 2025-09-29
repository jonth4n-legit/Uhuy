"""
Gmail API service untuk membaca email masuk dan mencari email konfirmasi.

Prasyarat:
1) Buat OAuth Client ID (Desktop) di Google Cloud Console dan unduh credentials.json
2) Letakkan credentials.json di root proyek atau tentukan via GmailService(credentials_path=...)
3) Pertama kali dijalankan akan membuka flow OAuth di browser dan menyimpan token.json
   - token.json akan digunakan otomatis untuk run berikutnya.
"""
from __future__ import annotations
import base64
import os
import time
from typing import List, Optional, Tuple, Dict, Any

from googleapiclient.discovery import build, build_from_document
from googleapiclient.errors import HttpError, UnknownApiNameOrVersion
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from bs4 import BeautifulSoup

from utils.logger import setup_logger

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


class GmailService:
    def __init__(self, credentials_path: Optional[str] = None, token_path: Optional[str] = None, logger=None) -> None:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.credentials_path = credentials_path or os.path.join(project_root, 'credentials.json')
        self.token_path = token_path or self.get_default_token_path()
        self._service = None
        self.logger = logger or setup_logger('GmailService')

    @staticmethod
    def get_default_token_path() -> str:
        """Lokasi default token.json di folder user-writable."""
        base = os.environ.get('LOCALAPPDATA')
        if not base:
            try:
                base = os.path.join(os.path.expanduser('~'), 'AppData', 'Local')
            except Exception:
                base = os.getcwd()
        token_dir = os.path.join(base, 'AutoCloudSkill', 'google')
        return os.path.join(token_dir, 'token.json')

    def _get_credentials(self) -> Credentials:
        creds: Optional[Credentials] = None
        if os.path.exists(self.token_path):
            try:
                creds = Credentials.from_authorized_user_file(self.token_path, SCOPES)
            except Exception:
                creds = None
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                except Exception as e:
                    self.logger.warning(f'Gagal refresh token: {e}')
                    creds = None
            if not creds:
                if not os.path.exists(self.credentials_path):
                    raise FileNotFoundError(
                        f'credentials.json tidak ditemukan di {self.credentials_path}. '
                        f'Silakan letakkan file OAuth client di path tersebut.'
                    )
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)
            # Persist token
            try:
                os.makedirs(os.path.dirname(self.token_path), exist_ok=True)
                with open(self.token_path, 'w', encoding='utf-8') as token:
                    token.write(creds.to_json())
            except Exception as e:
                self.logger.warning(f'Tidak bisa menyimpan token ke {self.token_path}: {e}')
        return creds

    def get_service(self):
        if self._service is None:
            creds = self._get_credentials()
            try:
                self._service = build('gmail', 'v1', credentials=creds)
            except UnknownApiNameOrVersion as e:
                # Fallback to local discovery document if needed
                doc_paths = []
                try:
                    import googleapiclient  # type: ignore
                    pkg_dir = os.path.dirname(googleapiclient.__file__)
                    doc_paths.append(os.path.join(pkg_dir, 'discovery_cache', 'documents', 'gmail.v1.json'))
                except Exception:
                    pass
                here = os.path.dirname(os.path.abspath(__file__))
                doc_paths.append(os.path.join(here, '..', 'googleapiclient', 'discovery_cache', 'documents', 'gmail.v1.json'))
                doc_paths.append(os.path.join(here, '..', '..', 'googleapiclient', 'discovery_cache', 'documents', 'gmail.v1.json'))
                doc_json = None
                for p in doc_paths:
                    try:
                        p_norm = os.path.normpath(p)
                        if os.path.exists(p_norm):
                            with open(p_norm, 'r', encoding='utf-8') as f:
                                doc_json = f.read()
                                break
                    except Exception:
                        continue
                if not doc_json:
                    raise e
                try:
                    self._service = build_from_document(doc_json, credentials=creds)
                except Exception:
                    raise e
        return self._service

    def search_messages(self, query: str, max_results: int = 10, user_id: str = 'me') -> List[Dict[str, Any]]:
        service = self.get_service()
        try:
            resp = service.users().messages().list(userId=user_id, q=query, maxResults=max_results).execute()
            return resp.get('messages', [])
        except HttpError as e:
            self.logger.error(f'Gmail API error saat search_messages: {e}')
            return []

    def get_message(self, msg_id: str, user_id: str = 'me') -> Optional[Dict[str, Any]]:
        service = self.get_service()
        try:
            return service.users().messages().get(userId=user_id, id=msg_id, format='full').execute()
        except HttpError as e:
            self.logger.error(f'Gmail API error saat get_message: {e}')
            return None

    def _decode_part(self, data: str) -> bytes:
        data = data.replace('-', '+').replace('_', '/')
        missing = len(data) % 4
        if missing:
            data += '=' * (4 - missing)
        return base64.b64decode(data)

    def _extract_text_and_html(self, payload: Dict[str, Any]) -> Tuple[str, str]:
        text = ''
        html = ''

        def walk(parts):
            nonlocal text, html
            for p in parts or []:
                mime = (p.get('mimeType') or '').lower()
                if mime.startswith('multipart/'):
                    walk(p.get('parts') or [])
                    continue
                body = p.get('body', {})
                data = body.get('data')
                if not data:
                    continue
                try:
                    raw = self._decode_part(data)
                except Exception:
                    continue
                if mime == 'text/plain':
                    try:
                        text += raw.decode(errors='ignore')
                    except Exception:
                        pass
                elif mime == 'text/html':
                    try:
                        html += raw.decode(errors='ignore')
                    except Exception:
                        pass

        if (payload.get('mimeType') or '').lower().startswith('multipart/'):
            walk(payload.get('parts') or [])
        else:
            body = payload.get('body', {})
            data = body.get('data')
            if data:
                try:
                    raw = self._decode_part(data)
                    mime = (payload.get('mimeType') or '').lower()
                    if mime == 'text/plain':
                        text += raw.decode(errors='ignore')
                    elif mime == 'text/html':
                        html += raw.decode(errors='ignore')
                except Exception:
                    pass
        return (text, html)

    def extract_message_content(self, message: Dict[str, Any]) -> Tuple[str, str]:
        payload = message.get('payload', {})
        return self._extract_text_and_html(payload)

    def extract_links(self, message: Dict[str, Any]) -> List[str]:
        text, html = self.extract_message_content(message)
        links: List[str] = []
        if html:
            try:
                soup = BeautifulSoup(html, 'html.parser')
                for a in soup.find_all('a', href=True):
                    links.append(a['href'])
            except Exception:
                pass
        for part in (text or '').split():
            if part.startswith('http://') or part.startswith('https://'):
                links.append(part)
        seen = set()
        uniq_links = []
        for u in links:
            if u not in seen:
                seen.add(u)
                uniq_links.append(u)
        return uniq_links

    def wait_for_email(
        self,
        target_email: str,
        subject_contains: Optional[str] = None,
        from_contains: Optional[str] = None,
        newer_than: str = '2d',
        timeout_sec: int = 180,
        poll_interval_sec: int = 5,
        max_results: int = 10,
    ) -> Optional[Dict[str, Any]]:
        """Polling sampai email yang sesuai ditemukan."""
        base = [f'newer_than:{newer_than}']
        if subject_contains:
            base.append(f'subject:{subject_contains}')
        if from_contains:
            base.append(f'from:{from_contains}')
        is_relay_addr = target_email and ('mozmail.com' in target_email or 'relay.firefox' in target_email)
        queries: List[str] = []
        if target_email and (not is_relay_addr):
            queries.append('in:anywhere ' + ' '.join([f'to:{target_email}'] + base))
        queries.append(f"in:anywhere {' '.join(base)}")
        if subject_contains:
            queries.append('in:anywhere ' + ' '.join([f'newer_than:{newer_than}', f'subject:{subject_contains}']))
        if from_contains:
            queries.append('in:anywhere ' + ' '.join([f'newer_than:{newer_than}', f'from:{from_contains}']))
        queries.append('in:anywhere ' + ' '.join([f'newer_than:{newer_than}', 'has:link']))

        try:
            self.logger.info('Gmail query variants:')
            for i, q in enumerate(queries, 1):
                self.logger.info(f'  q{i}: {q}')
        except Exception:
            pass

        end = time.time() + max(1, int(timeout_sec))
        last_ids = set()
        attempt = 0
        while time.time() < end:
            attempt += 1
            remaining = int(end - time.time())
            try:
                q_idx = (attempt - 1) % max(1, len(queries))
                q = queries[q_idx]
                self.logger.info(f'Gmail polling attempt={attempt} remaining={remaining}s | query={q}')
            except Exception:
                q = queries[0] if queries else 'in:anywhere newer_than:2d'
            msgs = self.search_messages(query=q, max_results=max_results)
            try:
                self.logger.info(f'Gmail polling returned {len(msgs)} message refs')
            except Exception:
                pass
            for m in msgs:
                mid = m.get('id')
                if not mid or mid in last_ids:
                    continue
                last_ids.add(mid)
                full = self.get_message(mid)
                if full:
                    try:
                        te = (target_email or '').strip().lower()
                        if te:
                            text_c, html_c = self.extract_message_content(full)
                            blob = (text_c or '') + '\n' + (html_c or '')
                            blob_l = blob.lower()
                            te_enc = te.replace('@', '%40')
                            has_ref = (te in blob_l) or (te_enc in blob_l)
                            if has_ref:
                                return full
                            try:
                                self.logger.info(f'Skip message {mid}: does not reference target relay {te}')
                            except Exception:
                                pass
                    except Exception:
                        pass
            time.sleep(max(1, int(poll_interval_sec)))
        return None


if __name__ == '__main__':
    svc = GmailService()
    msg = svc.wait_for_email(
        target_email='your.email@gmail.com',
        subject_contains='Welcome to Google Cloud Skills Boost',
        from_contains='noreply@cloudskillsboost.google',
        timeout_sec=60,
        poll_interval_sec=5,
    )
    if msg:
        text, html = svc.extract_message_content(msg)
        links = svc.extract_links(msg)
        print('Found email. Links:', links[:5])
    else:
        print('No email found in time.')