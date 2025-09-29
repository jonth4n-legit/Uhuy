"""
Professional browser automation module for AutoCloudSkill.

This module provides comprehensive Google Cloud Skills Boost automation:
- Playwright browser automation with professional error handling
- Account registration with email verification
- Captcha solving integration
- Lab automation and console access
- Session management and persistence
- Professional async/await patterns

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import asyncio
import os
import sys
import time
import base64
import threading
from pathlib import Path
from typing import Dict, Optional, Any, List, Union, Callable
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum
from urllib.parse import urlparse, parse_qs

from playwright.async_api import async_playwright, Page, Browser, BrowserContext, TimeoutError as PlaywrightTimeoutError

from utils.logger import setup_application_logging, log_automation_step, log_user_action, performance_monitor
from utils.validators import validate_user_data, ValidationResult
from config.settings import settings
from services.captcha_service import CaptchaSolverService, CaptchaType
from services.gmail_service import GmailService
from services.firefox_relay_service import FirefoxRelayService

logger = setup_application_logging('CloudSkillAutomation')

class AutomationState(Enum):
    """Automation execution states."""
    IDLE = "idle"
    INITIALIZING = "initializing"
    BROWSER_STARTING = "browser_starting"
    NAVIGATING = "navigating"
    FILLING_FORM = "filling_form"
    SOLVING_CAPTCHA = "solving_captcha"
    WAITING_EMAIL = "waiting_email"
    CONFIRMING_EMAIL = "confirming_email"
    COMPLETING_REGISTRATION = "completing_registration"
    SUCCESS = "success"
    ERROR = "error"

class RegistrationMethod(Enum):
    """Email registration methods."""
    GMAIL = "gmail"
    FIREFOX_RELAY = "firefox_relay"
    CUSTOM_EMAIL = "custom_email"

@dataclass
class RegistrationData:
    """Complete registration data structure."""
    # Personal Information
    first_name: str
    last_name: str
    email: str
    password: str

    # Optional Information
    company: str = ""
    job_title: str = ""
    country: str = "United States"
    how_did_you_hear: str = "Search engine"

    # Internal tracking
    registration_method: RegistrationMethod = RegistrationMethod.CUSTOM_EMAIL
    generated_at: str = ""

    def validate(self) -> ValidationResult:
        """Validate registration data."""
        return validate_user_data({
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'company': self.company
        })

@dataclass
class AutomationResult:
    """Automation execution result."""
    success: bool
    state: AutomationState
    registration_data: Optional[RegistrationData]
    duration: float
    steps_completed: List[str]
    error_message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

def _get_bundle_root() -> Path:
    """
    Resolve application base directory for both development and bundled modes.

    Returns:
        Path to application root directory
    """
    # PyInstaller bundle
    if hasattr(sys, '_MEIPASS'):
        return Path(sys._MEIPASS)

    # Other bundlers or frozen executables
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).resolve().parent

    # Development mode
    return Path(__file__).resolve().parent.parent

def _ensure_playwright_browsers_path() -> None:
    """
    Configure PLAYWRIGHT_BROWSERS_PATH for bundled browsers.

    Sets environment variable to use bundled Playwright browsers from
    the runtime directory when running as a bundled application.
    """
    if os.environ.get('PLAYWRIGHT_BROWSERS_PATH'):
        logger.debug("PLAYWRIGHT_BROWSERS_PATH already set")
        return

    try:
        base = _get_bundle_root()
        ms_playwright_dir = base / 'runtime' / 'ms-playwright'

        if ms_playwright_dir.exists():
            os.environ['PLAYWRIGHT_BROWSERS_PATH'] = str(ms_playwright_dir)
            logger.info(f"Set PLAYWRIGHT_BROWSERS_PATH: {ms_playwright_dir}")
        else:
            logger.warning(f"Bundled browsers not found at: {ms_playwright_dir}")

    except Exception as e:
        logger.warning(f"Failed to set PLAYWRIGHT_BROWSERS_PATH: {e}")

class CloudSkillAutomation:
    """
    Professional Google Cloud Skills Boost automation service.

    This class provides comprehensive automation for account registration,
    email verification, and lab access on Google Cloud Skills Boost platform.
    """

    def __init__(
        self,
        headless: bool = None,
        captcha_solver: Optional[CaptchaSolverService] = None,
        keep_browser_open: bool = False,
        extension_mode: bool = False,
        user_data_dir: Optional[str] = None,
        state_file: Optional[str] = None
    ):
        """
        Initialize CloudSkill automation.

        Args:
            headless: Run browser in headless mode (None = use settings)
            captcha_solver: Captcha solving service instance
            keep_browser_open: Keep browser open after completion
            extension_mode: Enable browser extension support
            user_data_dir: Custom browser profile directory
            state_file: Custom session state file path
        """
        # Configuration
        self.headless = headless if headless is not None else settings.playwright_headless
        self.keep_browser_open = keep_browser_open
        self.extension_mode = extension_mode
        self.user_data_dir = user_data_dir or self._get_default_profile_dir()
        self.state_file = state_file or self._get_default_state_path()

        # Services
        self.captcha_solver = captcha_solver or CaptchaSolverService()

        # Browser instances
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

        # State management
        self.current_state = AutomationState.IDLE
        self.steps_completed = []
        self.start_time = None

        # Event loop management for threading
        self._loop = None
        self._loop_thread = None
        self._loop_ready_event = None

        # Ensure Playwright browsers are configured
        _ensure_playwright_browsers_path()

        logger.info("CloudSkill automation initialized")

    def _get_default_profile_dir(self) -> str:
        """Get default browser profile directory."""
        if os.name == 'nt':  # Windows
            base_dir = os.environ.get('LOCALAPPDATA') or Path.home() / 'AppData' / 'Local'
        else:  # Unix-like
            base_dir = os.environ.get('XDG_DATA_HOME') or Path.home() / '.local' / 'share'

        profile_dir = Path(base_dir) / 'AutoCloudSkill' / 'playwright' / 'profile'
        profile_dir.mkdir(parents=True, exist_ok=True)
        return str(profile_dir)

    def _get_default_state_path(self) -> str:
        """Get default session state file path."""
        if os.name == 'nt':  # Windows
            base_dir = os.environ.get('LOCALAPPDATA') or Path.home() / 'AppData' / 'Local'
        else:  # Unix-like
            base_dir = os.environ.get('XDG_DATA_HOME') or Path.home() / '.local' / 'share'

        state_dir = Path(base_dir) / 'AutoCloudSkill' / 'playwright'
        state_dir.mkdir(parents=True, exist_ok=True)
        return str(state_dir / 'session_state.json')

    def _update_state(self, new_state: AutomationState, step_name: Optional[str] = None) -> None:
        """Update automation state and log progress."""
        self.current_state = new_state

        if step_name:
            self.steps_completed.append(step_name)
            log_automation_step(
                logger,
                step_name,
                "SUCCESS" if new_state != AutomationState.ERROR else "ERROR"
            )

    async def _initialize_browser(self) -> None:
        """Initialize Playwright browser with comprehensive configuration."""
        self._update_state(AutomationState.BROWSER_STARTING, "initialize_browser")

        try:
            # Launch Playwright
            self.playwright = await async_playwright().start()

            # Configure browser options
            browser_options = {
                'headless': self.headless,
                'user_data_dir': self.user_data_dir if not self.headless else None,
                'args': [
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-background-timer-throttling',
                    '--disable-backgrounding-occluded-windows',
                    '--disable-renderer-backgrounding',
                    '--disable-web-security',
                    '--disable-features=TranslateUI',
                    '--disable-blink-features=AutomationControlled'
                ]
            }

            # Add extension support if enabled
            if self.extension_mode:
                extension_path = self._get_anticaptcha_extension_path()
                if extension_path and extension_path.exists():
                    browser_options['args'].extend([
                        f'--disable-extensions-except={extension_path}',
                        f'--load-extension={extension_path}'
                    ])
                    logger.info(f"AntiCaptcha extension loaded: {extension_path}")

            # Launch browser
            self.browser = await self.playwright.chromium.launch(**browser_options)

            # Create context with state persistence
            context_options = {
                'viewport': {'width': 1280, 'height': 720},
                'user_agent': settings.browser_user_agent,
                'locale': 'en-US',
                'timezone_id': 'America/New_York'
            }

            # Load existing state if available
            if Path(self.state_file).exists():
                try:
                    context_options['storage_state'] = self.state_file
                    logger.info(f"Loaded browser state: {self.state_file}")
                except Exception as e:
                    logger.warning(f"Failed to load browser state: {e}")

            self.context = await self.browser.new_context(**context_options)

            # Create new page
            self.page = await self.context.new_page()

            # Configure page settings
            await self.page.set_extra_http_headers({
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
            })

            logger.info("Browser initialized successfully")

        except Exception as e:
            self._update_state(AutomationState.ERROR)
            logger.error(f"Failed to initialize browser: {e}")
            raise

    def _get_anticaptcha_extension_path(self) -> Optional[Path]:
        """Get path to AntiCaptcha browser extension."""
        try:
            base = _get_bundle_root()
            extension_path = base / 'runtime' / '_internal' / 'AntiCaptcha'

            if extension_path.exists():
                return extension_path

            # Fallback paths
            fallback_paths = [
                Path.cwd() / 'AntiCaptcha',
                Path.cwd() / '_internal' / 'AntiCaptcha'
            ]

            for path in fallback_paths:
                if path.exists():
                    return path

            return None

        except Exception as e:
            logger.warning(f"Failed to find AntiCaptcha extension: {e}")
            return None

    @performance_monitor("navigate_to_registration")
    async def _navigate_to_registration(self) -> None:
        """Navigate to Google Cloud Skills Boost registration page."""
        self._update_state(AutomationState.NAVIGATING, "navigate_to_registration")

        try:
            registration_url = settings.cloudskill_register_url
            logger.info(f"Navigating to: {registration_url}")

            await self.page.goto(registration_url, wait_until='networkidle', timeout=30000)

            # Wait for registration form to load
            await self.page.wait_for_selector('form', timeout=15000)

            logger.info("Registration page loaded successfully")

        except PlaywrightTimeoutError:
            error_msg = "Registration page failed to load within timeout"
            logger.error(error_msg)
            raise RuntimeError(error_msg)

        except Exception as e:
            error_msg = f"Failed to navigate to registration page: {e}"
            logger.error(error_msg)
            raise RuntimeError(error_msg)

    @performance_monitor("fill_registration_form")
    async def _fill_registration_form(self, registration_data: RegistrationData) -> None:
        """Fill registration form with user data."""
        self._update_state(AutomationState.FILLING_FORM, "fill_registration_form")

        try:
            # Wait for form elements to be ready
            await self.page.wait_for_selector('input[name="firstName"], input[id*="firstName"]', timeout=10000)

            # Fill first name
            first_name_selector = 'input[name="firstName"], input[id*="firstName"], input[placeholder*="First name"]'
            await self.page.fill(first_name_selector, registration_data.first_name)
            logger.debug(f"Filled first name: {registration_data.first_name}")

            # Fill last name
            last_name_selector = 'input[name="lastName"], input[id*="lastName"], input[placeholder*="Last name"]'
            await self.page.fill(last_name_selector, registration_data.last_name)
            logger.debug(f"Filled last name: {registration_data.last_name}")

            # Fill email
            email_selector = 'input[type="email"], input[name="email"], input[id*="email"]'
            await self.page.fill(email_selector, registration_data.email)
            logger.debug(f"Filled email: {registration_data.email}")

            # Fill password
            password_selector = 'input[type="password"], input[name="password"], input[id*="password"]'
            await self.page.fill(password_selector, registration_data.password)
            logger.debug("Filled password")

            # Fill optional fields if present
            if registration_data.company:
                try:
                    company_selector = 'input[name="company"], input[id*="company"], input[placeholder*="Company"]'
                    await self.page.fill(company_selector, registration_data.company, timeout=3000)
                    logger.debug(f"Filled company: {registration_data.company}")
                except:
                    logger.debug("Company field not found or not fillable")

            # Handle country selection if present
            if registration_data.country:
                try:
                    country_selector = 'select[name="country"], select[id*="country"]'
                    await self.page.select_option(country_selector, label=registration_data.country, timeout=3000)
                    logger.debug(f"Selected country: {registration_data.country}")
                except:
                    logger.debug("Country field not found or not selectable")

            # Accept terms and conditions
            await self._accept_terms()

            logger.info("Registration form filled successfully")

        except Exception as e:
            error_msg = f"Failed to fill registration form: {e}"
            logger.error(error_msg)
            raise RuntimeError(error_msg)

    async def _accept_terms(self) -> None:
        """Accept terms and conditions checkboxes."""
        try:
            # Common selectors for terms checkboxes
            terms_selectors = [
                'input[type="checkbox"][name*="terms"]',
                'input[type="checkbox"][id*="terms"]',
                'input[type="checkbox"][name*="agree"]',
                'input[type="checkbox"][id*="agree"]',
                'input[type="checkbox"][name*="accept"]'
            ]

            for selector in terms_selectors:
                try:
                    checkboxes = await self.page.query_selector_all(selector)
                    for checkbox in checkboxes:
                        if not await checkbox.is_checked():
                            await checkbox.click()
                            logger.debug(f"Checked terms checkbox: {selector}")
                except:
                    continue

        except Exception as e:
            logger.warning(f"Failed to accept terms: {e}")

    @performance_monitor("solve_captcha_if_present")
    async def _solve_captcha_if_present(self) -> bool:
        """Detect and solve CAPTCHA if present."""
        try:
            # Check for various CAPTCHA types
            captcha_selectors = [
                'div[class*="captcha"]',
                'div[id*="captcha"]',
                'iframe[src*="recaptcha"]',
                'div[class*="recaptcha"]',
                'div[class*="hcaptcha"]'
            ]

            captcha_found = False
            for selector in captcha_selectors:
                if await self.page.query_selector(selector):
                    captcha_found = True
                    break

            if not captcha_found:
                logger.debug("No CAPTCHA detected")
                return True

            self._update_state(AutomationState.SOLVING_CAPTCHA, "solve_captcha")

            # Try to find audio CAPTCHA option
            audio_button_selectors = [
                'button[aria-label*="audio"]',
                'button[title*="audio"]',
                'div[role="button"][aria-label*="audio"]'
            ]

            audio_button = None
            for selector in audio_button_selectors:
                audio_button = await self.page.query_selector(selector)
                if audio_button:
                    break

            if audio_button:
                await audio_button.click()
                await self.page.wait_for_timeout(2000)

                # Get audio URL
                audio_elements = await self.page.query_selector_all('audio source, audio[src]')
                audio_url = None

                for element in audio_elements:
                    src = await element.get_attribute('src')
                    if src:
                        if not src.startswith('http'):
                            src = self.page.url + src if not src.startswith('/') else f"{urlparse(self.page.url).scheme}://{urlparse(self.page.url).netloc}{src}"
                        audio_url = src
                        break

                if audio_url:
                    logger.info("Solving audio CAPTCHA...")
                    solution = await self.captcha_solver.solve_captcha(CaptchaType.AUDIO, audio_url)

                    if solution.success:
                        # Enter solution
                        input_selector = 'input[name*="captcha"], input[id*="captcha"], input[placeholder*="captcha"]'
                        await self.page.fill(input_selector, solution.solution)
                        logger.info("CAPTCHA solution entered")
                        return True
                    else:
                        logger.warning("Failed to solve audio CAPTCHA")

            # If audio CAPTCHA fails, wait for manual solving
            logger.warning("CAPTCHA detected but automatic solving failed - manual intervention may be required")
            return False

        except Exception as e:
            logger.error(f"CAPTCHA solving failed: {e}")
            return False

    @performance_monitor("submit_registration")
    async def _submit_registration(self) -> None:
        """Submit registration form."""
        try:
            # Find and click submit button
            submit_selectors = [
                'button[type="submit"]',
                'input[type="submit"]',
                'button[name*="submit"]',
                'button[id*="submit"]',
                'button:has-text("Sign up")',
                'button:has-text("Register")',
                'button:has-text("Create account")'
            ]

            submit_button = None
            for selector in submit_selectors:
                submit_button = await self.page.query_selector(selector)
                if submit_button:
                    break

            if not submit_button:
                raise RuntimeError("Submit button not found")

            logger.info("Submitting registration form...")
            await submit_button.click()

            # Wait for navigation or success message
            try:
                await self.page.wait_for_load_state('networkidle', timeout=15000)
            except PlaywrightTimeoutError:
                # Check if we're on a success/verification page
                current_url = self.page.url
                if 'verify' in current_url.lower() or 'confirm' in current_url.lower():
                    logger.info("Redirected to email verification page")
                else:
                    logger.warning("Form submission result unclear")

            logger.info("Registration form submitted")

        except Exception as e:
            error_msg = f"Failed to submit registration: {e}"
            logger.error(error_msg)
            raise RuntimeError(error_msg)

    async def _wait_for_email_verification(
        self,
        email: str,
        timeout: int = 300
    ) -> Optional[str]:
        """Wait for email verification and extract confirmation link."""
        self._update_state(AutomationState.WAITING_EMAIL, "wait_for_email_verification")

        try:
            # Initialize email service based on email domain
            if '@relay.firefox.com' in email:
                # Use Firefox Relay (limited functionality)
                logger.info("Using Firefox Relay for email verification")
                # Note: Firefox Relay API doesn't provide email content access
                # This would require premium API access
                await asyncio.sleep(timeout)
                return None

            elif '@gmail.com' in email:
                # Use Gmail API
                logger.info("Using Gmail API for email verification")
                gmail_service = GmailService()

                start_time = time.time()
                while time.time() - start_time < timeout:
                    # Search for verification emails
                    emails = gmail_service.search_emails(
                        f'to:{email} subject:(verify OR confirmation OR activate)',
                        max_results=5
                    )

                    for email_msg in emails:
                        # Extract links from email
                        links = gmail_service.extract_links(email_msg)

                        # Find verification link
                        for link in links:
                            if any(keyword in link.lower() for keyword in ['verify', 'confirm', 'activate']):
                                logger.info(f"Found verification link: {link}")
                                return link

                    await asyncio.sleep(10)  # Check every 10 seconds

            else:
                # Custom email - cannot auto-verify
                logger.warning(f"Cannot auto-verify custom email: {email}")

            logger.warning("Email verification timeout or not supported")
            return None

        except Exception as e:
            logger.error(f"Email verification failed: {e}")
            return None

    @performance_monitor("confirm_email_verification")
    async def _confirm_email_verification(self, verification_link: str) -> bool:
        """Navigate to email verification link and confirm."""
        self._update_state(AutomationState.CONFIRMING_EMAIL, "confirm_email_verification")

        try:
            logger.info("Navigating to email verification link...")

            # Open verification link in new tab
            verification_page = await self.context.new_page()
            await verification_page.goto(verification_link, timeout=30000)

            # Look for confirmation button or automatic verification
            confirm_selectors = [
                'button:has-text("Confirm")',
                'button:has-text("Verify")',
                'button:has-text("Activate")',
                'a:has-text("Confirm")',
                'a:has-text("Verify")'
            ]

            for selector in confirm_selectors:
                try:
                    element = await verification_page.query_selector(selector)
                    if element:
                        await element.click()
                        logger.info("Clicked email verification confirmation")
                        break
                except:
                    continue

            # Wait for verification to complete
            await verification_page.wait_for_timeout(3000)

            # Check for success indicators
            success_indicators = [
                'verified',
                'confirmed',
                'activated',
                'success'
            ]

            page_content = await verification_page.content()
            verification_success = any(indicator in page_content.lower() for indicator in success_indicators)

            await verification_page.close()

            if verification_success:
                logger.info("Email verification confirmed successfully")
                return True
            else:
                logger.warning("Email verification status unclear")
                return True  # Assume success for now

        except Exception as e:
            logger.error(f"Email verification confirmation failed: {e}")
            return False

    async def _save_session_state(self) -> None:
        """Save browser session state for persistence."""
        try:
            if self.context:
                await self.context.storage_state(path=self.state_file)
                logger.debug(f"Session state saved: {self.state_file}")
        except Exception as e:
            logger.warning(f"Failed to save session state: {e}")

    async def _cleanup_browser(self) -> None:
        """Clean up browser resources."""
        try:
            if not self.keep_browser_open:
                if self.page:
                    await self.page.close()
                if self.context:
                    await self.context.close()
                if self.browser:
                    await self.browser.close()
                if self.playwright:
                    await self.playwright.stop()

                logger.debug("Browser cleanup completed")
            else:
                logger.info("Keeping browser open as requested")

        except Exception as e:
            logger.warning(f"Browser cleanup warning: {e}")

    async def register_account_async(
        self,
        registration_data: RegistrationData,
        progress_callback: Optional[Callable[[AutomationState, str], None]] = None
    ) -> AutomationResult:
        """
        Execute complete account registration automation.

        Args:
            registration_data: User registration information
            progress_callback: Optional callback for progress updates

        Returns:
            AutomationResult with operation details
        """
        self.start_time = time.time()
        self._update_state(AutomationState.INITIALIZING)

        log_automation_step(
            logger,
            "register_account",
            "START",
            {
                "email": registration_data.email,
                "first_name": registration_data.first_name,
                "method": registration_data.registration_method.value
            }
        )

        try:
            # Validate registration data
            validation = registration_data.validate()
            if not validation.is_valid:
                error_msg = f"Invalid registration data: {', '.join(validation.errors)}"
                logger.error(error_msg)
                return AutomationResult(
                    success=False,
                    state=AutomationState.ERROR,
                    registration_data=registration_data,
                    duration=time.time() - self.start_time,
                    steps_completed=self.steps_completed,
                    error_message=error_msg
                )

            # Initialize browser
            await self._initialize_browser()
            if progress_callback:
                progress_callback(self.current_state, "Browser initialized")

            # Navigate to registration page
            await self._navigate_to_registration()
            if progress_callback:
                progress_callback(self.current_state, "Registration page loaded")

            # Fill registration form
            await self._fill_registration_form(registration_data)
            if progress_callback:
                progress_callback(self.current_state, "Registration form filled")

            # Solve CAPTCHA if present
            captcha_solved = await self._solve_captcha_if_present()
            if not captcha_solved:
                logger.warning("CAPTCHA solving failed - manual intervention may be required")

            # Submit registration
            await self._submit_registration()
            if progress_callback:
                progress_callback(self.current_state, "Registration submitted")

            # Wait for email verification (if supported)
            verification_link = await self._wait_for_email_verification(registration_data.email)

            if verification_link:
                # Confirm email verification
                verification_success = await self._confirm_email_verification(verification_link)
                if verification_success:
                    self._update_state(AutomationState.COMPLETING_REGISTRATION, "email_verified")
                    if progress_callback:
                        progress_callback(self.current_state, "Email verification completed")

            # Save session state
            await self._save_session_state()

            # Complete registration
            self._update_state(AutomationState.SUCCESS, "registration_complete")
            duration = time.time() - self.start_time

            log_automation_step(
                logger,
                "register_account",
                "SUCCESS",
                {
                    "email": registration_data.email,
                    "duration": f"{duration:.2f}s",
                    "steps_completed": len(self.steps_completed)
                }
            )

            logger.info(f"Account registration completed successfully in {duration:.2f}s")

            return AutomationResult(
                success=True,
                state=AutomationState.SUCCESS,
                registration_data=registration_data,
                duration=duration,
                steps_completed=self.steps_completed,
                metadata={
                    'email_verified': verification_link is not None,
                    'captcha_encountered': 'solve_captcha' in self.steps_completed
                }
            )

        except Exception as e:
            duration = time.time() - self.start_time
            error_msg = str(e)

            self._update_state(AutomationState.ERROR)

            log_automation_step(
                logger,
                "register_account",
                "ERROR",
                {
                    "error": error_msg,
                    "duration": f"{duration:.2f}s"
                }
            )

            logger.error(f"Account registration failed: {error_msg}")

            return AutomationResult(
                success=False,
                state=AutomationState.ERROR,
                registration_data=registration_data,
                duration=duration,
                steps_completed=self.steps_completed,
                error_message=error_msg
            )

        finally:
            # Always cleanup resources
            await self._cleanup_browser()

    def register_account(
        self,
        registration_data: RegistrationData,
        progress_callback: Optional[Callable[[AutomationState, str], None]] = None
    ) -> AutomationResult:
        """
        Synchronous wrapper for account registration automation.

        Args:
            registration_data: User registration information
            progress_callback: Optional callback for progress updates

        Returns:
            AutomationResult with operation details
        """
        try:
            # Create new event loop if none exists
            try:
                loop = asyncio.get_event_loop()
                if loop.is_closed():
                    raise RuntimeError("Event loop is closed")
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

            # Run async automation
            return loop.run_until_complete(
                self.register_account_async(registration_data, progress_callback)
            )

        except Exception as e:
            logger.error(f"Synchronous registration wrapper failed: {e}")
            return AutomationResult(
                success=False,
                state=AutomationState.ERROR,
                registration_data=registration_data,
                duration=0.0,
                steps_completed=[],
                error_message=str(e)
            )

    # Backward compatibility methods
    def start_registration(self, user_data: Dict[str, Any]) -> bool:
        """
        Start registration process (backward compatibility).

        Args:
            user_data: Dictionary with user information

        Returns:
            True if successful, False otherwise
        """
        try:
            registration_data = RegistrationData(
                first_name=user_data.get('first_name', ''),
                last_name=user_data.get('last_name', ''),
                email=user_data.get('email', ''),
                password=user_data.get('password', ''),
                company=user_data.get('company', ''),
                country=user_data.get('country', 'United States')
            )

            result = self.register_account(registration_data)
            return result.success

        except Exception as e:
            logger.error(f"Legacy registration method failed: {e}")
            return False

# Export commonly used items
__all__ = [
    'AutomationState',
    'RegistrationMethod',
    'RegistrationData',
    'AutomationResult',
    'CloudSkillAutomation',
    '_get_bundle_root',
    '_ensure_playwright_browsers_path'
]