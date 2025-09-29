"""Configuration package for Auto Cloud Skill Registration application."""

from .constants import *
from .settings import settings
from .licensing import ensure_license, get_machine_id, get_license_info

__all__ = [
    # Constants
    'APP_NAME', 'VERSION', 'AUTHOR',
    'BASE_URL', 'PRODUCT_CODE',
    'FIREFOX_RELAY_BASE_URL', 'RANDOMUSER_API_URL', 'CLOUDSKILL_REGISTER_URL',
    'DEBUG', 'AUTO_SAVE_LOGS', 'LOG_LEVEL', 'LOG_FILE',
    'PLAYWRIGHT_HEADLESS', 'PLAYWRIGHT_TIMEOUT', 'BROWSER_USER_AGENT',
    'DEFAULT_GENDER', 'DEFAULT_NATIONALITIES', 'DEFAULT_PASSWORD_LENGTH',
    'validate_config', 'get_browser_options',

    # Settings
    'settings',

    # Licensing
    'ensure_license', 'get_machine_id', 'get_license_info'
]