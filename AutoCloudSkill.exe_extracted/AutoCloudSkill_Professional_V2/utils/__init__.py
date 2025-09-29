"""
Utils module __init__.py for AutoCloudSkill Professional.

Provides convenient imports for all utility functions.
"""

from .logger import (
    setup_application_logging,
    setup_logger,
    log_user_action,
    log_automation_step,
    log_performance_metrics,
    performance_monitor,
    PerformanceLogger,
    main_logger
)

from .validators import (
    ValidationResult,
    ValidationSeverity,
    EmailValidator,
    PasswordValidator,
    NameValidator,
    CompanyValidator,
    validate_user_data,
    sanitize_input,
    format_phone_number,
    # Backward compatibility
    validate_email,
    is_password_strong,
    validate_name,
    validate_company_name,
    validate_password_strength
)

__all__ = [
    # Logging
    'setup_application_logging',
    'setup_logger',
    'log_user_action',
    'log_automation_step',
    'log_performance_metrics',
    'performance_monitor',
    'PerformanceLogger',
    'main_logger',

    # Validation
    'ValidationResult',
    'ValidationSeverity',
    'EmailValidator',
    'PasswordValidator',
    'NameValidator',
    'CompanyValidator',
    'validate_user_data',
    'sanitize_input',
    'format_phone_number',
    'validate_email',
    'is_password_strong',
    'validate_name',
    'validate_company_name',
    'validate_password_strength'
]