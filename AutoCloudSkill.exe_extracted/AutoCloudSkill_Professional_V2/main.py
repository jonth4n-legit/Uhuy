#!/usr/bin/env python3
"""
Auto Cloud Skill Registration Application

Professional rewrite of AutoCloudSkill.exe with clean architecture,
proper error handling, and dual-mode execution (script/executable).

This application provides:
- Google Cloud Skills Boost automatic registration
- Browser automation with Playwright + AntiCaptcha
- Professional GUI using ttkbootstrap
- Dual execution modes: Python script and standalone executable

Author: Professional Rewrite by Claude Opus 4.1
Original: SinyoRMX
Version: 2.0.0
License: Educational Use Only
"""

import sys
import os
import traceback
import asyncio
from pathlib import Path
from typing import Optional, Dict, Any
import logging

# Configure early logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('autocloudskill.log', encoding='utf-8')
    ]
)

def _setup_application_paths() -> Dict[str, Path]:
    """
    Setup Python paths and detect execution mode.

    Returns:
        Dict containing project_root, runtime_root, and execution_mode
    """
    paths = {}

    if getattr(sys, 'frozen', False):
        # Running as bundled executable (PyInstaller)
        if hasattr(sys, '_MEIPASS'):
            # PyInstaller temporary directory
            paths['project_root'] = Path(sys._MEIPASS)
            paths['runtime_root'] = Path(sys.executable).parent
            paths['execution_mode'] = 'bundled_pyinstaller'
        else:
            # Other bundler or cx_Freeze
            paths['project_root'] = Path(sys.executable).parent
            paths['runtime_root'] = paths['project_root']
            paths['execution_mode'] = 'bundled_other'
    else:
        # Running as Python script
        paths['project_root'] = Path(__file__).resolve().parent
        paths['runtime_root'] = paths['project_root']
        paths['execution_mode'] = 'development'

    # Add project root to Python path
    if str(paths['project_root']) not in sys.path:
        sys.path.insert(0, str(paths['project_root']))

    return paths

def _setup_runtime_environment(paths: Dict[str, Path]) -> None:
    """
    Configure runtime environment for Playwright and other dependencies.

    Args:
        paths: Application paths from _setup_application_paths()
    """
    try:
        # Set PLAYWRIGHT_BROWSERS_PATH for bundled browser
        if not os.environ.get('PLAYWRIGHT_BROWSERS_PATH'):
            runtime_playwright = paths['runtime_root'] / 'runtime' / 'ms-playwright'
            if runtime_playwright.exists():
                os.environ['PLAYWRIGHT_BROWSERS_PATH'] = str(runtime_playwright)
                logging.info(f"Set PLAYWRIGHT_BROWSERS_PATH: {runtime_playwright}")

        # Set additional runtime paths
        runtime_internal = paths['runtime_root'] / 'runtime' / '_internal'
        if runtime_internal.exists():
            # Add to Python path for internal modules
            if str(runtime_internal) not in sys.path:
                sys.path.insert(0, str(runtime_internal))

            # Set AntiCaptcha extension path
            anticaptcha_path = runtime_internal / 'AntiCaptcha'
            if anticaptcha_path.exists():
                os.environ['ANTICAPTCHA_EXTENSION_PATH'] = str(anticaptcha_path)
                logging.info(f"Set AntiCaptcha extension path: {anticaptcha_path}")

        # Set application root for modules
        os.environ['AUTOCLOUDSKILL_ROOT'] = str(paths['project_root'])

    except Exception as e:
        logging.warning(f"Runtime environment setup warning: {e}")

def _validate_dependencies() -> tuple[bool, list[str]]:
    """
    Validate that all required dependencies are available.

    Returns:
        Tuple of (success, missing_dependencies)
    """
    missing = []

    try:
        import tkinter
    except ImportError:
        missing.append("tkinter (GUI framework)")

    try:
        import ttkbootstrap
    except ImportError:
        missing.append("ttkbootstrap (modern GUI theme)")

    try:
        from playwright.async_api import async_playwright
    except ImportError:
        missing.append("playwright (browser automation)")

    try:
        import requests
    except ImportError:
        missing.append("requests (HTTP client)")

    # Check for optional but recommended dependencies
    try:
        import speech_recognition
    except ImportError:
        logging.warning("speech_recognition not available - some features may be limited")

    return len(missing) == 0, missing

def _show_dependency_error(missing_deps: list[str]) -> None:
    """
    Display user-friendly dependency error message.

    Args:
        missing_deps: List of missing dependency names
    """
    print("\n" + "="*60)
    print("❌ MISSING DEPENDENCIES")
    print("="*60)
    print("\nThe following required dependencies are missing:")
    for dep in missing_deps:
        print(f"  • {dep}")

    print("\n📥 INSTALLATION INSTRUCTIONS:")
    print("1. Install all dependencies:")
    print("   pip install -r requirements.txt")
    print("\n2. Install Playwright browser:")
    print("   playwright install chromium")
    print("\n3. Run the application again:")
    print("   python main.py")
    print("\n" + "="*60)

async def main_async() -> int:
    """
    Main async application entry point.

    Returns:
        Exit code (0 for success, 1 for error)
    """
    from gui.main_window import MainWindow
    from utils.logger import setup_application_logging
    from config.settings import settings

    # Setup application-specific logging
    logger = setup_application_logging('Main')

    try:
        logger.info("="*60)
        logger.info("🚀 Starting Auto Cloud Skill Registration Application")
        logger.info(f"Version: 2.0.0 Professional")
        logger.info(f"Python: {sys.version}")
        logger.info(f"Platform: {sys.platform}")
        logger.info("="*60)

        # Initialize and run GUI application
        app = MainWindow()

        logger.info("✅ GUI initialized successfully")
        logger.info("🎯 Starting main application loop...")

        # Start the GUI main loop
        await app.run_async()

        logger.info("✅ Application terminated normally")
        return 0

    except KeyboardInterrupt:
        logger.info("⚡ Application interrupted by user (Ctrl+C)")
        return 0

    except ImportError as e:
        logger.error(f"❌ Import error: {e}")
        logger.error("Check that all dependencies are installed correctly")
        print(f"\n❌ Import error: {e}")
        print("Run: pip install -r requirements.txt")
        return 1

    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        print(f"\n❌ Unexpected error: {e}")
        print("Check logs/autocloudskill.log for detailed information")
        return 1

def main() -> int:
    """
    Synchronous main entry point that handles async execution.

    Returns:
        Exit code (0 for success, 1 for error)
    """
    try:
        # Setup application paths and environment
        paths = _setup_application_paths()
        _setup_runtime_environment(paths)

        print("🔧 Auto Cloud Skill Registration v2.0.0")
        print(f"📁 Execution mode: {paths['execution_mode']}")
        print(f"📂 Project root: {paths['project_root']}")

        # Validate dependencies
        deps_ok, missing_deps = _validate_dependencies()
        if not deps_ok:
            _show_dependency_error(missing_deps)
            return 1

        print("✅ Dependencies validated")
        print("🚀 Starting application...\n")

        # Run async main function
        if sys.platform == "win32":
            # Use ProactorEventLoop on Windows for better performance
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

        return asyncio.run(main_async())

    except KeyboardInterrupt:
        print("\n⚡ Application interrupted by user")
        return 0

    except Exception as e:
        print(f"\n❌ Fatal startup error: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        return 1

if __name__ == '__main__':
    try:
        exit_code = main()
        sys.exit(exit_code)
    except SystemExit:
        raise
    except Exception as e:
        print(f"\n💥 Critical error during startup: {e}")
        sys.exit(1)