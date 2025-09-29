"""
Professional PyInstaller build configuration for AutoCloudSkill.

This module provides comprehensive build automation:
- One-folder executable build
- Runtime dependency bundling
- Professional build optimization
- Cross-platform support

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Optional

import PyInstaller.__main__

def get_project_root() -> Path:
    """Get project root directory."""
    return Path(__file__).parent

def get_runtime_data_files() -> List[tuple]:
    """
    Get runtime data files for bundling.

    Returns:
        List of (source, destination) tuples for PyInstaller
    """
    project_root = get_project_root()
    data_files = []

    # Bundle Playwright browsers
    runtime_dir = project_root / 'runtime'
    if runtime_dir.exists():
        ms_playwright = runtime_dir / 'ms-playwright'
        if ms_playwright.exists():
            data_files.append((str(ms_playwright), 'ms-playwright'))

        internal_dir = runtime_dir / '_internal'
        if internal_dir.exists():
            data_files.append((str(internal_dir), '_internal'))

    return data_files

def get_hidden_imports() -> List[str]:
    """
    Get hidden imports for PyInstaller.

    Returns:
        List of module names to include
    """
    return [
        # Core automation modules
        'automation.cloudskill_automation',
        'automation.confirm_actions',
        'automation.lab_actions_simple',

        # Service modules
        'services.captcha_service',
        'services.firefox_relay_service',
        'services.gmail_service',
        'services.randomuser_service',
        'services.genai_video_service',
        'services.video_postprocess_service',

        # Configuration modules
        'config.constants',
        'config.settings',
        'config.licensing',

        # Utility modules
        'utils.logger',
        'utils.validators',

        # External dependencies
        'playwright.async_api',
        'ttkbootstrap',
        'speech_recognition',
        'google.genai',
        'googleapiclient.discovery',
        'google_auth_oauthlib.flow',
        'requests',
        'aiohttp',
        'PIL',
        'cv2',
        'moviepy.audio.io.AudioFileClip',
        'imageio_ffmpeg',

        # Platform-specific
        'win32gui',
        'win32api',
        'machineid'
    ]

def get_collect_packages() -> List[str]:
    """
    Get packages to collect completely.

    Returns:
        List of package names
    """
    return [
        'playwright',
        'ttkbootstrap',
        'speech_recognition',
        'google',
        'googleapiclient',
        'requests',
        'PIL',
        'cv2'
    ]

def create_runtime_hooks() -> str:
    """
    Create runtime hooks file for PyInstaller.

    Returns:
        Path to runtime hooks file
    """
    project_root = get_project_root()
    hooks_file = project_root / 'runtime_hooks.py'

    hooks_content = '''"""
Runtime hooks for AutoCloudSkill PyInstaller build.

This module configures the runtime environment for bundled execution.
"""

import os
import sys
from pathlib import Path

def _setup_bundled_environment():
    """Setup environment for bundled execution."""
    if getattr(sys, 'frozen', False):
        # Running as bundled executable
        bundle_dir = Path(sys.executable).parent

        # Set PLAYWRIGHT_BROWSERS_PATH
        playwright_dir = bundle_dir / 'ms-playwright'
        if playwright_dir.exists():
            os.environ['PLAYWRIGHT_BROWSERS_PATH'] = str(playwright_dir)

        # Add internal directory to path
        internal_dir = bundle_dir / '_internal'
        if internal_dir.exists():
            sys.path.insert(0, str(internal_dir))

        # Set AntiCaptcha extension path
        anticaptcha_dir = internal_dir / 'AntiCaptcha'
        if anticaptcha_dir.exists():
            os.environ['ANTICAPTCHA_EXTENSION_PATH'] = str(anticaptcha_dir)

# Setup environment immediately
_setup_bundled_environment()
'''

    with open(hooks_file, 'w', encoding='utf-8') as f:
        f.write(hooks_content)

    return str(hooks_file)

def build_executable(
    output_dir: Optional[str] = None,
    name: str = 'AutoCloudSkill',
    console: bool = False,
    optimize: bool = True
) -> bool:
    """
    Build executable using PyInstaller.

    Args:
        output_dir: Output directory for build
        name: Executable name
        console: Show console window
        optimize: Enable build optimizations

    Returns:
        True if build successful, False otherwise
    """
    project_root = get_project_root()

    if output_dir:
        dist_dir = Path(output_dir)
    else:
        dist_dir = project_root / 'dist'

    # Create runtime hooks
    runtime_hooks = create_runtime_hooks()

    # Prepare PyInstaller arguments
    args = [
        '--onedir',  # One-folder bundle
        '--name', name,
        '--distpath', str(dist_dir),
        '--workpath', str(project_root / 'build'),
        '--specpath', str(project_root),
        '--runtime-hook', runtime_hooks
    ]

    # Console/windowed mode
    if console:
        args.append('--console')
    else:
        args.append('--windowed')

    # Add data files
    for source, dest in get_runtime_data_files():
        args.extend(['--add-data', f'{source};{dest}'])

    # Add hidden imports
    for module in get_hidden_imports():
        args.extend(['--hidden-import', module])

    # Collect packages
    for package in get_collect_packages():
        args.extend(['--collect-all', package])

    # Optimization options
    if optimize:
        args.extend([
            '--optimize', '2',
            '--strip',
            '--exclude-module', 'tkinter.test',
            '--exclude-module', 'test',
            '--exclude-module', 'unittest'
        ])

    # Platform-specific options
    if sys.platform.startswith('win'):
        # Windows-specific optimizations
        args.extend([
            '--exclude-module', 'FixTk',
            '--exclude-module', '_tkinter'
        ])

    # Add main script
    main_script = project_root / 'main.py'
    args.append(str(main_script))

    print("🔨 Building AutoCloudSkill executable...")
    print(f"📁 Output directory: {dist_dir}")
    print(f"⚙️ Build options: {'Optimized' if optimize else 'Debug'}, {'Console' if console else 'Windowed'}")

    try:
        # Run PyInstaller
        PyInstaller.__main__.run(args)

        # Verify build
        executable_path = dist_dir / name / f'{name}.exe' if sys.platform.startswith('win') else dist_dir / name / name

        if executable_path.exists():
            print(f"✅ Build successful: {executable_path}")
            print(f"📦 Executable size: {executable_path.stat().st_size / 1024 / 1024:.1f} MB")
            return True
        else:
            print("❌ Build failed: Executable not found")
            return False

    except Exception as e:
        print(f"❌ Build failed: {e}")
        return False

def create_installer_script() -> str:
    """
    Create installation script for easy deployment.

    Returns:
        Path to installer script
    """
    project_root = get_project_root()
    installer_script = project_root / 'install.py'

    installer_content = '''"""
