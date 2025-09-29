#!/usr/bin/env python3
"""
Auto Cloud Skill Registration Application

Professional rewrite of AutoCloudSkill.exe with clean architecture,
proper error handling, and dual-mode execution (script/executable).

Author: Professional Rewrite by Claude
Original: SinyoRMX
Version: 1.2.0
"""

import sys
import os
import traceback
from pathlib import Path
from typing import Optional

# Add project root to path for both script and bundled mode
def _setup_path() -> Path:
    """Setup Python path for both development and bundled execution."""
    if getattr(sys, 'frozen', False):
        # Running as bundled executable
        bundle_dir = Path(sys.executable).parent
        if hasattr(sys, '_MEIPASS'):
            # PyInstaller bundle
            project_root = Path(sys._MEIPASS)
        else:
            # Other bundler
            project_root = bundle_dir
    else:
        # Running as script
        project_root = Path(__file__).parent

    # Add to Python path
    sys.path.insert(0, str(project_root))
    return project_root

def _setup_runtime_environment(project_root: Path) -> None:
    """Setup runtime environment variables for bundled dependencies."""
    # Setup Playwright browsers path
    playwright_dir = project_root / 'runtime' / 'ms-playwright'
    if not playwright_dir.exists():
        playwright_dir = project_root / 'ms-playwright'

    if playwright_dir.exists() and not os.environ.get('PLAYWRIGHT_BROWSERS_PATH'):
        os.environ['PLAYWRIGHT_BROWSERS_PATH'] = str(playwright_dir)

    # Setup internal dependencies path
    internal_dir = project_root / 'runtime' / '_internal'
    if not internal_dir.exists():
        internal_dir = project_root / '_internal'

    if internal_dir.exists():
        sys.path.insert(0, str(internal_dir))

def main() -> int:
    """
    Main application entry point.

    Returns:
        int: Exit code (0 = success, 1 = error)
    """
    # Setup paths and environment
    project_root = _setup_path()
    _setup_runtime_environment(project_root)

    try:
        # Import after path setup
        from utils.logger import setup_logger
        from gui.main_window import MainWindow
        from config.constants import APP_NAME, VERSION

        # Setup logging
        logger = setup_logger('Main')
        logger.info(f'Starting {APP_NAME} v{VERSION}')
        logger.info(f'Project root: {project_root}')
        logger.info('Environment setup complete')

        # Initialize and run application
        app = MainWindow()
        app.run()

        logger.info('Application terminated normally')
        return 0

    except KeyboardInterrupt:
        print('\n⚠️  Application interrupted by user')
        return 0

    except ImportError as e:
        print(f'❌ Import error: {e}')
        print('\n📋 Installation steps:')
        print('1. Install dependencies: pip install -r requirements.txt')
        print('2. Install Playwright browsers: playwright install chromium')
        print('3. Ensure all runtime files are present')
        return 1

    except Exception as e:
        print(f'❌ Fatal error: {e}')
        print(f'\n🔍 Debug info:')
        print(f'Python: {sys.version}')
        print(f'Platform: {sys.platform}')
        print(f'Frozen: {getattr(sys, "frozen", False)}')
        print(f'Project root: {project_root}')
        print(f'\n📋 Traceback:')
        print(traceback.format_exc())
        return 1

if __name__ == '__main__':
    try:
        exit_code = main()
        sys.exit(exit_code)
    except Exception as e:
        print(f'❌ Critical error in main: {e}')
        sys.exit(1)