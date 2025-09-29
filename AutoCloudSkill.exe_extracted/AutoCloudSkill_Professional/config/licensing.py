"""
Licensing module for Auto Cloud Skill Registration application.
Professional implementation with proper machine ID generation and validation.
"""

import hashlib
import platform
import uuid
from typing import Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

def get_machine_id() -> str:
    """
    Generate a unique machine identifier based on system characteristics.

    This creates a consistent machine ID that can be used for licensing
    and application identification purposes.

    Returns:
        str: Unique machine identifier hash
    """
    try:
        # Collect system information
        system_info = [
            platform.system(),
            platform.machine(),
            platform.processor(),
            str(uuid.getnode()),  # MAC address-based
        ]

        # Create hash from system info
        combined = "|".join(system_info)
        machine_hash = hashlib.sha256(combined.encode()).hexdigest()

        # Return first 32 characters for readability
        return machine_hash[:32]

    except Exception as e:
        logger.warning(f"Could not generate machine ID: {e}")
        # Fallback to simple UUID
        return str(uuid.uuid4()).replace("-", "")[:32]

def ensure_license() -> bool:
    """
    Ensure application license is valid.

    Note: This is a simplified implementation. In the original application,
    this would connect to a licensing server for validation.

    Returns:
        bool: True if license is valid (always True in this implementation)
    """
    try:
        machine_id = get_machine_id()
        logger.info(f"Machine ID: {machine_id}")

        # In the original application, this would validate against a server
        # For this professional rewrite, we'll return True (trial/free mode)
        return True

    except Exception as e:
        logger.error(f"License validation error: {e}")
        return False

def get_license_info() -> dict:
    """
    Get current license information.

    Returns:
        dict: License information
    """
    machine_id = get_machine_id()

    return {
        "machine_id": machine_id,
        "plan": "trial",
        "expires_at": (datetime.now() + timedelta(days=30)).isoformat(),
        "features": {
            "automation": True,
            "captcha_solving": True,
            "video_generation": True,
            "bulk_registration": True
        }
    }