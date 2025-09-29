#!/usr/bin/env python3
"""
Build configuration for Auto Cloud Skill Registration application.

Professional PyInstaller build script with proper dependency bundling,
runtime hooks, and asset management for dual-mode execution.
"""

import PyInstaller.__main__
import os
import sys
import shutil
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def ensure_runtime_dependencies() -> bool:
    """
    Ensure runtime dependencies are available for bundling.

    Returns:
        bool: True if all dependencies are available
    """
    base_dir = Path(__file__).parent
    missing_deps = []

    # Check for ms-playwright
    playwright_dirs = [
        base_dir.parent / "ms-playwright",
        base_dir / "runtime" / "ms-playwright"
    ]

    playwright_found = False
    for playwright_dir in playwright_dirs:
        if playwright_dir.exists():
            playwright_found = True
            logger.info(f"Found Playwright browsers at: {playwright_dir}")
            break

    if not playwright_found:
        missing_deps.append("ms-playwright (Playwright browsers)")

    # Check for _internal
    internal_dirs = [
        base_dir.parent / "_internal",
        base_dir / "runtime" / "_internal"
    ]

    internal_found = False
    for internal_dir in internal_dirs:
        if internal_dir.exists():
            internal_found = True
            logger.info(f"Found internal dependencies at: {internal_dir}")
            break

    if not internal_found:
        missing_deps.append("_internal (Python runtime dependencies)")

    # Check for AntiCaptcha extension
    anticaptcha_dirs = []
    for internal_dir in internal_dirs:
        if internal_dir.exists():
            anticaptcha_dirs.append(internal_dir / "AntiCaptcha")

    anticaptcha_found = False
    for anticaptcha_dir in anticaptcha_dirs:
        if anticaptcha_dir.exists() and (anticaptcha_dir / "manifest.json").exists():
            anticaptcha_found = True
            logger.info(f"Found AntiCaptcha extension at: {anticaptcha_dir}")
            break

    if not anticaptcha_found:
        logger.warning("AntiCaptcha extension not found (optional)")

    if missing_deps:
        logger.error("Missing runtime dependencies:")
        for dep in missing_deps:
            logger.error(f"  - {dep}")
        return False

    return True

def copy_runtime_dependencies() -> None:
    """Copy runtime dependencies to the runtime directory."""
    base_dir = Path(__file__).parent
    runtime_dir = base_dir / "runtime"

    # Create runtime directory
    runtime_dir.mkdir(exist_ok=True)

    # Copy ms-playwright
    source_playwright = base_dir.parent / "ms-playwright"
    dest_playwright = runtime_dir / "ms-playwright"

    if source_playwright.exists() and not dest_playwright.exists():
        logger.info("Copying Playwright browsers...")
        shutil.copytree(source_playwright, dest_playwright)

    # Copy _internal
    source_internal = base_dir.parent / "_internal"
    dest_internal = runtime_dir / "_internal"

    if source_internal.exists() and not dest_internal.exists():
        logger.info("Copying internal dependencies...")
        shutil.copytree(source_internal, dest_internal)

def create_runtime_hook() -> Path:
    """
    Create PyInstaller runtime hook for path resolution.

    Returns:
        Path: Path to the created runtime hook
    """
    hook_content = '''"""
Runtime hook for Auto Cloud Skill Registration application.
Sets up environment variables and paths for bundled execution.
"""

import os
import sys
from pathlib import Path

def setup_bundled_environment():
    """Setup environment for bundled application."""
    if getattr(sys, 'frozen', False):
        # Running as bundled executable
        if hasattr(sys, '_MEIPASS'):
            # PyInstaller bundle
            bundle_dir = Path(sys._MEIPASS)
        else:
            # Other bundler
            bundle_dir = Path(sys.executable).parent

        # Set Playwright browsers path
        playwright_dirs = [
            bundle_dir / 'ms-playwright',
            bundle_dir / 'runtime' / 'ms-playwright'
        ]

        for playwright_dir in playwright_dirs:
            if playwright_dir.exists():
                os.environ['PLAYWRIGHT_BROWSERS_PATH'] = str(playwright_dir)
                break

        # Add internal dependencies to path
        internal_dirs = [
            bundle_dir / '_internal',
            bundle_dir / 'runtime' / '_internal'
        ]

        for internal_dir in internal_dirs:
            if internal_dir.exists():
                sys.path.insert(0, str(internal_dir))
                break

# Setup environment
setup_bundled_environment()
'''

    hook_file = Path(__file__).parent / "runtime_hook.py"
    with open(hook_file, 'w', encoding='utf-8') as f:
        f.write(hook_content)

    logger.info(f"Created runtime hook: {hook_file}")
    return hook_file

