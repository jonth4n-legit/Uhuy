"""
Professional application settings for AutoCloudSkill.

This module provides a centralized settings management system with:
- Environment-aware configuration
- Runtime setting modification
- Configuration validation
- Settings persistence
- Development/production modes

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import os
import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional, Union
from dataclasses import dataclass, asdict

from .constants import (
    APP_NAME, VERSION, AUTHOR, DEBUG, DEVELOPMENT_MODE,
    LOG_LEVEL, LOG_FILE, AUTO_SAVE_LOGS, LOG_MAX_SIZE, LOG_BACKUP_COUNT,
    PLAYWRIGHT_HEADLESS, PLAYWRIGHT_TIMEOUT, PLAYWRIGHT_SLOW_MO, BROWSER_USER_AGENT,
    FIREFOX_RELAY_API_KEY, FIREFOX_RELAY_BASE_URL, RANDOMUSER_API_URL,
    DEFAULT_GENDER, DEFAULT_NATIONALITIES, DEFAULT_PASSWORD_LENGTH,
    CLOUDSKILL_REGISTER_URL, CLOUDSKILL_URLS
)


@dataclass
class ApplicationSettings:
    """Application settings with type hints and default values."""

    # Application
    app_name: str = APP_NAME
    version: str = VERSION
    author: str = AUTHOR
    debug: bool = DEBUG
    development_mode: bool = DEVELOPMENT_MODE

    # Logging
    log_level: str = LOG_LEVEL
    log_file: str = LOG_FILE
    auto_save_logs: bool = AUTO_SAVE_LOGS
    log_max_size: int = LOG_MAX_SIZE
    log_backup_count: int = LOG_BACKUP_COUNT

    # Browser
    playwright_headless: bool = PLAYWRIGHT_HEADLESS
    playwright_timeout: int = PLAYWRIGHT_TIMEOUT
    playwright_slow_mo: int = PLAYWRIGHT_SLOW_MO
    browser_user_agent: str = BROWSER_USER_AGENT

    # Services
    firefox_relay_api_key: str = FIREFOX_RELAY_API_KEY
    firefox_relay_base_url: str = FIREFOX_RELAY_BASE_URL
    randomuser_api_url: str = RANDOMUSER_API_URL

    # CloudSkill URLs
    cloudskill_register_url: str = CLOUDSKILL_REGISTER_URL
    cloudskill_urls: Dict[str, str] = None

    # User Generation
    default_gender: str = DEFAULT_GENDER
    default_nationalities: str = ','.join(DEFAULT_NATIONALITIES)
    default_password_length: int = DEFAULT_PASSWORD_LENGTH

    # GUI Settings
    gui_theme: str = 'darkly'
    window_width: int = 800
    window_height: int = 700
    window_resizable: bool = True
    auto_save_settings: bool = True

    # Security Settings
    mask_sensitive_logs: bool = True
    encrypt_stored_data: bool = False
    max_session_duration: int = 3600

    # Performance Settings
    max_concurrent_operations: int = 5
    memory_limit_mb: int = 512
    cache_size: int = 100

    # Feature Flags
    enable_video_generation: bool = True
    enable_bulk_registration: bool = True
    enable_advanced_captcha: bool = True
    enable_email_verification: bool = True
    enable_ai_assistance: bool = True

    def __post_init__(self):
        """Initialize computed fields after dataclass creation."""
        if self.cloudskill_urls is None:
            self.cloudskill_urls = CLOUDSKILL_URLS

    def to_dict(self) -> Dict[str, Any]:
        """Convert settings to dictionary.

        Returns:
            Dictionary representation of settings
        """
        return asdict(self)

    def update_from_dict(self, data: Dict[str, Any]) -> None:
        """Update settings from dictionary.

        Args:
            data: Dictionary with setting updates
        """
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def save_to_file(self, file_path: Union[str, Path]) -> None:
        """Save settings to JSON file.

        Args:
            file_path: Path to save settings file
        """
        try:
            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)

        except Exception as e:
            logging.warning(f"Failed to save settings to {file_path}: {e}")

    def load_from_file(self, file_path: Union[str, Path]) -> bool:
        """Load settings from JSON file.

        Args:
            file_path: Path to settings file

        Returns:
            True if loaded successfully, False otherwise
        """
        try:
            file_path = Path(file_path)

            if not file_path.exists():
                return False

            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.update_from_dict(data)
            return True

        except Exception as e:
            logging.warning(f"Failed to load settings from {file_path}: {e}")
            return False

    def get_settings_file_path(self) -> Path:
        """Get default settings file path.

        Returns:
            Path to settings file
        """
        if self.development_mode:
            return Path('settings.json')
        else:
            # Use user's app data directory
            app_data = Path.home() / '.autocloudskill'
            app_data.mkdir(exist_ok=True)
            return app_data / 'settings.json'

    def load_settings(self) -> None:
        """Load settings from default location."""
        settings_file = self.get_settings_file_path()
        self.load_from_file(settings_file)

    def save_settings(self) -> None:
        """Save settings to default location."""
        if self.auto_save_settings:
            settings_file = self.get_settings_file_path()
            self.save_to_file(settings_file)

    def reset_to_defaults(self) -> None:
        """Reset all settings to default values."""
        default_settings = ApplicationSettings()
        self.update_from_dict(default_settings.to_dict())

    def validate_settings(self) -> Dict[str, str]:
        """Validate current settings and return any errors.

        Returns:
            Dictionary with validation errors (empty if all valid)
        """
        errors = {}

        # Validate timeouts
        if self.playwright_timeout < 1000:
            errors['playwright_timeout'] = 'Must be at least 1000ms'

        # Validate memory limit
        if self.memory_limit_mb < 128:
            errors['memory_limit_mb'] = 'Must be at least 128MB'

        # Validate password length
        if not (8 <= self.default_password_length <= 32):
            errors['default_password_length'] = 'Must be between 8 and 32 characters'

        # Validate log level
        valid_log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if self.log_level.upper() not in valid_log_levels:
            errors['log_level'] = f'Must be one of: {", ".join(valid_log_levels)}'

        return errors

    def apply_environment_overrides(self) -> None:
        """Apply environment variable overrides to settings."""
        env_mappings = {
            'AUTOCLOUDSKILL_DEBUG': ('debug', lambda x: x.lower() == 'true'),
            'AUTOCLOUDSKILL_LOG_LEVEL': ('log_level', str.upper),
            'AUTOCLOUDSKILL_HEADLESS': ('playwright_headless', lambda x: x.lower() == 'true'),
            'AUTOCLOUDSKILL_TIMEOUT': ('playwright_timeout', int),
            'FIREFOX_RELAY_API_KEY': ('firefox_relay_api_key', str),
        }

        for env_var, (setting_name, converter) in env_mappings.items():
            env_value = os.getenv(env_var)
            if env_value is not None:
                try:
                    converted_value = converter(env_value)
                    setattr(self, setting_name, converted_value)
                except (ValueError, TypeError) as e:
                    logging.warning(f"Invalid environment variable {env_var}={env_value}: {e}")


class SettingsManager:
    """Centralized settings management."""

    def __init__(self):
        """Initialize settings manager."""
        self._settings = ApplicationSettings()
        self._settings.apply_environment_overrides()
        self._settings.load_settings()

    @property
    def settings(self) -> ApplicationSettings:
        """Get current settings instance.

        Returns:
            Current application settings
        """
        return self._settings

    def update_setting(self, key: str, value: Any) -> bool:
        """Update a single setting.

        Args:
            key: Setting name
            value: New value

        Returns:
            True if updated successfully
        """
        if hasattr(self._settings, key):
            setattr(self._settings, key, value)
            self._settings.save_settings()
            return True
        return False

    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a setting value.

        Args:
            key: Setting name
            default: Default value if not found

        Returns:
            Setting value or default
        """
        return getattr(self._settings, key, default)

    def reset_settings(self) -> None:
        """Reset all settings to defaults."""
        self._settings.reset_to_defaults()
        self._settings.save_settings()

    def validate_all_settings(self) -> Dict[str, str]:
        """Validate all current settings.

        Returns:
            Dictionary with validation errors
        """
        return self._settings.validate_settings()


# Global settings instance
_settings_manager = None


def get_settings_manager() -> SettingsManager:
    """Get global settings manager instance.

    Returns:
        Global settings manager
    """
    global _settings_manager
    if _settings_manager is None:
        _settings_manager = SettingsManager()
    return _settings_manager


def get_settings() -> ApplicationSettings:
    """Get current application settings.

    Returns:
        Current application settings
    """
    return get_settings_manager().settings


# Create global settings instance for easy access
settings = get_settings()


# Export commonly used settings for convenience
DEFAULT_GENDER = settings.default_gender
DEFAULT_NATIONALITIES = settings.default_nationalities.split(',')
DEFAULT_PASSWORD_LENGTH = settings.default_password_length