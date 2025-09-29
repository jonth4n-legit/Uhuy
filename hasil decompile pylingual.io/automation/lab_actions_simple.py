# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: automation\lab_actions_simple.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
Flow minimal untuk Start Lab:
- Navigate ke lab_url
- Klik "Start Lab" jika terlihat
- Cek reCAPTCHA; jika ada, serahkan ke handler dari caller

Tambahan utilitas: open_cloud_console, handle_gcloud_terms, enable_genai_and_create_api_key
(Implementasi disederhanakan agar stabil setelah decompile.)
"""
from typing import Awaitable, Callable, Optional, Tuple, Dict
import re
import asyncio
from urllib.parse import urlparse
from playwright.async_api import Page, Browser, BrowserContext
from utils.logger import log_automation_step


async def start_lab(page: Page, logger, handle_captcha: Callable[[], Awaitable[bool]], lab_url: str, wait_networkidle: bool = True) -> Dict:
    log_automation_step(logger, 'LAB_START', 'START', {'url': lab_url})
    await page.goto(lab_url)
    try:
        await page.wait_for_load_state('domcontentloaded')
        if wait_networkidle:
            try:
                await page.wait_for_load_state('networkidle')
            except Exception:
                pass
        # Try several button variants
        for text in ['Start Lab', 'Mulai Lab', 'Begin Lab', 'Start', 'Mulai']:
            try:
                loc = page.get_by_role('button', name=text)
                if await loc.is_visible(timeout=800):
                    await loc.click()
                    break
            except Exception:
                pass
        await page.wait_for_timeout(1500)
        # reCAPTCHA detection
        rec_iframe = await page.query_selector("iframe[title*='reCAPTCHA'], iframe[src*='recaptcha']")
        if rec_iframe:
            ok = await handle_captcha()
            if not ok:
                log_automation_step(logger, 'LAB_START', 'CAPTCHA_FAILED')
                return {'success': False, 'error': 'Captcha not solved'}
        log_automation_step(logger, 'LAB_START', 'SUCCESS', {'url': page.url})
        return {'success': True, 'url': page.url}
    except Exception as e:
        log_automation_step(logger, 'LAB_START', 'ERROR', {'error': str(e)})
        return {'success': False, 'error': str(e)}


async def open_cloud_console(page: Page, logger, browser: Browser, timeout_sec: int = 400) -> Tuple[dict, Optional[BrowserContext], Optional[Page]]:
    """Cari dan klik tombol/tautan "Open Google Cloud console" secara sederhana."""
    texts = ['Open Google Cloud console', 'Open Google Cloud Console', 'Open Cloud Console', 'Buka Google Cloud console', 'Open Console']
    deadline = asyncio.get_event_loop().time() + max(5, timeout_sec)
    while asyncio.get_event_loop().time() < deadline:
        for t in texts:
            try:
                loc = page.get_by_role('button', name=t)
                if await loc.is_visible(timeout=800):
                    href = await loc.get_attribute('href')
                    if href and href.strip():
                        inc_ctx = await browser.new_context(viewport=None)
                        inc_page = await inc_ctx.new_page()
                        await inc_page.goto(href)
                        log_automation_step(logger, 'OPEN_CONSOLE', 'INCOGNITO_OPENED', {'url': inc_page.url})
                        return ({'opened': True, 'url': inc_page.url, 'incognito': True}, inc_ctx, inc_page)
                    await loc.click()
                    await page.wait_for_load_state('domcontentloaded')
                    inc_ctx = await browser.new_context(viewport=None)
                    inc_page = await inc_ctx.new_page()
                    await inc_page.goto(page.url)
                    log_automation_step(logger, 'OPEN_CONSOLE', 'INCOGNITO_OPENED', {'url': inc_page.url})
                    return ({'opened': True, 'url': inc_page.url, 'incognito': True}, inc_ctx, inc_page)
            except Exception:
                pass
        try:
            await page.wait_for_timeout(1000)
        except Exception:
            pass
    return ({'opened': False, 'url': ''}, None, None)


async def handle_gcloud_terms(inc_page: Optional[Page], logger, timeout_sec: int = 120) -> dict:
    if not inc_page:
        return {'handled': False, 'reason': 'no_incognito_page'}
    deadline = asyncio.get_event_loop().time() + timeout_sec
    while asyncio.get_event_loop().time() < deadline:
        try:
            if inc_page.is_closed():
                return {'handled': False, 'reason': 'page_closed'}
            # Look for a common checkbox/button
            cb = inc_page.get_by_role('checkbox')
            if await cb.count() > 0:
                try:
                    await cb.first.check()
                except Exception:
                    pass
            btn = inc_page.get_by_role('button', name='Agree and continue')
            if await btn.count() > 0:
                try:
                    await btn.first.click()
                    return {'handled': True, 'url': inc_page.url}
                except Exception:
                    pass
        except Exception:
            pass
        await asyncio.sleep(1)
    return {'handled': False, 'reason': 'timeout'}


async def enable_genai_and_create_api_key(inc_page: Page, logger, project_id: str, timeout_sec: int = 180) -> dict:
    """Placeholder minimal untuk enable API & create API key.
    Implementasi penuh membutuhkan selector kompleks; di sini hanya skeleton.
    """
    try:
        return {'success': False, 'api_key': ''}
    except Exception as e:
        return {'success': False, 'api_key': '', 'error': str(e)}