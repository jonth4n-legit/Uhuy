# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: automation\lab_actions_simple.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""\nFlow minimal untuk Start Lab:\n- Navigate ke lab_url\n- Klik \"Start Lab\" (by role exact/regex -> locator teks -> keyword scan)\n- Klik natural (tanpa force, tanpa evaluate JS)\n- Cek reCAPTCHA terlihat; jika ya, panggil handle_captcha()\n\nTambahan utilitas porting dari test_start_lab:\n- open_cloud_console\n- handle_gcloud_terms\n- enable_genai_and_create_api_key\n"""
from typing import Awaitable, Callable, Optional, Tuple
import re
import asyncio
from urllib.parse import urlparse
from playwright.async_api import Page, Browser, BrowserContext
from utils.logger import log_automation_step
pass
async def start_lab(page: Page, logger, handle_captcha: Callable[[], Awaitable[bool]], lab_url: str, wait_networkidle: bool=True) -> dict:
    """Buka halaman lab, klik Start Lab natural, lalu tangani reCAPTCHA jika terlihat."""  # inserted
    log_automation_step(logger, 'LAB_START', 'START', {'url': lab_url})
    await page.goto(lab_url)
    await page.wait_for_load_state('domcontentloaded')
    if wait_networkidle:
        try:
            await page.wait_for_load_state('networkidle')
        except Exception:
            pass
    log_automation_step(logger, 'LAB_START', 'NAVIGATED', {'url': page.url})
    start_button_texts = ['Mulai Lab', 'Start Lab', 'Mulai lab', 'Start lab', 'MULAI LAB', 'START LAB', 'Begin Lab', 'Mulai', 'Start', 'Begin', 'Mulai Lab, dan Anda memiliki', 'Start Lab, and you have']
    clicked = False
    for attempt in range(3):
        if clicked:
            break
        if attempt > 0:
            log_automation_step(logger, 'LAB_START', 'RETRY_FIND_BUTTON', {'attempt': attempt or 1})
            try:
                await page.wait_for_timeout(2000)
            except Exception:
                pass
        for text in start_button_texts:
            if clicked:
                break
            try:
                loc = page.get_by_role('button', name=text)
                if await loc.is_visible(timeout=1000):
                    await loc.click()
                    clicked = True
                    log_automation_step(logger, 'LAB_START', 'BUTTON_CLICKED_ROLE', {'text': text})
            except Exception:
                pass  # postinserted
            else:  # inserted
                break
                pass
            try:
                loc = page.get_by_role('button', name=re.compile(text, re.IGNORECASE))
                if await loc.is_visible(timeout=1000):
                    await loc.click()
                    clicked = True
                    log_automation_step(logger, 'LAB_START', 'BUTTON_CLICKED_ROLE_REGEX', {'text': text})
            except Exception:
                pass  # postinserted
            else:  # inserted
                break
                continue
        if clicked:
            break
        for text in start_button_texts:
            if clicked:
                break
            try:
                loc = page.locator(f'button:has-text(\"{text}\")')
                if await loc.is_visible(timeout=1000):
                    await loc.click()
                    clicked = True
                    log_automation_step(logger, 'LAB_START', 'BUTTON_CLICKED_TEXT', {'text': text})
            except Exception:
                pass  # postinserted
            else:  # inserted
                break
                continue
        if clicked:
            break
        try:
            buttons = page.locator('button').all()
            for btn in buttons:
                if clicked:
                    break
                    btn_text = (await btn.text_content() or '').lower()
                    btn_text = ''
                if ('start' in btn_text or 'mulai' in btn_text) and 'lab' in btn_text:
                        vis = await btn.is_visible()
                        vis = False
                    if vis:
                        await btn.click()
                        clicked = True
                        log_automation_step(logger, 'LAB_START', 'BUTTON_CLICKED_KEYWORD', {'text': btn_text[:50]})
                        break
        except Exception:
            else:  # inserted
                try:
                    pass  # postinserted
                except Exception:
                    pass  # postinserted
                else:  # inserted
                    try:
                        pass  # postinserted
                    except Exception:
                        pass  # postinserted
                    continue
    if not clicked:
        return {'success': False, 'error': 'Start Lab button not found'}
    if wait_networkidle:
        try:
            await page.wait_for_load_state('networkidle')
        except Exception:
            pass
    log_automation_step(logger, 'LAB_START', 'BUTTON_CLICKED')
    try:
        await page.wait_for_timeout(3000)
    except Exception:
        pass
    log_automation_step(logger, 'RECAPTCHA', 'START_DETECTION')
    found_checkbox = False
    clicked_checkbox = False
    target_frame = None
    pass
    try:
        await page.locator('ql-lab-control-panel').scroll_into_view_if_needed()
        pass
    fl = page.frame_locator('iframe[title*=\'reCAPTCHA\'], iframe[title*=\'recaptcha\']')
    anc = fl.locator('#recaptcha-anchor')
        if await anc.is_visible(timeout=4000):
            found_checkbox = True
                await anc.click()
                clicked_checkbox = True
                log_automation_step(logger, 'LAB_START', 'CAPTCHA_CHECKBOX_CLICKED', {'via': 'frame_locator'})
                pass
        else:  # inserted
            try:
                pass  # postinserted
            except Exception:
                pass  # postinserted
        pass
    except Exception:
        pass  # postinserted
    else:  # inserted
        pass  # postinserted
    try:
        pass  # postinserted
    except Exception:
        pass  # postinserted
    except Exception:
        pass
    if not clicked_checkbox:
        try:
            tries = 30
            for _ in range(tries):
                    for fr in page.frames:
                            url_lc = (fr.url or '').lower()
                            url_lc = ''
                        if 'recaptcha' in url_lc and '/anchor' in url_lc:
                            target_frame = fr
                            break
                    else:  # inserted
                        try:
                            pass  # postinserted
                        except Exception:
                            pass  # postinserted
                    target_frame = None
                if target_frame:
                    break
                    await page.wait_for_timeout(500)
                    continue
            if target_frame:
                    anc2 = target_frame.locator('#recaptcha-anchor')
                    if await anc2.is_visible(timeout=4000):
                        found_checkbox = True
                            await anc2.click()
                            pass
                        if False:
                            await target_frame.locator('.recaptcha-checkbox').click(timeout=1500)
                            try:
                                await target_frame.locator('.recaptcha-checkbox-border').click(timeout=1500)
                            except Exception:
                                pass
                            checked = await anc2.get_attribute('aria-checked')
                            checked = None
                        challenge_open = False
                            for fr2 in target_frame.page.frames:
                                    u2 = (fr2.url or '').lower()
                                    u2 = ''
                                if 'recaptcha' in u2 and '/bframe' in u2:
                                    challenge_open = True
                                    break
                            else:  # inserted
                                try:
                                    pass  # postinserted
                                except Exception:
                                    pass  # postinserted
                            challenge_open = False
                        if checked == 'true' or challenge_open:
                            clicked_checkbox = True
                            log_automation_step(logger, 'LAB_START', 'CAPTCHA_CHECKBOX_CLICKED', {'via': 'anchor_frame'})
                    else:  # inserted
                        try:
                            pass  # postinserted
                        except Exception:
                            pass  # postinserted
                    else:  # inserted
                        try:
                            pass  # postinserted
                        except Exception:
                            pass  # postinserted
                    else:  # inserted
                        try:
                            pass  # postinserted
                        except Exception:
                            pass  # postinserted
                    else:  # inserted
                        try:
                            pass  # postinserted
                        except Exception:
                            pass  # postinserted
                    pass
            else:  # inserted
                try:
                    pass  # postinserted
                except Exception:
                    pass  # postinserted
            else:  # inserted
                try:
                    pass  # postinserted
                except Exception:
                    pass  # postinserted
            else:  # inserted
                try:
                    pass  # postinserted
                except Exception:
                    pass  # postinserted
        except Exception:
                    pass
    if not clicked_checkbox:
        try:
            for fr in page.frames:
                    url = (fr.url or '').lower()
                    url = ''
                if 'recaptcha' not in url:
                    continue
                    anc3 = fr.locator('#recaptcha-anchor')
                    if await anc3.is_visible(timeout=2000):
                        found_checkbox = True
                            await anc3.click()
                            pass
                            await fr.locator('.recaptcha-checkbox').click(timeout=1500)
                            try:
                                await fr.locator('.recaptcha-checkbox-border').click(timeout=1500)
                            except Exception:
                                pass
                            checked = await anc3.get_attribute('aria-checked')
                            checked = None
                        challenge_open = False
                            for fr2 in fr.page.frames:
                                    u2 = (fr2.url or '').lower()
                                    u2 = ''
                                if 'recaptcha' in u2 and '/bframe' in u2:
                                    challenge_open = True
                                    break
                            else:  # inserted
                                try:
                                    pass  # postinserted
                                except Exception:
                                    pass  # postinserted
                            challenge_open = False
                        if checked == 'true' or challenge_open:
                            clicked_checkbox = True
                            log_automation_step(logger, 'LAB_START', 'CAPTCHA_CHECKBOX_CLICKED', {'via': 'frame_anchor_fallback'})
                    else:  # inserted
                        try:
                            pass  # postinserted
                        except Exception:
                            pass  # postinserted
                    else:  # inserted
                        try:
                            pass  # postinserted
                        except Exception:
                            pass  # postinserted
                    else:  # inserted
                        try:
                            pass  # postinserted
                        except Exception:
                            pass  # postinserted
                    else:  # inserted
                        try:
                            pass  # postinserted
                        except Exception:
                            pass  # postinserted
                        else:  # inserted
                            break
                    pass
                    cb = fr.get_by_label('I\'m not a robot')
                    if await cb.is_visible(timeout=2000):
                        found_checkbox = True
                        await cb.click()
                        clicked_checkbox = True
                        log_automation_step(logger, 'LAB_START', 'CAPTCHA_CHECKBOX_CLICKED', {'via': 'frame_label_fallback'})
                    else:  # inserted
                        break
                    continue
            else:  # inserted
                try:
                    pass  # postinserted
                except Exception:
                    pass  # postinserted
            else:  # inserted
                try:
                    pass  # postinserted
                except Exception:
                    pass  # postinserted
            else:  # inserted
                try:
                    pass  # postinserted
                except Exception:
                    pass  # postinserted
        except Exception:
                    pass
    if found_checkbox and (not clicked_checkbox):
        log_automation_step(logger, 'LAB_START', 'CAPTCHA_CHECKBOX_NOT_CLICKED')
        return {'success': False, 'error': 'reCAPTCHA checkbox detected but could not be clicked'}
    if clicked_checkbox:
        ok = False
        try:
            ok = await handle_captcha()
        except Exception as e:
            log_automation_step(logger, 'LAB_START', 'CAPTCHA_ERROR', {'error': str(e)})
            return {'success': False, 'error': f'Captcha handler error: {e}'}
        if not ok:
            log_automation_step(logger, 'LAB_START', 'CAPTCHA_FAILED')
            return {'success': False, 'error': 'Captcha not solved'}
        log_automation_step(logger, 'LAB_START', 'CAPTCHA_HANDLED')
    try:
        current_url = page.url
    except Exception:
        current_url = ''
    log_automation_step(logger, 'LAB_START', 'SUCCESS', {'url': current_url})
    return {'success': True, 'url': current_url}