AutoCloudSkill Installation Script

This script helps with dependency installation and environment setup.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False

    print(f"✅ Python {sys.version} is compatible")
    return True

def install_dependencies():
    """Install required dependencies."""
    requirements_file = Path(__file__).parent / 'requirements.txt'

    if not requirements_file.exists():
        print("❌ requirements.txt not found")
        return False

    print("📦 Installing dependencies...")
    try:
        subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-r', str(requirements_file)
        ], check=True)

        print("✅ Dependencies installed successfully")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def install_playwright_browsers():
    """Install Playwright browsers."""
    print("🌐 Installing Playwright browsers...")
    try:
        subprocess.run([
            sys.executable, '-m', 'playwright', 'install', 'chromium'
        ], check=True)

        print("✅ Playwright browsers installed successfully")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Playwright browsers: {e}")
        return False

def main():
    """Main installation process."""
    print("🚀 AutoCloudSkill Installation")
    print("=" * 40)

    if not check_python_version():
        return False

    if not install_dependencies():
        return False

    if not install_playwright_browsers():
        return False

    print("=" * 40)
    print("🎉 Installation completed successfully!")
    print("📝 You can now run: python main.py")
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
'''

    with open(installer_script, 'w', encoding='utf-8') as f:
        f.write(installer_content)

    return str(installer_script)

def clean_build_artifacts():
    """Clean build artifacts and temporary files."""
    project_root = get_project_root()

    # Directories to clean
    clean_dirs = [
        project_root / 'build',
        project_root / '__pycache__',
        project_root / '.pytest_cache'
    ]

    # Files to clean
    clean_files = [
        project_root / 'runtime_hooks.py',
        project_root / 'AutoCloudSkill.spec'
    ]

    cleaned_count = 0

    for directory in clean_dirs:
        if directory.exists():
            shutil.rmtree(directory)
            cleaned_count += 1
            print(f"🗑️ Removed: {directory}")

    for file_path in clean_files:
        if file_path.exists():
            file_path.unlink()
            cleaned_count += 1
            print(f"🗑️ Removed: {file_path}")

    # Clean Python cache files
    for cache_file in project_root.rglob('*.pyc'):
        cache_file.unlink()
        cleaned_count += 1

    for cache_dir in project_root.rglob('__pycache__'):
        if cache_dir.is_dir():
            shutil.rmtree(cache_dir)
            cleaned_count += 1

    print(f"✅ Cleaned {cleaned_count} build artifacts")

def main():
    """Main build script entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='AutoCloudSkill Build System')
    parser.add_argument('--output', '-o', help='Output directory')
    parser.add_argument('--name', '-n', default='AutoCloudSkill', help='Executable name')
    parser.add_argument('--console', '-c', action='store_true', help='Console mode')
    parser.add_argument('--debug', '-d', action='store_true', help='Debug build (no optimization)')
    parser.add_argument('--clean', action='store_true', help='Clean build artifacts only')
    parser.add_argument('--installer', action='store_true', help='Create installer script')

    args = parser.parse_args()

    if args.clean:
        clean_build_artifacts()
        return

    if args.installer:
        installer_path = create_installer_script()
        print(f"✅ Installer script created: {installer_path}")
        return

    # Build executable
    success = build_executable(
        output_dir=args.output,
        name=args.name,
        console=args.console,
        optimize=not args.debug
    )

    if success:
        print("\n🎉 Build completed successfully!")
        print("📝 To run the executable:")
        print(f"   cd dist/{args.name}")
        print(f"   ./{args.name}")
    else:
        print("\n❌ Build failed!")
        sys.exit(1)

if __name__ == '__main__':
    main()