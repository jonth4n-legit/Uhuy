"""
Firefox Relay Service for Auto Cloud Skill Registration application.

Professional implementation of Firefox Relay API integration for temporary
email address generation with proper error handling and API management.
"""

import requests
import time
from typing import Dict, Optional, List, Any
import logging
from datetime import datetime, timedelta

from config.constants import FIREFOX_RELAY_BASE_URL
from utils.logger import log_service_call
from utils.validators import validate_api_key, validate_email, ValidationError

logger = logging.getLogger(__name__)

class FirefoxRelayService:
    """
    Service for managing temporary email addresses through Firefox Relay API.

    This service provides temporary email addresses for account registration
    with proper lifecycle management and error handling.
    """

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """
        Initialize Firefox Relay service.

        Args:
            api_key: Firefox Relay API key
            base_url: API base URL (defaults to production)

        Raises:
            ValueError: If API key is invalid or missing
        """
        self.api_key = api_key
        self.base_url = base_url or FIREFOX_RELAY_BASE_URL

        # Validate API key if provided
        if self.api_key:
            try:
                validate_api_key(self.api_key, "Firefox Relay")
            except ValidationError as e:
                raise ValueError(f"Invalid Firefox Relay API key: {e}")

        # Setup session
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Auto-Cloud-Skill/1.2.0'
        })

        # Set auth header if API key provided
        if self.api_key:
            self.session.headers['Authorization'] = f'Bearer {self.api_key}'

        # Track created masks for cleanup
        self.created_masks: List[str] = []

    def set_api_key(self, api_key: str) -> bool:
        """
        Set or update the API key.

        Args:
            api_key: New API key

        Returns:
            bool: True if key is valid and set successfully
        """
        try:
            validate_api_key(api_key, "Firefox Relay")
            self.api_key = api_key
            self.session.headers['Authorization'] = f'Bearer {api_key}'
            logger.info("Firefox Relay API key updated successfully")
            return True

        except ValidationError as e:
            logger.error(f"Invalid API key: {e}")
            return False

    def create_relay_mask(self, description: Optional[str] = None) -> Optional[Dict]:
        """
        Create a new email relay mask.

        Args:
            description: Optional description for the mask

        Returns:
            Dict: Mask information or None if failed
        """
        if not self.api_key:
            logger.error("No API key configured for Firefox Relay")
            return None

        start_time = datetime.now()

        try:
            url = f"{self.base_url}/api/v1/relayaddresses/"
            data = {}

            if description:
                data['description'] = description[:100]  # Limit description length

            logger.info(f"Creating relay mask: {description or 'No description'}")

            response = self.session.post(url, json=data, timeout=30)
            response.raise_for_status()

            mask_data = response.json()

            # Validate response
            if not mask_data.get('full_address'):
                raise ValueError("Invalid response: missing email address")

            # Track created mask
            mask_id = mask_data.get('id')
            if mask_id:
                self.created_masks.append(mask_id)

            # Log successful creation
            response_time = (datetime.now() - start_time).total_seconds()
            log_service_call('Firefox Relay', 'create_relay_mask', 'SUCCESS', response_time)

            logger.info(f"Created relay mask: {mask_data['full_address']}")
            return mask_data

        except requests.HTTPError as e:
            status_code = e.response.status_code if e.response else 'Unknown'
            logger.error(f"HTTP error creating mask (status {status_code}): {e}")

            if status_code == 401:
                logger.error("Invalid API key or authentication failed")
            elif status_code == 429:
                logger.error("Rate limit exceeded - too many requests")
            elif status_code == 403:
                logger.error("Access forbidden - check API key permissions")

            log_service_call('Firefox Relay', 'create_relay_mask', 'FAILED')
            return None

        except requests.RequestException as e:
            logger.error(f"Network error creating relay mask: {e}")
            log_service_call('Firefox Relay', 'create_relay_mask', 'FAILED')
            return None

        except Exception as e:
            logger.error(f"Unexpected error creating relay mask: {e}")
            log_service_call('Firefox Relay', 'create_relay_mask', 'ERROR')
            return None

    def get_relay_masks(self) -> Optional[List[Dict]]:
        """
        Get list of existing relay masks.

        Returns:
            List[Dict]: List of mask information or None if failed
        """
        if not self.api_key:
            logger.error("No API key configured for Firefox Relay")
            return None

        start_time = datetime.now()

        try:
            url = f"{self.base_url}/api/v1/relayaddresses/"
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            masks = response.json()

            # Log successful retrieval
            response_time = (datetime.now() - start_time).total_seconds()
            log_service_call('Firefox Relay', 'get_relay_masks', 'SUCCESS', response_time)

            return masks

        except Exception as e:
            logger.error(f"Error retrieving relay masks: {e}")
            log_service_call('Firefox Relay', 'get_relay_masks', 'FAILED')
            return None

    def delete_relay_mask(self, mask_id: str) -> bool:
        """
        Delete a specific relay mask.

        Args:
            mask_id: ID of the mask to delete

        Returns:
            bool: True if deleted successfully
        """
        if not self.api_key:
            logger.error("No API key configured for Firefox Relay")
            return False

        start_time = datetime.now()

        try:
            url = f"{self.base_url}/api/v1/relayaddresses/{mask_id}/"
            response = self.session.delete(url, timeout=30)
            response.raise_for_status()

            # Remove from tracking
            if mask_id in self.created_masks:
                self.created_masks.remove(mask_id)

            # Log successful deletion
            response_time = (datetime.now() - start_time).total_seconds()
            log_service_call('Firefox Relay', 'delete_relay_mask', 'SUCCESS', response_time)

            logger.info(f"Deleted relay mask: {mask_id}")
            return True

        except Exception as e:
            logger.error(f"Error deleting relay mask {mask_id}: {e}")
            log_service_call('Firefox Relay', 'delete_relay_mask', 'FAILED')
            return False

    def delete_all_masks(self) -> int:
        """
        Delete all relay masks created by this service instance.

        Returns:
            int: Number of masks successfully deleted
        """
        if not self.created_masks:
            logger.info("No masks to delete")
            return 0

        deleted_count = 0
        masks_to_delete = self.created_masks.copy()

        for mask_id in masks_to_delete:
            if self.delete_relay_mask(mask_id):
                deleted_count += 1
                time.sleep(0.5)  # Rate limiting

        logger.info(f"Deleted {deleted_count}/{len(masks_to_delete)} masks")
        return deleted_count

    def test_connection(self) -> bool:
        """
        Test connection to Firefox Relay API.

        Returns:
            bool: True if API is accessible
        """
        if not self.api_key:
            logger.warning("No API key configured - cannot test connection")
            return False

        try:
            url = f"{self.base_url}/api/v1/relayaddresses/"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            logger.info("Firefox Relay API connection test successful")
            return True

        except Exception as e:
            logger.error(f"Firefox Relay API connection test failed: {e}")
            return False

    def get_status_info(self) -> Dict[str, Any]:
        """
        Get service status information.

        Returns:
            Dict: Service status and statistics
        """
        return {
            'api_key_configured': bool(self.api_key),
            'base_url': self.base_url,
            'created_masks_count': len(self.created_masks),
            'connection_test': self.test_connection() if self.api_key else False,
            'service_available': bool(self.api_key)
        }