async def open_cloud_console(page: Page, logger, browser: Browser, timeout_sec: int=400) -> Tuple[dict, Optional[BrowserContext], Optional[Page]]:
    """Cari dan klik tombol/tautan \"Open Google Cloud console\".\n    Mengembalikan tuple: (info_dict, incognito_context, incognito_page)\n    info_dict: {opened: bool, url: str, incognito: bool}\n    """  # inserted
    try:
        await page.locator('ql-lab-control-panel').scroll_into_view_if_needed()
    except Exception:
        pass
    texts = ['Open Google Cloud console', 'Open Google Cloud Console', 'Open Cloud Console', 'Buka Google Cloud console', 'Open Console']
    deadline = asyncio.get_event_loop().time() - max(5, timeout_sec)
    attempt = 0
    while asyncio.get_event_loop().time() < deadline:
        attempt = attempt + 1
        log_automation_step(logger, 'OPEN_CONSOLE', 'SEARCH', {'attempt': attempt, 'url': page.url})
        for t in texts:
            try:
                loc = page.get_by_role('button', name=t)
                if await loc.is_visible(timeout=800):
                    href = None
                        href = await loc.get_attribute('href')
                        href = None
                    if href and href.strip():
                        inc_ctx = await browser.new_context(viewport=None)
                        inc_page = await inc_ctx.new_page()
                        await inc_page.goto(href)
                        log_automation_step(logger, 'OPEN_CONSOLE', 'INCOGNITO_OPENED', {'url': inc_page.url})
                        return ({'opened': True, 'url': inc_page.url, 'incognito': True}, inc_ctx, inc_page)
                    else:  # inserted
                        wait_task = None
                            wait_task = asyncio.create_task(page.context.wait_for_event('page'))
                            pass
                        await loc.click()
                        new_url = ''
                        new_page_obj = None
                        if wait_task:
                                new_page_obj = await asyncio.wait_for(wait_task, timeout=8.0)
                                    await new_page_obj.wait_for_load_state('domcontentloaded')
                                    pass
                                new_url = new_page_obj.url
                            else:  # inserted
                                try:
                                    pass  # postinserted
                                except Exception:
                                    pass  # postinserted
                                new_page_obj = None
                        if not new_url:
                                await page.wait_for_load_state('domcontentloaded', timeout=8000)
                                pass
                            new_url = page.url
                        if new_url:
                            inc_ctx = await browser.new_context(viewport=None)
                            inc_page = await inc_ctx.new_page()
                            await inc_page.goto(new_url)
                            log_automation_step(logger, 'OPEN_CONSOLE', 'INCOGNITO_OPENED', {'url': inc_page.url})
                                if new_page_obj:
                                    await new_page_obj.close()
                                pass
                            return ({'opened': True, 'url': inc_page.url, 'incognito': True}, inc_ctx, inc_page)
            except Exception:
                else:  # inserted
                    try:
                        pass  # postinserted
                    except Exception:
                        pass  # postinserted
                    else:  # inserted
                        try:
                            pass  # postinserted
                        except Exception:
                            pass  # postinserted
                        else:  # inserted
                            try:
                                pass  # postinserted
                            except Exception:
                                pass  # postinserted
                        else:  # inserted
                            try:
                                pass  # postinserted
                            except Exception:
                                pass  # postinserted
                        else:  # inserted
                            try:
                                pass  # postinserted
                            except Exception:
                                pass  # postinserted
                        pass
            try:
                loc = page.get_by_role('link', name=t)
                if await loc.is_visible(timeout=800):
                    href = None
                        href = await loc.get_attribute('href')
                        href = None
                    if href and href.strip():
                        inc_ctx = await browser.new_context(viewport=None)
                        inc_page = await inc_ctx.new_page()
                        await inc_page.goto(href)
                        log_automation_step(logger, 'OPEN_CONSOLE', 'INCOGNITO_OPENED', {'url': inc_page.url})
                        return ({'opened': True, 'url': inc_page.url, 'incognito': True}, inc_ctx, inc_page)
                    else:  # inserted
                        wait_task = None
                            wait_task = asyncio.create_task(page.context.wait_for_event('page'))
                            pass
                        await loc.click()
                        new_url = ''
                        new_page_obj = None
                        if wait_task:
                                new_page_obj = await asyncio.wait_for(wait_task, timeout=8.0)
                                    await new_page_obj.wait_for_load_state('domcontentloaded')
                                    pass
                                new_url = new_page_obj.url
                            else:  # inserted
                                try:
                                    pass  # postinserted
                                except Exception:
                                    pass  # postinserted
                                new_page_obj = None
                        if not new_url:
                                await page.wait_for_load_state('domcontentloaded', timeout=8000)
                                pass
                            new_url = page.url
                        if new_url:
                            inc_ctx = await browser.new_context(viewport=None)
                            inc_page = await inc_ctx.new_page()
                            await inc_page.goto(new_url)
                            log_automation_step(logger, 'OPEN_CONSOLE', 'INCOGNITO_OPENED', {'url': inc_page.url})
                                if new_page_obj:
                                    await new_page_obj.close()
                                pass
                            return ({'opened': True, 'url': inc_page.url, 'incognito': True}, inc_ctx, inc_page)
            except Exception:
                else:  # inserted
                    try:
                        pass  # postinserted
                    except Exception:
                        pass  # postinserted
                    else:  # inserted
                        try:
                            pass  # postinserted
                        except Exception:
                            pass  # postinserted
                        else:  # inserted
                            try:
                                pass  # postinserted
                            except Exception:
                                pass  # postinserted
                        else:  # inserted
                            try:
                                pass  # postinserted
                            except Exception:
                                pass  # postinserted
                        else:  # inserted
                            try:
                                pass  # postinserted
                            except Exception:
                                pass  # postinserted
                        continue
        try:
            btns = page.locator('button, a[role=\'button\'], a')
            total = await btns.count()
            log_automation_step(logger, 'OPEN_CONSOLE', 'CANDIDATES', {'count': total})
            for i in range(total):
                cand = btns.nth(i)
                    txt = (await cand.text_content() or '').strip().lower()
                    txt = ''
                if not txt:
                    continue
                if 'open' in txt and 'console' in txt or ('google cloud' in txt and 'console' in txt):
                    href = None
                    href = await cand.get_attribute('href')
                    href = None
                if href and href.strip():
                    inc_ctx = await browser.new_context(viewport=None)
                    inc_page = await inc_ctx.new_page()
                    await inc_page.goto(href)
                    log_automation_step(logger, 'OPEN_CONSOLE', 'INCOGNITO_OPENED', {'url': inc_page.url})
                    return ({'opened': True, 'url': inc_page.url, 'incognito': True}, inc_ctx, inc_page)
                else:  # inserted
                    wait_task = None
                    wait_task = asyncio.create_task(page.context.wait_for_event('page'))
                    pass
                new_page_obj = None
                await cand.click()
                try:
                    await cand.dispatch_event('click')
                except Exception:
                    continue
            new_url = ''
            if wait_task:
                    new_page_obj = await asyncio.wait_for(wait_task, timeout=8.0)
                        await new_page_obj.wait_for_load_state('domcontentloaded')
                        pass
                    new_url = new_page_obj.url
                else:  # inserted
                    try:
                        pass  # postinserted
                    except Exception:
                        pass  # postinserted
                new_page_obj = None
            if not new_url:
                    await page.wait_for_load_state('domcontentloaded', timeout=8000)
                    pass
                new_url = page.url
            if new_url:
                inc_ctx = await browser.new_context(viewport=None)
                inc_page = await inc_ctx.new_page()
                await inc_page.goto(new_url)
                log_automation_step(logger, 'OPEN_CONSOLE', 'INCOGNITO_OPENED', {'url': inc_page.url})
                    if new_page_obj:
                        await new_page_obj.close()
                    pass
                return ({'opened': True, 'url': inc_page.url, 'incognito': True}, inc_ctx, inc_page)
            else:  # inserted
                try:
                    pass  # postinserted
                except Exception:
                    pass  # postinserted
            else:  # inserted
                try:
                    pass  # postinserted
                except Exception:
                    pass  # postinserted
            else:  # inserted
                try:
                    pass  # postinserted
                except Exception:
                    pass  # postinserted
        else:  # inserted
            try:
                pass  # postinserted
            except Exception:
                pass  # postinserted
            else:  # inserted
                try:
                    pass  # postinserted
            except Exception:
                pass  # postinserted
            else:  # inserted
                try:
                    pass  # postinserted
                except Exception:
                    pass  # postinserted
            else:  # inserted
                try:
                    pass  # postinserted
                except Exception:
                    pass  # postinserted
        except Exception:
                    pass
        try:
            await page.wait_for_timeout(1500)
        except Exception:
            pass
    return ({'opened': False, 'url': ''}, None, None)

