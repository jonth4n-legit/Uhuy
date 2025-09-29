"""
Aksi konfirmasi email dan login untuk Cloud Skills Boost.
Dipanggil oleh CloudSkillAutomation agar file utama tetap ringkas.
"""
from typing import Optional, Dict
from playwright.async_api import Page, BrowserContext
from utils.logger import log_automation_step

async def confirm_via_link_action(context: BrowserContext, page: Page, logger, 
                                 url: str, password: str, email: Optional[str] = None) -> Dict:
    """
    Buka link konfirmasi pada tab aktif (single-tab policy sudah diterapkan di context).
    Jika setelah konfirmasi muncul form login, isi password (dan email jika perlu), lalu submit.
    """
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
            
    confirmed = False
    try:
        if await _is_confirmation_success(page):
            log_automation_step(logger, 'EMAIL_CONFIRM', 'CONFIRMATION_OK')
            confirmed = True
    except Exception:
        pass
        
    try:
        has_pwd = await page.query_selector('input[type=\'password\']')
    except Exception:
        has_pwd = None
        
    if confirmed and (not has_pwd):
        try:
            await page.goto('https://www.cloudskillsboost.google/users/sign_in')
            await page.wait_for_load_state('domcontentloaded')
            log_automation_step(logger, 'EMAIL_CONFIRM', 'NAVIGATE_TO_SIGN_IN_AFTER_CONFIRM')
        except Exception:
            pass
            
    try:
        await page.wait_for_selector('input[type=\'password\']', timeout=30000)
        log_automation_step(logger, 'EMAIL_CONFIRM', 'LOGIN_FORM_DETECTED')
        
        # Fill email if provided
        try:
            if email:
                email_loc = await page.query_selector('input[type=\'email\'], input[name=\'email\']')
                if email_loc:
                    await email_loc.fill('')
                    await email_loc.fill(email.strip())
                    log_automation_step(logger, 'EMAIL_CONFIRM', 'EMAIL_FILLED_FORCE')
        except Exception:
            pass
            
        # Fill password
        pwd_loc = page.locator('input[type=\'password\']').first
        await pwd_loc.fill('')
        await pwd_loc.type((password or '').strip(), delay=20)
        log_automation_step(logger, 'EMAIL_CONFIRM', 'CREDENTIALS_USED', {'email': email or '(prefilled)'})
        
        # Submit form
        submitted = False
        submit_selectors = [
            'button[type=\'submit\']', 
            'input[type=\'submit\']', 
            'button:has-text(\'Sign in\')', 
            'button:has-text(\'Sign In\')', 
            'button:has-text(\'Log in\')', 
            'button:has-text(\'Log In\')'
        ]
        
        for sel in submit_selectors:
            try:
                btn = page.locator(sel).first
                if await btn.count() > 0:
                    await btn.click()
                    submitted = True
                    break
            except Exception:
                continue
                
        if not submitted:
            try:
                await pwd_loc.press('Enter')
                submitted = True
            except Exception:
                pass
                
        await page.wait_for_load_state('networkidle', timeout=20000)
        log_automation_step(logger, 'EMAIL_CONFIRM', 'SUBMITTED')
        
        # Check for errors
        try:
            candidates = ['div[role=\'alert\']', '.alert', '.errors', '.error']
            error_keywords = [
                'invalid', 'incorrect', 'does not match', 'doesn\'t match', 
                'mismatch', 'not found'
            ]
            
            for sel in candidates:
                try:
                    el = await page.query_selector(sel)
                except Exception:
                    el = None
                    
                if not el:
                    continue
                    
                try:
                    txt = (await el.text_content() or '').strip().lower()
                except Exception:
                    txt = ''
                    
                if 'successfully confirmed' in txt or 'account has been confirmed' in txt:
                    continue
                    
                if any(k in txt for k in error_keywords):
                    log_automation_step(logger, 'EMAIL_CONFIRM', 'LOGIN_FAILED', {'selector': sel, 'text': txt[:200]})
                    return {'success': False, 'error': 'Invalid email or password'}
        except Exception:
            pass
            
    except Exception:
        log_automation_step(logger, 'EMAIL_CONFIRM', 'NO_LOGIN_FORM')
        
    current_url = page.url
    log_automation_step(logger, 'EMAIL_CONFIRM', 'SUCCESS', {'url': current_url})
    return {'success': True, 'url': current_url}

async def _is_confirmation_success(page: Page) -> bool:
    """Check for confirmation success indicators"""
    patterns = [
        'successfully confirmed', 
        'your account was successfully confirmed', 
        'your account has been confirmed', 
        'email address has been successfully confirmed'
    ]
    
    containers = [
        'div[role=\'alert\']', 
        '.alert.alert-success', 
        '.notice', 
        '.flash--success', 
        '#notice', 
        '[class*=\'success\']'
    ]
    
    for sel in containers:
        try:
            el = await page.query_selector(sel)
        except Exception:
            el = None
            
        if not el:
            continue
            
        try:
            txt = (await el.text_content() or '').strip().lower()
        except Exception:
            txt = ''
            
        for pat in patterns:
            if pat in txt:
                return True
                
    # Check body text
    try:
        body_txt = (await page.text_content('body') or '').lower()
        return any(pat in body_txt for pat in patterns)
    except Exception:
        return False