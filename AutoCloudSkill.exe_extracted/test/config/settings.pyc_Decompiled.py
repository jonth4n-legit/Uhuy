# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: config\settings.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
Konfigurasi aplikasi - menggunakan constants untuk build dengan Nuitka
"""
from config.constants import *

class Settings:
    """Konfigurasi aplikasi menggunakan constants"""
    FIREFOX_RELAY_API_KEY = FIREFOX_RELAY_API_KEY
    FIREFOX_RELAY_BASE_URL = FIREFOX_RELAY_BASE_URL
    RANDOMUSER_API_URL = RANDOMUSER_API_URL
    DEBUG = DEBUG
    AUTO_SAVE_LOGS = AUTO_SAVE_LOGS
    PLAYWRIGHT_HEADLESS = PLAYWRIGHT_HEADLESS
    PLAYWRIGHT_TIMEOUT = PLAYWRIGHT_TIMEOUT
    CLOUDSKILL_REGISTER_URL = CLOUDSKILL_REGISTER_URL
    LOG_LEVEL = LOG_LEVEL
    LOG_FILE = LOG_FILE
    DEFAULT_GENDER = DEFAULT_GENDER
    DEFAULT_NATIONALITIES = DEFAULT_NATIONALITIES
    DEFAULT_PASSWORD_LENGTH = DEFAULT_PASSWORD_LENGTH
    BROWSER_USER_AGENT = BROWSER_USER_AGENT
    VERSION = VERSION
    APP_NAME = APP_NAME
    AUTHOR = AUTHOR

    @classmethod
    def validate_config(cls) -> bool:
        """
        Validasi konfigurasi yang diperlukan
        
        Returns:
            True jika konfigurasi valid, False jika ada yang missing
        """
        return validate_config()

    @classmethod
    def get_browser_options(cls) -> dict:
        """
        Get browser options untuk Playwright
        
        Returns:
            Dict dengan browser options
        """
        return get_browser_options()
settings = Settings()