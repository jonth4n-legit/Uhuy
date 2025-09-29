"""
Cloud Skill Automation for Auto Cloud Skill Registration application.

Professional implementation of Google Cloud Skills Boost registration automation
with robust browser handling, proper error recovery, and comprehensive logging.
"""

import asyncio
import os
import sys
from pathlib import Path
from typing import Dict, Optional, Any, List
import logging
import time
from urllib.parse import urlparse, parse_qs
import json

from playwright.async_api import async_playwright, Page, Browser, BrowserContext, Playwright

from config.constants import (
    CLOUDSKILL_REGISTER_URL,
    BROWSER_USER_AGENT,
    PLAYWRIGHT_HEADLESS,
    PLAYWRIGHT_TIMEOUT
)
from utils.logger import setup_logger, log_automation_step
from utils.validators import validate_email, validate_url, ValidationError

logger = logging.getLogger(__name__)

def _get_bundle_root() -> Path:
    """
    Resolve base directory for both development and bundled execution.

    Returns:
        Path: Project root directory
    """
    if getattr(sys, 'frozen', False):
        # Running as bundled executable
        if hasattr(sys, '_MEIPASS'):
            # PyInstaller bundle
            return Path(sys._MEIPASS)
        else:
            # Other bundler
            return Path(sys.executable).parent
    else:
        # Running as script
        return Path(__file__).parent.parent

def _ensure_playwright_browsers_path() -> None:
    """
    Ensure Playwright can find browsers in bundled environment.

    Sets PLAYWRIGHT_BROWSERS_PATH environment variable to bundled browsers
    if they exist and the variable is not already set.
    """
    if os.environ.get('PLAYWRIGHT_BROWSERS_PATH'):
        return

    try:
        base = _get_bundle_root()

        # Try different possible locations
        possible_paths = [
            base / 'runtime' / 'ms-playwright',
            base / 'ms-playwright',
            base.parent / 'ms-playwright'
        ]

        for ms_dir in possible_paths:
            if ms_dir.exists():
                os.environ['PLAYWRIGHT_BROWSERS_PATH'] = str(ms_dir)
                logger.info(f"Set PLAYWRIGHT_BROWSERS_PATH to: {ms_dir}")
                return

        logger.warning("No bundled Playwright browsers found")

    except Exception as e:
        logger.warning(f"Could not setup Playwright browsers path: {e}")

