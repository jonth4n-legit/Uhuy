#!/usr/bin/env python3
"""
Test script to verify all fixed modules are working correctly.
Run this to check which components are functional.
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

def test_imports():
    """Test if all modules can be imported"""
    print("=" * 60)
    print("Testing Module Imports")
    print("=" * 60)
    
    tests = []
    
    # Config modules
    try:
        from config import constants, settings, licensing
        tests.append(("✅", "config.constants"))
        tests.append(("✅", "config.settings"))
        tests.append(("✅", "config.licensing"))
    except Exception as e:
        tests.append(("❌", f"config: {e}"))
    
    # Utils modules
    try:
        from utils import logger, validators
        tests.append(("✅", "utils.logger"))
        tests.append(("✅", "utils.validators"))
    except Exception as e:
        tests.append(("❌", f"utils: {e}"))
    
    # Service modules
    services = [
        'randomuser_service',
        'firefox_relay_service',
        'gmail_service',
        'captcha_service',
        'genai_video_service',
        'video_postprocess_service'
    ]
    
    for service in services:
        try:
            __import__(f'services.{service}')
            tests.append(("✅", f"services.{service}"))
        except Exception as e:
            tests.append(("❌", f"services.{service}: {e}"))
    
    # Automation modules (expected to fail)
    automation_files = [
        'cloudskill_automation',
        'lab_actions_simple',
        'confirm_actions'
    ]
    
    for module in automation_files:
        try:
            __import__(f'automation.{module}')
            tests.append(("✅", f"automation.{module}"))
        except Exception as e:
            tests.append(("⚠️", f"automation.{module}: {str(e)[:50]}..."))
    
    # GUI modules (expected to fail)
    try:
        from gui import main_window
        tests.append(("✅", "gui.main_window"))
    except Exception as e:
        tests.append(("⚠️", f"gui.main_window: {str(e)[:50]}..."))
    
    # Print results
    for status, result in tests:
        print(f"{status} {result}")
    
    working = sum(1 for s, _ in tests if s == "✅")
    total = len(tests)
    print(f"\nWorking: {working}/{total} ({working*100//total}%)")

def test_services():
    """Test if services can be instantiated and used"""
    print("\n" + "=" * 60)
    print("Testing Service Functionality")
    print("=" * 60)
    
    # Test RandomUserService
    try:
        from services.randomuser_service import RandomUserService
        svc = RandomUserService()
        user = svc.get_random_user()
        if user:
            print(f"✅ RandomUserService: Generated user {user.get('first_name')} {user.get('last_name')}")
        else:
            print("⚠️ RandomUserService: Initialized but API call failed")
    except Exception as e:
        print(f"❌ RandomUserService: {e}")
    
    # Test Logger
    try:
        from utils.logger import setup_logger
        logger = setup_logger('test')
        logger.info("Test message")
        print("✅ Logger: Working correctly")
    except Exception as e:
        print(f"❌ Logger: {e}")
    
    # Test Validators
    try:
        from utils.validators import validate_email, validate_password_strength
        is_valid = validate_email("test@example.com")
        strength = validate_password_strength("TestPass123!")
        if is_valid and strength:
            print("✅ Validators: Working correctly")
        else:
            print("⚠️ Validators: Functions returned unexpected values")
    except Exception as e:
        print(f"❌ Validators: {e}")
    
    # Test CaptchaSolver (initialization only)
    try:
        from services.captcha_service import CaptchaSolverService
        solver = CaptchaSolverService()
        print("✅ CaptchaSolverService: Initialized successfully")
    except Exception as e:
        print(f"❌ CaptchaSolverService: {e}")
    
    # Test Firefox Relay (initialization only, requires API key)
    try:
        # This will fail without API key, but we're testing if it imports
        from services.firefox_relay_service import FirefoxRelayService
        print("✅ FirefoxRelayService: Module imported successfully (needs API key to test)")
    except Exception as e:
        print(f"❌ FirefoxRelayService: {e}")
    
    # Test Gmail Service (initialization only, requires credentials)
    try:
        from services.gmail_service import GmailService
        print("✅ GmailService: Module imported successfully (needs credentials to test)")
    except Exception as e:
        print(f"❌ GmailService: {e}")

def test_config():
    """Test configuration system"""
    print("\n" + "=" * 60)
    print("Testing Configuration System")
    print("=" * 60)
    
    try:
        from config import constants
        print(f"✅ APP_NAME: {constants.APP_NAME}")
        print(f"✅ VERSION: {constants.VERSION}")
        print(f"✅ AUTHOR: {constants.AUTHOR}")
        print(f"✅ BASE_URL: {constants.BASE_URL}")
        print(f"✅ Config validation: {constants.validate_config()}")
    except Exception as e:
        print(f"❌ Configuration: {e}")
    
    try:
        from config.settings import settings
        print(f"✅ Settings object created")
        print(f"✅ DEBUG: {settings.DEBUG}")
        print(f"✅ LOG_LEVEL: {settings.LOG_LEVEL}")
    except Exception as e:
        print(f"❌ Settings: {e}")
    
    try:
        from config.licensing import get_machine_id
        # Don't actually call it to avoid errors
        print(f"✅ Licensing module imported")
    except Exception as e:
        print(f"❌ Licensing: {e}")

def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("AutoCloudSkill - Testing Fixed Modules")
    print("=" * 60 + "\n")
    
    test_imports()
    test_services()
    test_config()
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print("✅ = Working correctly")
    print("⚠️ = Module has known issues (automation/gui)")
    print("❌ = Critical error")
    print("\nSee DECOMPILATION_ANALYSIS_REPORT.md for details")
    print("=" * 60 + "\n")

if __name__ == '__main__':
    main()