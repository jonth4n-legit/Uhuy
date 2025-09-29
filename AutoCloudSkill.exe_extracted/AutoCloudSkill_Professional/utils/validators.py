"""
Data validation utilities for Auto Cloud Skill Registration application.

This module provides comprehensive validation functions for user data,
email addresses, URLs, and other input validation needs.
"""

import re
import urllib.parse
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

# Validation patterns
EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
)

URL_PATTERN = re.compile(
    r'^https?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)*[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?'  # domain
    r'|localhost'  # localhost
    r'|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

PHONE_PATTERN = re.compile(r'^\+?1?-?\.?\s??\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$')

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_email(email: str) -> bool:
    """
    Validate email address format.

    Args:
        email: Email address to validate

    Returns:
        bool: True if email is valid

    Raises:
        ValidationError: If email is invalid
    """
    if not email or not isinstance(email, str):
        raise ValidationError("Email cannot be empty")

    email = email.strip().lower()

    if not EMAIL_PATTERN.match(email):
        raise ValidationError(f"Invalid email format: {email}")

    # Additional checks
    if len(email) > 254:  # RFC 5321 limit
        raise ValidationError("Email address too long")

    local, domain = email.split('@')
    if len(local) > 64:  # RFC 5321 limit
        raise ValidationError("Email local part too long")

    return True

def validate_url(url: str) -> bool:
    """
    Validate URL format.

    Args:
        url: URL to validate

    Returns:
        bool: True if URL is valid

    Raises:
        ValidationError: If URL is invalid
    """
    if not url or not isinstance(url, str):
        raise ValidationError("URL cannot be empty")

    url = url.strip()

    if not URL_PATTERN.match(url):
        raise ValidationError(f"Invalid URL format: {url}")

    # Additional parsing check
    try:
        parsed = urllib.parse.urlparse(url)
        if not parsed.netloc:
            raise ValidationError("URL missing domain")
    except Exception as e:
        raise ValidationError(f"URL parsing error: {e}")

    return True

def validate_password(password: str, min_length: int = 8) -> bool:
    """
    Validate password strength.

    Args:
        password: Password to validate
        min_length: Minimum password length

    Returns:
        bool: True if password is valid

    Raises:
        ValidationError: If password is invalid
    """
    if not password or not isinstance(password, str):
        raise ValidationError("Password cannot be empty")

    if len(password) < min_length:
        raise ValidationError(f"Password must be at least {min_length} characters")

    # Check for basic complexity
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if not (has_upper and has_lower and has_digit):
        logger.warning("Password lacks complexity (uppercase, lowercase, digit)")

    return True

def validate_user_data(user_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate complete user data dictionary.

    Args:
        user_data: Dictionary containing user information

    Returns:
        Dict[str, Any]: Validated and cleaned user data

    Raises:
        ValidationError: If any validation fails
    """
    if not isinstance(user_data, dict):
        raise ValidationError("User data must be a dictionary")

    validated = {}
    errors = []

    # Required fields
    required_fields = ['first_name', 'last_name', 'email', 'password']
    for field in required_fields:
        if field not in user_data or not user_data[field]:
            errors.append(f"Missing required field: {field}")

    if errors:
        raise ValidationError(f"Validation errors: {', '.join(errors)}")

    # Validate and clean each field
    try:
        # Names
        validated['first_name'] = validate_name(user_data['first_name'])
        validated['last_name'] = validate_name(user_data['last_name'])

        # Email
        validate_email(user_data['email'])
        validated['email'] = user_data['email'].strip().lower()

        # Password
        validate_password(user_data['password'])
        validated['password'] = user_data['password']

        # Optional fields
        if 'company' in user_data and user_data['company']:
            validated['company'] = validate_name(user_data['company'])

        if 'phone' in user_data and user_data['phone']:
            validated['phone'] = validate_phone(user_data['phone'])

        # Copy other fields as-is (gender, nationality, etc.)
        for key, value in user_data.items():
            if key not in validated and value is not None:
                validated[key] = value

    except ValidationError as e:
        raise ValidationError(f"User data validation failed: {e}")

    return validated

def validate_name(name: str) -> str:
    """
    Validate and clean a name field.

    Args:
        name: Name to validate

    Returns:
        str: Cleaned name

    Raises:
        ValidationError: If name is invalid
    """
    if not name or not isinstance(name, str):
        raise ValidationError("Name cannot be empty")

    name = name.strip()

    if len(name) < 1:
        raise ValidationError("Name cannot be empty")

    if len(name) > 50:
        raise ValidationError("Name too long (max 50 characters)")

    # Remove invalid characters
    cleaned = re.sub(r'[^a-zA-Z\s\'-.]', '', name)
    if not cleaned:
        raise ValidationError("Name contains no valid characters")

    return cleaned.title()

def validate_phone(phone: str) -> str:
    """
    Validate and format phone number.

    Args:
        phone: Phone number to validate

    Returns:
        str: Formatted phone number

    Raises:
        ValidationError: If phone is invalid
    """
    if not phone or not isinstance(phone, str):
        raise ValidationError("Phone number cannot be empty")

    # Remove all non-digit characters except +
    cleaned = re.sub(r'[^\d+]', '', phone.strip())

    if not cleaned:
        raise ValidationError("Phone number contains no digits")

    # Basic length check (7-15 digits for international numbers)
    digits_only = re.sub(r'[^\d]', '', cleaned)
    if len(digits_only) < 7 or len(digits_only) > 15:
        raise ValidationError("Phone number must be 7-15 digits")

    return cleaned

def validate_api_key(api_key: str, service_name: str = "API") -> bool:
    """
    Validate API key format.

    Args:
        api_key: API key to validate
        service_name: Name of the service (for error messages)

    Returns:
        bool: True if API key is valid

    Raises:
        ValidationError: If API key is invalid
    """
    if not api_key or not isinstance(api_key, str):
        raise ValidationError(f"{service_name} key cannot be empty")

    api_key = api_key.strip()

    if len(api_key) < 10:
        raise ValidationError(f"{service_name} key too short")

    if len(api_key) > 500:
        raise ValidationError(f"{service_name} key too long")

    return True