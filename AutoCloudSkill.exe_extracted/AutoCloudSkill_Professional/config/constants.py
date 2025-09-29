"""
Configuration constants for Auto Cloud Skill Registration application.
Professional rewrite with clean structure and proper validation.
"""

# Application Information
APP_NAME = "Auto Cloud Skill"
VERSION = "1.2.0"
AUTHOR = "SinyoRMX"

# API Configuration
BASE_URL = "https://sinyormx.vercel.app"
PRODUCT_CODE = "accsb"

# Firefox Relay Configuration
FIREFOX_RELAY_PRODUCTION_URL = "https://relay.firefox.com"
FIREFOX_RELAY_DEV_URL = "https://dev.fxprivaterelay.nonprod.cloudops.mozgcp.net"
FIREFOX_RELAY_BASE_URL = FIREFOX_RELAY_PRODUCTION_URL

# External APIs
RANDOMUSER_API_URL = "https://randomuser.me/api/"
CLOUDSKILL_REGISTER_URL = "https://www.cloudskillsboost.google/users/sign_up"

# Application Settings
DEBUG = False
AUTO_SAVE_LOGS = True
LOG_LEVEL = "INFO"
LOG_FILE = "autocloudskill.log"

# Browser Configuration
PLAYWRIGHT_HEADLESS = False
PLAYWRIGHT_TIMEOUT = 30000
BROWSER_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

# Default User Data
DEFAULT_GENDER = "female"
DEFAULT_NATIONALITIES = "gb,us,es"
DEFAULT_PASSWORD_LENGTH = 12

def validate_config() -> bool:
    """
    Validate application configuration.

    Note: API keys are now input via GUI, so this always returns True.
    Configuration validation happens at runtime through the UI.

    Returns:
        bool: Always True (legacy compatibility)
    """
    return True

def get_browser_options() -> dict:
    """
    Get browser configuration options for Playwright.

    Returns:
        dict: Browser options dictionary
    """
    return {
        "headless": PLAYWRIGHT_HEADLESS,
        "user_agent": BROWSER_USER_AGENT,
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
        "java_script_enabled": True,
    }