def build_executable() -> bool:
    """
    Build the executable using PyInstaller.

    Returns:
        bool: True if build successful
    """
    try:
        # Ensure dependencies are available
        if not ensure_runtime_dependencies():
            logger.error("Cannot build: missing runtime dependencies")
            return False

        # Copy dependencies to runtime directory
        copy_runtime_dependencies()

        # Create runtime hook
        runtime_hook = create_runtime_hook()

        # Build configuration
        base_dir = Path(__file__).parent
        main_script = base_dir / "main.py"

        if not main_script.exists():
            logger.error(f"Main script not found: {main_script}")
            return False

        # PyInstaller arguments
        pyinstaller_args = [
            str(main_script),
            '--onedir',
            '--windowed',
            '--name=AutoCloudSkill',
            '--distpath=dist',
            '--workpath=build',
            '--specpath=build',

            # Runtime hook
            f'--runtime-hook={runtime_hook}',

            # Data files
            '--add-data=runtime/ms-playwright;ms-playwright',
            '--add-data=runtime/_internal;_internal',

            # Hidden imports
            '--hidden-import=automation.cloudskill_automation',
            '--hidden-import=services.randomuser_service',
            '--hidden-import=services.firefox_relay_service',
            '--hidden-import=services.captcha_service',
            '--hidden-import=gui.main_window',
            '--hidden-import=playwright.async_api',
            '--hidden-import=ttkbootstrap',
            '--hidden-import=speech_recognition',
            '--hidden-import=requests',
            '--hidden-import=google.generativeai',

            # Collect packages
            '--collect-all=playwright',
            '--collect-all=ttkbootstrap',
            '--collect-data=ttkbootstrap',

            # Optimization
            '--noconfirm',
            '--clean',

            # Console for debugging (remove for release)
            '--console',
        ]

        # Add icon if available
        icon_path = base_dir / "assets" / "icon.ico"
        if icon_path.exists():
            pyinstaller_args.append(f'--icon={icon_path}')

        logger.info("Starting PyInstaller build...")
        logger.info(f"Build arguments: {' '.join(pyinstaller_args)}")

        # Run PyInstaller
        PyInstaller.__main__.run(pyinstaller_args)

        # Verify build
        dist_dir = base_dir / "dist" / "AutoCloudSkill"
        exe_file = dist_dir / "AutoCloudSkill.exe"

        if exe_file.exists():
            logger.info(f"Build successful! Executable created at: {exe_file}")
            logger.info(f"Distribution directory: {dist_dir}")

            # Show build summary
            logger.info("\n" + "="*50)
            logger.info("BUILD SUMMARY")
            logger.info("="*50)
            logger.info(f"Executable: {exe_file}")
            logger.info(f"Size: {exe_file.stat().st_size / (1024*1024):.1f} MB")
            logger.info(f"Dependencies bundled:")

            if (dist_dir / "ms-playwright").exists():
                logger.info(f"  ✅ Playwright browsers")

            if (dist_dir / "_internal").exists():
                logger.info(f"  ✅ Python runtime")

                if (dist_dir / "_internal" / "AntiCaptcha").exists():
                    logger.info(f"  ✅ AntiCaptcha extension")

            logger.info("="*50)
            return True
        else:
            logger.error("Build failed: executable not found")
            return False

    except Exception as e:
        logger.error(f"Build failed with error: {e}")
        return False

def build_development_mode() -> bool:
    """
    Setup for development mode execution.

    Returns:
        bool: True if setup successful
    """
    try:
        logger.info("Setting up development mode...")

        # Ensure dependencies are copied to runtime directory
        copy_runtime_dependencies()

        # Verify main script can be run
        base_dir = Path(__file__).parent
        main_script = base_dir / "main.py"

        if not main_script.exists():
            logger.error(f"Main script not found: {main_script}")
            return False

        logger.info("Development mode setup complete!")
        logger.info(f"Run with: python {main_script}")
        return True

    except Exception as e:
        logger.error(f"Development setup failed: {e}")
        return False

def clean_build() -> None:
    """Clean build artifacts."""
    base_dir = Path(__file__).parent

    # Directories to clean
    clean_dirs = [
        base_dir / "build",
        base_dir / "dist",
        base_dir / "__pycache__"
    ]

    # Files to clean
    clean_files = [
        base_dir / "runtime_hook.py"
    ]

    for clean_dir in clean_dirs:
        if clean_dir.exists():
            logger.info(f"Removing: {clean_dir}")
            shutil.rmtree(clean_dir)

    for clean_file in clean_files:
        if clean_file.exists():
            logger.info(f"Removing: {clean_file}")
            clean_file.unlink()

    logger.info("Build artifacts cleaned")

def main():
    """Main build script entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Build Auto Cloud Skill Registration application")
    parser.add_argument("--mode", choices=["build", "dev", "clean"], default="build",
                       help="Build mode: build (executable), dev (development), clean (clean artifacts)")

    args = parser.parse_args()

    if args.mode == "clean":
        clean_build()
    elif args.mode == "dev":
        success = build_development_mode()
        sys.exit(0 if success else 1)
    else:  # build
        success = build_executable()
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()