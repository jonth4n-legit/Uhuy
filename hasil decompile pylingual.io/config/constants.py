# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: config\constants.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
Constants untuk aplikasi Auto Cloud Skill Registration
Ganti nilai sesuai kebutuhan sebelum build dengan Nuitka
"""
BASE_URL: str = 'https://sinyormx.vercel.app'
PRODUCT_CODE: str = 'accsb'
FIREFOX_RELAY_API_KEY = 'your_api_key_here'
FIREFOX_RELAY_PRODUCTION_URL = 'https://relay.firefox.com'
FIREFOX_RELAY_DEV_URL = 'https://dev.fxprivaterelay.nonprod.cloudops.mozgcp.net'
FIREFOX_RELAY_BASE_URL = FIREFOX_RELAY_PRODUCTION_URL
RANDOMUSER_API_URL = 'https://randomuser.me/api/'
DEBUG = False
AUTO_SAVE_LOGS = True
PLAYWRIGHT_HEADLESS = False
PLAYWRIGHT_TIMEOUT = 30000
CLOUDSKILL_REGISTER_URL = 'https://www.cloudskillsboost.google/users/sign_up'
LOG_LEVEL = 'INFO'
LOG_FILE = 'autocloudskill.log'
DEFAULT_GENDER = 'female'
DEFAULT_NATIONALITIES = 'gb,us,es'
DEFAULT_PASSWORD_LENGTH = 12
BROWSER_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
VERSION = '1.2.0'
APP_NAME = 'Auto Cloud Skill'
AUTHOR = 'SinyoRMX'

def validate_config() -> bool:
    """
    Validasi konfigurasi yang diperlukan - DEPRECATED
    API Key sekarang diinput via GUI, jadi tidak perlu validasi di startup
    
    Returns:
        Always True - validation moved to GUI
    """
    return True

def get_browser_options() -> dict:
    """
    Get browser options untuk Playwright
    
    Returns:
        Dict dengan browser options
    """
    return {
        'headless': PLAYWRIGHT_HEADLESS,
        'timeout': PLAYWRIGHT_TIMEOUT,
        'user_agent': BROWSER_USER_AGENT
    }