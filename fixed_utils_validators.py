"""
Utility functions untuk validasi data
"""
import re
from typing import Dict, List, Optional

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_password(password: str) -> Dict[str, bool]:
    """Validate password strength"""
    return {
        'length': len(password) >= 8,
        'has_upper': bool(re.search(r'[A-Z]', password)),
        'has_lower': bool(re.search(r'[a-z]', password)),
        'has_digit': bool(re.search(r'\d', password)),
        'has_special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }

def validate_user_data(user_data: Dict) -> Dict[str, List[str]]:
    """Validate complete user data"""
    errors = {
        'first_name': [],
        'last_name': [],
        'email': [],
        'password': [],
        'password_confirm': []
    }
    
    # First name validation
    if not user_data.get('first_name'):
        errors['first_name'].append('First name is required')
    elif len(user_data['first_name']) < 2:
        errors['first_name'].append('First name must be at least 2 characters')
    
    # Last name validation
    if not user_data.get('last_name'):
        errors['last_name'].append('Last name is required')
    elif len(user_data['last_name']) < 2:
        errors['last_name'].append('Last name must be at least 2 characters')
    
    # Email validation
    email = user_data.get('email', '')
    if not email:
        errors['email'].append('Email is required')
    elif not validate_email(email):
        errors['email'].append('Invalid email format')
    
    # Password validation
    password = user_data.get('password', '')
    if not password:
        errors['password'].append('Password is required')
    else:
        password_checks = validate_password(password)
        if not password_checks['length']:
            errors['password'].append('Password must be at least 8 characters')
        if not password_checks['has_upper']:
            errors['password'].append('Password must contain uppercase letter')
        if not password_checks['has_lower']:
            errors['password'].append('Password must contain lowercase letter')
        if not password_checks['has_digit']:
            errors['password'].append('Password must contain digit')
        if not password_checks['has_special']:
            errors['password'].append('Password must contain special character')
    
    # Password confirmation validation
    password_confirm = user_data.get('password_confirm', '')
    if not password_confirm:
        errors['password_confirm'].append('Password confirmation is required')
    elif password != password_confirm:
        errors['password_confirm'].append('Passwords do not match')
    
    return errors

def is_valid_lab_url(url: str) -> bool:
    """Validate lab URL format"""
    if not url:
        return False
    
    # Check if it's a valid URL format
    pattern = r'^https?://.*cloudskillsboost\.google\.com.*'
    return bool(re.match(pattern, url))

def sanitize_filename(filename: str) -> str:
    """Sanitize filename for safe file operations"""
    # Remove or replace invalid characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Remove leading/trailing spaces and dots
    filename = filename.strip(' .')
    
    # Ensure filename is not empty
    if not filename:
        filename = 'untitled'
    
    return filename