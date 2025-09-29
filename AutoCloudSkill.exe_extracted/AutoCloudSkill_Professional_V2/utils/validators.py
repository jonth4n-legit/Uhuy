"""
Professional data validation utilities for AutoCloudSkill application.

This module provides comprehensive validation capabilities:
- Email and password validation with security requirements
- Name and company validation with internationalization support
- Phone number formatting and validation
- Data sanitization and security filtering
- Custom validation rules and error reporting

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import re
import unicodedata
from typing import Dict, List, Optional, Union, Any, Tuple
from dataclasses import dataclass
from enum import Enum
import hashlib
import secrets

class ValidationSeverity(Enum):
    """Validation message severity levels."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

@dataclass
class ValidationResult:
    """Result of a validation operation."""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    suggestions: List[str]
    metadata: Dict[str, Any]

    def add_error(self, message: str) -> None:
        """Add an error message."""
        self.errors.append(message)
        self.is_valid = False

    def add_warning(self, message: str) -> None:
        """Add a warning message."""
        self.warnings.append(message)

    def add_suggestion(self, message: str) -> None:
        """Add a suggestion message."""
        self.suggestions.append(message)

class EmailValidator:
    """Advanced email validation with multiple RFC compliance levels."""

    # Basic email pattern (simplified for common use)
    BASIC_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # More strict RFC 5322 compliant pattern
    RFC_PATTERN = r'^[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?$'

    # Common disposable email domains
    DISPOSABLE_DOMAINS = {
        '10minutemail.com', 'tempmail.org', 'guerrillamail.com',
        'mailinator.com', 'throwaway.email', 'temp-mail.org'
    }

    @classmethod
    def validate(cls, email: str, strict: bool = False, check_disposable: bool = True) -> ValidationResult:
        """
        Comprehensive email validation.

        Args:
            email: Email address to validate
            strict: Use RFC-compliant validation
            check_disposable: Check against disposable email providers

        Returns:
            ValidationResult with detailed feedback
        """
        result = ValidationResult(True, [], [], [], {})

        if not email:
            result.add_error("Email is required")
            return result

        email = email.strip().lower()
        result.metadata['normalized_email'] = email

        # Length check
        if len(email) > 254:
            result.add_error("Email address is too long (max 254 characters)")

        # Pattern validation
        pattern = cls.RFC_PATTERN if strict else cls.BASIC_PATTERN
        if not re.match(pattern, email):
            result.add_error("Invalid email format")
            return result

        # Split local and domain parts
        local, domain = email.rsplit('@', 1)

        # Local part validation
        if len(local) > 64:
            result.add_error("Local part of email is too long (max 64 characters)")

        if local.startswith('.') or local.endswith('.'):
            result.add_error("Local part cannot start or end with a dot")

        if '..' in local:
            result.add_error("Local part cannot contain consecutive dots")

        # Domain part validation
        if len(domain) > 253:
            result.add_error("Domain part is too long (max 253 characters)")

        # Check for disposable email providers
        if check_disposable and domain in cls.DISPOSABLE_DOMAINS:
            result.add_warning(f"Email uses disposable provider: {domain}")
            result.add_suggestion("Consider using a permanent email address")

        # Common typo detection
        common_domains = {
            'gmail.com': ['gmai.com', 'gmial.com', 'gamail.com'],
            'yahoo.com': ['yaho.com', 'yahooo.com', 'yahoo.co'],
            'hotmail.com': ['hotmial.com', 'hotmai.com', 'hotmail.co']
        }

        for correct, typos in common_domains.items():
            if domain in typos:
                result.add_suggestion(f"Did you mean '{local}@{correct}'?")

        return result

