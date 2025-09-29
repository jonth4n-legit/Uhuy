"""
Professional GUI tabs package for AutoCloudSkill Application.

This package contains all tab modules for the main application interface:
- Registration Tab: User data input and validation
- Settings Tab: API configuration and preferences
- Logs Tab: Real-time logging and progress tracking
- Video Generator Tab: GenAI video creation interface
- About Tab: Application and system information

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

from .registration_tab import RegistrationTab
from .settings_tab import SettingsTab
from .logs_tab import LogsTab
from .video_generator_tab import VideoGeneratorTab
from .about_tab import AboutTab

__all__ = [
    'RegistrationTab',
    'SettingsTab',
    'LogsTab',
    'VideoGeneratorTab',
    'AboutTab'
]

__version__ = '2.0.0'
__author__ = 'Claude Opus 4.1 (Professional Rewrite)'