#!/usr/bin/env python3
"""
Main entry point untuk aplikasi Auto Cloud Skill Registration
"""
import sys
import os
import traceback
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

try:
    from gui.main_window import MainWindow
    from config.settings import settings
    from utils.logger import setup_logger, main_logger
except ImportError as e:
    print(f'❌ Import error: {e}')
    print('\nPastikan semua dependencies sudah diinstall:')
    print('pip install -r requirements.txt')
    print('\nDan pastikan Playwright browser sudah diinstall:')
    print('playwright install chromium')
    sys.exit(1)

def main():
    """Main function"""
    logger = setup_logger('Main')
    try:
        logger.info('Starting Auto Cloud Skill Registration application')
        logger.info('Skipping config validation - API key will be input via GUI')
        
        app = MainWindow()
        app.run()
        
        logger.info('Application terminated normally')
        return 0
        
    except KeyboardInterrupt:
        logger.info('Application interrupted by user')
        return 0
    except Exception as e:
        logger.error(f'Unexpected error: {e}')
        logger.error(f'Traceback: {traceback.format_exc()}')
        print(f'\n❌ Unexpected error: {e}')
        print('Check logs for more details.')
        return 1

if __name__ == '__main__':
    try:
        sys.exit(main())
    except ImportError as e:
        print(f'❌ Import error: {e}')
        print('\nPastikan semua dependencies sudah diinstall:')
        print('pip install -r requirements.txt')
        print('\nDan pastikan Playwright browser sudah diinstall:')
        print('playwright install chromium')
        sys.exit(1)
    except Exception as e:
        print(f'❌ Fatal error: {e}')
        print(f'Traceback: {traceback.format_exc()}')
        sys.exit(1)