#!/usr/bin/env python3
"""
Validation script for Auto Cloud Skill Registration application.
Tests the project structure and core functionality without external dependencies.
"""

import sys
from pathlib import Path
import importlib
import inspect

def test_project_structure():
    """Test that all required files and directories exist."""
    print("🔍 Testing project structure...")

    base_dir = Path(__file__).parent
    required_files = [
        "main.py",
        "requirements.txt",
        "setup.py",
        "build_config.py",
        "README.md"
    ]

    required_dirs = [
        "config",
        "utils",
        "services",
        "automation",
        "gui",
        "runtime"
    ]

    missing_files = []
    missing_dirs = []

    for file in required_files:
        if not (base_dir / file).exists():
            missing_files.append(file)

    for dir in required_dirs:
        if not (base_dir / dir).exists():
            missing_dirs.append(dir)

    if missing_files or missing_dirs:
        print(f"❌ Missing files: {missing_files}")
        print(f"❌ Missing directories: {missing_dirs}")
        return False

    print("✅ Project structure complete")
    return True

def test_core_imports():
    """Test core imports that don't require external dependencies."""
    print("\n🔍 Testing core imports...")

    core_modules = [
        "config.constants",
        "config.settings",
        "config.licensing",
        "utils.validators"
    ]

    failed_imports = []

    for module in core_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            failed_imports.append(module)

    return len(failed_imports) == 0

def test_configuration():
    """Test configuration loading."""
    print("\n🔍 Testing configuration...")

    try:
        from config.constants import APP_NAME, VERSION, AUTHOR
        from config.settings import settings
        from config.licensing import get_machine_id

        print(f"✅ App: {APP_NAME} v{VERSION} by {AUTHOR}")
        print(f"✅ Settings loaded: {type(settings).__name__}")
        print(f"✅ Machine ID: {get_machine_id()[:8]}...")

        return True
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def test_utilities():
    """Test utility functions."""
    print("\n🔍 Testing utilities...")

    try:
        from utils.validators import validate_email, validate_user_data, ValidationError

        # Test email validation
        try:
            validate_email("test@example.com")
            print("✅ Email validation working")
        except ValidationError:
            print("❌ Email validation failed")
            return False

        # Test user data validation
        test_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "password": "SecurePass123!"
        }

        validated = validate_user_data(test_data)
        print("✅ User data validation working")

        return True
    except Exception as e:
        print(f"❌ Utilities test failed: {e}")
        return False

def test_logging():
    """Test logging system."""
    print("\n🔍 Testing logging...")

    try:
        from utils.logger import setup_logger, log_user_action, log_automation_step

        logger = setup_logger("TestLogger")
        logger.info("Test log message")

        log_user_action("Test action", {"test": "data"})
        log_automation_step("Test step", "SUCCESS", "Test details")

        print("✅ Logging system working")
        return True
    except Exception as e:
        print(f"❌ Logging test failed: {e}")
        return False

def test_services_structure():
    """Test services module structure (without external dependencies)."""
    print("\n🔍 Testing services structure...")

    try:
        # Test that service modules can be imported at the module level
        import services
        print("✅ Services package imported")

        # Check that service classes exist
        service_files = [
            "services.randomuser_service",
            "services.firefox_relay_service",
            "services.captcha_service"
        ]

        for service_file in service_files:
            try:
                module = importlib.import_module(service_file)
                print(f"✅ {service_file} structure OK")
            except ImportError as e:
                if "No module named" in str(e) and any(dep in str(e) for dep in ["requests", "speech_recognition"]):
                    print(f"⚠️  {service_file} needs external deps (expected)")
                else:
                    print(f"❌ {service_file} structure error: {e}")
                    return False

        return True
    except Exception as e:
        print(f"❌ Services structure test failed: {e}")
        return False

def test_runtime_dependencies():
    """Test runtime dependencies are present."""
    print("\n🔍 Testing runtime dependencies...")

    base_dir = Path(__file__).parent
    runtime_dir = base_dir / "runtime"

    if not runtime_dir.exists():
        print("❌ Runtime directory missing")
        return False

    # Check for Playwright browsers
    playwright_dirs = [
        runtime_dir / "ms-playwright",
        base_dir.parent / "ms-playwright"
    ]

    playwright_found = False
    for p_dir in playwright_dirs:
        if p_dir.exists():
            print(f"✅ Playwright browsers found at: {p_dir}")
            playwright_found = True
            break

    if not playwright_found:
        print("⚠️  Playwright browsers not found (will need installation)")

    # Check for internal dependencies
    internal_dirs = [
        runtime_dir / "_internal",
        base_dir.parent / "_internal"
    ]

    internal_found = False
    for i_dir in internal_dirs:
        if i_dir.exists():
            print(f"✅ Internal dependencies found at: {i_dir}")
            internal_found = True

            # Check for AntiCaptcha
            anticaptcha_dir = i_dir / "AntiCaptcha"
            if anticaptcha_dir.exists():
                print(f"✅ AntiCaptcha extension found")

            break

    if not internal_found:
        print("⚠️  Internal dependencies not found")

    return True

def run_validation():
    """Run complete validation suite."""
    print("="*60)
    print("AUTO CLOUD SKILL - PROFESSIONAL VALIDATION")
    print("="*60)

    tests = [
        ("Project Structure", test_project_structure),
        ("Core Imports", test_core_imports),
        ("Configuration", test_configuration),
        ("Utilities", test_utilities),
        ("Logging", test_logging),
        ("Services Structure", test_services_structure),
        ("Runtime Dependencies", test_runtime_dependencies)
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"❌ {test_name} crashed: {e}")

    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    print(f"Tests passed: {passed}/{total}")

    if passed == total:
        print("🎉 ALL TESTS PASSED!")
        print("\nProject is ready for:")
        print("  • Development: python main.py (after installing deps)")
        print("  • Setup: python setup.py")
        print("  • Build: python build_config.py")
    else:
        print("⚠️  Some tests failed - check issues above")

    print("="*60)
    return passed == total

if __name__ == "__main__":
    success = run_validation()
    sys.exit(0 if success else 1)