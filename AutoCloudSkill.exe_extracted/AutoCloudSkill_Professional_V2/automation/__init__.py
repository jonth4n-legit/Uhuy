"""
Automation module __init__.py for AutoCloudSkill Professional.

Provides convenient imports for all automation components.
"""

from .cloudskill_automation import (
    AutomationState,
    RegistrationMethod,
    RegistrationData,
    AutomationResult,
    CloudSkillAutomation,
    _get_bundle_root,
    _ensure_playwright_browsers_path
)

from .confirm_actions import (
    ConfirmationResult,
    EmailConfirmationService,
    confirm_via_link_action
)

from .lab_actions_simple import (
    LabStatus,
    LabResult,
    LabAutomationService,
    start_lab,
    open_cloud_console,
    handle_gcloud_terms,
    enable_genai_and_create_api_key
)

__all__ = [
    # Core Automation
    'AutomationState',
    'RegistrationMethod',
    'RegistrationData',
    'AutomationResult',
    'CloudSkillAutomation',
    '_get_bundle_root',
    '_ensure_playwright_browsers_path',

    # Email Confirmation
    'ConfirmationResult',
    'EmailConfirmationService',
    'confirm_via_link_action',

    # Lab Actions
    'LabStatus',
    'LabResult',
    'LabAutomationService',
    'start_lab',
    'open_cloud_console',
    'handle_gcloud_terms',
    'enable_genai_and_create_api_key'
]