class PasswordValidator:
    """Advanced password validation with security analysis."""

    @dataclass
    class PasswordStrength:
        """Password strength analysis result."""
        score: int  # 0-100
        level: str  # weak, fair, good, strong, excellent
        meets_minimum: bool
        entropy: float

    COMMON_PASSWORDS = {
        'password', '123456', 'password123', 'admin', 'qwerty',
        'letmein', 'welcome', 'monkey', '1234567890', 'password1'
    }

    @classmethod
    def validate_strength(cls, password: str) -> Dict[str, bool]:
        """
        Analyze password strength against multiple criteria.

        Args:
            password: Password to analyze

        Returns:
            Dictionary with boolean results for each criterion
        """
        if not password:
            return {
                'min_length': False,
                'has_uppercase': False,
                'has_lowercase': False,
                'has_digit': False,
                'has_special': False,
                'no_spaces': True,
                'not_common': True,
                'no_personal_info': True
            }

        return {
            'min_length': len(password) >= 8,
            'has_uppercase': bool(re.search(r'[A-Z]', password)),
            'has_lowercase': bool(re.search(r'[a-z]', password)),
            'has_digit': bool(re.search(r'\d', password)),
            'has_special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=\[\]\\|`~]', password)),
            'no_spaces': ' ' not in password,
            'not_common': password.lower() not in cls.COMMON_PASSWORDS,
            'no_personal_info': True  # Placeholder for personal info check
        }

    @classmethod
    def calculate_entropy(cls, password: str) -> float:
        """
        Calculate password entropy (randomness).

        Args:
            password: Password to analyze

        Returns:
            Entropy value in bits
        """
        if not password:
            return 0.0

        # Character set size estimation
        charset_size = 0
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'\d', password):
            charset_size += 10
        if re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=\[\]\\|`~]', password):
            charset_size += 32

        if charset_size == 0:
            return 0.0

        import math
        return len(password) * math.log2(charset_size)

    @classmethod
    def analyze_strength(cls, password: str) -> PasswordStrength:
        """
        Comprehensive password strength analysis.

        Args:
            password: Password to analyze

        Returns:
            PasswordStrength object with detailed analysis
        """
        if not password:
            return cls.PasswordStrength(0, 'invalid', False, 0.0)

        strength_criteria = cls.validate_strength(password)
        entropy = cls.calculate_entropy(password)

        # Calculate score based on criteria (0-100)
        score = 0
        weights = {
            'min_length': 20,
            'has_uppercase': 10,
            'has_lowercase': 10,
            'has_digit': 10,
            'has_special': 15,
            'no_spaces': 5,
            'not_common': 20,
            'no_personal_info': 10
        }

        for criterion, weight in weights.items():
            if strength_criteria.get(criterion, False):
                score += weight

        # Entropy bonus
        if entropy > 50:
            score += 10
        elif entropy > 40:
            score += 5

        # Length bonus
        if len(password) >= 12:
            score += 10
        elif len(password) >= 10:
            score += 5

        # Determine strength level
        if score >= 90:
            level = 'excellent'
        elif score >= 75:
            level = 'strong'
        elif score >= 60:
            level = 'good'
        elif score >= 40:
            level = 'fair'
        else:
            level = 'weak'

        meets_minimum = all(strength_criteria[k] for k in ['min_length', 'has_uppercase', 'has_lowercase', 'has_digit'])

        return cls.PasswordStrength(score, level, meets_minimum, entropy)

class NameValidator:
    """International name validation with cultural awareness."""

    @classmethod
    def validate_name(cls, name: str, allow_unicode: bool = True, max_length: int = 50) -> ValidationResult:
        """
        Validate person name with international support.

        Args:
            name: Name to validate
            allow_unicode: Allow Unicode characters
            max_length: Maximum allowed length

        Returns:
            ValidationResult with detailed feedback
        """
        result = ValidationResult(True, [], [], [], {})

        if not name:
            result.add_error("Name is required")
            return result

        name = name.strip()
        result.metadata['normalized_name'] = name

        # Length validation
        if len(name) > max_length:
            result.add_error(f"Name is too long (max {max_length} characters)")

        if len(name) < 2:
            result.add_error("Name is too short (min 2 characters)")

        # Character validation
        if allow_unicode:
            # Allow letters, spaces, hyphens, apostrophes, and common diacritics
            if not re.match(r'^[\p{L}\s\-\'\.]+$', name, re.UNICODE):
                result.add_error("Name contains invalid characters")
        else:
            # ASCII only with basic punctuation
            if not re.match(r'^[a-zA-Z\s\-\'\.]+$', name):
                result.add_error("Name contains invalid characters (ASCII only)")

        # Structure validation
        if name.startswith((' ', '-', "'")) or name.endswith((' ', '-', "'")):
            result.add_error("Name cannot start or end with space, hyphen, or apostrophe")

        if '  ' in name:  # Multiple consecutive spaces
            result.add_warning("Name contains multiple consecutive spaces")
            result.add_suggestion("Remove extra spaces")

        # Common issues
        if name.isupper():
            result.add_warning("Name is all uppercase")
            result.add_suggestion("Consider using proper capitalization")

        if name.islower():
            result.add_warning("Name is all lowercase")
            result.add_suggestion("Consider using proper capitalization")

        return result

class CompanyValidator:
    """Company name validation with business context."""

    @classmethod
    def validate_company(cls, company: str, max_length: int = 100) -> ValidationResult:
        """
        Validate company name.

        Args:
            company: Company name to validate
            max_length: Maximum allowed length

        Returns:
            ValidationResult with detailed feedback
        """
        result = ValidationResult(True, [], [], [], {})

        if not company:
            result.add_error("Company name is required")
            return result

        company = company.strip()
        result.metadata['normalized_company'] = company

        # Length validation
        if len(company) > max_length:
            result.add_error(f"Company name is too long (max {max_length} characters)")

        if len(company) < 2:
            result.add_error("Company name is too short (min 2 characters)")

        # Character validation - allow business-appropriate characters
        if not re.match(r'^[\p{L}\p{N}\s\-&.,()\/\'"!]+$', company, re.UNICODE):
            result.add_error("Company name contains invalid characters")

        # Structure validation
        if company.startswith((' ', '-')) or company.endswith((' ', '-')):
            result.add_warning("Company name should not start or end with space or hyphen")

        return result

def sanitize_input(
    text: str,
    max_length: Optional[int] = None,
    remove_html: bool = True,
    normalize_unicode: bool = True
) -> str:
    """
    Sanitize user input with comprehensive cleaning.

    Args:
        text: Text to sanitize
        max_length: Maximum length (truncate if longer)
        remove_html: Remove HTML tags
        normalize_unicode: Normalize Unicode characters

    Returns:
        Sanitized text
    """
    if not text:
        return ''

    # Normalize Unicode
    if normalize_unicode:
        text = unicodedata.normalize('NFKC', text)

    # Remove HTML tags
    if remove_html:
        text = re.sub(r'<[^>]+>', '', text)

    # Remove control characters except newlines and tabs
    text = ''.join(char for char in text if unicodedata.category(char)[0] != 'C' or char in '\n\t')

    # Trim whitespace
    text = text.strip()

    # Truncate if necessary
    if max_length and len(text) > max_length:
        text = text[:max_length].rstrip()

    return text

def validate_user_data(user_data: Dict[str, Any]) -> ValidationResult:
    """
    Comprehensive user data validation.

    Args:
        user_data: Dictionary containing user data

    Returns:
        ValidationResult with all validation errors and suggestions
    """
    result = ValidationResult(True, [], [], [], {})

    # Validate first name
    first_name = user_data.get('first_name', '')
    name_result = NameValidator.validate_name(first_name)
    if not name_result.is_valid:
        result.errors.extend([f"First name: {error}" for error in name_result.errors])
        result.is_valid = False
    result.warnings.extend([f"First name: {warning}" for warning in name_result.warnings])

    # Validate last name
    last_name = user_data.get('last_name', '')
    name_result = NameValidator.validate_name(last_name)
    if not name_result.is_valid:
        result.errors.extend([f"Last name: {error}" for error in name_result.errors])
        result.is_valid = False
    result.warnings.extend([f"Last name: {warning}" for warning in name_result.warnings])

    # Validate email
    email = user_data.get('email', '')
    email_result = EmailValidator.validate(email)
    if not email_result.is_valid:
        result.errors.extend([f"Email: {error}" for error in email_result.errors])
        result.is_valid = False
    result.warnings.extend([f"Email: {warning}" for warning in email_result.warnings])
    result.suggestions.extend([f"Email: {suggestion}" for suggestion in email_result.suggestions])

    # Validate password
    password = user_data.get('password', '')
    password_strength = PasswordValidator.analyze_strength(password)
    if not password_strength.meets_minimum:
        result.add_error("Password does not meet minimum security requirements")
    if password_strength.score < 60:
        result.add_warning(f"Password strength is {password_strength.level} (score: {password_strength.score}/100)")
        result.add_suggestion("Consider using a stronger password with more character variety")

    # Validate company (optional)
    company = user_data.get('company', '')
    if company:
        company_result = CompanyValidator.validate_company(company)
        if not company_result.is_valid:
            result.errors.extend([f"Company: {error}" for error in company_result.errors])
            result.is_valid = False
        result.warnings.extend([f"Company: {warning}" for warning in company_result.warnings])

    # Store validation metadata
    result.metadata.update({
        'password_strength': password_strength,
        'email_normalized': email_result.metadata.get('normalized_email', email),
        'validation_timestamp': str(hash(str(user_data)))
    })

    return result

def format_phone_number(phone: str, country_code: str = '+1') -> str:
    """
    Format phone number with international support.

    Args:
        phone: Phone number to format
        country_code: Default country code

    Returns:
        Formatted phone number
    """
    if not phone:
        return ''

    # Remove all non-digit characters except +
    cleaned = re.sub(r'[^\d+]', '', phone)

    if not cleaned:
        return ''

    # If already has country code, return as is
    if cleaned.startswith('+'):
        return cleaned

    # Add country code if missing
    if not cleaned.startswith(country_code.replace('+', '')):
        return f"{country_code}{cleaned}"

    return f"+{cleaned}"

def validate_email(email: str) -> bool:
    """
    Simple email validation for backward compatibility.

    Args:
        email: Email to validate

    Returns:
        True if valid, False otherwise
    """
    return EmailValidator.validate(email).is_valid

def is_password_strong(password: str) -> bool:
    """
    Check if password meets strong criteria for backward compatibility.

    Args:
        password: Password to check

    Returns:
        True if strong, False otherwise
    """
    return PasswordValidator.analyze_strength(password).meets_minimum

def validate_name(name: str) -> bool:
    """
    Simple name validation for backward compatibility.

    Args:
        name: Name to validate

    Returns:
        True if valid, False otherwise
    """
    return NameValidator.validate_name(name).is_valid

def validate_company_name(company: str) -> bool:
    """
    Simple company validation for backward compatibility.

    Args:
        company: Company name to validate

    Returns:
        True if valid, False otherwise
    """
    return CompanyValidator.validate_company(company).is_valid

def validate_password_strength(password: str) -> Dict[str, bool]:
    """
    Password strength validation for backward compatibility.

    Args:
        password: Password to validate

    Returns:
        Dictionary with validation results
    """
    return PasswordValidator.validate_strength(password)

# Export commonly used items
__all__ = [
    'ValidationResult',
    'ValidationSeverity',
    'EmailValidator',
    'PasswordValidator',
    'NameValidator',
    'CompanyValidator',
    'validate_user_data',
    'sanitize_input',
    'format_phone_number',
    # Backward compatibility
    'validate_email',
    'is_password_strong',
    'validate_name',
    'validate_company_name',
    'validate_password_strength'
]