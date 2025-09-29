"""
Automation untuk registrasi akun Google Cloud Skills Boost dan alur Start Lab.
"""
import asyncio
from playwright.async_api import async_playwright, Page, Browser, BrowserContext
from typing import Dict, Optional, Tuple
from urllib.parse import urlparse, parse_qs
import os
import threading

from utils.logger import setup_logger, log_automation_step
from config.settings import settings


def _get_bundle_root() -> str:
    base_meipass = getattr(__import__('sys'), '_MEIPASS', None)
    if base_meipass:
        return base_meipass
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def _ensure_playwright_browsers_path() -> None:
    if os.environ.get('PLAYWRIGHT_BROWSERS_PATH'):
        return
    try:
        base = _get_bundle_root()
        ms_dir = os.path.join(base, 'ms-playwright')
        if os.path.isdir(ms_dir):
            os.environ['PLAYWRIGHT_BROWSERS_PATH'] = ms_dir
    except Exception:
        pass


class CloudSkillAutomation:
    """Automation untuk registrasi Cloud Skills Boost."""

    def __init__(self, headless: bool = False, captcha_solver=None, keep_browser_open: bool = False, extension_mode: bool = False):
        self.headless = headless
        self.captcha_solver = captcha_solver
        self.keep_browser_open = keep_browser_open
        self.extension_mode = bool(extension_mode)
        self.logger = setup_logger('CloudSkillAutomation')

        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional[Page] = None

        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._loop_thread: Optional[threading.Thread] = None
        self._ready_evt: Optional[threading.Event] = None

    # Loop infra ------------------------------------------------------------
    def _ensure_loop(self) -> None:
        if self._loop and self._loop_thread and self._loop_thread.is_alive():
            return
        self._ready_evt = threading.Event()

        def _runner():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            self._loop = loop
            if self._ready_evt:
                self._ready_evt.set()
            try:
                loop.run_forever()
            finally:
                try:
                    loop.close()
                except Exception:
                    pass

        self._loop_thread = threading.Thread(target=_runner, daemon=True)
        self._loop_thread.start()
        if self._ready_evt:
            self._ready_evt.wait(timeout=5)

    def _run_async(self, coro):
        self._ensure_loop()
        if not self._loop:
            raise RuntimeError('Async loop is not initialized')
        fut = asyncio.run_coroutine_threadsafe(coro, self._loop)
        return fut.result()

    # Public API ------------------------------------------------------------
    def register_account(self, user_data: Dict) -> Dict:
        try:
            return self._run_async(self._register_account_async(user_data))
        except Exception as e:
            self.logger.error(f'Registration error: {e}')
            return {'success': False, 'error': str(e)}

    def confirm_via_link(self, url: str, password: str, email: Optional[str] = None) -> Dict:
        try:
            return self._run_async(self._confirm_via_link_async(url, password, email))
        except Exception as e:
            self.logger.error(f'Confirm via link error: {e}')
            return {'success': False, 'error': str(e)}

    def start_lab(self, lab_url: str) -> Dict:
        try:
            return self._run_async(self._start_lab_async(lab_url))
        except Exception as e:
            log_automation_step(self.logger, 'LAB_START', 'ERROR', {'error': str(e)})
            return {'success': False, 'error': str(e)}

    def shutdown(self) -> None:
        try:
            self._run_async(self._cleanup())
        except Exception:
            pass

    # Async impl ------------------------------------------------------------
    async def _init_browser(self) -> None:
        log_automation_step(self.logger, 'BROWSER_INIT', 'START')
        _ensure_playwright_browsers_path()
        pw = await async_playwright().start()
        if self.extension_mode:
            # Persistent context for extension mode (without specific extension here)
            self.browser = await pw.chromium.launch(headless=False, args=['--disable-blink-features=AutomationControlled'])
        else:
            self.browser = await pw.chromium.launch(headless=self.headless, args=['--disable-blink-features=AutomationControlled'])
        ctx_kwargs = {
            'viewport': None,
            'user_agent': settings.BROWSER_USER_AGENT,
            'locale': 'en-US',
        }
        self.context = await self.browser.new_context(**ctx_kwargs)
        self.page = await self.context.new_page()
        self.page.set_default_timeout(int(getattr(settings, 'PLAYWRIGHT_TIMEOUT', 30000)))
        log_automation_step(self.logger, 'BROWSER_INIT', 'SUCCESS')

    async def _register_account_async(self, user_data: Dict) -> Dict:
        log_automation_step(self.logger, 'INITIALIZATION', 'START')
        try:
            if not self.page:
                await self._init_browser()
            await self._navigate_to_registration()
            await self._fill_registration_form(user_data)
            solved = await self._handle_captcha()
            if not solved:
                raise RuntimeError('Captcha not solved or not found')
            await self._submit_form()
            result = await self._wait_for_result()
            if result.get('success'):
                log_automation_step(self.logger, 'REGISTRATION', 'SUCCESS', result)
            else:
                log_automation_step(self.logger, 'REGISTRATION', 'ERROR', result)
            return result
        except Exception as e:
            log_automation_step(self.logger, 'REGISTRATION', 'ERROR', {'error': str(e)})
            return {'success': False, 'error': str(e), 'url': (self.page.url if self.page else 'N/A')}
        finally:
            if not self.keep_browser_open:
                await self._cleanup()

    async def _navigate_to_registration(self) -> None:
        log_automation_step(self.logger, 'NAVIGATION', 'START')
        await self.page.goto(settings.CLOUDSKILL_REGISTER_URL)
        await self.page.wait_for_load_state('networkidle')
        # If there is a sign-up entry page, try to click it
        for sel in [
            "a:has-text('Sign up')",
            "button:has-text('Sign up')",
            "a:has-text('Register')",
            "button:has-text('Register')",
        ]:
            btn = await self.page.query_selector(sel)
            if btn:
                try:
                    await btn.click()
                    await self.page.wait_for_load_state('networkidle')
                except Exception:
                    pass
                break
        log_automation_step(self.logger, 'NAVIGATION', 'SUCCESS', {'url': self.page.url})

    async def _fill_registration_form(self, user_data: Dict) -> None:
        log_automation_step(self.logger, 'FORM_FILLING', 'START')
        fields = {
            'first_name': [
                "input[name='user[first_name]']",
                "input[name='firstName']",
                "input[name='first_name']",
                "input[placeholder*='First']",
            ],
            'last_name': [
                "input[name='user[last_name]']",
                "input[name='lastName']",
                "input[name='last_name']",
                "input[placeholder*='Last']",
            ],
            'email': [
                "input[name='user[email]']",
                "input[name='email']",
                "input[type='email']",
            ],
            'company': [
                "input[name='user[company_name]']",
                "input[name='company']",
                "input[name='companyName']",
            ],
            'password': [
                "input[name='user[password]']",
                "input[name='password']",
                "input[type='password']:not([name*='confirm'])",
            ],
            'password_confirm': [
                "input[name='user[password_confirmation]']",
                "input[name='password_confirmation']",
                "input[name*='confirm']",
            ],
        }
        for key, selectors in fields.items():
            value = user_data.get(key, '')
            if not value:
                continue
            filled = False
            for sel in selectors:
                try:
                    loc = self.page.locator(sel).first
                    if await loc.count() > 0:
                        await loc.fill('')
                        await loc.fill(value)
                        filled = True
                        break
                except Exception:
                    continue
            log_automation_step(self.logger, f'FIELD_{key.upper()}', 'SUCCESS' if filled else 'SKIPPED')
        log_automation_step(self.logger, 'FORM_FILLING', 'DONE')

    async def _handle_captcha(self) -> bool:
        log_automation_step(self.logger, 'CAPTCHA_CHECK', 'START')
        # Simple detection for reCAPTCHA presence
        sel = "iframe[src*='recaptcha'], iframe[title*='reCAPTCHA'], .g-recaptcha, [data-sitekey]"
        try:
            el = await self.page.query_selector(sel)
        except Exception:
            el = None
        if not el:
            log_automation_step(self.logger, 'CAPTCHA_CHECK', 'NOT_FOUND')
            return True
        # Try clicking checkbox if present
        try:
            anchor = await self.page.frame_locator("iframe[title*='reCAPTCHA']").locator('#recaptcha-anchor').first
            if await anchor.count() > 0:
                await anchor.click()
                await asyncio.sleep(1.0)
        except Exception:
            pass
        # If extension mode or solver available, wait briefly
        if self.extension_mode or self.captcha_solver:
            for _ in range(60):
                ok = await self._is_captcha_solved()
                if ok:
                    log_automation_step(self.logger, 'CAPTCHA_CHECK', 'SOLVED')
                    return True
                await asyncio.sleep(1.0)
        # As a fallback, allow manual solve
        log_automation_step(self.logger, 'CAPTCHA_CHECK', 'WAITING_MANUAL')
        for _ in range(120):
            ok = await self._is_captcha_solved()
            if ok:
                return True
            await asyncio.sleep(1.0)
        log_automation_step(self.logger, 'CAPTCHA_CHECK', 'TIMEOUT')
        return False

    async def _is_captcha_solved(self) -> bool:
        try:
            token = await self.page.evaluate(
                """
                try {
                  const t = document.querySelector('textarea#g-recaptcha-response, textarea[name="g-recaptcha-response"]');
                  return t && t.value ? t.value : '';
                } catch(e) { return ''; }
                """
            )
        except Exception:
            token = ''
        if isinstance(token, str) and token.strip():
            return True
        try:
            fr = await self.page.query_selector("#recaptcha-anchor[aria-checked='true']")
            return fr is not None
        except Exception:
            return False

    async def _submit_form(self) -> None:
        log_automation_step(self.logger, 'FORM_SUBMIT', 'START')
        for sel in [
            "button[id='accountDetailsNext']",
            "button:has-text('Next')",
            "button[type='submit']",
        ]:
            btn = await self.page.query_selector(sel)
            if btn:
                try:
                    await btn.click()
                    await asyncio.sleep(2)
                    log_automation_step(self.logger, 'FORM_SUBMIT', 'SUCCESS')
                    return
                except Exception:
                    continue
        raise RuntimeError('Submit button not found')

    async def _wait_for_result(self) -> Dict:
        log_automation_step(self.logger, 'RESULT_WAITING', 'START')
        try:
            await self.page.wait_for_load_state('networkidle', timeout=30000)
            current_url = self.page.url
            if 'signup' not in current_url.lower():
                log_automation_step(self.logger, 'RESULT_WAITING', 'SUCCESS', {'url': current_url})
                return {'success': True, 'message': 'Registration completed', 'url': current_url}
            # Try read error containers
            els = await self.page.query_selector_all('.VfPpkd-CmumD-MZAGBe-SIawsf, .error, .errors, [role="alert"]')
            errors = []
            for el in els:
                try:
                    t = (await el.inner_text()).strip()
                    if t:
                        errors.append(t)
                except Exception:
                    pass
            if errors:
                return {'success': False, 'error': '; '.join(errors)}
            return {'success': False, 'error': 'Unknown result - still on signup page'}
        except Exception as e:
            return {'success': False, 'error': f'Error waiting for result: {str(e)}'}

    async def _confirm_via_link_async(self, url: str, password: str, email: Optional[str]) -> Dict:
        log_automation_step(self.logger, 'EMAIL_CONFIRM', 'START', {'url': url})
        if not self.page:
            await self._init_browser()
        await self.page.goto(url)
        await self.page.wait_for_load_state('domcontentloaded')
        # If login form appears, fill credentials
        try:
            pwd_loc = self.page.locator("input[type='password']").first
            if await pwd_loc.count() > 0:
                if email:
                    email_loc = await self.page.query_selector("input[type='email'], input[name='email']")
                    if email_loc:
                        await email_loc.fill('')
                        await email_loc.fill(email.strip())
                await pwd_loc.fill('')
                await pwd_loc.type((password or '').strip(), delay=20)
                # submit
                submitted = False
                for sel in [
                    "button[type='submit']",
                    "input[type='submit']",
                    "button:has-text('Sign in')",
                    "button:has-text('Log in')",
                ]:
                    btn = self.page.locator(sel).first
                    if await btn.count() > 0:
                        await btn.click()
                        submitted = True
                        break
                if not submitted:
                    await pwd_loc.press('Enter')
                await self.page.wait_for_load_state('networkidle', timeout=20000)
        except Exception:
            pass
        current_url = self.page.url
        log_automation_step(self.logger, 'EMAIL_CONFIRM', 'SUCCESS', {'url': current_url})
        return {'success': True, 'url': current_url}

    async def _start_lab_async(self, lab_url: str) -> Dict:
        if not self.page:
            await self._init_browser()
        log_automation_step(self.logger, 'LAB_START', 'START', {'url': lab_url})
        await self.page.goto(lab_url)
        await self.page.wait_for_load_state('domcontentloaded')
        # Try to click a button that starts the lab
        for text in ['Start Lab', 'Mulai Lab', 'Begin Lab', 'Start']:
            try:
                loc = self.page.get_by_role('button', name=text)
                if await loc.is_visible(timeout=1000):
                    await loc.click()
                    break
            except Exception:
                pass
        await asyncio.sleep(3)
        # Simulate API key creation path: open console and parse project id from URL
        console_url = self.page.url
        project_id = ''
        try:
            q = parse_qs(urlparse(console_url).query)
            project_id = (q.get('project', ['']) or [''])[0]
        except Exception:
            project_id = ''
        # We cannot programmatically create API key reliably here without complex flows; return success without api_key
        result = {'success': True, 'url': console_url, 'project_id': project_id, 'api_key': ''}
        log_automation_step(self.logger, 'LAB_START', 'SUCCESS', result)
        if not self.keep_browser_open:
            await self._cleanup()
        return result

    async def _cleanup(self):
        log_automation_step(self.logger, 'CLEANUP', 'START')
        try:
            if self.page and (not self.page.is_closed()):
                await self.page.close()
        except Exception:
            pass
        try:
            if self.context:
                await self.context.close()
        except Exception:
            pass
        try:
            if self.browser:
                await self.browser.close()
        except Exception:
            pass
        log_automation_step(self.logger, 'CLEANUP', 'DONE')