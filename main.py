#!/usr/bin/env python3
"""
Auto Cloud Skill Registration - Main Application
Fixed and optimized version of the decompiled code

This application automates Google Cloud Skills Boost registration using:
- Firefox Relay for email management
- Playwright for browser automation
- Gmail API for email confirmation
- Google GenAI for video generation

Features:
- Automated account registration
- Email confirmation handling
- Lab automation with API key extraction
- Video generation using Google GenAI
- Comprehensive logging and error handling
"""

import sys
import os
import traceback
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def check_dependencies():
    """Check if all required dependencies are installed"""
    missing_deps = []
    
    try:
        import tkinter
    except ImportError:
        missing_deps.append('tkinter')
    
    try:
        import ttkbootstrap
    except ImportError:
        missing_deps.append('ttkbootstrap')
    
    try:
        import requests
    except ImportError:
        missing_deps.append('requests')
    
    try:
        import playwright
    except ImportError:
        missing_deps.append('playwright')
    
    try:
        from google import genai
    except ImportError:
        missing_deps.append('google-genai')
    
    if missing_deps:
        print("❌ Missing dependencies:")
        for dep in missing_deps:
            print(f"   - {dep}")
        print("\nPlease install missing dependencies:")
        print("pip install -r requirements.txt")
        print("\nFor Playwright browser:")
        print("playwright install chromium")
        return False
    
    return True

def setup_directories():
    """Create necessary directories"""
    directories = [
        project_root / 'logs',
        project_root / 'temp',
        project_root / 'output',
        project_root / 'assets'
    ]
    
    for directory in directories:
        directory.mkdir(exist_ok=True)

def main():
    """Main application entry point"""
    print("🚀 Starting Auto Cloud Skill Registration...")
    
    # Check dependencies
    if not check_dependencies():
        return 1
    
    # Setup directories
    setup_directories()
    
    try:
        # Import after dependency check
        from gui.main_window import MainWindow
        from config.settings import settings
        from utils.logger import setup_logger
        
        # Setup logging
        logger = setup_logger('Main')
        logger.info('Starting Auto Cloud Skill Registration application')
        logger.info('Skipping config validation - API key will be input via GUI')
        
        # Create and run application
        app = MainWindow()
        app.run()
        
        logger.info('Application terminated normally')
        return 0
        
    except KeyboardInterrupt:
        print("\n⏹️ Application interrupted by user")
        return 0
    except ImportError as e:
        print(f'❌ Import error: {e}')
        print('\nPastikan semua dependencies sudah diinstall:')
        print('pip install -r requirements.txt')
        print('\nDan pastikan Playwright browser sudah diinstall:')
        print('playwright install chromium')
        return 1
    except Exception as e:
        print(f'❌ Unexpected error: {e}')
        print(f'Traceback: {traceback.format_exc()}')
        print('\nCheck logs for more details.')
        return 1

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        print(f'❌ Fatal error: {e}')
        print(f'Traceback: {traceback.format_exc()}')
        sys.exit(1)