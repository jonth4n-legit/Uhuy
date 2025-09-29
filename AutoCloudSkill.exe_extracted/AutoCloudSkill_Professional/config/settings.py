"""
Application settings module using configuration constants.
Professional implementation with proper type hints and validation.
"""

from typing import Dict, Any
from config.constants import *

class Settings:
    """
    Application settings class providing centralized configuration access.

    This class serves as a bridge between constants and the application,
    allowing for dynamic configuration management and validation.
    """

    # API Configuration
    FIREFOX_RELAY_BASE_URL = FIREFOX_RELAY_BASE_URL
    RANDOMUSER_API_URL = RANDOMUSER_API_URL
    CLOUDSKILL_REGISTER_URL = CLOUDSKILL_REGISTER_URL

    # Application Behavior
    DEBUG = DEBUG
    AUTO_SAVE_LOGS = AUTO_SAVE_LOGS
    LOG_LEVEL = LOG_LEVEL
    LOG_FILE = LOG_FILE

    # Browser Settings
    PLAYWRIGHT_HEADLESS = PLAYWRIGHT_HEADLESS
    PLAYWRIGHT_TIMEOUT = PLAYWRIGHT_TIMEOUT
    BROWSER_USER_AGENT = BROWSER_USER_AGENT

    # Default Values
    DEFAULT_GENDER = DEFAULT_GENDER
    DEFAULT_NATIONALITIES = DEFAULT_NATIONALITIES
    DEFAULT_PASSWORD_LENGTH = DEFAULT_PASSWORD_LENGTH

    # Application Info
    VERSION = VERSION
    APP_NAME = APP_NAME
    AUTHOR = AUTHOR

    @classmethod
    def validate_config(cls) -> bool:
        """
        Validate application configuration.

        Returns:
            bool: True if configuration is valid
        """
        return validate_config()

    @classmethod
    def get_browser_options(cls) -> Dict[str, Any]:
        """
        Get browser configuration options.

        Returns:
            Dict[str, Any]: Browser options for Playwright
        """
        return get_browser_options()

    @classmethod
    def get_log_config(cls) -> Dict[str, Any]:
        """
        Get logging configuration.

        Returns:
            Dict[str, Any]: Logging configuration
        """
        return {
            "level": cls.LOG_LEVEL,
            "filename": cls.LOG_FILE,
            "auto_save": cls.AUTO_SAVE_LOGS,
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }

    @classmethod
    def get_default_user_config(cls) -> Dict[str, Any]:
        """
        Get default user generation configuration.

        Returns:
            Dict[str, Any]: Default user configuration
        """
        return {
            "gender": cls.DEFAULT_GENDER,
            "nationalities": cls.DEFAULT_NATIONALITIES.split(","),
            "password_length": cls.DEFAULT_PASSWORD_LENGTH
        }

# Global settings instance
settings = Settings()