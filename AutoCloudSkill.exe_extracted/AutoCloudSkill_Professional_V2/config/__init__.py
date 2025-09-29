"""
Config module __init__.py for AutoCloudSkill Professional.

Provides convenient imports for all configuration components.
"""

from .constants import (
    APP_NAME, VERSION, AUTHOR, DESCRIPTION,
    DEBUG, DEVELOPMENT_MODE,
    BASE_URL, PRODUCT_CODE,
    FIREFOX_RELAY_API_KEY, FIREFOX_RELAY_BASE_URL,
    RANDOMUSER_API_URL, CLOUDSKILL_REGISTER_URL,
    CLOUDSKILL_URLS,
    AUTO_SAVE_LOGS, LOG_LEVEL, LOG_FILE,
    PLAYWRIGHT_HEADLESS, PLAYWRIGHT_TIMEOUT,
    BROWSER_USER_AGENT, USER_AGENTS,
    DEFAULT_GENDER, DEFAULT_NATIONALITIES, DEFAULT_PASSWORD_LENGTH
)

from .settings import (
    ApplicationSettings,
    SettingsManager,
    get_settings_manager,
    get_settings,
    settings
)

from .licensing import (
    LicenseManager,
    LicenseInfo
)

__all__ = [
    # Constants
    'APP_NAME', 'VERSION', 'AUTHOR', 'DESCRIPTION',
    'DEBUG', 'DEVELOPMENT_MODE',
    'BASE_URL', 'PRODUCT_CODE',
    'FIREFOX_RELAY_API_KEY', 'FIREFOX_RELAY_BASE_URL',
    'RANDOMUSER_API_URL', 'CLOUDSKILL_REGISTER_URL',
    'CLOUDSKILL_URLS',
    'AUTO_SAVE_LOGS', 'LOG_LEVEL', 'LOG_FILE',
    'PLAYWRIGHT_HEADLESS', 'PLAYWRIGHT_TIMEOUT',
    'BROWSER_USER_AGENT', 'USER_AGENTS',
    'DEFAULT_GENDER', 'DEFAULT_NATIONALITIES', 'DEFAULT_PASSWORD_LENGTH',

    # Settings
    'ApplicationSettings',
    'SettingsManager',
    'get_settings_manager',
    'get_settings',
    'settings',

    # Licensing
    'LicenseManager',
    'LicenseInfo'
]

# Version info
__version__ = VERSION
__author__ = AUTHOR