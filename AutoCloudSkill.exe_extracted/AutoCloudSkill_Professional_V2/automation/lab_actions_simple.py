"""
Professional lab automation actions for AutoCloudSkill.

This module provides comprehensive lab automation capabilities:
- Lab starting automation with intelligent button detection
- Google Cloud Console access automation
- GCloud terms handling
- GenAI API key creation automation
- Professional error handling and retry logic

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import asyncio
import re
import logging
from typing import Dict, List, Optional, Callable, Awaitable, Any
from dataclasses import dataclass
from enum import Enum
from urllib.parse import urlparse

from playwright.async_api import Page, Browser, BrowserContext, TimeoutError as PlaywrightTimeoutError

from utils.logger import setup_application_logging, log_automation_step, performance_monitor

logger = setup_application_logging('LabActions')

class LabStatus(Enum):
    """Lab operation status."""
    IDLE = "idle"
    STARTING = "starting"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CAPTCHA_REQUIRED = "captcha_required"

@dataclass
class LabResult:
    """Lab operation result."""
    success: bool
    status: LabStatus
    lab_url: str
    console_url: Optional[str] = None
    api_key: Optional[str] = None
    error_message: Optional[str] = None
    metadata: Dict[str, Any] = None

class LabAutomationService:
    """Professional lab automation service."""

    def __init__(self):
        """Initialize lab automation service."""
        self.logger = logger

        # Common button texts for lab starting
        self.start_button_texts = [
            # English variants
            'Start Lab',
            'START LAB',
            'Begin Lab',
            'Start',
            'Begin',

            # Indonesian variants
            'Mulai Lab',
            'MULAI LAB',
            'Mulai',

            # Extended variants
            'Start Lab, and you have',
            'Mulai Lab, dan Anda memiliki',

            # Case variations
            'start lab',
            'mulai lab',
            'Start lab',
            'Mulai lab'
        ]

    @performance_monitor("start_lab")
    async def start_lab(
        self,
        page: Page,
        lab_url: str,
        handle_captcha: Optional[Callable[[], Awaitable[bool]]] = None,
        wait_networkidle: bool = True,
        max_attempts: int = 3
    ) -> LabResult:
        """
        Start a lab with comprehensive automation.

        Args:
            page: Playwright page instance
            lab_url: URL of the lab to start
            handle_captcha: Optional CAPTCHA handler function
            wait_networkidle: Wait for network idle after navigation
            max_attempts: Maximum button click attempts

        Returns:
            LabResult with operation details
        """
        log_automation_step(
            self.logger,
            "start_lab",
            "START",
            {"lab_url": lab_url, "wait_networkidle": wait_networkidle}
        )

        try:
            # Navigate to lab page
            await self._navigate_to_lab(page, lab_url, wait_networkidle)

            # Attempt to click start button
            button_clicked = await self._click_start_button(page, max_attempts)

            if not button_clicked:
                error_msg = "Failed to find or click start lab button"
                return LabResult(
                    success=False,
                    status=LabStatus.FAILED,
                    lab_url=lab_url,
                    error_message=error_msg
                )

            # Handle CAPTCHA if present
            captcha_handled = True
            if handle_captcha:
                captcha_handled = await self._handle_captcha_if_present(page, handle_captcha)

            # Determine final status
            status = LabStatus.RUNNING if captcha_handled else LabStatus.CAPTCHA_REQUIRED

            result = LabResult(
                success=button_clicked and captcha_handled,
                status=status,
                lab_url=lab_url,
                metadata={
                    'button_clicked': button_clicked,
                    'captcha_handled': captcha_handled,
                    'final_url': page.url
                }
            )

            log_automation_step(
                self.logger,
                "start_lab",
                "SUCCESS" if result.success else "WARNING",
                {
                    "status": status.value,
                    "captcha_required": not captcha_handled
                }
            )

            return result

        except Exception as e:
            error_msg = f"Lab start failed: {e}"
            self.logger.error(error_msg)

            log_automation_step(
                self.logger,
                "start_lab",
                "ERROR",
                {"error": error_msg}
            )

            return LabResult(
                success=False,
                status=LabStatus.FAILED,
                lab_url=lab_url,
                error_message=error_msg
            )

    async def _navigate_to_lab(self, page: Page, lab_url: str, wait_networkidle: bool) -> None:
        """Navigate to lab page with proper waiting."""
        self.logger.info(f"Navigating to lab: {lab_url}")

        await page.goto(lab_url, wait_until='domcontentloaded', timeout=30000)

        if wait_networkidle:
            try:
                await page.wait_for_load_state('networkidle', timeout=15000)
            except PlaywrightTimeoutError:
                self.logger.warning("Network idle timeout - proceeding anyway")

        log_automation_step(
            self.logger,
            "navigate_lab",
            "SUCCESS",
            {"final_url": page.url}
        )

    async def _click_start_button(self, page: Page, max_attempts: int) -> bool:
        """Find and click start lab button with multiple strategies."""
        for attempt in range(max_attempts):
            if attempt > 0:
                log_automation_step(
                    self.logger,
                    "find_start_button",
                    "RETRY",
                    {"attempt": attempt + 1}
                )
                await page.wait_for_timeout(2000)

            # Strategy 1: Role-based button detection
            for text in self.start_button_texts:
                try:
                    # Exact text match
                    button = page.get_by_role('button', name=text)
                    if await button.is_visible(timeout=1000):
                        await button.click()
                        log_automation_step(
                            self.logger,
                            "start_button_click",
                            "SUCCESS",
                            {"method": "role_exact", "text": text}
                        )
                        return True

                    # Regex match
                    button = page.get_by_role('button', name=re.compile(text, re.IGNORECASE))
                    if await button.is_visible(timeout=1000):
                        await button.click()
                        log_automation_step(
                            self.logger,
                            "start_button_click",
                            "SUCCESS",
                            {"method": "role_regex", "text": text}
                        )
                        return True

                except Exception:
                    continue

            # Strategy 2: Text-based locator
            for text in self.start_button_texts:
                try:
                    button = page.get_by_text(text, exact=True)
                    if await button.is_visible(timeout=1000):
                        await button.click()
                        log_automation_step(
                            self.logger,
                            "start_button_click",
                            "SUCCESS",
                            {"method": "text_exact", "text": text}
                        )
                        return True

                    button = page.get_by_text(re.compile(text, re.IGNORECASE))
                    if await button.is_visible(timeout=1000):
                        await button.click()
                        log_automation_step(
                            self.logger,
                            "start_button_click",
                            "SUCCESS",
                            {"method": "text_regex", "text": text}
                        )
                        return True

                except Exception:
                    continue

            # Strategy 3: CSS selector-based detection
            button_selectors = [
                'button:has-text("Start Lab")',
                'button:has-text("Mulai Lab")',
                '[role="button"]:has-text("Start Lab")',
                '[role="button"]:has-text("Mulai Lab")',
                'a:has-text("Start Lab")',
                'a:has-text("Mulai Lab")'
            ]

            for selector in button_selectors:
                try:
                    button = page.locator(selector).first
                    if await button.is_visible(timeout=1000):
                        await button.click()
                        log_automation_step(
                            self.logger,
                            "start_button_click",
                            "SUCCESS",
                            {"method": "selector", "selector": selector}
                        )
                        return True

                except Exception:
                    continue

        self.logger.warning("Failed to find start lab button after all attempts")
        return False

    async def _handle_captcha_if_present(
        self,
        page: Page,
        handle_captcha: Callable[[], Awaitable[bool]]
    ) -> bool:
        """Check for CAPTCHA and handle if present."""
        try:
            # Wait a moment for CAPTCHA to potentially appear
            await page.wait_for_timeout(2000)

            # Check for CAPTCHA indicators
            captcha_selectors = [
                'div[class*="captcha"]',
                'div[id*="captcha"]',
                'iframe[src*="recaptcha"]',
                'div[class*="recaptcha"]',
                '.g-recaptcha',
                '#g-recaptcha'
            ]

            captcha_present = False
            for selector in captcha_selectors:
                try:
                    element = await page.query_selector(selector)
                    if element and await element.is_visible():
                        captcha_present = True
                        break
                except Exception:
                    continue

            if not captcha_present:
                self.logger.debug("No CAPTCHA detected")
                return True

            log_automation_step(
                self.logger,
                "handle_captcha",
                "START",
                {"captcha_detected": True}
            )

            # Call the provided CAPTCHA handler
            captcha_result = await handle_captcha()

            log_automation_step(
                self.logger,
                "handle_captcha",
                "SUCCESS" if captcha_result else "FAILED",
                {"captcha_solved": captcha_result}
            )

            return captcha_result

        except Exception as e:
            self.logger.error(f"CAPTCHA handling failed: {e}")
            return False

    @performance_monitor("open_cloud_console")
    async def open_cloud_console(
        self,
        page: Page,
        project_id: Optional[str] = None
    ) -> LabResult:
        """
        Open Google Cloud Console for the current project.

        Args:
            page: Playwright page instance
            project_id: Optional specific project ID

        Returns:
            LabResult with console access details
        """
        log_automation_step(
            self.logger,
            "open_cloud_console",
            "START",
            {"project_id": project_id}
        )

        try:
            # Build console URL
            if project_id:
                console_url = f"https://console.cloud.google.com/home/dashboard?project={project_id}"
            else:
                console_url = "https://console.cloud.google.com"

            # Navigate to console
            await page.goto(console_url, wait_until='domcontentloaded', timeout=30000)

            # Wait for console to load
            await page.wait_for_load_state('networkidle', timeout=15000)

            result = LabResult(
                success=True,
                status=LabStatus.COMPLETED,
                lab_url=page.url,
                console_url=console_url,
                metadata={
                    'project_id': project_id,
                    'console_loaded': True
                }
            )

            log_automation_step(
                self.logger,
                "open_cloud_console",
                "SUCCESS",
                {"console_url": console_url}
            )

            return result

        except Exception as e:
            error_msg = f"Failed to open cloud console: {e}"
            self.logger.error(error_msg)

            return LabResult(
                success=False,
                status=LabStatus.FAILED,
                lab_url=page.url,
                error_message=error_msg
            )

    @performance_monitor("handle_gcloud_terms")
    async def handle_gcloud_terms(self, page: Page) -> LabResult:
        """
        Handle Google Cloud terms and conditions acceptance.

        Args:
            page: Playwright page instance

        Returns:
            LabResult with terms handling status
        """
        log_automation_step(
            self.logger,
            "handle_gcloud_terms",
            "START"
        )

        try:
            # Look for terms acceptance elements
            terms_selectors = [
                'input[type="checkbox"][name*="terms"]',
                'input[type="checkbox"][id*="terms"]',
                'input[type="checkbox"][name*="agree"]',
                'input[type="checkbox"][id*="agree"]',
                'button:has-text("Accept")',
                'button:has-text("Agree")',
                'button:has-text("I agree")'
            ]

            terms_handled = False

            for selector in terms_selectors:
                try:
                    elements = await page.query_selector_all(selector)
                    for element in elements:
                        if await element.is_visible():
                            if 'checkbox' in selector:
                                if not await element.is_checked():
                                    await element.click()
                                    terms_handled = True
                            else:
                                await element.click()
                                terms_handled = True

                            self.logger.info(f"Handled terms element: {selector}")

                except Exception as e:
                    self.logger.debug(f"Terms selector failed {selector}: {e}")
                    continue

            result = LabResult(
                success=True,
                status=LabStatus.COMPLETED,
                lab_url=page.url,
                metadata={
                    'terms_found': terms_handled,
                    'terms_accepted': terms_handled
                }
            )

            log_automation_step(
                self.logger,
                "handle_gcloud_terms",
                "SUCCESS",
                {"terms_handled": terms_handled}
            )

            return result

        except Exception as e:
            error_msg = f"Failed to handle GCloud terms: {e}"
            self.logger.error(error_msg)

            return LabResult(
                success=False,
                status=LabStatus.FAILED,
                lab_url=page.url,
                error_message=error_msg
            )

    @performance_monitor("enable_genai_and_create_api_key")
    async def enable_genai_and_create_api_key(
        self,
        page: Page,
        api_name: str = "Generative AI API"
    ) -> LabResult:
        """
        Enable GenAI API and create API key.

        Args:
            page: Playwright page instance
            api_name: Name of the API to enable

        Returns:
            LabResult with API key creation status
        """
        log_automation_step(
            self.logger,
            "enable_genai_api",
            "START",
            {"api_name": api_name}
        )

        try:
            # Navigate to API library
            api_library_url = "https://console.cloud.google.com/apis/library"
            await page.goto(api_library_url, wait_until='domcontentloaded', timeout=30000)

            # Search for GenAI API
            search_selectors = [
                'input[placeholder*="Search"]',
                'input[name*="search"]',
                'input[type="search"]'
            ]

            for selector in search_selectors:
                try:
                    search_box = await page.query_selector(selector)
                    if search_box and await search_box.is_visible():
                        await search_box.fill(api_name)
                        await page.keyboard.press('Enter')
                        break
                except Exception:
                    continue

            # Wait for search results and enable API
            await page.wait_for_timeout(3000)

            # Look for enable button
            enable_selectors = [
                'button:has-text("Enable")',
                'button:has-text("ENABLE")',
                '[role="button"]:has-text("Enable")'
            ]

            api_enabled = False
            for selector in enable_selectors:
                try:
                    enable_button = await page.query_selector(selector)
                    if enable_button and await enable_button.is_visible():
                        await enable_button.click()
                        api_enabled = True
                        break
                except Exception:
                    continue

            # Navigate to credentials page
            credentials_url = "https://console.cloud.google.com/apis/credentials"
            await page.goto(credentials_url, wait_until='domcontentloaded', timeout=30000)

            # Create API key
            create_key_selectors = [
                'button:has-text("Create Credentials")',
                'button:has-text("CREATE CREDENTIALS")',
                'button:has-text("API Key")',
                '[role="button"]:has-text("Create")'
            ]

            api_key_created = False
            api_key = None

            for selector in create_key_selectors:
                try:
                    create_button = await page.query_selector(selector)
                    if create_button and await create_button.is_visible():
                        await create_button.click()

                        # Look for API Key option
                        await page.wait_for_timeout(2000)
                        api_key_option = await page.query_selector('text="API Key"')
                        if api_key_option:
                            await api_key_option.click()

                        # Wait for API key to be generated and extract it
                        await page.wait_for_timeout(3000)

                        # Look for API key in various possible locations
                        api_key_selectors = [
                            'input[readonly]',
                            'code',
                            '[data-testid*="api"]',
                            '.api-key'
                        ]

                        for key_selector in api_key_selectors:
                            try:
                                key_element = await page.query_selector(key_selector)
                                if key_element:
                                    key_text = await key_element.text_content()
                                    if key_text and len(key_text) > 20:  # Basic validation
                                        api_key = key_text.strip()
                                        api_key_created = True
                                        break
                            except Exception:
                                continue

                        break

                except Exception:
                    continue

            result = LabResult(
                success=api_enabled or api_key_created,
                status=LabStatus.COMPLETED if (api_enabled or api_key_created) else LabStatus.FAILED,
                lab_url=page.url,
                api_key=api_key,
                metadata={
                    'api_enabled': api_enabled,
                    'api_key_created': api_key_created,
                    'api_key_length': len(api_key) if api_key else 0
                }
            )

            log_automation_step(
                self.logger,
                "enable_genai_api",
                "SUCCESS" if result.success else "WARNING",
                {
                    "api_enabled": api_enabled,
                    "api_key_created": api_key_created,
                    "has_api_key": api_key is not None
                }
            )

            return result

        except Exception as e:
            error_msg = f"Failed to enable GenAI API: {e}"
            self.logger.error(error_msg)

            return LabResult(
                success=False,
                status=LabStatus.FAILED,
                lab_url=page.url,
                error_message=error_msg
            )

# Backward compatibility functions
async def start_lab(
    page: Page,
    logger,
    handle_captcha: Callable[[], Awaitable[bool]],
    lab_url: str,
    wait_networkidle: bool = True
) -> dict:
    """
    Start lab (backward compatibility).

    Args:
        page: Page instance
        logger: Logger instance (unused, using internal logger)
        handle_captcha: CAPTCHA handler function
        lab_url: Lab URL
        wait_networkidle: Wait for network idle

    Returns:
        Dictionary with operation result
    """
    service = LabAutomationService()
    result = await service.start_lab(page, lab_url, handle_captcha, wait_networkidle)

    return {
        'success': result.success,
        'status': result.status.value,
        'error': result.error_message,
        'metadata': result.metadata
    }

async def open_cloud_console(page: Page, logger, project_id: Optional[str] = None) -> dict:
    """Open cloud console (backward compatibility)."""
    service = LabAutomationService()
    result = await service.open_cloud_console(page, project_id)

    return {
        'success': result.success,
        'console_url': result.console_url,
        'error': result.error_message
    }

async def handle_gcloud_terms(page: Page, logger) -> dict:
    """Handle GCloud terms (backward compatibility)."""
    service = LabAutomationService()
    result = await service.handle_gcloud_terms(page)

    return {
        'success': result.success,
        'terms_handled': result.metadata.get('terms_handled', False) if result.metadata else False,
        'error': result.error_message
    }

async def enable_genai_and_create_api_key(
    page: Page,
    logger,
    api_name: str = "Generative AI API"
) -> dict:
    """Enable GenAI and create API key (backward compatibility)."""
    service = LabAutomationService()
    result = await service.enable_genai_and_create_api_key(page, api_name)

    return {
        'success': result.success,
        'api_key': result.api_key,
        'api_enabled': result.metadata.get('api_enabled', False) if result.metadata else False,
        'error': result.error_message
    }

# Export commonly used items
__all__ = [
    'LabStatus',
    'LabResult',
    'LabAutomationService',
    'start_lab',
    'open_cloud_console',
    'handle_gcloud_terms',
    'enable_genai_and_create_api_key'
]