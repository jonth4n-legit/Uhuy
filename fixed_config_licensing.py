"""
Licensing module untuk aplikasi
"""
import os
import requests
import hashlib
import logging
from typing import Dict, Optional
from config.settings import settings

logger = logging.getLogger(__name__)

def get_machine_id() -> str:
    """Generate unique machine ID"""
    try:
        # Try to get machine ID from various sources
        machine_id = None
        
        # Try Windows machine ID
        try:
            import wmi
            c = wmi.WMI()
            for system in c.Win32_ComputerSystem():
                machine_id = system.Name
                break
        except ImportError:
            pass
        
        # Try MAC address as fallback
        if not machine_id:
            import uuid
            machine_id = str(uuid.getnode())
        
        # Hash the machine ID for privacy
        return hashlib.sha256(machine_id.encode()).hexdigest()[:16]
        
    except Exception as e:
        logger.error(f'Error generating machine ID: {e}')
        return 'unknown'

def check_license_status() -> Dict[str, any]:
    """Check license status from remote server"""
    try:
        machine_id = get_machine_id()
        
        # Make request to license server
        response = requests.post(
            f'{settings.BASE_URL}/api/license/check',
            json={
                'machine_id': machine_id,
                'product_code': settings.PRODUCT_CODE,
                'version': settings.VERSION
            },
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            return {
                'is_allowed': False,
                'plan': 'free',
                'status': 'error',
                'reason': f'Server returned status {response.status_code}'
            }
            
    except Exception as e:
        logger.error(f'License check error: {e}')
        return {
            'is_allowed': True,  # Allow offline usage
            'plan': 'offline',
            'status': 'offline',
            'reason': 'Offline mode - license check failed'
        }

def ensure_license() -> Dict[str, any]:
    """Ensure license is valid, return license info"""
    try:
        license_info = check_license_status()
        
        if not license_info.get('is_allowed', True):
            logger.warning(f'License not allowed: {license_info.get("reason", "Unknown")}')
        else:
            logger.info(f'License valid: {license_info.get("plan", "unknown")} plan')
        
        return license_info
        
    except Exception as e:
        logger.error(f'License ensure error: {e}')
        return {
            'is_allowed': True,  # Allow offline usage
            'plan': 'offline',
            'status': 'error',
            'reason': str(e)
        }