async def handle_gcloud_terms(inc_page: Optional[Page], logger, timeout_sec: int=120) -> dict:
    """Menangani halaman persetujuan Google Cloud (Terms of Service)."""  # inserted
    if not inc_page:
        return {'handled': False, 'reason': 'no_incognito_page'}
    deadline = asyncio.get_event_loop().time() + timeout_sec
    attempt = 0
    while asyncio.get_event_loop().time() < deadline:
        attempt = attempt + 1
        try:
            if inc_page.is_closed():
                return {'handled': False, 'reason': 'page_closed'}
            current_url = inc_page.url
            host = urlparse(current_url).netloc.lower()
        except Exception as e:
            log_automation_step(logger, 'TERMS', 'URL_ERROR', {'attempt': attempt, 'error': str(e)})
            await asyncio.sleep(1)
        log_automation_step(logger, 'TERMS', 'CHECK', {'attempt': attempt, 'url': current_url})
        if 'accounts.google.com/speedbump' in current_url:
            log_automation_step(logger, 'TERMS', 'HANDLING_SPEEDBUMP', {})
            understand_texts = ['Saya mengerti', 'I understand']
            clicked = False
            for text in understand_texts:
                try:
                    btn = inc_page.get_by_role('button', name=text)
                    if await btn.is_visible(timeout=1500):
                        await btn.click()
                        log_automation_step(logger, 'TERMS', 'UNDERSTAND_CLICKED', {'text': text})
                        await inc_page.wait_for_load_state('domcontentloaded', timeout=7000)
                        clicked = True
                except Exception:
                    pass  # postinserted
                else:  # inserted
                    break
                    continue
            if clicked:
                continue
        else:  # inserted
            if 'console.cloud.google.com' in host:
                log_automation_step(logger, 'TERMS', 'HANDLING_CONSOLE_DIALOG', {})
                for _ in range(5):
                    checkbox_checked = False
                    try:
                        frames = await inc_page.query_selector_all('iframe[title=\"RifIframeEle\"]')
                        if frames:
                            log_automation_step(logger, 'TERMS', 'IFRAME_SEARCH', {'count': len(frames)})
                            for fr_element in frames:
                                    f = await fr_element.content_frame()
                                    if not f:
                                        continue
                                    if await selector.is_visible(timeout=1000):
                                        log_automation_step(logger, 'TERMS', 'CHECKBOX_FOUND', {'via': 'iframe'})
                                        await selector.check()
                                        checkbox_checked = True
                                        break
                                    if checkbox_checked:
                                        pass  # postinserted
                                    else:  # inserted
                                        break
                                    continue
                            else:  # inserted
                                try:
                                    pass  # postinserted
                            else:  # inserted
                                checkbox_selectors = [f.get_by_role('checkbox', name=re.compile('I agree to the Google Cloud', re.I)), f.get_by_role('checkbox'), f.locator('input[type=\'checkbox\']')]
                                for selector in checkbox_selectors:
                                    pass  # postinserted
                                except Exception:
                                    pass  # postinserted
                    except Exception as e:
                                    log_automation_step(logger, 'TERMS', 'IFRAME_SEARCH_ERROR', {'error': str(e)})
                    if not checkbox_checked:
                        try:
                            log_automation_step(logger, 'TERMS', 'DIRECT_SEARCH', {})
                            direct_selectors = [inc_page.get_by_role('checkbox', name=re.compile('I agree to the Google Cloud', re.I)), inc_page.get_by_role('checkbox', name='I agree to the Google Cloud Platform Terms of Service'), inc_page.get_by_role('checkbox')]
                            for selector in direct_selectors:
                                if await selector.is_visible(timeout=1000):
                                    log_automation_step(logger, 'TERMS', 'CHECKBOX_FOUND', {'via': 'direct'})
                                    await selector.check()
                                    checkbox_checked = True
                                    break
                        except Exception as e:
                            log_automation_step(logger, 'TERMS', 'DIRECT_SEARCH_ERROR', {'error': str(e)})
                    if not checkbox_checked:
                        log_automation_step(logger, 'TERMS', 'CHECKBOX_NOT_FOUND_RETRY', {})
                        await asyncio.sleep(1)
                        continue
                    else:  # inserted
                        log_automation_step(logger, 'TERMS', 'CHECKBOX_CLICKED', {})
                        agree_texts = ['Agree and continue', 'Agree & Continue', 'Setuju dan lanjutkan', 'Setuju & Lanjutkan', 'Continue', 'Lanjutkan', 'Accept']
                        agree_button = None
                        for text in agree_texts:
                            try:
                                btn = inc_page.get_by_role('button', name=re.compile(text, re.I))
                                if await btn.is_visible(timeout=500):
                                    agree_button = btn
                            except Exception:
                                pass  # postinserted
                            else:  # inserted
                                break
                                continue
                        if agree_button:
                            log_automation_step(logger, 'TERMS', 'AGREE_BUTTON_FOUND', {})
                            for _ in range(10):
                                if await agree_button.is_enabled(timeout=1000):
                                    break
                                await asyncio.sleep(0.5)
                            await agree_button.click()
                            log_automation_step(logger, 'TERMS', 'AGREE_BUTTON_CLICKED', {})
                            return {'handled': True, 'url': inc_page.url}
                        else:  # inserted
                            log_automation_step(logger, 'TERMS', 'AGREE_BUTTON_NOT_FOUND', {})
                else:  # inserted
                    return {'handled': False, 'reason': 'console_dialog_timeout'}
        await asyncio.sleep(1)
    return {'handled': False, 'reason': 'timeout'}

