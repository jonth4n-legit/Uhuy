#!/usr/bin/env python3
"""
PyInstaller build script untuk AutoCloudSkill
Menghasilkan executable yang identik dengan original
"""

import os
import sys
import shutil
from pathlib import Path

def prepare_build():
    """Persiapkan file dan folder untuk build"""
    print("🔧 Preparing build environment...")
    
    # Buat folder dist jika belum ada
    dist_dir = Path("dist")
    dist_dir.mkdir(exist_ok=True)
    
    # Copy assets
    if Path("_internal/assets").exists():
        shutil.copytree("_internal/assets", "assets", dirs_exist_ok=True)
        print("✅ Copied assets/")
    
    # Copy AntiCaptcha extension
    if Path("_internal/AntiCaptcha").exists():
        shutil.copytree("_internal/AntiCaptcha", "AntiCaptcha", dirs_exist_ok=True)
        print("✅ Copied AntiCaptcha/")
    
    # Copy ms-playwright
    if Path("_internal/ms-playwright").exists():
        shutil.copytree("_internal/ms-playwright", "ms-playwright", dirs_exist_ok=True)
        print("✅ Copied ms-playwright/")
    
    print("✅ Build environment prepared!")

def build_executable():
    """Build executable dengan PyInstaller"""
    print("🚀 Building executable...")
    
    import PyInstaller.__main__
    
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--windowed',
        '--name=AutoCloudSkill',
        '--icon=assets/logo.ico',
        '--add-data=assets;assets',
        '--add-data=AntiCaptcha;AntiCaptcha',
        '--add-data=ms-playwright;ms-playwright',
        '--hidden-import=playwright',
        '--hidden-import=google.genai',
        '--hidden-import=ttkbootstrap',
        '--hidden-import=speech_recognition',
        '--hidden-import=moviepy',
        '--hidden-import=imageio_ffmpeg',
        '--hidden-import=machineid',
        '--hidden-import=requests',
        '--hidden-import=beautifulsoup4',
        '--hidden-import=numpy',
        '--hidden-import=PIL',
        '--hidden-import=pydantic',
        '--collect-all=playwright',
        '--collect-all=google',
        '--collect-all=ttkbootstrap',
        '--collect-all=requests',
        '--collect-all=beautifulsoup4',
        '--collect-all=numpy',
        '--collect-all=PIL',
        '--collect-all=pydantic',
        '--distpath=dist',
        '--workpath=build',
        '--specpath=.',
        '--clean'
    ])
    
    print("✅ Build completed!")

def main():
    """Main build function"""
    print("🏗️  AutoCloudSkill Build Script")
    print("=" * 50)
    
    # Check if main.py exists
    if not Path("main.py").exists():
        print("❌ main.py not found!")
        print("Please run this script from the project root directory.")
        sys.exit(1)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print(f"✅ PyInstaller {PyInstaller.__version__} found")
    except ImportError:
        print("❌ PyInstaller not found!")
        print("Please install PyInstaller: pip install pyinstaller")
        sys.exit(1)
    
    # Prepare build environment
    prepare_build()
    
    # Build executable
    build_executable()
    
    print("\n🎉 Build completed successfully!")
    print("📁 Executable location: dist/AutoCloudSkill.exe")
    print("\n📋 Next steps:")
    print("1. Test the executable: dist/AutoCloudSkill.exe")
    print("2. Check if all features work correctly")
    print("3. Distribute the executable")

if __name__ == "__main__":
    main()
