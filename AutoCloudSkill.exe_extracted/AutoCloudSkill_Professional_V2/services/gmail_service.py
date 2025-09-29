"""
Professional Gmail service for AutoCloudSkill.

This module provides comprehensive Gmail API integration:
- OAuth 2.0 authentication with secure token management
- Email reading and monitoring
- Email search with advanced filters
- HTML content parsing and text extraction
- Automatic credential refresh
- Cross-platform token storage

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import os
import time
import base64
import json
import logging
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple, Union
from dataclasses import dataclass
from datetime import datetime, timedelta
from html import unescape

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

from utils.logger import setup_application_logging, log_automation_step, performance_monitor
from config.settings import settings

logger = setup_application_logging('GmailService')

# Gmail API scopes
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.modify'
]

@dataclass
class EmailMessage:
    """Gmail message representation."""
    id: str
    thread_id: str
    subject: str
    sender: str
    recipient: str
    date: str
    snippet: str
    body_text: str
    body_html: str
    labels: List[str]
    is_unread: bool
    attachments: List[Dict[str, Any]]

    @classmethod
    def from_gmail_message(cls, message_data: Dict[str, Any], service) -> 'EmailMessage':
        """Create EmailMessage from Gmail API response."""
        headers = {h['name']: h['value'] for h in message_data['payload'].get('headers', [])}

        # Extract body content
        body_text, body_html = cls._extract_body_content(message_data['payload'])

        # Extract attachments
        attachments = cls._extract_attachments(message_data['payload'])

        return cls(
            id=message_data['id'],
            thread_id=message_data['threadId'],
            subject=headers.get('Subject', ''),
            sender=headers.get('From', ''),
            recipient=headers.get('To', ''),
            date=headers.get('Date', ''),
            snippet=message_data.get('snippet', ''),
            body_text=body_text,
            body_html=body_html,
            labels=message_data.get('labelIds', []),
            is_unread='UNREAD' in message_data.get('labelIds', []),
            attachments=attachments
        )

    @staticmethod
    def _extract_body_content(payload: Dict[str, Any]) -> Tuple[str, str]:
        """Extract text and HTML body content from message payload."""
        body_text = ""
        body_html = ""

        def extract_parts(part):
            nonlocal body_text, body_html

            if part.get('mimeType') == 'text/plain':
                data = part.get('body', {}).get('data', '')
                if data:
                    decoded = base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
                    body_text += decoded

            elif part.get('mimeType') == 'text/html':
                data = part.get('body', {}).get('data', '')
                if data:
                    decoded = base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
                    body_html += decoded

            # Recursively process multipart messages
            if part.get('parts'):
                for subpart in part['parts']:
                    extract_parts(subpart)

        extract_parts(payload)
        return body_text.strip(), body_html.strip()

    @staticmethod
    def _extract_attachments(payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract attachment information from message payload."""
        attachments = []

        def extract_attachment_parts(part):
            if part.get('filename') and part.get('body', {}).get('attachmentId'):
                attachments.append({
                    'filename': part['filename'],
                    'mimeType': part.get('mimeType', ''),
                    'size': part.get('body', {}).get('size', 0),
                    'attachmentId': part['body']['attachmentId']
                })

            if part.get('parts'):
                for subpart in part['parts']:
                    extract_attachment_parts(subpart)

        extract_attachment_parts(payload)
        return attachments

    def get_plain_text(self) -> str:
        """Get plain text version of email body."""
        if self.body_text:
            return self.body_text

        # Convert HTML to text if no plain text available
        if self.body_html and BS4_AVAILABLE:
            soup = BeautifulSoup(self.body_html, 'html.parser')
            return soup.get_text(separator=' ', strip=True)

        return self.snippet

    def search_content(self, pattern: str, case_sensitive: bool = False) -> List[str]:
        """
        Search for pattern in email content.

        Args:
            pattern: Search pattern
            case_sensitive: Whether search is case sensitive

        Returns:
            List of matching text segments
        """
        import re

        flags = 0 if case_sensitive else re.IGNORECASE
        content = f"{self.subject} {self.get_plain_text()}"

        matches = re.findall(pattern, content, flags)
        return matches

