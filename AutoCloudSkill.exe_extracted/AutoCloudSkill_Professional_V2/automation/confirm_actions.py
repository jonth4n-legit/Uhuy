"""
Professional email confirmation automation for AutoCloudSkill.

This module provides email confirmation and login automation:
- Email verification link processing
- Automatic login after confirmation
- Password and credential management
- Multi-step authentication handling

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import asyncio
import logging
from typing import Dict, Optional, Any
from dataclasses import dataclass

from playwright.async_api import Page, BrowserContext, TimeoutError as PlaywrightTimeoutError

from utils.logger import setup_application_logging, log_automation_step, performance_monitor

logger = setup_application_logging('ConfirmActions')

@dataclass
class ConfirmationResult:
    """Email confirmation operation result."""
    success: bool
    confirmed: bool
    logged_in: bool
    final_url: str
    error_message: Optional[str] = None
    metadata: Dict[str, Any] = None

class EmailConfirmationService:
    """Professional email confirmation and login automation."""

    def __init__(self):
        """Initialize email confirmation service."""
        self.logger = logger

    @performance_monitor("confirm_via_link")
    async def confirm_via_link_action(
        self,
        context: BrowserContext,
        page: Page,
        url: str,
        password: str,
        email: Optional[str] = None,
        auto_login: bool = True
    ) -> ConfirmationResult:
        """
        Open email confirmation link and handle subsequent login if required.

        Args:
            context: Browser context
            page: Current page instance
            url: Email confirmation URL
            password: User password for login
            email: User email (optional, usually pre-filled)
            auto_login: Automatically attempt login after confirmation

        Returns:
            ConfirmationResult with operation details
        """
        log_automation_step(
            self.logger,
            "confirm_via_link",
            "START",
            {"url": url[:100], "email": email, "auto_login": auto_login}
        )

        try:
            # Navigate to confirmation URL
            await self._navigate_to_confirmation(page, url)

            # Check if confirmation was successful
            confirmed = await self._check_confirmation_success(page)

            # Handle login if required
            logged_in = False
            if auto_login:
                logged_in = await self._handle_login_if_required(page, password, email)

            result = ConfirmationResult(
                success=True,
                confirmed=confirmed,
                logged_in=logged_in,
                final_url=page.url,
                metadata={
                    'confirmation_detected': confirmed,
                    'login_attempted': auto_login,
                    'login_successful': logged_in
                }
            )

            log_automation_step(
                self.logger,
                "confirm_via_link",
                "SUCCESS",
                {
                    "confirmed": confirmed,
                    "logged_in": logged_in,
                    "final_url": page.url
                }
            )

            return result

        except Exception as e:
            error_msg = f"Email confirmation failed: {e}"
            self.logger.error(error_msg)

            log_automation_step(
                self.logger,
                "confirm_via_link",
                "ERROR",
                {"error": error_msg}
            )

            return ConfirmationResult(
                success=False,
                confirmed=False,
                logged_in=False,
                final_url=page.url if page else "",
                error_message=error_msg
            )

    async def _navigate_to_confirmation(self, page: Page, url: str) -> None:
        """Navigate to confirmation URL with retry logic."""
        log_automation_step(
            self.logger,
            "navigate_confirmation",
            "START",
            {"url": url[:100]}
        )

        max_retries = 3
        for attempt in range(max_retries):
            try:
                if page.is_closed():
                    raise RuntimeError("Page is closed, cannot navigate")

                await page.goto(url, wait_until='domcontentloaded', timeout=30000)

                log_automation_step(
                    self.logger,
                    "navigate_confirmation",
                    "SUCCESS",
                    {"attempt": attempt + 1, "final_url": page.url}
                )
                return

            except Exception as e:
                if attempt == max_retries - 1:
                    raise RuntimeError(f"Failed to navigate after {max_retries} attempts: {e}")

                log_automation_step(
                    self.logger,
                    "navigate_confirmation",
                    "RETRY",
                    {"attempt": attempt + 1, "error": str(e)}
                )

                await asyncio.sleep(2 ** attempt)  # Exponential backoff

    async def _check_confirmation_success(self, page: Page) -> bool:
        """Check if email confirmation was successful."""
        try:
            # Wait for page to load completely
            await page.wait_for_load_state('networkidle', timeout=10000)

            # Check for confirmation success indicators
            success_indicators = [
                # Text-based indicators
                'confirmed',
                'verified',
                'activated',
                'success',
                'complete',
                'thank you',
                'welcome',

                # URL-based indicators
                'confirm',
                'verify',
                'success',
                'welcome'
            ]

            # Check page content
            page_content = await page.content()
            page_text = await page.text_content('body') or ""
            current_url = page.url.lower()

            # Check for success indicators in content
            content_indicates_success = any(
                indicator in page_text.lower() or indicator in page_content.lower()
                for indicator in success_indicators
            )

            # Check for success indicators in URL
            url_indicates_success = any(
                indicator in current_url
                for indicator in ['confirm', 'verify', 'success', 'welcome']
            )

            # Check for specific success elements
            success_elements = await page.query_selector_all(
                '[class*="success"], [class*="confirmed"], [class*="verified"], '
                '[id*="success"], [id*="confirmed"], [id*="verified"]'
            )

            element_indicates_success = len(success_elements) > 0

            is_confirmed = content_indicates_success or url_indicates_success or element_indicates_success

            log_automation_step(
                self.logger,
                "check_confirmation",
                "SUCCESS" if is_confirmed else "INFO",
                {
                    "confirmed": is_confirmed,
                    "content_match": content_indicates_success,
                    "url_match": url_indicates_success,
                    "element_match": element_indicates_success
                }
            )

            return is_confirmed

        except Exception as e:
            self.logger.warning(f"Failed to check confirmation success: {e}")
            return False

    async def _handle_login_if_required(
        self,
        page: Page,
        password: str,
        email: Optional[str] = None
    ) -> bool:
        """Handle login if login form is present."""
        try:
            # Check if password field is present (indicates login required)
            password_field = await page.query_selector('input[type="password"]')

            if not password_field:
                # No login form present, try navigating to sign-in page
                try:
                    signin_url = 'https://www.cloudskillsboost.google/users/sign_in'
                    await page.goto(signin_url, wait_until='domcontentloaded', timeout=15000)

                    # Check again for password field
                    password_field = await page.query_selector('input[type="password"]')

                    if not password_field:
                        self.logger.info("No login form found after navigation")
                        return False

                except Exception as e:
                    self.logger.warning(f"Failed to navigate to sign-in page: {e}")
                    return False

            log_automation_step(
                self.logger,
                "handle_login",
                "START",
                {"email": email, "has_password_field": True}
            )

            # Wait for login form to be ready
            await page.wait_for_selector('input[type="password"]', timeout=30000)

            # Fill email if provided and field is present
            if email:
                email_selectors = [
                    'input[type="email"]',
                    'input[name="email"]',
                    'input[id*="email"]',
                    'input[placeholder*="email"]'
                ]

                for selector in email_selectors:
                    try:
                        email_field = await page.query_selector(selector)
                        if email_field:
                            await email_field.clear()
                            await email_field.fill(email.strip())
                            log_automation_step(
                                self.logger,
                                "handle_login",
                                "EMAIL_FILLED",
                                {"selector": selector}
                            )
                            break
                    except Exception:
                        continue

            # Fill password
            password_locator = page.locator('input[type="password"]').first
            await password_locator.clear()
            await password_locator.type(password.strip(), delay=50)

            log_automation_step(
                self.logger,
                "handle_login",
                "CREDENTIALS_FILLED",
                {"email_provided": email is not None}
            )

            # Submit login form
            submitted = await self._submit_login_form(page)

            if submitted:
                # Wait for login to complete
                await page.wait_for_load_state('networkidle', timeout=15000)

                # Check if login was successful
                login_success = await self._verify_login_success(page)

                log_automation_step(
                    self.logger,
                    "handle_login",
                    "SUCCESS" if login_success else "WARNING",
                    {"login_successful": login_success, "final_url": page.url}
                )

                return login_success

            return False

        except PlaywrightTimeoutError:
            self.logger.warning("Login form timeout - manual intervention may be required")
            return False

        except Exception as e:
            self.logger.error(f"Login handling failed: {e}")
            return False

    async def _submit_login_form(self, page: Page) -> bool:
        """Submit login form using various selectors."""
        submit_selectors = [
            'button[type="submit"]',
            'input[type="submit"]',
            'button:has-text("Sign in")',
            'button:has-text("Sign In")',
            'button:has-text("Log in")',
            'button:has-text("Log In")',
            'button:has-text("Login")',
            'button[name*="submit"]',
            'button[id*="submit"]'
        ]

        for selector in submit_selectors:
            try:
                submit_button = await page.query_selector(selector)
                if submit_button and await submit_button.is_visible():
                    await submit_button.click()

                    log_automation_step(
                        self.logger,
                        "submit_login",
                        "SUCCESS",
                        {"selector": selector}
                    )

                    return True

            except Exception as e:
                self.logger.debug(f"Submit attempt failed for {selector}: {e}")
                continue

        # Try Enter key as fallback
        try:
            await page.keyboard.press('Enter')
            log_automation_step(
                self.logger,
                "submit_login",
                "SUCCESS",
                {"method": "enter_key"}
            )
            return True

        except Exception as e:
            self.logger.warning(f"Failed to submit login form: {e}")
            return False

    async def _verify_login_success(self, page: Page) -> bool:
        """Verify if login was successful."""
        try:
            current_url = page.url.lower()

            # Check for successful login indicators
            success_indicators = [
                'dashboard',
                'profile',
                'home',
                'welcome',
                'catalog'
            ]

            # Check for failure indicators
            failure_indicators = [
                'error',
                'invalid',
                'incorrect',
                'failed',
                'sign_in',
                'login'
            ]

            # URL-based checks
            url_success = any(indicator in current_url for indicator in success_indicators)
            url_failure = any(indicator in current_url for indicator in failure_indicators)

            # Element-based checks
            error_elements = await page.query_selector_all(
                '[class*="error"], [class*="invalid"], [id*="error"], [id*="invalid"]'
            )

            success_elements = await page.query_selector_all(
                '[class*="dashboard"], [class*="profile"], [class*="welcome"]'
            )

            has_errors = len(error_elements) > 0
            has_success_elements = len(success_elements) > 0

            # Determine login success
            login_success = (url_success or has_success_elements) and not (url_failure or has_errors)

            return login_success

        except Exception as e:
            self.logger.warning(f"Failed to verify login success: {e}")
            return False

# Backward compatibility function
async def confirm_via_link_action(
    context: BrowserContext,
    page: Page,
    logger,
    url: str,
    password: str,
    email: Optional[str] = None
) -> Dict:
    """
    Backward compatibility wrapper for email confirmation.

    Args:
        context: Browser context
        page: Page instance
        logger: Logger instance (unused, using internal logger)
        url: Confirmation URL
        password: User password
        email: User email (optional)

    Returns:
        Dictionary with operation result
    """
    service = EmailConfirmationService()
    result = await service.confirm_via_link_action(context, page, url, password, email)

    return {
        'success': result.success,
        'confirmed': result.confirmed,
        'logged_in': result.logged_in,
        'error': result.error_message,
        'final_url': result.final_url
    }

# Export commonly used items
__all__ = [
    'ConfirmationResult',
    'EmailConfirmationService',
    'confirm_via_link_action'
]