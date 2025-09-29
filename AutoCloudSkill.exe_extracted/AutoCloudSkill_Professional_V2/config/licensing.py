"""
Professional licensing system for AutoCloudSkill.

This module provides comprehensive license management:
- Machine ID-based licensing
- Automatic trial provisioning
- License validation with caching
- Secure API communication
- Offline grace period support
- License status tracking

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import os
import requests
import hashlib
import json
import logging
import time
from typing import Any, Dict, Optional, Tuple
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from .constants import VERSION, BASE_URL, PRODUCT_CODE

logger = logging.getLogger(__name__)

@dataclass
class LicenseInfo:
    """License information container."""
    is_valid: bool
    is_allowed: bool
    key: str
    plan: Optional[str]
    status: Optional[str]
    expires_at: Optional[str]
    reason: Optional[str]
    checked_at: str
    machine_id: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'LicenseInfo':
        """Create from dictionary."""
        return cls(**data)

    def is_expired(self) -> bool:
        """Check if license has expired."""
        if not self.expires_at:
            return False

        try:
            expires = datetime.fromisoformat(self.expires_at.replace('Z', '+00:00'))
            return datetime.now(expires.tzinfo) > expires
        except Exception:
            return True

    def days_until_expiry(self) -> Optional[int]:
        """Calculate days until license expiry."""
        if not self.expires_at:
            return None

        try:
            expires = datetime.fromisoformat(self.expires_at.replace('Z', '+00:00'))
            delta = expires - datetime.now(expires.tzinfo)
            return max(0, delta.days)
        except Exception:
            return None

class LicenseManager:
    """Professional license management system."""

    def __init__(
        self,
        base_url: str = BASE_URL,
        product_code: str = PRODUCT_CODE,
        cache_ttl: int = 3600,  # 1 hour
        offline_grace_period: int = 86400  # 24 hours
    ):
        """
        Initialize license manager.

        Args:
            base_url: License server base URL
            product_code: Product identifier
            cache_ttl: Cache time-to-live in seconds
            offline_grace_period: Grace period for offline validation
        """
        self.base_url = base_url
        self.product_code = product_code
        self.cache_ttl = cache_ttl
        self.offline_grace_period = offline_grace_period

        self._cache_file = self._get_cache_file()
        self._cached_license: Optional[LicenseInfo] = None
        self._machine_id: Optional[str] = None

        # Load cached license
        self._load_cache()

    def _get_cache_file(self) -> Path:
        """Get license cache file path."""
        if os.name == 'nt':
            cache_dir = Path(os.environ.get('LOCALAPPDATA', Path.home() / 'AppData' / 'Local'))
        else:
            cache_dir = Path(os.environ.get('XDG_CACHE_HOME', Path.home() / '.cache'))

        license_cache = cache_dir / 'AutoCloudSkill' / '.license_cache'
        license_cache.parent.mkdir(parents=True, exist_ok=True)
        return license_cache

    def _load_cache(self) -> None:
        """Load cached license information."""
        try:
            if self._cache_file.exists():
                with open(self._cache_file, 'r', encoding='utf-8') as f:
                    cache_data = json.load(f)
                    self._cached_license = LicenseInfo.from_dict(cache_data)
                    logger.debug("License cache loaded successfully")
        except Exception as e:
            logger.warning(f"Failed to load license cache: {e}")
            self._cached_license = None

    def _save_cache(self, license_info: LicenseInfo) -> None:
        """Save license information to cache."""
        try:
            with open(self._cache_file, 'w', encoding='utf-8') as f:
                json.dump(license_info.to_dict(), f, indent=2)
            logger.debug("License cache saved successfully")
        except Exception as e:
            logger.warning(f"Failed to save license cache: {e}")

    def get_machine_id(self) -> str:
        """
        Get unique machine identifier.

        Returns:
            Machine ID string

        Raises:
            RuntimeError: If unable to get machine ID
        """
        if self._machine_id:
            return self._machine_id

        try:
            import machineid
            self._machine_id = machineid.id()
            return self._machine_id
        except ImportError:
            logger.warning("machineid package not available, using fallback")

        # Fallback method using platform-specific identifiers
        try:
            import platform
            import uuid

            # Create machine ID from multiple system attributes
            system_info = [
                platform.node(),
                platform.machine(),
                platform.processor(),
                str(uuid.getnode())  # MAC address
            ]

            combined = '|'.join(system_info)
            self._machine_id = hashlib.sha256(combined.encode('utf-8')).hexdigest()
            return self._machine_id

        except Exception as e:
            raise RuntimeError(f"Unable to get machine ID: {e}")

    def get_hashed_machine_id(self) -> str:
        """
        Get SHA-256 hashed machine identifier.

        Returns:
            Hashed machine ID
        """
        raw_id = self.get_machine_id()
        return hashlib.sha256(raw_id.encode('utf-8')).hexdigest()

    def _api_post(
        self,
        path: str,
        payload: Dict[str, Any],
        timeout: int = 20
    ) -> requests.Response:
        """
        Make POST request to license API.

        Args:
            path: API endpoint path
            payload: Request payload
            timeout: Request timeout in seconds

        Returns:
            Response object

        Raises:
            requests.RequestException: On network error
        """
        url = f"{self.base_url}{path}"
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': f'AutoCloudSkill/{VERSION}'
        }

        logger.debug(f"API POST: {url}")
        response = requests.post(url, json=payload, headers=headers, timeout=timeout)
        return response

    def check_license(
        self,
        key: str,
        device_id: Optional[str] = None,
        version: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Check license validity with license server.

        Args:
            key: License key
            device_id: Device identifier (optional)
            version: Application version (optional)

        Returns:
            Normalized license check response
        """
        payload = {
            'key': key,
            'product_code': self.product_code
        }

        if device_id:
            payload['device_id'] = device_id
        if version:
            payload['version'] = version

        try:
            response = self._api_post('/api/licenses/check', payload)
            data = response.json() if response.ok else {}

            return {
                'ok': response.ok,
                'http_status': response.status_code,
                'valid': bool(data.get('valid', False)),
                'plan': data.get('plan'),
                'status': data.get('status'),
                'expiresAt': data.get('expiresAt'),
                'reason': data.get('reason'),
                'raw': data
            }

        except requests.RequestException as e:
            logger.error(f"License check API error: {e}")
            return {
                'ok': False,
                'http_status': 0,
                'valid': False,
                'plan': None,
                'status': 'error',
                'expiresAt': None,
                'reason': f'Network error: {str(e)}',
                'raw': {}
            }

    def provision_trial(
        self,
        device_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Provision trial license for device.

        Args:
            device_id: Device identifier (optional)

        Returns:
            Provisioning response with license key
        """
        payload = {
            'product_code': self.product_code,
            'plan': 'trial'
        }

        if device_id:
            payload['device_id'] = device_id

        try:
            response = self._api_post('/api/licenses/provision', payload)
            data = response.json() if response.status_code in (200, 201) else {}

            key = data.get('key')
            plan = data.get('plan', 'trial')
            expires_at = data.get('expires_at') or data.get('expiresAt')
            ok = response.status_code in (200, 201)

            logger.info(f"Trial provisioning: {response.status_code} - {plan}")

            return {
                'ok': ok,
                'http_status': response.status_code,
                'key': key,
                'plan': plan,
                'expiresAt': expires_at,
                'raw': data
            }

        except requests.RequestException as e:
            logger.error(f"Trial provisioning API error: {e}")
            return {
                'ok': False,
                'http_status': 0,
                'key': None,
                'plan': 'trial',
                'expiresAt': None,
                'raw': {}
            }

    def ensure_license(
        self,
        force_check: bool = False,
        version: Optional[str] = VERSION
    ) -> LicenseInfo:
        """
        Ensure valid license exists, with automatic trial provisioning.

        This method implements the complete licensing workflow:
        1. Check cache for recent validation
        2. Get machine ID and use as license key
        3. Check license with server
        4. Auto-provision trial if not found
        5. Re-check after provisioning

        Args:
            force_check: Force fresh validation (bypass cache)
            version: Application version for validation

        Returns:
            LicenseInfo object with validation results
        """
        # Check cache first
        if not force_check and self._cached_license:
            cache_age = datetime.now() - datetime.fromisoformat(self._cached_license.checked_at)
            if cache_age.total_seconds() < self.cache_ttl:
                logger.debug("Using cached license information")
                return self._cached_license

        # Get machine ID
        try:
            machine_id = self.get_hashed_machine_id()
        except Exception as e:
            logger.error(f"Machine ID error: {e}")
            return LicenseInfo(
                is_valid=False,
                is_allowed=False,
                key='',
                plan=None,
                status='error',
                expires_at=None,
                reason=f'Machine ID error: {str(e)}',
                checked_at=datetime.now().isoformat(),
                machine_id=''
            )

        key = machine_id
        device_id = machine_id

        # Check license
        try:
            check_result = self.check_license(key, device_id=device_id, version=version)
        except Exception as e:
            logger.error(f"License check error: {e}")
            # Return cached license if available (offline grace period)
            if self._cached_license:
                cache_age = datetime.now() - datetime.fromisoformat(self._cached_license.checked_at)
                if cache_age.total_seconds() < self.offline_grace_period:
                    logger.warning("Using cached license (offline mode)")
                    return self._cached_license

            return LicenseInfo(
                is_valid=False,
                is_allowed=False,
                key=key,
                plan=None,
                status='error',
                expires_at=None,
                reason=f'API error: {str(e)}',
                checked_at=datetime.now().isoformat(),
                machine_id=machine_id
            )

        # If license not valid, try to provision trial
        if not check_result.get('valid'):
            logger.info("License not found, attempting trial provisioning")

            try:
                provision_result = self.provision_trial(device_id=device_id)

                if provision_result.get('ok'):
                    logger.info("Trial provisioning successful, re-checking license")
                    # Re-check after provisioning
                    check_result = self.check_license(key, device_id=device_id, version=version)
                else:
                    logger.warning(f"Trial provisioning failed: {provision_result}")

            except Exception as e:
                logger.error(f"Trial provisioning error: {e}")

        # Create license info
        valid = bool(check_result.get('valid', False))
        plan = check_result.get('plan', '').lower() if check_result.get('plan') else None
        status = check_result.get('status', '').lower() if check_result.get('status') else None

        # Determine if license allows usage
        is_allowed = valid and plan not in ['free', None] and status != 'suspended'

        license_info = LicenseInfo(
            is_valid=valid,
            is_allowed=is_allowed,
            key=key,
            plan=plan,
            status=status,
            expires_at=check_result.get('expiresAt'),
            reason=check_result.get('reason'),
            checked_at=datetime.now().isoformat(),
            machine_id=machine_id
        )

        # Cache license info
        self._cached_license = license_info
        self._save_cache(license_info)

        logger.info(f"License validation complete: allowed={is_allowed}, plan={plan}, status={status}")

        return license_info

    def invalidate_cache(self) -> None:
        """Invalidate cached license information."""
        self._cached_license = None
        if self._cache_file.exists():
            try:
                self._cache_file.unlink()
                logger.debug("License cache invalidated")
            except Exception as e:
                logger.warning(f"Failed to delete license cache: {e}")

# Create global license manager instance
_license_manager = LicenseManager()

# Backward compatibility functions
def get_machine_id() -> str:
    """Get machine ID (backward compatibility)."""
    return _license_manager.get_machine_id()

def get_hashed_machine_id() -> str:
    """Get hashed machine ID (backward compatibility)."""
    return _license_manager.get_hashed_machine_id()

def check_license(
    key: str,
    product_code: str,
    device_id: Optional[str] = None,
    version: Optional[str] = None
) -> Dict[str, Any]:
    """Check license (backward compatibility)."""
    manager = LicenseManager(product_code=product_code)
    return manager.check_license(key, device_id=device_id, version=version)

def provision_trial(
    product_code: str,
    device_id: Optional[str] = None
) -> Dict[str, Any]:
    """Provision trial (backward compatibility)."""
    manager = LicenseManager(product_code=product_code)
    return manager.provision_trial(device_id=device_id)

def ensure_license(
    product_code: str = PRODUCT_CODE,
    version: Optional[str] = VERSION
) -> Dict[str, Any]:
    """
    Ensure license exists (backward compatibility).

    Returns:
        Dictionary with license information for backward compatibility
    """
    manager = LicenseManager(product_code=product_code)
    license_info = manager.ensure_license(version=version)

    return {
        'is_allowed': license_info.is_allowed,
        'valid': license_info.is_valid,
        'plan': license_info.plan,
        'status': license_info.status,
        'expiresAt': license_info.expires_at,
        'reason': license_info.reason,
        'check': {
            'machine_id': license_info.machine_id,
            'checked_at': license_info.checked_at
        }
    }

# Export commonly used items
__all__ = [
    'LicenseInfo',
    'LicenseManager',
    'get_machine_id',
    'get_hashed_machine_id',
    'check_license',
    'provision_trial',
    'ensure_license'
]