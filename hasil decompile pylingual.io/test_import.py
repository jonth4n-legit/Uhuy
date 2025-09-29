#!/usr/bin/env python3
"""
Test script to verify that all modules can be imported without major syntax errors
"""

def test_imports():
    """Test importing all main modules"""
    print("Testing imports...")
    
    # Test basic modules
    try:
        from config import constants, settings
        print("✅ Config modules imported successfully")
    except Exception as e:
        print(f"❌ Config import error: {e}")
    
    try:
        from utils import logger, validators
        print("✅ Utils modules imported successfully")
    except Exception as e:
        print(f"❌ Utils import error: {e}")
    
    try:
        from services import randomuser_service, captcha_service
        print("✅ Services modules imported successfully")
    except Exception as e:
        print(f"❌ Services import error: {e}")
        
    try:
        from services import firefox_relay_service, gmail_service
        print("✅ Additional services imported successfully")
    except Exception as e:
        print(f"❌ Additional services import error: {e}")
    
    try:
        from automation import cloudskill_automation, lab_actions_simple, confirm_actions
        print("✅ Automation modules imported successfully")
    except Exception as e:
        print(f"❌ Automation import error: {e}")
    
    print("\nTesting service initialization...")
    
    try:
        from services.randomuser_service import RandomUserService
        service = RandomUserService()
        print("✅ RandomUserService initialized")
    except Exception as e:
        print(f"❌ RandomUserService error: {e}")
        
    try:
        from services.captcha_service import CaptchaSolverService
        service = CaptchaSolverService()
        print("✅ CaptchaSolverService initialized")
    except Exception as e:
        print(f"❌ CaptchaSolverService error: {e}")
    
    try:
        from utils.validators import validate_email, validate_password_strength
        result1 = validate_email("test@example.com")
        result2 = validate_password_strength("TestPass123!")
        print(f"✅ Validators working: email={result1}, password={result2}")
    except Exception as e:
        print(f"❌ Validators error: {e}")
    
    print("\nAll import tests completed!")

if __name__ == "__main__":
    test_imports()