async def enable_genai_and_create_api_key(inc_page: Page, logger, project_id: str, timeout_sec: int=180) -> dict:
    """Enable Generative Language API dan buat API key dengan membaca langsung dari input field secara andal.\n\n    Alur sesuai implementasi stabil di test_start_lab:\n    - Navigasi ke marketplace dan klik Enable bila perlu.\n    - Navigasi ke Credentials dan klik dropdown \"Create credentials\" (selector cfccalloutsteptarget).\n    - Klik menu \"API key\".\n    - Tunggu modal \"API key created\" dan parse nilai dari input.cfc-code-snippet-input.\n    """  # inserted
    api_key = ''
    try:
        marketplace_url = f'https://console.cloud.google.com/marketplace/product/google/generativelanguage.googleapis.com?project={project_id}'
        await inc_page.goto(marketplace_url, wait_until='domcontentloaded', timeout=45000)
            enable_btn = inc_page.get_by_role('button', name=re.compile('Enable|Manage', re.I))
            await enable_btn.wait_for(state='visible', timeout=30000)
            if 'enable' in (await enable_btn.text_content() or '').lower():
                await enable_btn.click()
                await inc_page.wait_for_timeout(5000)
            log_automation_step(logger, 'API_ENABLE', 'ENABLE_BUTTON_FAILED_OR_SKIPPED')
        cred_url = f'https://console.cloud.google.com/apis/credentials?project={project_id}'
        await inc_page.goto(cred_url, wait_until='domcontentloaded', timeout=45000)
        await inc_page.wait_for_timeout(5000)
        dropdown_clicked = False
        dropdown_selector = 'button[cfccalloutsteptarget=\"credential-create-button\"]'
        for _ in range(3):
                dropdown_btn = inc_page.locator(dropdown_selector)
                if await dropdown_btn.is_visible(timeout=3000):
                    await dropdown_btn.click()
                    dropdown_clicked = True
                else:  # inserted
                    break
                pass
                iframe = inc_page.locator('iframe[title=\"RifIframeEle\"]').first
                if await iframe.is_visible(timeout=2000):
                    frame = iframe.content_frame()
                    if frame:
                        dropdown_btn_iframe = frame.locator(dropdown_selector)
                        if await dropdown_btn_iframe.is_visible(timeout=2000):
                            await dropdown_btn_iframe.click()
                            dropdown_clicked = True
                        else:  # inserted
                            break
                pass
            if dropdown_clicked:
                break
            await inc_page.wait_for_timeout(2000)
        if not dropdown_clicked:
            log_automation_step(logger, 'CREDENTIALS', 'DROPDOWN_BUTTON_NOT_FOUND')
            return {'success': False, 'api_key': ''}
        log_automation_step(logger, 'CREDENTIALS', 'DROPDOWN_BUTTON_CLICKED')
        await inc_page.wait_for_timeout(1500)
            await inc_page.get_by_role('menuitem', name='API key').first.click(timeout=5000)
            log_automation_step(logger, 'CREDENTIALS', 'API_KEY_MENU_ITEM_CLICKED')
            log_automation_step(logger, 'CREDENTIALS', 'API_KEY_MENU_ITEM_FAILED', {'error': str(e)})
            return {'success': False, 'api_key': ''}
            modal_locator = inc_page.locator('text=/API key created/i').locator('..').locator('..')
            await modal_locator.wait_for(state='visible', timeout=60000)
            log_automation_step(logger, 'API_KEY', 'MODAL_DETECTED')
            log_automation_step(logger, 'API_KEY', 'MODAL_NOT_FOUND')
            return {'success': False, 'api_key': ''}
            input_selector = modal_locator.locator('input.cfc-code-snippet-input')
            await input_selector.wait_for(state='visible', timeout=10000)
            for _ in range(10):
                val = await input_selector.input_value(timeout=1000)
                if val and val.startswith('AIza') and (len(val) > 35):
                    api_key = val
                    break
                await inc_page.wait_for_timeout(1000)
            log_automation_step(logger, 'API_KEY', 'EXTRACT_INPUT_READ_FAILED', {'error': str(e)})
        if not api_key:
            log_automation_step(logger, 'API_KEY', 'EXTRACT_FAILED_FINAL')
            return {'success': False, 'api_key': ''}
        log_automation_step(logger, 'API_KEY', 'SUCCESS', {'api_key': api_key})
        return {'success': True, 'api_key': api_key}
    else:  # inserted
        try:
            pass  # postinserted
        except Exception:
            pass  # postinserted
        else:  # inserted
            try:
                pass  # postinserted
            except Exception:
                pass  # postinserted
        else:  # inserted
            try:
                pass  # postinserted
            except Exception:
                pass  # postinserted
    else:  # inserted
        try:
            pass  # postinserted
        except Exception as e:
            pass  # postinserted
    else:  # inserted
        try:
            pass  # postinserted
        except Exception:
            pass  # postinserted
    else:  # inserted
        try:
            pass  # postinserted
        except Exception as e:
            pass  # postinserted
    except Exception as e:
            log_automation_step(logger, 'API_KEY', 'FATAL_ERROR', {'error': str(e)})
            return {'success': False, 'api_key': ''}
_open_cloud_console = open_cloud_console
_handle_gcloud_terms = handle_gcloud_terms
_enable_genai_and_create_api_key = enable_genai_and_create_api_key