"""
Application constants for AutoCloudSkill Professional.

This module contains all configuration constants that may need to be
modified for different deployments or builds.

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import os
from typing import Dict, List

# Application Information
APP_NAME = "Auto Cloud Skill Professional"
VERSION = "2.0.0"
AUTHOR = "SinyoRMX (Professional Rewrite by Claude)"
DESCRIPTION = "Professional Google Cloud Skills Boost automation tool"

# Build Configuration
DEBUG = os.getenv('AUTOCLOUDSKILL_DEBUG', 'false').lower() == 'true'
DEVELOPMENT_MODE = os.getenv('AUTOCLOUDSKILL_DEV', 'false').lower() == 'true'

# License Server Configuration
BASE_URL = os.getenv('AUTOCLOUDSKILL_BASE_URL', 'https://sinyormx.vercel.app')
PRODUCT_CODE = 'accsb'

# External Service URLs
FIREFOX_RELAY_API_KEY = os.getenv('FIREFOX_RELAY_API_KEY', 'your_api_key_here')
FIREFOX_RELAY_PRODUCTION_URL = 'https://relay.firefox.com'
FIREFOX_RELAY_DEV_URL = 'https://dev.fxprivaterelay.nonprod.cloudops.mozgcp.net'
FIREFOX_RELAY_BASE_URL = FIREFOX_RELAY_PRODUCTION_URL

RANDOMUSER_API_URL = 'https://randomuser.me/api/'
CLOUDSKILL_REGISTER_URL = 'https://www.cloudskillsboost.google/users/sign_up'

# Google Cloud Skills Boost URLs
CLOUDSKILL_URLS = {
    'register': 'https://www.cloudskillsboost.google/users/sign_up',
    'login': 'https://www.cloudskillsboost.google/users/sign_in',
    'dashboard': 'https://www.cloudskillsboost.google/',
    'labs': 'https://www.cloudskillsboost.google/quests',
    'profile': 'https://www.cloudskillsboost.google/public_profiles',
    'console': 'https://console.cloud.google.com'
}

# Logging Configuration
AUTO_SAVE_LOGS = True
LOG_LEVEL = os.getenv('AUTOCLOUDSKILL_LOG_LEVEL', 'INFO').upper()
LOG_FILE = 'autocloudskill.log'
LOG_MAX_SIZE = 10 * 1024 * 1024  # 10MB
LOG_BACKUP_COUNT = 5
LOG_CLEANUP_DAYS = 7

# Browser Configuration
PLAYWRIGHT_HEADLESS = os.getenv('AUTOCLOUDSKILL_HEADLESS', 'false').lower() == 'true'
PLAYWRIGHT_TIMEOUT = int(os.getenv('AUTOCLOUDSKILL_TIMEOUT', '30000'))
PLAYWRIGHT_SLOW_MO = int(os.getenv('AUTOCLOUDSKILL_SLOW_MO', '100'))  # ms delay between actions

# Browser User Agent
BROWSER_USER_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/120.0.0.0 Safari/537.36'
)

# Alternative user agents for randomization
USER_AGENTS = [
    BROWSER_USER_AGENT,
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/120.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
]

# Default User Data Generation
DEFAULT_GENDER = 'female'
DEFAULT_NATIONALITIES = ['gb', 'us', 'es', 'au', 'ca']
DEFAULT_PASSWORD_LENGTH = 12
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 32

# Captcha Service Configuration
CAPTCHA_SERVICES = {
    'anticaptcha': {
        'enabled': True,
        'timeout': 300,  # 5 minutes
        'retry_attempts': 3
    },
    '2captcha': {
        'enabled': False,
        'timeout': 300,
        'retry_attempts': 3
    }
}

# Automation Timeouts (in milliseconds)
TIMEOUTS = {
    'page_load': 30000,
    'element_wait': 10000,
    'form_submission': 20000,
    'captcha_solve': 300000,  # 5 minutes
    'email_verification': 180000,  # 3 minutes
    'navigation': 15000
}

# Retry Configuration
RETRY_SETTINGS = {
    'max_attempts': 3,
    'delay_between_attempts': 2000,  # 2 seconds
    'exponential_backoff': True,
    'max_delay': 30000  # 30 seconds
}

# Email Configuration
EMAIL_SETTINGS = {
    'verification_timeout': 300,  # 5 minutes
    'check_interval': 10,  # 10 seconds
    'max_checks': 30,
    'supported_providers': [
        'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com',
        'firefox.com', 'relay.firefox.com'
    ]
}

# GUI Configuration
GUI_SETTINGS = {
    'theme': 'darkly',
    'window_size': (800, 700),
    'min_window_size': (650, 600),
    'resizable': True,
    'always_on_top': False,
    'auto_save_settings': True
}

# File Paths
DEFAULT_PATHS = {
    'downloads': os.path.expanduser('~/Downloads'),
    'documents': os.path.expanduser('~/Documents'),
    'desktop': os.path.expanduser('~/Desktop')
}

# Security Settings
SECURITY_SETTINGS = {
    'mask_sensitive_logs': True,
    'encrypt_stored_data': True,
    'secure_memory_clear': True,
    'max_session_duration': 7200,  # 2 hours
    'idle_timeout': 1800  # 30 minutes
}

# Performance Settings
PERFORMANCE_SETTINGS = {
    'max_concurrent_operations': 3,
    'memory_limit_mb': 512,
    'cache_size': 100,
    'preload_resources': True
}

# Feature Flags
FEATURES = {
    'video_generation': True,
    'bulk_registration': True,
    'advanced_captcha': True,
    'email_verification': True,
    'proxy_support': False,  # Future feature
    'dark_web_api': False,   # Future feature
    'ai_assistance': True
}

# Error Messages
ERROR_MESSAGES = {
    'license_invalid': 'License is invalid or expired. Please contact support.',
    'browser_launch_failed': 'Failed to launch browser. Please check Playwright installation.',
    'captcha_solve_failed': 'Failed to solve CAPTCHA. Please try again.',
    'email_verification_failed': 'Email verification failed or timed out.',
    'registration_failed': 'Account registration failed. Please check your information.',
    'network_error': 'Network connection error. Please check your internet connection.'
}

# Success Messages
SUCCESS_MESSAGES = {
    'license_valid': 'License is valid and active.',
    'browser_launched': 'Browser launched successfully.',
    'captcha_solved': 'CAPTCHA solved successfully.',
    'email_verified': 'Email verification completed.',
    'registration_success': 'Account registration completed successfully.',
    'operation_complete': 'Operation completed successfully.'
}

# Validation Rules
VALIDATION_RULES = {
    'email': {
        'max_length': 254,
        'allow_unicode': False,
        'check_disposable': True
    },
    'password': {
        'min_length': 8,
        'max_length': 128,
        'require_uppercase': True,
        'require_lowercase': True,
        'require_digit': True,
        'require_special': True
    },
    'name': {
        'min_length': 2,
        'max_length': 50,
        'allow_unicode': True,
        'allow_spaces': True
    },
    'company': {
        'min_length': 2,
        'max_length': 100,
        'allow_unicode': True,
        'allow_special_chars': True
    }
}

def get_browser_options() -> Dict:
    """
    Get browser options for Playwright.

    Returns:
        Dictionary with browser configuration options
    """
    return {
        'headless': PLAYWRIGHT_HEADLESS,
        'args': [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-accelerated-2d-canvas',
            '--no-first-run',
            '--no-zygote',
            '--disable-gpu',
            '--disable-background-timer-throttling',
            '--disable-backgrounding-occluded-windows',
            '--disable-renderer-backgrounding'
        ],
        'user_agent': BROWSER_USER_AGENT,
        'viewport': {'width': 1280, 'height': 720},
        'ignore_https_errors': True,
        'java_script_enabled': True,
        'accept_downloads': True,
        'slow_mo': PLAYWRIGHT_SLOW_MO if DEBUG else 0
    }

def get_development_config() -> Dict:
    """
    Get development-specific configuration.

    Returns:
        Dictionary with development settings
    """
    if not DEVELOPMENT_MODE:
        return {}

    return {
        'debug_mode': True,
        'verbose_logging': True,
        'disable_license_check': True,
        'mock_services': True,
        'test_data_enabled': True,
        'performance_monitoring': True
    }

def validate_config() -> bool:
    """
    Validate configuration for required settings.

    Returns:
        True if configuration is valid, False otherwise
    """
    required_settings = [
        APP_NAME, VERSION, BASE_URL, PRODUCT_CODE,
        CLOUDSKILL_REGISTER_URL, LOG_LEVEL
    ]

    for setting in required_settings:
        if not setting:
            return False

    # Validate timeouts
    if PLAYWRIGHT_TIMEOUT <= 0:
        return False

    # Validate log level
    valid_log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    if LOG_LEVEL not in valid_log_levels:
        return False

    return True

# Export commonly used items
__all__ = [
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
    'TIMEOUTS', 'RETRY_SETTINGS', 'EMAIL_SETTINGS',
    'GUI_SETTINGS', 'SECURITY_SETTINGS', 'PERFORMANCE_SETTINGS',
    'FEATURES', 'ERROR_MESSAGES', 'SUCCESS_MESSAGES',
    'VALIDATION_RULES',
    'get_browser_options', 'get_development_config', 'validate_config'
]