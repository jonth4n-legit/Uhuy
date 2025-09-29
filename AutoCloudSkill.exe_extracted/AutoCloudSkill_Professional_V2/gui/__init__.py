"""
Professional GUI package for AutoCloudSkill Application.

This package provides a complete professional GUI implementation with:
- Modern dark-themed interface using ttkbootstrap
- Multi-tab layout for organized functionality
- Real-time logging and progress tracking
- Comprehensive settings management
- Professional video generation interface
- Application information and system details

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

# GUI module imports for easier access
from .main_window import MainWindow

# Tab modules
from .tabs.registration_tab import RegistrationTab
from .tabs.settings_tab import SettingsTab
from .tabs.logs_tab import LogsTab
from .tabs.video_generator_tab import VideoGeneratorTab
from .tabs.about_tab import AboutTab

__all__ = [
    'MainWindow',
    'RegistrationTab',
    'SettingsTab',
    'LogsTab',
    'VideoGeneratorTab',
    'AboutTab'
]

__version__ = '2.0.0'
__author__ = 'Claude Opus 4.1 (Professional Rewrite)'