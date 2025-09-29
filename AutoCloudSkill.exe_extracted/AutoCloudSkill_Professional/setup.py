#!/usr/bin/env python3
"""
Setup script for Auto Cloud Skill Registration application.

Automated environment setup, dependency installation, and validation.
"""

import subprocess
import sys
import os
from pathlib import Path
import logging
import shutil

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def check_python_version() -> bool:
    """
    Check if Python version meets requirements.

    Returns:
        bool: True if Python version is compatible
    """
    version = sys.version_info
    if version.major != 3 or version.minor < 8:
        logger.error(f"Python 3.8+ required, found {version.major}.{version.minor}")
        return False

    logger.info(f"Python version OK: {version.major}.{version.minor}.{version.micro}")
    return True

def install_dependencies() -> bool:
    """
    Install Python dependencies from requirements.txt.

    Returns:
        bool: True if installation successful
    """
    try:
        requirements_file = Path(__file__).parent / "requirements.txt"

        if not requirements_file.exists():
            logger.error("requirements.txt not found")
            return False

        logger.info("Installing Python dependencies...")

        # Upgrade pip first
        subprocess.run([
            sys.executable, "-m", "pip", "install", "--upgrade", "pip"
        ], check=True)

        # Install requirements
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ], check=True)

        logger.info("Dependencies installed successfully")
        return True

    except subprocess.CalledProcessError as e:
        logger.error(f"Dependency installation failed: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during installation: {e}")
        return False

def install_playwright_browsers() -> bool:
    """
    Install Playwright browsers if not bundled.

    Returns:
        bool: True if browsers are available
    """
    try:
        # Check if browsers are already bundled
        base_dir = Path(__file__).parent
        bundled_playwright = [
            base_dir / "runtime" / "ms-playwright",
            base_dir.parent / "ms-playwright"
        ]

        for playwright_dir in bundled_playwright:
            if playwright_dir.exists():
                logger.info(f"Using bundled Playwright browsers at: {playwright_dir}")
                return True

        # Install browsers via playwright
        logger.info("Installing Playwright browsers...")
        subprocess.run([
            sys.executable, "-m", "playwright", "install", "chromium"
        ], check=True)

        logger.info("Playwright browsers installed successfully")
        return True

    except subprocess.CalledProcessError as e:
        logger.error(f"Playwright browser installation failed: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during browser installation: {e}")
        return False

def verify_installation() -> bool:
    """
    Verify that all components are properly installed.

    Returns:
        bool: True if verification successful
    """
    try:
        logger.info("Verifying installation...")

        # Test imports
        test_imports = [
            "tkinter",
            "ttkbootstrap",
            "playwright",
            "requests",
            "speech_recognition",
            "moviepy",
            "numpy",
            "PIL"
        ]

        failed_imports = []

        for module in test_imports:
            try:
                __import__(module)
                logger.debug(f"✅ {module}")
            except ImportError:
                failed_imports.append(module)
                logger.error(f"❌ {module}")

        if failed_imports:
            logger.error(f"Import verification failed for: {', '.join(failed_imports)}")
            return False

        # Test Playwright
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                browser.close()
            logger.info("✅ Playwright browser test successful")
        except Exception as e:
            logger.warning(f"Playwright test failed (may need browsers): {e}")

        logger.info("Installation verification completed")
        return True

    except Exception as e:
        logger.error(f"Verification failed: {e}")
        return False

def setup_environment_variables() -> None:
    """Setup recommended environment variables."""
    try:
        # Set UTF-8 encoding
        os.environ['PYTHONIOENCODING'] = 'utf-8'

        # Set Playwright browsers path if bundled
        base_dir = Path(__file__).parent
        playwright_dirs = [
            base_dir / "runtime" / "ms-playwright",
            base_dir.parent / "ms-playwright"
        ]

        for playwright_dir in playwright_dirs:
            if playwright_dir.exists():
                os.environ['PLAYWRIGHT_BROWSERS_PATH'] = str(playwright_dir)
                logger.info(f"Set PLAYWRIGHT_BROWSERS_PATH to: {playwright_dir}")
                break

        logger.info("Environment variables configured")

    except Exception as e:
        logger.warning(f"Could not setup environment variables: {e}")

def create_shortcuts() -> bool:
    """
    Create desktop shortcuts (Windows only).

    Returns:
        bool: True if shortcuts created successfully
    """
    try:
        if sys.platform != "win32":
            logger.info("Shortcuts only supported on Windows")
            return True

        # Try to create shortcut
        import winshell
        from win32com.client import Dispatch

        desktop = winshell.desktop()
        main_script = Path(__file__).parent / "main.py"

        shortcut_path = os.path.join(desktop, "Auto Cloud Skill.lnk")

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = sys.executable
        shortcut.Arguments = f'"{main_script}"'
        shortcut.WorkingDirectory = str(main_script.parent)
        shortcut.IconLocation = sys.executable
        shortcut.save()

        logger.info(f"Desktop shortcut created: {shortcut_path}")
        return True

    except ImportError:
        logger.info("Shortcut creation requires pywin32 (optional)")
        return True
    except Exception as e:
        logger.warning(f"Could not create shortcuts: {e}")
        return True

def setup_application() -> bool:
    """
    Complete application setup process.

    Returns:
        bool: True if setup successful
    """
    logger.info("Starting Auto Cloud Skill Registration setup...")

    # Check Python version
    if not check_python_version():
        return False

    # Install dependencies
    if not install_dependencies():
        return False

    # Install Playwright browsers
    if not install_playwright_browsers():
        return False

    # Setup environment
    setup_environment_variables()

    # Verify installation
    if not verify_installation():
        return False

    # Create shortcuts
    create_shortcuts()

    logger.info("\n" + "="*50)
    logger.info("SETUP COMPLETED SUCCESSFULLY!")
    logger.info("="*50)
    logger.info("The application is ready to use.")
    logger.info("\nTo run the application:")
    logger.info(f"  python {Path(__file__).parent / 'main.py'}")
    logger.info("\nTo build an executable:")
    logger.info(f"  python {Path(__file__).parent / 'build_config.py'}")
    logger.info("="*50)

    return True

def main():
    """Main setup entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Setup Auto Cloud Skill Registration application")
    parser.add_argument("--verify-only", action="store_true",
                       help="Only verify installation, don't install anything")

    args = parser.parse_args()

    if args.verify_only:
        success = verify_installation()
    else:
        success = setup_application()

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()