class CloudSkillAutomation:
    """
    Professional automation class for Google Cloud Skills Boost registration.

    This class provides comprehensive automation capabilities with proper
    error handling, browser management, and captcha solving integration.
    """

    def __init__(self,
                 headless: bool = None,
                 captcha_solver=None,
                 keep_browser_open: bool = False,
                 extension_mode: bool = False,
                 timeout: int = None):
        """
        Initialize the automation service.

        Args:
            headless: Run browser in headless mode (default from config)
            captcha_solver: Captcha solver service instance
            keep_browser_open: Keep browser open after automation
            extension_mode: Use browser extensions (e.g., AntiCaptcha)
            timeout: Operation timeout in milliseconds
        """
        self.headless = headless if headless is not None else PLAYWRIGHT_HEADLESS
        self.captcha_solver = captcha_solver
        self.keep_browser_open = keep_browser_open
        self.extension_mode = extension_mode
        self.timeout = timeout or PLAYWRIGHT_TIMEOUT

        # Browser components
        self.playwright: Optional[Playwright] = None
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None

        # Setup logging
        self.logger = setup_logger('CloudSkillAutomation')

        # Ensure browser path is set
        _ensure_playwright_browsers_path()

        # State management
        self.state_file = self._get_state_file_path()
        self.profile_dir = self._get_profile_directory()

        self.logger.info("CloudSkill automation initialized")

    async def initialize_browser(self) -> bool:
        """
        Initialize browser and context.

        Returns:
            bool: True if initialization successful
        """
        try:
            log_automation_step("Browser initialization", "STARTED")

            # Start Playwright
            self.playwright = await async_playwright().start()

            # Setup browser options
            browser_options = {
                "headless": self.headless,
                "args": [
                    "--no-sandbox",
                    "--disable-blink-features=AutomationControlled",
                    "--disable-web-security",
                    "--disable-features=VizDisplayCompositor",
                    "--disable-dev-shm-usage",
                    f"--user-agent={BROWSER_USER_AGENT}"
                ]
            }

            # Add extension support if enabled
            if self.extension_mode:
                extension_path = self._get_extension_path()
                if extension_path and extension_path.exists():
                    browser_options["args"].extend([
                        f"--load-extension={extension_path}",
                        "--disable-extensions-except=" + str(extension_path)
                    ])
                    self.logger.info(f"Loading extension from: {extension_path}")

            # Launch browser
            self.browser = await self.playwright.chromium.launch(**browser_options)

            # Create context with state persistence
            context_options = {
                "user_agent": BROWSER_USER_AGENT,
                "viewport": {"width": 1920, "height": 1080},
                "locale": "en-US",
                "timezone_id": "America/New_York",
                "ignore_https_errors": True,
                "java_script_enabled": True,
                "accept_downloads": True
            }

            # Load existing state if available
            if self.state_file.exists():
                try:
                    context_options["storage_state"] = str(self.state_file)
                    self.logger.info("Loaded existing browser state")
                except Exception as e:
                    self.logger.warning(f"Could not load browser state: {e}")

            self.context = await self.browser.new_context(**context_options)

            # Create new page
            self.page = await self.context.new_page()

            # Set default timeout
            self.page.set_default_timeout(self.timeout)

            log_automation_step("Browser initialization", "SUCCESS")
            return True

        except Exception as e:
            self.logger.error(f"Browser initialization failed: {e}")
            log_automation_step("Browser initialization", "FAILED", str(e))
            return False

    async def register_account(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Register a new Google Cloud Skills Boost account.

        Args:
            user_data: User registration data

        Returns:
            Dict: Registration result
        """
        result = {
            "success": False,
            "email": user_data.get("email"),
            "message": "",
            "steps_completed": [],
            "error": None
        }

        try:
            if not self.page:
                if not await self.initialize_browser():
                    result["error"] = "Browser initialization failed"
                    return result

            # Validate user data
            self._validate_user_data(user_data)

            # Step 1: Navigate to registration page
            log_automation_step("Navigate to registration", "STARTED")
            await self.page.goto(CLOUDSKILL_REGISTER_URL, wait_until="domcontentloaded")
            await self.page.wait_for_load_state("networkidle", timeout=10000)
            result["steps_completed"].append("navigation")
            log_automation_step("Navigate to registration", "SUCCESS")

            # Step 2: Fill registration form
            log_automation_step("Fill registration form", "STARTED")
            if await self._fill_registration_form(user_data):
                result["steps_completed"].append("form_fill")
                log_automation_step("Fill registration form", "SUCCESS")
            else:
                raise Exception("Failed to fill registration form")

            # Step 3: Handle captcha if present
            if await self._handle_captcha():
                result["steps_completed"].append("captcha")
                log_automation_step("Captcha handling", "SUCCESS")

            # Step 4: Submit form
            log_automation_step("Submit registration", "STARTED")
            if await self._submit_registration_form():
                result["steps_completed"].append("submit")
                log_automation_step("Submit registration", "SUCCESS")
            else:
                raise Exception("Failed to submit registration")

            # Step 5: Verify registration success
            log_automation_step("Verify registration", "STARTED")
            if await self._verify_registration_success():
                result["success"] = True
                result["message"] = "Registration completed successfully"
                result["steps_completed"].append("verification")
                log_automation_step("Verify registration", "SUCCESS")
            else:
                result["message"] = "Registration submitted but verification unclear"

            # Save browser state
            await self._save_browser_state()

            return result

        except Exception as e:
            error_msg = str(e)
            result["error"] = error_msg
            result["message"] = f"Registration failed: {error_msg}"
            self.logger.error(f"Registration failed: {e}")
            log_automation_step("Account registration", "FAILED", error_msg)
            return result

    async def _fill_registration_form(self, user_data: Dict[str, Any]) -> bool:
        """
        Fill the registration form with user data.

        Args:
            user_data: User registration data

        Returns:
            bool: True if form filled successfully
        """
        try:
            # Wait for form to be visible
            await self.page.wait_for_selector("form", timeout=10000)

            # Fill first name
            first_name_selector = 'input[name="firstName"], input[id*="firstName"], input[placeholder*="first name" i]'
            if await self.page.is_visible(first_name_selector):
                await self.page.fill(first_name_selector, user_data.get("first_name", ""))

            # Fill last name
            last_name_selector = 'input[name="lastName"], input[id*="lastName"], input[placeholder*="last name" i]'
            if await self.page.is_visible(last_name_selector):
                await self.page.fill(last_name_selector, user_data.get("last_name", ""))

            # Fill email
            email_selector = 'input[type="email"], input[name="email"], input[id*="email"]'
            if await self.page.is_visible(email_selector):
                await self.page.fill(email_selector, user_data.get("email", ""))

            # Fill password
            password_selector = 'input[type="password"], input[name="password"], input[id*="password"]'
            if await self.page.is_visible(password_selector):
                await self.page.fill(password_selector, user_data.get("password", ""))

            # Fill company if present
            company_selector = 'input[name="company"], input[id*="company"], input[placeholder*="company" i]'
            if await self.page.is_visible(company_selector):
                await self.page.fill(company_selector, user_data.get("company", ""))

            # Handle additional fields as needed
            await self._handle_additional_form_fields(user_data)

            return True

        except Exception as e:
            self.logger.error(f"Form filling failed: {e}")
            return False

    async def _handle_additional_form_fields(self, user_data: Dict[str, Any]) -> None:
        """
        Handle additional form fields that may be present.

        Args:
            user_data: User registration data
        """
        try:
            # Handle checkboxes (terms, privacy, etc.)
            checkboxes = await self.page.query_selector_all('input[type="checkbox"]')
            for checkbox in checkboxes:
                try:
                    await checkbox.check()
                except Exception:
                    pass  # Some checkboxes may not be checkable

            # Handle select dropdowns
            selects = await self.page.query_selector_all("select")
            for select in selects:
                try:
                    # Try to select first non-empty option
                    options = await select.query_selector_all("option")
                    if len(options) > 1:
                        await select.select_option(index=1)
                except Exception:
                    pass

        except Exception as e:
            self.logger.warning(f"Error handling additional form fields: {e}")

    async def _handle_captcha(self) -> bool:
        """
        Handle captcha challenges if present.

        Returns:
            bool: True if captcha handled or not present
        """
        try:
            # Check for various captcha types
            captcha_selectors = [
                'iframe[src*="recaptcha"]',
                '.g-recaptcha',
                '.h-captcha',
                'iframe[src*="hcaptcha"]',
                '[data-sitekey]'
            ]

            for selector in captcha_selectors:
                if await self.page.is_visible(selector):
                    self.logger.info(f"Captcha detected: {selector}")

                    if self.extension_mode:
                        # Wait for extension to solve
                        log_automation_step("Captcha (Extension)", "WAITING")
                        await self.page.wait_for_timeout(5000)
                        return True

                    elif self.captcha_solver:
                        # Try automated solving
                        return await self._solve_captcha_automatically()

                    else:
                        self.logger.warning("Captcha detected but no solver available")
                        return False

            return True  # No captcha found

        except Exception as e:
            self.logger.error(f"Captcha handling failed: {e}")
            return False

    async def _solve_captcha_automatically(self) -> bool:
        """
        Attempt to solve captcha automatically using captcha solver.

        Returns:
            bool: True if captcha solved
        """
        try:
            # Look for audio captcha option
            audio_button = await self.page.query_selector('button[aria-label*="audio"], button[title*="audio"]')
            if audio_button:
                await audio_button.click()
                await self.page.wait_for_timeout(2000)

                # Get audio source
                audio_element = await self.page.query_selector('audio source, audio')
                if audio_element:
                    audio_src = await audio_element.get_attribute('src')
                    if audio_src and self.captcha_solver:
                        result = self.captcha_solver.solve_audio_captcha(audio_src)
                        if result:
                            # Enter the result
                            input_field = await self.page.query_selector('input[type="text"]')
                            if input_field:
                                await input_field.fill(result)
                                return True

            return False

        except Exception as e:
            self.logger.error(f"Automatic captcha solving failed: {e}")
            return False

    async def _submit_registration_form(self) -> bool:
        """
        Submit the registration form.

        Returns:
            bool: True if form submitted successfully
        """
        try:
            # Find and click submit button
            submit_selectors = [
                'button[type="submit"]',
                'input[type="submit"]',
                'button:has-text("Sign up")',
                'button:has-text("Register")',
                'button:has-text("Create")',
                '.submit-button',
                '#submit'
            ]

            for selector in submit_selectors:
                try:
                    element = await self.page.query_selector(selector)
                    if element and await element.is_visible():
                        await element.click()
                        await self.page.wait_for_timeout(2000)
                        return True
                except Exception:
                    continue

            return False

        except Exception as e:
            self.logger.error(f"Form submission failed: {e}")
            return False

    async def _verify_registration_success(self) -> bool:
        """
        Verify that registration was successful.

        Returns:
            bool: True if registration appears successful
        """
        try:
            # Wait for navigation or success indicators
            await self.page.wait_for_timeout(3000)

            # Check for success indicators
            success_indicators = [
                "check your email",
                "confirmation email",
                "account created",
                "registration successful",
                "welcome",
                "verify your email"
            ]

            page_content = await self.page.content()
            page_content_lower = page_content.lower()

            for indicator in success_indicators:
                if indicator in page_content_lower:
                    self.logger.info(f"Success indicator found: {indicator}")
                    return True

            # Check URL change
            current_url = self.page.url
            if current_url != CLOUDSKILL_REGISTER_URL:
                self.logger.info(f"URL changed to: {current_url}")
                return True

            return False

        except Exception as e:
            self.logger.error(f"Registration verification failed: {e}")
            return False

    def _validate_user_data(self, user_data: Dict[str, Any]) -> None:
        """
        Validate user data before registration.

        Args:
            user_data: User data to validate

        Raises:
            ValidationError: If validation fails
        """
        required_fields = ["first_name", "last_name", "email", "password"]

        for field in required_fields:
            if not user_data.get(field):
                raise ValidationError(f"Missing required field: {field}")

        # Validate email format
        validate_email(user_data["email"])

    def _get_state_file_path(self) -> Path:
        """Get path for browser state persistence."""
        try:
            local_app_data = os.environ.get('LOCALAPPDATA')
            if not local_app_data:
                local_app_data = Path.home() / "AppData" / "Local"

            state_dir = Path(local_app_data) / "AutoCloudSkill" / "playwright"
            state_dir.mkdir(parents=True, exist_ok=True)
            return state_dir / ".pw-state.json"

        except Exception:
            return Path.cwd() / ".pw-state.json"

    def _get_profile_directory(self) -> Path:
        """Get path for browser profile directory."""
        try:
            local_app_data = os.environ.get('LOCALAPPDATA')
            if not local_app_data:
                local_app_data = Path.home() / "AppData" / "Local"

            profile_dir = Path(local_app_data) / "AutoCloudSkill" / "playwright" / "profile"
            profile_dir.mkdir(parents=True, exist_ok=True)
            return profile_dir

        except Exception:
            return Path.cwd() / "profile"

    def _get_extension_path(self) -> Optional[Path]:
        """Get path to browser extension."""
        base = _get_bundle_root()

        possible_paths = [
            base / "runtime" / "_internal" / "AntiCaptcha",
            base / "_internal" / "AntiCaptcha",
            base.parent / "_internal" / "AntiCaptcha"
        ]

        for path in possible_paths:
            if path.exists() and (path / "manifest.json").exists():
                return path

        return None

    async def _save_browser_state(self) -> None:
        """Save current browser state for persistence."""
        try:
            if self.context:
                await self.context.storage_state(path=str(self.state_file))
                self.logger.info("Browser state saved")
        except Exception as e:
            self.logger.warning(f"Could not save browser state: {e}")

    async def cleanup(self) -> None:
        """Clean up browser resources."""
        try:
            if not self.keep_browser_open:
                if self.context:
                    await self.context.close()
                if self.browser:
                    await self.browser.close()
                if self.playwright:
                    await self.playwright.stop()

            self.logger.info("Automation cleanup completed")

        except Exception as e:
            self.logger.error(f"Cleanup failed: {e}")

    async def __aenter__(self):
        """Async context manager entry."""
        await self.initialize_browser()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.cleanup()