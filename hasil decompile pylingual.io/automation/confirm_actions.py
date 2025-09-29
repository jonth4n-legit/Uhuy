# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: automation\confirm_actions.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
Aksi konfirmasi email dan login untuk Cloud Skills Boost.
Dipanggil oleh CloudSkillAutomation agar file utama tetap ringkas.
"""
from typing import Optional, Dict
from playwright.async_api import Page, BrowserContext
from utils.logger import log_automation_step


async def confirm_via_link_action(context: BrowserContext, page: Page, logger, url: str, password: str, email: Optional[str] = None) -> Dict:
    log_automation_step(logger, 'EMAIL_CONFIRM', 'NAVIGATE', {'url': url})
    try:
        await page.goto(url)
        await page.wait_for_load_state('domcontentloaded')
    except Exception as e:
        log_automation_step(logger, 'EMAIL_CONFIRM', 'NAVIGATE_RETRY', {'error': str(e)})
        try:
            if page.is_closed():
                page = await context.new_page()
            await page.goto(url)
            await page.wait_for_load_state('domcontentloaded')
        except Exception as e2:
            log_automation_step(logger, 'EMAIL_CONFIRM', 'NAVIGATE_RETRY_FAILED', {'error': str(e2)})
            return {'success': False, 'error': str(e2)}

    # If login appears, fill credentials
    try:
        await page.wait_for_selector("input[type='password']", timeout=30000)
        log_automation_step(logger, 'EMAIL_CONFIRM', 'LOGIN_FORM_DETECTED')
        if email:
            email_loc = await page.query_selector("input[type='email'], input[name='email']")
            if email_loc:
                await email_loc.fill('')
                await email_loc.fill(email.strip())
                log_automation_step(logger, 'EMAIL_CONFIRM', 'EMAIL_FILLED_FORCE')
        pwd_loc = page.locator("input[type='password']").first
        await pwd_loc.fill('')
        await pwd_loc.type((password or '').strip(), delay=20)
        submitted = False
        for sel in [
            "button[type='submit']",
            "input[type='submit']",
            "button:has-text('Sign in')",
            "button:has-text('Log in')",
        ]:
            btn = page.locator(sel).first
            if await btn.count() > 0:
                await btn.click()
                submitted = True
                break
        if not submitted:
            await pwd_loc.press('Enter')
        await page.wait_for_load_state('networkidle', timeout=20000)
        log_automation_step(logger, 'EMAIL_CONFIRM', 'SUBMITTED')
    except Exception:
        log_automation_step(logger, 'EMAIL_CONFIRM', 'NO_LOGIN_FORM')

    current_url = page.url
    log_automation_step(logger, 'EMAIL_CONFIRM', 'SUCCESS', {'url': current_url})
    return {'success': True, 'url': current_url}