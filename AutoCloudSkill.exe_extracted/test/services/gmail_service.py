# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: services\gmail_service.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
Service untuk integrasi dengan Gmail API
"""
import os
import base64
import logging
from typing import List, Dict, Optional, Any
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from utils.logger import setup_logger

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

class GmailService:
    """Service untuk akses Gmail API"""

    def __init__(self, credentials_path: str = None, token_path: str = None, logger: logging.Logger = None):
        """
        Initialize Gmail service

        Args:
            credentials_path: Path ke credentials.json (OAuth client)
            token_path: Path ke token.json (user token)
            logger: Logger instance
        """
        self.credentials_path = credentials_path or os.path.join(os.getcwd(), 'credentials.json')
        self.token_path = token_path or self.get_default_token_path()
        self.logger = logger or setup_logger('GmailService')

    @staticmethod
    def get_default_token_path() -> str:
        """
        Lokasi default token.json di folder user-writable.
        Prioritas: %LOCALAPPDATA%\\AutoCloudSkill\\google\\token.json, fallback ke Home/AppData/Local.
        """
        base = None
        try:
            base = os.environ.get('LOCALAPPDATA')
        except Exception:
            base = None
        if not base:
            try:
                base = os.path.join(os.path.expanduser('~'), 'AppData', 'Local')
            except Exception:
                base = os.getcwd()
        token_dir = os.path.join(base, 'AutoCloudSkill', 'google')
        return os.path.join(token_dir, 'token.json')

    def _get_credentials(self) -> Credentials:
        creds = None
        if os.path.exists(self.token_path):
            creds = Credentials.from_authorized_user_file(self.token_path, SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                except Exception as e:
                    self.logger.warning(f'Gagal refresh token: {e}')
                    creds = None
            if not creds:
                if not os.path.exists(self.credentials_path):
                    raise FileNotFoundError(f'credentials.json tidak ditemukan di {self.credentials_path}. Silakan letakkan file OAuth client di path tersebut.')
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)
            try:
                os.makedirs(os.path.dirname(self.token_path), exist_ok=True)
                with open(self.token_path, 'w', encoding='utf-8') as token:
                    token.write(creds.to_json())
            except Exception:
                pass
        return creds

    def is_authenticated(self) -> bool:
        """
        Cek apakah sudah ter-autentikasi ke Gmail

        Returns:
            True jika sudah autentikasi, False jika belum
        """
        try:
            creds = self._get_credentials()
            return creds and creds.valid
        except Exception:
            return False

    def search_emails(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """
        Cari email berdasarkan query Gmail (mis. to:, from:, subject:, newer_than:).
        Contoh query:
          - f\"to:{target_email} subject:Welcome newer_than:1d\"
          - f\"from:noreply@cloudskillsboost.google newer_than:1d\"
        """
        try:
            creds = self._get_credentials()
            service = build('gmail', 'v1', credentials=creds)

            results = service.users().messages().list(userId='me', q=query, maxResults=max_results).execute()
            messages = results.get('messages', [])

            emails = []
            for msg in messages:
                full_msg = service.users().messages().get(userId='me', id=msg['id']).execute()
                emails.append(self._parse_message(full_msg))

            return emails
        except HttpError as error:
            self.logger.error(f'Gmail API error: {error}')
            return []
        except Exception as error:
            self.logger.error(f'Error searching emails: {error}')
            return []

    def _decode_base64url(self, data: str) -> bytes:
        """Decode base64url string ke bytes."""
        data += '=' * (4 - len(data) % 4)
        return base64.urlsafe_b64decode(data)

    def _parse_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """Ekstrak text/plain dan text/html dari payload message."""
        payload = message.get('payload', {})
        headers = {h['name']: h['value'] for h in payload.get('headers', [])}

        text = None
        html = None

        def extract_parts(part):
            nonlocal html
            nonlocal text

            if part.get('mimeType') == 'text/plain':
                data = part.get('body', {}).get('data')
                if data:
                    text = self._decode_base64url(data).decode('utf-8', errors='ignore')
            elif part.get('mimeType') == 'text/html':
                data = part.get('body', {}).get('data')
                if data:
                    html = self._decode_base64url(data).decode('utf-8', errors='ignore')

            if 'parts' in part:
                for subpart in part['parts']:
                    extract_parts(subpart)

        if payload.get('mimeType') == 'text/plain':
            data = payload.get('body', {}).get('data')
            if data:
                text = self._decode_base64url(data).decode('utf-8', errors='ignore')
        elif payload.get('mimeType') == 'text/html':
            data = payload.get('body', {}).get('data')
            if data:
                html = self._decode_base64url(data).decode('utf-8', errors='ignore')
        else:
            extract_parts(payload)

        return {
            'id': message['id'],
            'thread_id': message.get('threadId'),
            'subject': headers.get('Subject', ''),
            'from': headers.get('From', ''),
            'to': headers.get('To', ''),
            'date': headers.get('Date', ''),
            'text': text,
            'html': html,
            'headers': headers
        }

if __name__ == '__main__':
    gmail = GmailService()
    print(f'Gmail service initialized. Authenticated: {gmail.is_authenticated()}')
    if gmail.is_authenticated():
        emails = gmail.search_emails('is:unread', max_results=5)
        print(f'Found {len(emails)} unread emails')