"""
Licensing module for application
"""
import hashlib
import uuid
import platform
from typing import Dict, Optional

def get_machine_id() -> str:
    """Get unique machine identifier"""
    try:
        # Use MAC address and hostname for machine ID
        mac = uuid.getnode()
        hostname = platform.node()
        machine_info = f"{mac}-{hostname}-{platform.system()}"
        return hashlib.sha256(machine_info.encode()).hexdigest()[:16]
    except Exception:
        return "unknown-machine"

def ensure_license() -> Dict:
    """Ensure license is valid"""
    # For demo purposes, return a free plan
    return {
        'is_allowed': True,
        'plan': 'demo',
        'status': 'active',
        'reason': 'Demo version',
        'expiresAt': None
    }