class GmailService:
    """Professional Gmail service with comprehensive features."""

    def __init__(
        self,
        credentials_path: Optional[str] = None,
        token_path: Optional[str] = None,
        scopes: Optional[List[str]] = None
    ):
        """
        Initialize Gmail service.

        Args:
            credentials_path: Path to OAuth credentials JSON file
            token_path: Path to store/load authentication token
            scopes: Gmail API scopes to request

        Raises:
            FileNotFoundError: If credentials file is not found
        """
        self.scopes = scopes or SCOPES
        self.credentials_path = credentials_path or self._get_default_credentials_path()
        self.token_path = token_path or self._get_default_token_path()

        self._service = None
        self._credentials = None

        logger.info("Gmail service initialized")

    def _get_default_credentials_path(self) -> str:
        """Get default path for OAuth credentials file."""
        # Check current directory first
        local_path = Path.cwd() / 'credentials.json'
        if local_path.exists():
            return str(local_path)

        # Check config directory
        config_dir = self._get_config_directory()
        config_path = config_dir / 'credentials.json'
        return str(config_path)

    def _get_default_token_path(self) -> str:
        """Get default path for authentication token."""
        config_dir = self._get_config_directory()
        return str(config_dir / 'gmail_token.json')

    def _get_config_directory(self) -> Path:
        """Get configuration directory for Gmail service."""
        if os.name == 'nt':  # Windows
            base_dir = os.environ.get('LOCALAPPDATA') or Path.home() / 'AppData' / 'Local'
        else:  # Unix-like
            base_dir = os.environ.get('XDG_CONFIG_HOME') or Path.home() / '.config'

        config_dir = Path(base_dir) / 'AutoCloudSkill' / 'gmail'
        config_dir.mkdir(parents=True, exist_ok=True)
        return config_dir

    def _get_credentials(self) -> Credentials:
        """
        Get valid Gmail API credentials.

        Returns:
            Valid credentials object

        Raises:
            FileNotFoundError: If credentials file is not found
        """
        creds = None

        # Load existing token
        if os.path.exists(self.token_path):
            try:
                creds = Credentials.from_authorized_user_file(self.token_path, self.scopes)
                logger.debug("Loaded existing credentials")
            except Exception as e:
                logger.warning(f"Failed to load existing token: {e}")

        # Refresh expired credentials
        if creds and creds.expired and creds.refresh_token:
            try:
                logger.info("Refreshing expired credentials")
                creds.refresh(Request())
                logger.info("Credentials refreshed successfully")
            except Exception as e:
                logger.warning(f"Failed to refresh credentials: {e}")
                creds = None

        # Create new credentials if needed
        if not creds or not creds.valid:
            if not os.path.exists(self.credentials_path):
                raise FileNotFoundError(
                    f"Gmail credentials file not found: {self.credentials_path}\n"
                    "Please:\n"
                    "1. Create OAuth 2.0 Client ID in Google Cloud Console\n"
                    "2. Download credentials.json file\n"
                    "3. Place it at the specified path"
                )

            logger.info("Starting OAuth flow for new credentials")
            flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, self.scopes)

            # Try to run local server, fallback to console flow
            try:
                creds = flow.run_local_server(port=0, open_browser=True)
            except Exception as e:
                logger.warning(f"Local server OAuth failed, using console: {e}")
                creds = flow.run_console()

            # Save credentials
            try:
                os.makedirs(os.path.dirname(self.token_path), exist_ok=True)
                with open(self.token_path, 'w', encoding='utf-8') as token_file:
                    token_file.write(creds.to_json())
                logger.info(f"Credentials saved to {self.token_path}")
            except Exception as e:
                logger.warning(f"Failed to save credentials: {e}")

        self._credentials = creds
        return creds

    @performance_monitor("gmail_service_build")
    def get_service(self):
        """
        Get Gmail API service object.

        Returns:
            Gmail API service instance
        """
        if self._service is None:
            creds = self._get_credentials()
            try:
                self._service = build('gmail', 'v1', credentials=creds, cache_discovery=False)
                logger.info("Gmail API service created successfully")
            except Exception as e:
                logger.error(f"Failed to create Gmail service: {e}")
                raise

        return self._service

    @performance_monitor("search_emails")
    def search_emails(
        self,
        query: str,
        max_results: int = 10,
        include_spam_trash: bool = False
    ) -> List[EmailMessage]:
        """
        Search emails using Gmail search syntax.

        Args:
            query: Gmail search query (e.g., "from:example.com subject:confirmation")
            max_results: Maximum number of results to return
            include_spam_trash: Include spam and trash messages

        Returns:
            List of EmailMessage objects
        """
        log_automation_step(
            logger,
            "search_emails",
            "START",
            {"query": query, "max_results": max_results}
        )

        try:
            service = self.get_service()

            # Search for messages
            search_result = service.users().messages().list(
                userId='me',
                q=query,
                maxResults=max_results,
                includeSpamTrash=include_spam_trash
            ).execute()

            messages = search_result.get('messages', [])
            email_messages = []

            # Get full message details
            for message in messages:
                try:
                    full_message = service.users().messages().get(
                        userId='me',
                        id=message['id'],
                        format='full'
                    ).execute()

                    email_message = EmailMessage.from_gmail_message(full_message, service)
                    email_messages.append(email_message)

                except Exception as e:
                    logger.warning(f"Failed to get message {message['id']}: {e}")

            log_automation_step(
                logger,
                "search_emails",
                "SUCCESS",
                {"found_count": len(email_messages)}
            )

            logger.info(f"Found {len(email_messages)} emails matching query: {query}")
            return email_messages

        except HttpError as e:
            log_automation_step(
                logger,
                "search_emails",
                "ERROR",
                {"error": str(e)}
            )
            logger.error(f"Gmail API error: {e}")
            return []

        except Exception as e:
            log_automation_step(
                logger,
                "search_emails",
                "ERROR",
                {"error": str(e)}
            )
            logger.error(f"Failed to search emails: {e}")
            return []

    def get_recent_emails(
        self,
        hours: int = 1,
        sender_filter: Optional[str] = None,
        subject_filter: Optional[str] = None
    ) -> List[EmailMessage]:
        """
        Get recent emails with optional filters.

        Args:
            hours: Number of hours to look back
            sender_filter: Filter by sender email/domain
            subject_filter: Filter by subject content

        Returns:
            List of recent EmailMessage objects
        """
        # Build search query
        query_parts = []

        # Time filter
        timestamp = int((datetime.now() - timedelta(hours=hours)).timestamp())
        query_parts.append(f"after:{timestamp}")

        # Sender filter
        if sender_filter:
            query_parts.append(f"from:{sender_filter}")

        # Subject filter
        if subject_filter:
            query_parts.append(f"subject:{subject_filter}")

        query = " ".join(query_parts)
        return self.search_emails(query, max_results=50)

    def wait_for_email(
        self,
        sender_pattern: str,
        subject_pattern: Optional[str] = None,
        content_pattern: Optional[str] = None,
        timeout: int = 300,
        check_interval: int = 10
    ) -> Optional[EmailMessage]:
        """
        Wait for specific email to arrive.

        Args:
            sender_pattern: Sender email or domain pattern
            subject_pattern: Subject pattern to match
            content_pattern: Content pattern to search for
            timeout: Maximum wait time in seconds
            check_interval: Check interval in seconds

        Returns:
            EmailMessage if found, None if timeout
        """
        log_automation_step(
            logger,
            "wait_for_email",
            "START",
            {
                "sender_pattern": sender_pattern,
                "subject_pattern": subject_pattern,
                "timeout": timeout
            }
        )

        start_time = time.time()
        last_check_time = datetime.now()

        while time.time() - start_time < timeout:
            try:
                # Search for emails since last check
                hours_since_start = (time.time() - start_time) / 3600 + 0.5  # Add buffer
                emails = self.get_recent_emails(
                    hours=max(1, int(hours_since_start)),
                    sender_filter=sender_pattern,
                    subject_filter=subject_pattern
                )

                # Check each email
                for email in emails:
                    # Parse email date
                    try:
                        from email.utils import parsedate_to_datetime
                        email_date = parsedate_to_datetime(email.date)
                        if email_date < last_check_time:
                            continue  # Skip old emails
                    except Exception:
                        pass  # If date parsing fails, check anyway

                    # Check subject pattern
                    if subject_pattern and subject_pattern.lower() not in email.subject.lower():
                        continue

                    # Check content pattern
                    if content_pattern:
                        content = email.get_plain_text()
                        if content_pattern.lower() not in content.lower():
                            continue

                    # Found matching email
                    log_automation_step(
                        logger,
                        "wait_for_email",
                        "SUCCESS",
                        {
                            "email_id": email.id,
                            "subject": email.subject,
                            "sender": email.sender
                        }
                    )

                    logger.info(f"Found matching email: {email.subject}")
                    return email

                # Update last check time
                last_check_time = datetime.now()

                # Wait before next check
                logger.debug(f"Waiting for email... ({int(time.time() - start_time)}s elapsed)")
                time.sleep(check_interval)

            except Exception as e:
                logger.warning(f"Error during email wait: {e}")
                time.sleep(check_interval)

        log_automation_step(
            logger,
            "wait_for_email",
            "ERROR",
            {"error": "Timeout waiting for email"}
        )

        logger.warning(f"Email wait timeout ({timeout}s)")
        return None

    def extract_links(self, email: EmailMessage) -> List[str]:
        """
        Extract all links from email content.

        Args:
            email: EmailMessage to extract links from

        Returns:
            List of URLs found in email
        """
        import re

        links = []
        content = email.body_html or email.get_plain_text()

        # Extract HTML links
        if email.body_html and BS4_AVAILABLE:
            soup = BeautifulSoup(email.body_html, 'html.parser')
            for link in soup.find_all('a', href=True):
                links.append(link['href'])

        # Extract plain text URLs
        url_pattern = r'https?://[^\s<>"\']+|www\.[^\s<>"\']+|[^\s<>"\'\@]+\.[a-zA-Z]{2,}[^\s<>"\']*'
        text_links = re.findall(url_pattern, content)
        links.extend(text_links)

        # Clean and deduplicate
        clean_links = []
        for link in links:
            link = link.strip()
            if link and link not in clean_links:
                clean_links.append(link)

        return clean_links

    def mark_as_read(self, email: EmailMessage) -> bool:
        """
        Mark email as read.

        Args:
            email: EmailMessage to mark as read

        Returns:
            True if successful, False otherwise
        """
        try:
            service = self.get_service()
            service.users().messages().modify(
                userId='me',
                id=email.id,
                body={'removeLabelIds': ['UNREAD']}
            ).execute()

            logger.info(f"Marked email as read: {email.id}")
            return True

        except Exception as e:
            logger.error(f"Failed to mark email as read: {e}")
            return False

    # Backward compatibility methods
    def get_user_info(self) -> Optional[Dict[str, str]]:
        """
        Get Gmail user profile information (backward compatibility).

        Returns:
            Dictionary with user info or None
        """
        try:
            service = self.get_service()
            profile = service.users().getProfile(userId='me').execute()

            return {
                'email': profile.get('emailAddress', ''),
                'messages_total': str(profile.get('messagesTotal', 0)),
                'threads_total': str(profile.get('threadsTotal', 0))
            }

        except Exception as e:
            logger.error(f"Failed to get user info: {e}")
            return None

# Export commonly used items
__all__ = [
    'EmailMessage',
    'GmailService',
    'SCOPES'
]