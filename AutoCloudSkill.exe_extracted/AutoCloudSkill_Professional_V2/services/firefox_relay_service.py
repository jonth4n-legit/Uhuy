"""
Professional Firefox Relay service for AutoCloudSkill.

This module provides comprehensive email relay management:
- Firefox Relay API integration
- Email mask creation and management
- Email monitoring and retrieval
- Multiple authentication methods
- Comprehensive error handling and retry logic

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import os
import time
import asyncio
import logging
from typing import Dict, List, Optional, Any, Union, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum

import requests
import aiohttp

from utils.logger import setup_application_logging, log_automation_step, performance_monitor
from config.settings import settings

logger = setup_application_logging('FirefoxRelayService')

class RelayStatus(Enum):
    """Email relay status options."""
    ENABLED = "enabled"
    DISABLED = "disabled"
    BLOCKED = "blocked"

@dataclass
class EmailMask:
    """Email mask information."""
    id: str
    address: str
    domain: str
    full_address: str
    description: Optional[str]
    enabled: bool
    created_at: str
    blocked: bool = False
    num_forwarded: int = 0
    num_blocked: int = 0
    num_spam: int = 0

    @classmethod
    def from_api_response(cls, data: Dict[str, Any]) -> 'EmailMask':
        """Create EmailMask from API response data."""
        return cls(
            id=data.get('id', ''),
            address=data.get('address', ''),
            domain=data.get('domain', ''),
            full_address=data.get('full_address', ''),
            description=data.get('description'),
            enabled=data.get('enabled', True),
            created_at=data.get('created_at', ''),
            blocked=data.get('blocked', False),
            num_forwarded=data.get('num_forwarded', 0),
            num_blocked=data.get('num_blocked', 0),
            num_spam=data.get('num_spam', 0)
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)

@dataclass
class EmailMessage:
    """Email message information."""
    id: str
    subject: str
    sender: str
    recipient: str
    received_at: str
    content_preview: str
    is_spam: bool = False
    is_blocked: bool = False

class FirefoxRelayService:
    """Professional Firefox Relay email service with comprehensive features."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: int = 30,
        max_retries: int = 3
    ):
        """
        Initialize Firefox Relay service.

        Args:
            api_key: Firefox Relay API key
            base_url: API base URL (default from settings)
            timeout: Request timeout in seconds
            max_retries: Maximum retry attempts for failed requests

        Raises:
            ValueError: If API key is not provided
        """
        self.api_key = api_key or settings.firefox_relay_api_key
        self.base_url = base_url or settings.firefox_relay_base_url
        self.timeout = timeout
        self.max_retries = max_retries

        if not self.api_key or self.api_key == 'your_api_key_here':
            raise ValueError(
                'Firefox Relay API key required. '
                'Set FIREFOX_RELAY_API_KEY environment variable or provide via constructor.'
            )

        # Configure session
        self.session = requests.Session()
        self._setup_session()

        # Cache for created masks
        self._mask_cache: Dict[str, EmailMask] = {}

        logger.info("Firefox Relay service initialized")

    def _setup_session(self) -> None:
        """Configure HTTP session with headers and authentication."""
        self.session.headers.update({
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': f'AutoCloudSkill/{settings.version}'
        })

    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None
    ) -> requests.Response:
        """
        Make HTTP request with retry logic and error handling.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint
            data: Request payload
            params: Query parameters

        Returns:
            Response object

        Raises:
            requests.RequestException: On request failure
        """
        url = f"{self.base_url}{endpoint}"

        for attempt in range(self.max_retries + 1):
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    json=data,
                    params=params,
                    timeout=self.timeout
                )

                # Handle authentication errors with fallback methods
                if response.status_code == 401:
                    logger.warning(f"Authentication failed (attempt {attempt + 1})")
                    if attempt < self.max_retries:
                        self._try_alternative_auth()
                        continue

                # Handle rate limiting
                if response.status_code == 429:
                    retry_after = int(response.headers.get('Retry-After', 60))
                    logger.warning(f"Rate limited, waiting {retry_after}s")
                    time.sleep(retry_after)
                    continue

                response.raise_for_status()
                return response

            except requests.RequestException as e:
                if attempt == self.max_retries:
                    logger.error(f"Request failed after {self.max_retries + 1} attempts: {e}")
                    raise
                else:
                    wait_time = 2 ** attempt  # Exponential backoff
                    logger.warning(f"Request failed (attempt {attempt + 1}), retrying in {wait_time}s: {e}")
                    time.sleep(wait_time)

    def _try_alternative_auth(self) -> None:
        """Try alternative authentication formats."""
        auth_formats = [
            f'Token {self.api_key}',
            f'Bearer {self.api_key}',
            f'API-Key {self.api_key}',
            self.api_key
        ]

        for auth_format in auth_formats:
            logger.debug(f"Trying auth format: {auth_format[:20]}...")

            test_session = requests.Session()
            test_session.headers.update({
                'Authorization': auth_format,
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            })

            try:
                test_response = test_session.get(
                    f"{self.base_url}/api/v1/relayaddresses/",
                    timeout=10
                )

                if test_response.status_code != 401:
                    logger.info(f"Authentication successful with format: {auth_format[:20]}...")
                    self.session.headers['Authorization'] = auth_format
                    return

            except Exception:
                continue

        logger.error("All authentication formats failed")

    @performance_monitor("create_relay_mask")
    def create_mask(
        self,
        description: Optional[str] = None,
        enabled: bool = True
    ) -> Optional[EmailMask]:
        """
        Create a new email relay mask.

        Args:
            description: Optional description for the mask
            enabled: Whether the mask should be enabled

        Returns:
            EmailMask object or None if creation failed
        """
        log_automation_step(
            logger,
            "create_relay_mask",
            "START",
            {"description": description, "enabled": enabled}
        )

        try:
            data = {"enabled": enabled}
            if description:
                data["description"] = description

            response = self._make_request("POST", "/api/v1/relayaddresses/", data=data)
            response_data = response.json()

            mask = EmailMask.from_api_response(response_data)

            # Cache the mask
            self._mask_cache[mask.id] = mask

            log_automation_step(
                logger,
                "create_relay_mask",
                "SUCCESS",
                {
                    "mask_id": mask.id,
                    "address": mask.full_address,
                    "enabled": mask.enabled
                }
            )

            logger.info(f"Created relay mask: {mask.full_address}")
            return mask

        except requests.RequestException as e:
            log_automation_step(
                logger,
                "create_relay_mask",
                "ERROR",
                {"error": str(e)}
            )
            logger.error(f"Failed to create relay mask: {e}")
            return None

        except Exception as e:
            log_automation_step(
                logger,
                "create_relay_mask",
                "ERROR",
                {"error": str(e)}
            )
            logger.error(f"Unexpected error creating mask: {e}")
            return None

    @performance_monitor("list_masks")
    def list_masks(self, refresh_cache: bool = False) -> List[EmailMask]:
        """
        List all email relay masks.

        Args:
            refresh_cache: Force refresh from API

        Returns:
            List of EmailMask objects
        """
        try:
            response = self._make_request("GET", "/api/v1/relayaddresses/")
            data = response.json()

            masks = []
            for mask_data in data.get('results', []):
                mask = EmailMask.from_api_response(mask_data)
                masks.append(mask)

                # Update cache
                if refresh_cache:
                    self._mask_cache[mask.id] = mask

            logger.info(f"Retrieved {len(masks)} email masks")
            return masks

        except requests.RequestException as e:
            logger.error(f"Failed to list masks: {e}")
            return []

    @performance_monitor("get_mask")
    def get_mask(self, mask_id: str) -> Optional[EmailMask]:
        """
        Get specific email mask by ID.

        Args:
            mask_id: Mask identifier

        Returns:
            EmailMask object or None if not found
        """
        # Check cache first
        if mask_id in self._mask_cache:
            return self._mask_cache[mask_id]

        try:
            response = self._make_request("GET", f"/api/v1/relayaddresses/{mask_id}/")
            data = response.json()

            mask = EmailMask.from_api_response(data)
            self._mask_cache[mask_id] = mask

            return mask

        except requests.RequestException as e:
            logger.error(f"Failed to get mask {mask_id}: {e}")
            return None

    @performance_monitor("update_mask")
    def update_mask(
        self,
        mask_id: str,
        enabled: Optional[bool] = None,
        description: Optional[str] = None,
        blocked: Optional[bool] = None
    ) -> Optional[EmailMask]:
        """
        Update email mask settings.

        Args:
            mask_id: Mask identifier
            enabled: Enable/disable mask
            description: Update description
            blocked: Block/unblock mask

        Returns:
            Updated EmailMask object or None if failed
        """
        try:
            data = {}
            if enabled is not None:
                data["enabled"] = enabled
            if description is not None:
                data["description"] = description
            if blocked is not None:
                data["blocked"] = blocked

            if not data:
                logger.warning("No update data provided")
                return self.get_mask(mask_id)

            response = self._make_request("PATCH", f"/api/v1/relayaddresses/{mask_id}/", data=data)
            response_data = response.json()

            mask = EmailMask.from_api_response(response_data)
            self._mask_cache[mask_id] = mask

            logger.info(f"Updated mask {mask_id}: {data}")
            return mask

        except requests.RequestException as e:
            logger.error(f"Failed to update mask {mask_id}: {e}")
            return None

    @performance_monitor("delete_mask")
    def delete_mask(self, mask_id: str) -> bool:
        """
        Delete email relay mask.

        Args:
            mask_id: Mask identifier

        Returns:
            True if deleted successfully, False otherwise
        """
        try:
            response = self._make_request("DELETE", f"/api/v1/relayaddresses/{mask_id}/")

            # Remove from cache
            self._mask_cache.pop(mask_id, None)

            logger.info(f"Deleted mask {mask_id}")
            return True

        except requests.RequestException as e:
            logger.error(f"Failed to delete mask {mask_id}: {e}")
            return False

    def find_available_mask(
        self,
        description_pattern: Optional[str] = None,
        create_if_none: bool = True
    ) -> Optional[EmailMask]:
        """
        Find an available email mask for use.

        Args:
            description_pattern: Pattern to match in description
            create_if_none: Create new mask if none available

        Returns:
            Available EmailMask or None
        """
        masks = self.list_masks()

        # Filter by description pattern if provided
        if description_pattern:
            masks = [mask for mask in masks if mask.description and description_pattern in mask.description]

        # Find enabled masks
        available_masks = [mask for mask in masks if mask.enabled and not mask.blocked]

        if available_masks:
            # Return the most recently created
            return max(available_masks, key=lambda m: m.created_at)

        if create_if_none:
            description = f"AutoCloudSkill {datetime.now().strftime('%Y%m%d_%H%M%S')}"
            if description_pattern:
                description += f" - {description_pattern}"

            return self.create_mask(description=description)

        return None

    def wait_for_email(
        self,
        mask: EmailMask,
        timeout: int = 300,
        check_interval: int = 10,
        subject_pattern: Optional[str] = None
    ) -> Optional[EmailMessage]:
        """
        Wait for email to arrive at relay mask.

        Note: This is a placeholder implementation as Firefox Relay API
        doesn't provide email content retrieval in the public API.

        Args:
            mask: Email mask to monitor
            timeout: Maximum wait time in seconds
            check_interval: Check interval in seconds
            subject_pattern: Subject pattern to match

        Returns:
            EmailMessage if found, None if timeout
        """
        logger.warning(
            "Email waiting functionality requires Firefox Relay Premium API access. "
            "This is a placeholder implementation."
        )

        start_time = time.time()
        while time.time() - start_time < timeout:
            # In a real implementation, this would check for new emails
            # For now, we simulate the waiting process
            logger.info(f"Checking for emails on {mask.full_address}...")

            # Update mask statistics
            updated_mask = self.get_mask(mask.id)
            if updated_mask and updated_mask.num_forwarded > mask.num_forwarded:
                logger.info(f"New email detected for {mask.full_address}")
                # In real implementation, would return EmailMessage with content
                return EmailMessage(
                    id="simulated",
                    subject="Email Confirmation",
                    sender="noreply@example.com",
                    recipient=mask.full_address,
                    received_at=datetime.now().isoformat(),
                    content_preview="Please click the link to confirm..."
                )

            time.sleep(check_interval)

        logger.warning(f"Email wait timeout for {mask.full_address}")
        return None

    def cleanup_old_masks(self, older_than_days: int = 7) -> int:
        """
        Clean up old email masks.

        Args:
            older_than_days: Delete masks older than this many days

        Returns:
            Number of masks deleted
        """
        try:
            masks = self.list_masks()
            cutoff_date = datetime.now() - timedelta(days=older_than_days)

            deleted_count = 0
            for mask in masks:
                try:
                    mask_date = datetime.fromisoformat(mask.created_at.replace('Z', '+00:00'))
                    if mask_date < cutoff_date:
                        if self.delete_mask(mask.id):
                            deleted_count += 1
                            logger.info(f"Deleted old mask: {mask.full_address}")
                except Exception as e:
                    logger.warning(f"Failed to delete mask {mask.id}: {e}")

            logger.info(f"Cleaned up {deleted_count} old masks")
            return deleted_count

        except Exception as e:
            logger.error(f"Failed to cleanup old masks: {e}")
            return 0

    # Backward compatibility methods
    def create_relay_mask(self, description: Optional[str] = None) -> Optional[Dict]:
        """
        Create relay mask (backward compatibility).

        Args:
            description: Mask description

        Returns:
            Dictionary with mask info or None
        """
        mask = self.create_mask(description=description)
        return mask.to_dict() if mask else None

    def get_relay_masks(self) -> List[Dict]:
        """
        Get all relay masks (backward compatibility).

        Returns:
            List of mask dictionaries
        """
        masks = self.list_masks()
        return [mask.to_dict() for mask in masks]

# Export commonly used items
__all__ = [
    'RelayStatus',
    'EmailMask',
    'EmailMessage',
    'FirefoxRelayService'
]