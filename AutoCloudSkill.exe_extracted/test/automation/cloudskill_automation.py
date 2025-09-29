"""
Automation untuk registrasi akun Google Cloud Skills Boost
"""
import asyncio
from playwright.async_api import async_playwright, Page, Browser, BrowserContext
from urllib.parse import urlparse, parse_qs
import time
import base64
from typing import Dict, Optional
from pathlib import Path
import logging
import os
import sys
import threading
import concurrent.futures
from automation.lab_actions_simple import start_lab as start_lab_action, open_cloud_console as open_console_action, handle_gcloud_terms as handle_terms_action, enable_genai_and_create_api_key as enable_key_action
from automation.confirm_actions import confirm_via_link_action
from utils.logger import setup_logger, log_automation_step
from config.settings import settings

def _get_bundle_root() -> Path:
    """Resolve base directory depending on frozen/development mode."""
    base_meipass = getattr(sys, '_MEIPASS', None)
    if base_meipass:
        return Path(base_meipass)
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent.parent

def _ensure_playwright_browsers_path() -> None:
    """Set env PLAYWRIGHT_BROWSERS_PATH ke folder ms-playwright lokal (jika ada).
    Meniru pola di topazcreator agar saat build (Nuitka/one-dir) Playwright tetap
    menemukan binary browser.
    """
    if os.environ.get('PLAYWRIGHT_BROWSERS_PATH'):
        return
    try:
        base = _get_bundle_root()
        ms_dir = base / 'ms-playwright'
        if ms_dir.exists():
            os.environ['PLAYWRIGHT_BROWSERS_PATH'] = str(ms_dir)
            return
    except Exception:
        pass

class CloudSkillAutomation:
    """Automation untuk registrasi Google Cloud Skills Boost"""

    def __init__(self, headless: bool=False, captcha_solver=None, keep_browser_open: bool=False, extension_mode: bool=False):
        """
        Initialize automation
        
        Args:
            headless: Jalankan browser dalam headless mode
            captcha_solver: Instance captcha solver service
        """
        self.headless = headless
        self.captcha_solver = captcha_solver
        self.logger = setup_logger('CloudSkillAutomation')
        self.browser = None
        self.context = None
        self.page = None
        self.extension_mode = bool(extension_mode)
        self.keep_browser_open = keep_browser_open
        self._popup_mode = 'redirect'
        self._loop = None
        self._loop_thread = None
        self._loop_ready_evt = None

    @staticmethod
    def get_default_pw_state_path() -> str:
        """Lokasi default untuk menyimpan Playwright storage state (.pw-state.json).
        Prioritas: %LOCALAPPDATA%\\AutoCloudSkill\\playwright\\.pw-state.json, fallback ke Home/AppData/Local.
        """
        base = None
        try:
            base = os.environ.get('LOCALAPPDATA')
        except Exception:
            base = None
        if not base:
            try:
                base = os.path.join(os.path.expanduser('~'), 'AppData', 'Local')
            except Exception:
                base = os.getcwd()
        state_dir = os.path.join(base, 'AutoCloudSkill', 'playwright')
        return os.path.join(state_dir, '.pw-state.json')

    @staticmethod
    def get_default_pw_profile_dir() -> str:
        """Lokasi default untuk persistent user-data-dir Playwright (profil Chromium).
        Disimpan di %LOCALAPPDATA% agar writable saat aplikasi terinstall di Program Files.
        """
        base = None
        try:
            base = os.environ.get('LOCALAPPDATA')
        except Exception:
            base = None
        if not base:
            try:
                base = os.path.join(os.path.expanduser('~'), 'AppData', 'Local')
            except Exception:
                base = os.getcwd()
        return os.path.join(base, 'AutoCloudSkill', 'playwright', 'profile')

    def _ensure_loop(self) -> None:
        if self._loop and self._loop_thread and self._loop_thread.is_alive():
            return
        self._loop_ready_evt = threading.Event()

        def _runner():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            self._loop = loop
            try:
                if self._loop_ready_evt:
                    self._loop_ready_evt.set()
                loop.run_forever()
            finally:
                try:
                    loop.close()
                except Exception:
                    pass
        self._loop_thread = threading.Thread(target=_runner, daemon=True)
        self._loop_thread.start()
        if self._loop_ready_evt:
            self._loop_ready_evt.wait(timeout=5)

    def _run_async(self, coro):
        """Jalankan coroutine di event loop internal dan kembalikan hasilnya (blocking)."""
        self._ensure_loop()
        if not self._loop:
            raise RuntimeError('Async loop is not initialized')
        fut = asyncio.run_coroutine_threadsafe(coro, self._loop)
        return fut.result()

    def register_account(self, user_data: Dict) -> Dict:
        """
        Jalankan proses registrasi akun
        
        Args:
            user_data: Data user untuk registrasi
            
        Returns:
            Dict dengan hasil registrasi
        """
        try:
            return self._run_async(self._register_account_async(user_data))
        except Exception as e:
            self.logger.error(f'Registration error: {e}')
            return {'success': False, 'error': str(e)}

    async def _register_account_async(self, user_data: Dict) -> Dict:
        """Async implementation registrasi akun"""
        log_automation_step(self.logger, 'INITIALIZATION', 'START')
        try:
            await self._init_browser()
            await self._navigate_to_registration()
            await self._fill_registration_form(user_data)
            try:
                await self._scroll_to_recaptcha(max_steps=3, fast=True, skip_fallback=True)
            except Exception:
                pass
            captcha_ok = await self._handle_captcha()
            if not captcha_ok:
                raise Exception('Captcha not solved or timed out')
            await self._submit_form()
            result = await self._wait_for_result()
            log_automation_step(self.logger, 'REGISTRATION', 'SUCCESS' if result.get('success') else 'ERROR', result)
            if not self.keep_browser_open:
                await self._cleanup()
            return result
        except Exception as e:
            log_automation_step(self.logger, 'REGISTRATION', 'ERROR', {'error': str(e)})
            return {'success': False, 'error': str(e), 'url': getattr(self.page, 'url', 'N/A') if hasattr(self, 'page') else 'N/A'}
        finally:
            if not self.keep_browser_open:
                try:
                    await self._cleanup()
                except Exception:
                    pass

    async def _is_confirmation_success(self) -> bool:
        """Deteksi indikator sukses konfirmasi di halaman saat ini."""
        try:
            success_patterns = ['successfully confirmed', 'your account was successfully confirmed', 'your account has been confirmed', 'email address has been successfully confirmed']
            containers = ['div[role=\'alert\']', '.alert.alert-success', '.notice', '.flash--success', '#notice', '[class*=\'success\']']
            for sel in containers:
                try:
                    el = await self.page.query_selector(sel)
                    if el:
                        txt = await el.text_content()
                        if txt:
                            txt = txt.strip().lower()
                        else:
                            txt = ""
                        
                        for pat in success_patterns:
                            if pat in txt:
                                return True
                except Exception:
                    pass
            
            # Cek di body jika tidak ditemukan di container
            try:
                body_txt = await self.page.text_content('body')
                if body_txt:
                    body_txt = body_txt.lower()
                else:
                    body_txt = ""
                
                for pat in success_patterns:
                    if pat in body_txt:
                        return True
            except Exception:
                pass
            
            return False
        except Exception:
            return False

    async def _bind_single_page_policy(self):
        """Ikatan kebijakan single-page: tutup tab lain setiap ada page baru muncul."""
        try:
            if not self.context:
                return None
            
            script = '''
            (function(){
                try {
                    // Jangan override di domain Cloud Skills Boost; biarkan popup agar bisa ditangani Playwright
                    var h = (location && location.hostname) ? location.hostname : '';
                    if (h.includes('cloudskillsboost.google')) {
                        return;
                    }
                } catch(e) {}
                try { window.open = function(u){ try { window.location.href = u; } catch(e) {} return null; }; } catch(e) {}
                try {
                    document.addEventListener('click', function(ev){
                        const a = ev.target && ev.target.closest ? ev.target.closest('a[target="_blank"]') : null;
                        if (a && a.href) { try { ev.preventDefault(); window.location.href = a.href; } catch(e){} }
                    }, true);
                } catch(e) {}
            })();
            '''
            
            try:
                await self.context.add_init_script(script)
            except Exception:
                pass
            
            # Handler untuk page event
            async def _handler(page):
                try:
                    target_url = None
                    
                    for _ in range(20):
                        try:
                            u = page.url
                        except Exception:
                            u = ""
                        
                        if u and u != 'about:blank':
                            target_url = u
                            break
                        
                        await asyncio.sleep(0.1)
                    
                    if not target_url:
                        try:
                            await page.wait_for_load_state('domcontentloaded', timeout=3000)
                            target_url = page.url
                        except Exception:
                            pass
                    
                    mode = getattr(self, '_popup_mode', 'redirect')
                    
                    if mode == 'switch':
                        if target_url and not target_url.startswith('about:blank'):
                            self.page = page
                            try:
                                await page.bring_to_front()
                            except Exception:
                                pass
                            return
                        
                        try:
                            await page.close()
                        except Exception:
                            pass
                        return
                    
                    if mode == 'ignore':
                        try:
                            await page.close()
                        except Exception:
                            pass
                        return
                    
                    if self.page and target_url and not target_url.startswith('about:blank'):
                        try:
                            await self.page.goto(target_url)
                        except Exception:
                            pass
                    
                    try:
                        await page.close()
                    except Exception:
                        pass
                    return
                except Exception:
                    return None
            
            try:
                self.context.remove_listeners('page')
            except Exception:
                pass
            
            try:
                self.context.on('page', lambda page: asyncio.create_task(_handler(page)))
            except Exception:
                pass
            
            pass
        except Exception:
            pass

    async def _unbind_page_policy(self):
        """Lepas semua listener 'page' sementara (misal saat Start Lab)."""
        try:
            if self.context:
                self.context.remove_listeners('page')
        except Exception:
            pass

    def confirm_via_link(self, url: str, password: str, email: Optional[str]=None) -> Dict:
        """Wrapper sync untuk konfirmasi via link email dan login (reuse loop/sesi)."""
        try:
            return self._run_async(self._confirm_via_link_async(url, password, email))
        except Exception as e:
            self.logger.error(f'Confirm via link error: {e}')
            return {'success': False, 'error': str(e)}

    def start_lab(self, lab_url: str) -> Dict:
        """Wrapper sinkron: mulai lab menggunakan session/page yang sudah ada (reuse)."""
        try:
            return self._run_async(self._start_lab_async(lab_url))
        except Exception as e:
            log_automation_step(self.logger, 'LAB_START', 'ERROR', {'error': str(e)})
            return {'success': False, 'error': str(e)}

    async def _start_lab_async(self, lab_url: str) -> Dict:
        """Implementasi async untuk mulai lab. Reuse self.page saat ini tanpa membuka sesi baru."""
        if not self.page:
            raise RuntimeError('Page is not initialized')
        try:
            prev_mode = self._popup_mode
            self._popup_mode = 'ignore'
            try:
                await self._unbind_page_policy()
            except Exception:
                pass
            
            result = await start_lab_action(page=self.page, logger=self.logger, handle_captcha=lambda: self._handle_captcha(), lab_url=lab_url, wait_networkidle=True)
            if not result.get('success'):
                try:
                    self._popup_mode = prev_mode
                    await self._bind_single_page_policy()
                except Exception:
                    pass
                return result
            
            inc_ctx = None
            inc_page = None
            try:
                if not self.browser:
                    return {'success': False, 'error': 'Browser not initialized'}
                
                console_info, inc_ctx, inc_page = await open_console_action(self.page, self.logger, self.browser, timeout_sec=300)
                if not console_info.get('opened') or not inc_page:
                    log_automation_step(self.logger, 'OPEN_CONSOLE', 'FAILED')
                    return {'success': False, 'error': 'Could not open Google Cloud console', 'url': getattr(self.page, 'url', '')}
                
                terms_res = await handle_terms_action(inc_page, self.logger, timeout_sec=120)
                if not terms_res.get('handled'):
                    log_automation_step(self.logger, 'TERMS', 'SKIPPED_OR_FAILED', {'reason': terms_res.get('reason', '')})
                else:
                    log_automation_step(self.logger, 'TERMS', 'DONE', {'url': terms_res.get('url', '')})
                
                project_id = ''
                try:
                    q = parse_qs(urlparse(inc_page.url).query)
                    project_id = (q.get('project', ['']) or [''])[0]
                except Exception:
                    project_id = ''
                
                if not project_id:
                    return {'success': False, 'error': 'Could not parse project_id from console URL', 'console_opened': True, 'console_url': inc_page.url if hasattr(inc_page, 'url') else ''}
                
                log_automation_step(self.logger, 'GCP_PROJECT', 'PARSED', {'project_id': project_id})
                
                api_res = await enable_key_action(inc_page, self.logger, project_id, timeout_sec=180)
                api_key_val = api_res.get('api_key', '')
                
                if not api_res.get('success') or not api_key_val:
                    log_automation_step(self.logger, 'API_KEY', 'FAILED_CREATE_OR_EXTRACT')
                    return {'success': False, 'error': 'Failed to create or extract API key', 'project_id': project_id, 'console_url': inc_page.url if hasattr(inc_page, 'url') else '', 'console_opened': True}
                
                log_automation_step(self.logger, 'API_KEY', 'SUCCESS', {'prefix': api_key_val[:10]})
                
                result_out = {'success': True, 'url': getattr(self.page, 'url', ''), 'console_opened': True, 'console_url': inc_page.url if hasattr(inc_page, 'url') else '', 'console_incognito': True, 'project_id': project_id, 'api_key': api_key_val}
                
                try:
                    if inc_ctx and not self.keep_browser_open:
                        await inc_ctx.close()
                except Exception:
                    pass
                
                return result_out
            finally:
                try:
                    if inc_ctx and not self.keep_browser_open:
                        await inc_ctx.close()
                except Exception:
                    pass
                
                self._popup_mode = prev_mode
                try:
                    await self._bind_single_page_policy()
                except Exception:
                    pass
        except Exception as e:
            log_automation_step(self.logger, 'LAB_START', 'ERROR', {'error': str(e)})
            return {'success': False, 'error': str(e)}
        finally:
            self._popup_mode = prev_mode
            try:
                await self._bind_single_page_policy()
            except Exception:
                pass

    def shutdown(self) -> None:
        """Tutup browser secara sinkron (wrapper untuk _cleanup)."""
        try:
            self._run_async(self._cleanup())
        except Exception:
            return None

    async def _confirm_via_link_async(self, url: str, password: str, email: Optional[str]=None) -> Dict:
        """Buka link konfirmasi dari email. Jika halaman login muncul dan email sudah terisi,
        isi password yang digunakan saat registrasi dan submit.
        """
        log_automation_step(self.logger, 'EMAIL_CONFIRM', 'START', {'url': url})
        try:
            await self._ensure_page_ready()
            if not self.context or not self.page:
                raise RuntimeError('Context/Page not initialized')
            
            result = await confirm_via_link_action(self.context, self.page, self.logger, url, password, email)
            
            try:
                if self.context.pages:
                    self.page = self.context.pages[-1]
            except Exception:
                pass
            
            return result
        except Exception as e:
            log_automation_step(self.logger, 'EMAIL_CONFIRM', 'ERROR', {'error': str(e)})
            return {'success': False, 'error': str(e)}

    async def _ensure_page_ready(self):
        """Pastikan context & page tersedia dan tidak tertutup."""
        try:
            needs_init = False
            if not self.context or not self.page:
                needs_init = True
            else:
                try:
                    if self.page.is_closed():
                        needs_init = True
                except Exception:
                    needs_init = True
            
            if needs_init:
                await self._init_browser()
        except Exception:
            try:
                await self._init_browser()
            except Exception:
                pass

    async def _close_other_pages(self, keep_current: bool=True) -> None:
        """Tutup page lain yang bukan current, termasuk about:blank agar tidak ada window kosong tersisa."""
        try:
            if not self.context:
                return
            
            for p in list(self.context.pages):
                try:
                    if keep_current:
                        if self.page and p == self.page:
                            continue
                    
                    url = p.url
                    if not p.is_closed():
                        if not url.startswith('about:blank'):
                            pass
                        await p.close()
                except Exception:
                    continue
        except Exception:
            return None

    async def _init_browser(self):
        """Initialize browser.
        - Jika folder ekstensi AntiCaptcha (rekTCaptcha) tersedia di project root, gunakan persistent context dan load ekstensi.
        - Jika tidak, gunakan incognito context dengan preload storage_state.
        """
        log_automation_step(self.logger, 'BROWSER_INIT', 'START')
        try:
            _ensure_playwright_browsers_path()
        except Exception:
            pass
        
        pw = await async_playwright().start()
        project_root = _get_bundle_root()
        state_path_str = self.get_default_pw_state_path()
        user_data_dir_str = self.get_default_pw_profile_dir()
        
        try:
            os.makedirs(os.path.dirname(state_path_str), exist_ok=True)
            os.makedirs(user_data_dir_str, exist_ok=True)
        except Exception:
            pass
        
        ext_dir = project_root / 'AntiCaptcha'
        
        try:
            sp = Path(state_path_str)
            if sp.exists():
                sp.unlink()
        except Exception:
            pass
        
        try:
            import shutil
            if os.path.isdir(user_data_dir_str):
                shutil.rmtree(user_data_dir_str, ignore_errors=True)
        except Exception:
            pass
        
        if self.extension_mode and ext_dir.exists():
            try:
                args = ['--disable-blink-features=AutomationControlled', f'--disable-extensions-except={ext_dir}', f'--load-extension={ext_dir}']
                self.context = await pw.chromium.launch_persistent_context(
                    user_data_dir=str(user_data_dir_str), 
                    headless=False, 
                    args=args, 
                    viewport=None, 
                    user_agent=settings.BROWSER_USER_AGENT, 
                    locale='en-US'
                )
                try:
                    self.browser = self.context.browser
                except Exception:
                    self.browser = None
                
                await self._bind_single_page_policy()
                self.page = await self.context.new_page()
                self.page.set_default_timeout(settings.PLAYWRIGHT_TIMEOUT)
                log_automation_step(self.logger, 'BROWSER_INIT', 'EXTENSION_MODE', {'ext_dir': str(ext_dir), 'profile': user_data_dir_str})
                return
            except Exception as e:
                log_automation_step(self.logger, 'BROWSER_INIT', 'EXTENSION_MODE_FAILED', {'error': str(e), 'profile': user_data_dir_str})
        
        self.browser = await pw.chromium.launch(headless=self.headless, args=['--disable-blink-features=AutomationControlled'])
        context_kwargs = {'viewport': None, 'user_agent': settings.BROWSER_USER_AGENT, 'locale': 'en-US'}
        self.context = await self.browser.new_context(**context_kwargs)
        await self._bind_single_page_policy()
        self.page = await self.context.new_page()
        self.page.set_default_timeout(settings.PLAYWRIGHT_TIMEOUT)
        log_automation_step(self.logger, 'BROWSER_INIT', 'STANDARD_MODE')

    async def _navigate_to_registration(self):
        """Navigate ke halaman registrasi Cloud Skills Boost"""
        log_automation_step(self.logger, 'NAVIGATION', 'START')
        try:
            await self.page.goto(settings.CLOUDSKILL_REGISTER_URL)
            await self.page.wait_for_load_state('networkidle')
            
            try:
                await self.page.wait_for_selector('input[type=\'email\'], input[name=\'email\'], input[type=\'text\']', timeout=15000)
            except Exception:
                sign_up_btn = await self.page.query_selector('a:has-text(\'Sign up\'), button:has-text(\'Sign up\'), a:has-text(\'Register\'), button:has-text(\'Register\')')
                if sign_up_btn:
                    await sign_up_btn.click()
                    await self.page.wait_for_load_state('networkidle')
                    await self.page.wait_for_selector('input[type=\'email\'], input[name=\'email\'], input[type=\'text\']', timeout=10000)
            
            log_automation_step(self.logger, 'NAVIGATION', 'SUCCESS', {'url': self.page.url})
        except Exception as e:
            log_automation_step(self.logger, 'NAVIGATION', 'ERROR', {'error': str(e)})
            raise

    async def _fill_registration_form(self, user_data: Dict):
        """Fill form registrasi Cloud Skills Boost dengan deep DOM search"""
        log_automation_step(self.logger, 'FORM_FILLING', 'START')
        try:
            deep_fill_field_js = '''
            const selector = arguments[0];
            const maxDepth = 5;
            const queue = [{ root: document, depth: 0 }];
            
            while (queue.length) {
                const { root, depth } = queue.shift();
                try {
                    const el = root.querySelector(selector);
                    if (el) return el;
                } catch (e) {}
                
                let nodes = [];
                try { 
                    nodes = root.querySelectorAll('*'); 
                } catch (e) { 
                    nodes = []; 
                }
                
                for (const n of nodes) {
                    if (n && n.shadowRoot && depth < maxDepth) {
                        queue.push({ root: n.shadowRoot, depth: depth + 1 });
                    }
                }
            }
            return null;
            '''
            
            deep_query_script = '''
            const element = arguments[0];
            const value = arguments[1];
            
            function setVal(el) {
                if (!el) return false;
                if (el.readOnly || el.disabled) return false;
                
                try { el.focus(); } catch(e) {}
                try { el.value = ''; } catch(e) {}
                try { el.dispatchEvent(new Event('input', { bubbles: true })); } catch(e) {}
                try { el.value = value; } catch(e) { return false; }
                try { el.dispatchEvent(new Event('input', { bubbles: true })); } catch(e) {}
                try { el.dispatchEvent(new Event('change', { bubbles: true })); } catch(e) {}
                return true;
            }
            
            const tag = (element.tagName || '').toUpperCase();
            if (tag === 'INPUT' || tag === 'TEXTAREA') {
                return setVal(element);
            }
            
            if (typeof element.value !== 'undefined') {
                try { element.focus?.(); } catch(e) {}
                try { element.value = value; } catch(e) {}
                try { element.dispatchEvent(new Event('input', { bubbles: true })); } catch(e) {}
                try { element.dispatchEvent(new Event('change', { bubbles: true })); } catch(e) {}
                return true;
            }
            
            // Try shadow DOM
            let inp = null;
            if (element.shadowRoot) {
                inp = element.shadowRoot.querySelector('input,textarea');
                if (inp && setVal(inp)) return true;
            }
            
            inp = element.querySelector?.('input,textarea') || null;
            if (inp && setVal(inp)) return true;
            
            return false;
            '''

            async def smart_fill_field(labels, placeholders, selectors, value, field_name):
                for lbl in labels or []:
                    try:
                        base = self.page.get_by_label(lbl)
                        if await base.count() > 0:
                            locator = base.first
                            await locator.scroll_into_view_if_needed()
                            await locator.wait_for(state='visible', timeout=5000)
                            await locator.click()
                            await locator.fill(value)
                            await asyncio.sleep(0.1)
                            if await locator.input_value() == value:
                                log_automation_step(self.logger, f'{field_name}_FILLED', 'SUCCESS', {'method': 'get_by_label', 'label': lbl})
                                return True
                    except Exception as e:
                        log_automation_step(self.logger, f'{field_name}_ATTEMPT', 'FAILED', {'method': 'get_by_label', 'label': lbl, 'error': str(e)})
                
                for ph in placeholders or []:
                    try:
                        base = self.page.get_by_placeholder(ph)
                        if await base.count() > 0:
                            locator = base.first
                            await locator.scroll_into_view_if_needed()
                            await locator.wait_for(state='visible', timeout=5000)
                            await locator.click()
                            await locator.fill(value)
                            await asyncio.sleep(0.1)
                            if await locator.input_value() == value:
                                log_automation_step(self.logger, f'{field_name}_FILLED', 'SUCCESS', {'method': 'get_by_placeholder', 'placeholder': ph})
                                return True
                    except Exception as e:
                        log_automation_step(self.logger, f'{field_name}_ATTEMPT', 'FAILED', {'method': 'get_by_placeholder', 'placeholder': ph, 'error': str(e)})
                
                return await deep_fill_field(selectors, value, field_name)

            async def deep_fill_field(field_selectors, value, field_name):
                for selector in field_selectors:
                    try:
                        base_loc = self.page.locator(selector)
                        if await base_loc.count() > 0:
                            locator = base_loc.first
                            try:
                                await locator.fill('')
                            except Exception:
                                pass
                            
                            await locator.click(force=True)
                            await locator.fill(value)
                            await asyncio.sleep(0.2)
                            
                            try:
                                filled_value = await locator.input_value()
                            except Exception:
                                filled_value = ''
                            
                            if filled_value == value:
                                log_automation_step(self.logger, f'{field_name}_FILLED', 'SUCCESS', {'selector': selector, 'method': 'locator_fill', 'value': filled_value})
                                return True
                            
                            handle = await locator.element_handle()
                            if handle:
                                result = await self.page.evaluate(deep_query_script, handle, value)
                                if result:
                                    try:
                                        filled_value = await locator.input_value()
                                    except Exception:
                                        filled_value = value
                                    
                                    log_automation_step(self.logger, f'{field_name}_FILLED', 'SUCCESS', {'selector': selector, 'method': 'locator_script', 'value': filled_value})
                                    return True
                            
                            handle = await self.page.evaluate_handle(deep_query_script, selector)
                            is_null = await self.page.evaluate('el => el === null', handle)
                            if not is_null:
                                result = await self.page.evaluate(deep_query_script, handle, value)
                                if result:
                                    log_automation_step(self.logger, f'{field_name}_FILLED', 'SUCCESS', {'selector': selector, 'method': 'deep_query'})
                                    return True
                    except Exception as e:
                        log_automation_step(self.logger, f'{field_name}_ATTEMPT', 'FAILED', {'selector': selector, 'error': str(e)})
                
                log_automation_step(self.logger, f'{field_name}_FILLED', 'FAILED', {'reason': 'No working selector found'})
                return False

            fill_input_script = {'first_name': False, 'last_name': False, 'email': False, 'company': False, 'password': False, 'password_confirm': False}
            
            first_name_selectors = ['input[name=\'user[first_name]\']', 'input[name=\'firstName\']', 'input[name=\'first_name\']', 'input[placeholder*=\'First name\']', 'input[placeholder*=\'First\']', 'input[id*=\'first\']', 'input[type=\'text\']:first-of-type']
            fill_input_script['first_name'] = await smart_fill_field(labels=['First name'], placeholders=['First name'], selectors=first_name_selectors, value=user_data['first_name'], field_name='FIRST_NAME')
            
            last_name_selectors = ['input[name=\'user[last_name]\']', 'input[name=\'lastName\']', 'input[name=\'last_name\']', 'input[placeholder*=\'Last name\']', 'input[placeholder*=\'Last\']', 'input[id*=\'last\']']
            fill_input_script['last_name'] = await smart_fill_field(labels=['Last name'], placeholders=['Last name'], selectors=last_name_selectors, value=user_data['last_name'], field_name='LAST_NAME')
            
            email_selectors = ['input[name=\'user[email]\']', 'input[name=\'email\']', 'input[type=\'email\']', 'input[placeholder*=\'Email\']', 'input[placeholder*=\'email\']', 'input[id*=\'email\']']
            fill_input_script['email'] = await smart_fill_field(labels=['Email'], placeholders=['Email'], selectors=email_selectors, value=user_data['email'], field_name='EMAIL')
            
            company_selectors = ['input[name=\'user[company_name]\']', 'input[name=\'company\']', 'input[name=\'companyName\']', 'input[name=\'company_name\']', 'input[placeholder*=\'Company\']', 'input[placeholder*=\'company\']', 'input[id*=\'company\']']
            fill_input_script['company'] = await smart_fill_field(labels=['Company'], placeholders=['Company'], selectors=company_selectors, value=user_data['company'], field_name='COMPANY')
            
            password_selectors = ['input[name=\'user[password]\']', 'input[name=\'password\']', 'input[type=\'password\']:first-of-type', 'input[id*=\'password\']:not([id*=\'confirm\'])', 'input[placeholder*=\'Password\']']
            fill_input_script['password'] = await smart_fill_field(labels=['Password'], placeholders=['Password'], selectors=password_selectors, value=user_data['password'], field_name='PASSWORD')
            
            confirm_selectors = ['input[name=\'user[password_confirmation]\']', 'input[name=\'password_confirmation\']', 'input[name=\'passwordConfirmation\']', 'input[name=\'confirmPassword\']', 'input[type=\'password\']:last-of-type', 'input[id*=\'confirm\']', 'input[placeholder*=\'Password confirmation\']']
            fill_input_script['password_confirm'] = await smart_fill_field(labels=['Password confirmation'], placeholders=['Password confirmation'], selectors=confirm_selectors, value=user_data['password'], field_name='PASSWORD_CONFIRM')
            
            await self._fill_birth_date()
            await self._handle_newsletter_checkbox()
            
            try:
                await self.page.evaluate('''
                    (sk) => {
                        try {
                            const byKey = document.querySelector(`div.g-recaptcha[data-sitekey="${sk}"]`);
                            const any = byKey || document.querySelector("div.g-recaptcha");
                            if (any) { try { any.scrollIntoView({block:"center"}); } catch(e) {} }
                            return !!any;
                        } catch(e) { return false; }
                    }
                ''', '6LeOI8IUAAAAAPkHlMAE9NReCD_1WD81iYlBlCnV')
                await asyncio.sleep(0.2)
            except Exception:
                pass
            
            try:
                await self._scroll_to_recaptcha(max_steps=5, fast=True, skip_fallback=True)
            except Exception:
                pass
            
            failed_fields = [field for field, success in fill_input_script.items() if not success]
            successful_fields = [field for field, success in fill_input_script.items() if success]
            
            log_automation_step(self.logger, 'FORM_VALIDATION', 'SUMMARY', {
                'successful_fields': successful_fields, 
                'failed_fields': failed_fields, 
                'success_rate': f'{len(successful_fields)}/{len(fill_input_script)}'
            })
            
            critical_fields = ['first_name', 'email', 'password']
            critical_failed = [field for field in critical_fields if not fill_input_script.get(field, False)]
            
            if critical_failed:
                error_msg = f"Critical fields tidak terisi: {', '.join(critical_failed)}"
                log_automation_step(self.logger, 'FORM_FILLING', 'CRITICAL_ERROR', {'failed_critical_fields': critical_failed})
                raise Exception(error_msg)
            
            if len(failed_fields) > 2:
                error_msg = f"Terlalu banyak field yang gagal diisi: {', '.join(failed_fields)}"
                log_automation_step(self.logger, 'FORM_FILLING', 'ERROR', {'failed_fields': failed_fields})
                raise Exception(error_msg)
            
            log_automation_step(self.logger, 'FORM_FILLING', 'SUCCESS', {'filled_fields': successful_fields, 'skipped_fields': failed_fields})
        except Exception as e:
            log_automation_step(self.logger, 'FORM_FILLING', 'ERROR', {'error': str(e)})
            raise

    async def _fill_birth_date(self):
        """Fill birth date fields (month dropdown, day, year)"""
        log_automation_step(self.logger, 'BIRTH_DATE', 'START')
        try:
            import random
            from datetime import datetime
            
            current_year = datetime.now().year
            birth_year = random.randint(current_year - 65, current_year - 18)
            birth_month = random.randint(1, 12)
            birth_day = random.randint(1, 28)
            
            month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            month_name = month_names[birth_month - 1]
            
            month_selectors = ['select[name=\'dob_month\']', 'select[name=\'user[dob_month]\']', 'select[name=\'month\']', 'select[id*=\'month\']']
            for selector in month_selectors:
                try:
                    element = await self.page.query_selector(selector)
                    if element:
                        await element.select_option(label=month_name)
                        log_automation_step(self.logger, 'BIRTH_MONTH', 'SUCCESS', {'month': month_name})
                        break
                except Exception:
                    pass
            
            day_selectors = ['input[name=\'dob_day\']', 'input[name=\'user[dob_day]\']', 'input[name=\'day\']', 'input[id*=\'day\']']
            for selector in day_selectors:
                try:
                    element = await self.page.query_selector(selector)
                    if element:
                        await element.fill(str(birth_day))
                        log_automation_step(self.logger, 'BIRTH_DAY', 'SUCCESS', {'day': birth_day})
                        break
                except Exception:
                    pass
            
            year_selectors = ['input[name=\'dob_year\']', 'input[name=\'user[dob_year]\']', 'input[name=\'year\']', 'input[id*=\'year\']']
            for selector in year_selectors:
                try:
                    element = await self.page.query_selector(selector)
                    if element:
                        await element.fill(str(birth_year))
                        log_automation_step(self.logger, 'BIRTH_YEAR', 'SUCCESS', {'year': birth_year})
                        break
                except Exception:
                    pass
            
            log_automation_step(self.logger, 'BIRTH_DATE', 'SUCCESS')
        except Exception as e:
            log_automation_step(self.logger, 'BIRTH_DATE', 'ERROR', {'error': str(e)})

    async def _handle_newsletter_checkbox(self):
        """Handle newsletter/updates checkbox"""
        log_automation_step(self.logger, 'NEWSLETTER_CHECKBOX', 'START')
        try:
            checkbox_selectors = [
                'input[type=\'checkbox\'][name*=\'updates\']', 
                'input[type=\'checkbox\'][name*=\'newsletter\']', 
                'input[type=\'checkbox\'][name*=\'marketing\']', 
                'input[type=\'checkbox\']:visible'
            ]
            
            for selector in checkbox_selectors:
                try:
                    element = await self.page.query_selector(selector)
                    if element:
                        is_checked = await element.is_checked()
                        if not is_checked:
                            await element.check()
                            log_automation_step(self.logger, 'NEWSLETTER_CHECKBOX', 'SUCCESS', {'action': 'checked'})
                        else:
                            log_automation_step(self.logger, 'NEWSLETTER_CHECKBOX', 'SUCCESS', {'action': 'already_checked'})
                        return
                except Exception:
                    pass
        except Exception as e:
            log_automation_step(self.logger, 'NEWSLETTER_CHECKBOX', 'ERROR', {'error': str(e)})

    async def _find_recaptcha_frames(self):
        """Temukan frame anchor (checkbox) dan bframe (challenge) reCAPTCHA jika ada."""
        anchor_frame = None
        challenge_frame = None
        try:
            for fr in self.page.frames:
                url = (fr.url or '').lower()
                if 'api2/anchor' in url or 'enterprise/anchor' in url:
                    anchor_frame = fr
                if 'api2/bframe' in url or 'enterprise/bframe' in url:
                    challenge_frame = fr
        except Exception:
            pass
        return (anchor_frame, challenge_frame)

    async def _scroll_to_recaptcha(self, max_steps: int=8, fast: bool=False, skip_fallback: bool=False) -> bool:
        """Auto-scroll halaman agar elemen reCAPTCHA (iframe/container) masuk viewport.
        Args:
            max_steps: jumlah langkah scroll incremental maksimum.
            fast: jika True, langsung lompat ke bawah terlebih dulu untuk mempercepat.
            skip_fallback: jika True, lewati PageDown/End fallback agar selesai seketika.
        Return True jika setelah scroll elemen terdeteksi, else False.
        """
        try:
            js = '''
            async (opts) => {
              const maxSteps = (opts && opts.maxSteps) || 20;
              const fast = !!(opts && opts.fast);
              const sel = "iframe[src*='api2/anchor'], iframe[src*='enterprise/anchor'], .g-recaptcha, [data-sitekey]";
              const exists = () => !!document.querySelector(sel);
              const center = () => {
                try {
                  const t = document.querySelector(sel);
                  t?.scrollIntoView({block:'center', inline:'center'});
                } catch(_){}
              };
              // Jika frame anchor sudah ada, anggap captcha sudah render
              try {
                const frs = Array.from(window.top.frames || []);
                for (const fr of frs) {
                  try {
                    const u = (fr.location?.href || '').toLowerCase();
                    if (u.includes('api2/anchor') || u.includes('enterprise/anchor')) { return true; }
                  } catch(_){}
                }
              } catch(_){}
              if (exists()) { center(); return true; }
              const uniq = (arr) => Array.from(new Set(arr.filter(Boolean)));
              const getScrollable = () => {
                const list = [];
                try { list.push(document.scrollingElement || document.documentElement || document.body); } catch(_){}
                const cand = Array.from(document.querySelectorAll('main, [role="main"], form, .container, [class*="container"], [class*="content"], [style*="overflow"], body'));
                for (const el of cand) {
                  try {
                    const cs = getComputedStyle(el);
                    const can = (el.scrollHeight > (el.clientHeight||0)+10) && /(auto|scroll)/i.test(cs.overflowY || cs.overflow || '');
                    if (can) list.push(el);
                  } catch(_){}
                }
                return uniq(list);
              };
              const scrollers = getScrollable();
              // Fast path: langsung ke bawah dulu
              if (fast) {
                try {
                  for (const el of scrollers){
                    try {
                      if (el === document.body || el === document.documentElement){
                        window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight || 999999);
                      } else {
                        el.scrollTop = el.scrollHeight;
                      }
                    } catch(_){}}
                  await new Promise(r=>setTimeout(r, 30));
                  if (exists()) { center(); return true; }
                } catch(_){}}
              for (let i=0; i<Math.max(1, maxSteps||20); i++){
                for (const el of scrollers){
                  try {
                    if (el === document.body || el === document.documentElement){
                      window.scrollBy(0, Math.round((window.innerHeight||600)*0.9));
                    } else if (el.scrollBy){
                      el.scrollBy(0, Math.round((el.clientHeight||400)*0.9));
                    } else {
                      el.scrollTop = Math.min(el.scrollTop + Math.round((el.clientHeight||400)*0.9), el.scrollHeight);
                    }
                  } catch(_){}
                }
                await new Promise(r=>setTimeout(r, 180));
                if (exists()) { center(); return true; }
              }
              // Paksa ke bawah
              for (const el of scrollers){ try { el.scrollTop = el.scrollHeight; } catch(_){} }
              await new Promise(r=>setTimeout(r, 200));
              if (exists()) { center(); return true; }
              return false;
            }
            '''
            
            ok = await self.page.evaluate(js, {'maxSteps': max_steps, 'fast': fast})
            
            if ok:
                log_automation_step(self.logger, 'CAPTCHA_SCROLL', 'FOUND')
            else:
                log_automation_step(self.logger, 'CAPTCHA_SCROLL', 'NOT_FOUND')
            
            if ok:
                return True
            
            if skip_fallback:
                return False
            
            try:
                await self.page.evaluate('try{document.activeElement && document.activeElement.blur()}catch(e){}')
            except Exception:
                pass
            
            sel = 'iframe[src*=\'api2/anchor\'], iframe[src*=\'enterprise/anchor\'], .g-recaptcha, [data-sitekey]'
            
            for _ in range(12):
                await self.page.keyboard.press('PageDown')
                await asyncio.sleep(0.15)
                el = await self.page.query_selector(sel)
                if el:
                    try:
                        await el.scroll_into_view_if_needed()
                    except Exception:
                        pass
                    log_automation_step(self.logger, 'CAPTCHA_SCROLL', 'FOUND_AFTER_PAGEDOWN')
                    return True
            
            try:
                await self.page.keyboard.press('End')
            except Exception:
                pass
            
            await asyncio.sleep(0.2)
            el = await self.page.query_selector(sel)
            if el:
                try:
                    await el.scroll_into_view_if_needed()
                except Exception:
                    pass
                log_automation_step(self.logger, 'CAPTCHA_SCROLL', 'FOUND_AFTER_END')
                return True
            
            return False
        except Exception as e:
            log_automation_step(self.logger, 'CAPTCHA_SCROLL', 'ERROR', {'error': str(e)})
            return False

    async def _click_recaptcha_checkbox(self) -> bool:
        """Klik checkbox reCAPTCHA di anchor frame. Return True jika checkbox terklik/solved."""
        try:
            try:
                await self._scroll_to_recaptcha(max_steps=5, fast=True, skip_fallback=True)
            except Exception:
                pass
            
            anchor_frame = None
            _challenge = None
            
            for _ in range(3):
                anchor_frame, _challenge = await self._find_recaptcha_frames()
                if anchor_frame:
                    break
                await asyncio.sleep(0.05)
            
            target = anchor_frame or self.page
            sel_candidates = ['#recaptcha-anchor', 'div[role=\'checkbox\'][aria-checked=\'false\']']
            
            for sel in sel_candidates:
                try:
                    el = await target.query_selector(sel)
                    if not el:
                        continue
                    
                    await el.scroll_into_view_if_needed()
                    await asyncio.sleep(0.6)
                    
                    try:
                        await el.click()
                    except Exception:
                        try:
                            await target.evaluate('e => e.click()', el)
                        except Exception:
                            continue
                    
                    await asyncio.sleep(0.2)
                    if await self._is_captcha_solved():
                        log_automation_step(self.logger, 'CAPTCHA_CHECK', 'CHECKBOX_CLICKED')
                        return True
                except Exception:
                    continue
            
            return False
        except Exception as e:
            log_automation_step(self.logger, 'CAPTCHA_CHECK', 'CHECKBOX_CLICK_ERROR', {'error': str(e)})
            return False

    async def _handle_captcha(self) -> bool:
        """Handle captcha dan pastikan terselesaikan sebelum lanjut.
        Returns True jika captcha tidak ada atau berhasil di-solve, False jika gagal."""
        log_automation_step(self.logger, 'CAPTCHA_CHECK', 'START')
        
        try:
            try:
                await self._scroll_to_recaptcha(max_steps=5, fast=True, skip_fallback=True)
            except Exception:
                pass
            
            captcha_selectors = [
                'iframe[title*=\'reCAPTCHA\']', 
                'iframe[src*=\'recaptcha\']', 
                '.g-recaptcha', 
                '[data-sitekey]', 
                '.captcha', 
                '.h-captcha'
            ]
            
            captcha_found = False
            for selector in captcha_selectors:
                if await self.page.query_selector(selector):
                    captcha_found = True
                    log_automation_step(self.logger, 'CAPTCHA_DETECTED', 'FOUND', {'selector': selector})
                    break
            
            if not captcha_found:
                log_automation_step(self.logger, 'CAPTCHA_CHECK', 'NOT_FOUND_AFTER_SCROLL')
                return True
            
            clicked = await self._click_recaptcha_checkbox()
            
            if clicked:
                if await self._is_captcha_solved():
                    return True
            
            if self.extension_mode:
                log_automation_step(self.logger, 'CAPTCHA_EXTENSION', 'EXTENSION_WAIT')
                ok = await self._wait_for_manual_captcha_solve(timeout=180)
                if ok:
                    log_automation_step(self.logger, 'CAPTCHA_EXTENSION', 'EXTENSION_SOLVED')
                    return True
                log_automation_step(self.logger, 'CAPTCHA_EXTENSION', 'EXTENSION_TIMEOUT')
                return False
            
            if self.captcha_solver:
                log_automation_step(self.logger, 'CAPTCHA_AUTO_SOLVE', 'START')
                await asyncio.sleep(0.5)
                solved = await self._solve_audio_captcha()
                await asyncio.sleep(0.5)
                if solved or await self._is_captcha_solved():
                    log_automation_step(self.logger, 'CAPTCHA_AUTO_SOLVE', 'SUCCESS')
                    return True
                log_automation_step(self.logger, 'CAPTCHA_AUTO_SOLVE', 'FAILED')
            
            log_automation_step(self.logger, 'CAPTCHA_MANUAL', 'WAITING')
            await self._wait_for_manual_captcha_solve()
            if await self._is_captcha_solved():
                log_automation_step(self.logger, 'CAPTCHA_MANUAL', 'COMPLETED')
                return True
            
            log_automation_step(self.logger, 'CAPTCHA_MANUAL', 'TIMEOUT')
            return False
        except Exception as e:
            log_automation_step(self.logger, 'CAPTCHA_CHECK', 'ERROR', {'error': str(e)})
            return False

    async def _wait_for_manual_captcha_solve(self, timeout: int=180) -> bool:
        """Tunggu user menyelesaikan captcha secara manual hingga timeout."""
        try:
            end = time.time() + timeout
            while time.time() < end:
                if await self._is_captcha_solved():
                    return True
                await asyncio.sleep(2)
            return False
        except Exception:
            return False

    async def _solve_audio_captcha(self) -> bool:
        """Solve audio captcha menggunakan speech recognition - AUDIO ONLY.
        Returns True jika captcha benar-benar solved, else False"""
        log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'START')
        try:
            max_attempts = 2
            attempt = 0
            
            while attempt < max_attempts:
                attempt += 1
                log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'ATTEMPT', {'attempt': attempt})
                
                _, challenge_frame = await self._find_recaptcha_frames()
                target = challenge_frame or self.page
                
                audio_button_selectors = [
                    'button[id=\'recaptcha-audio-button\']', 
                    'button[title*=\'audio\']', 
                    'button[aria-label*=\'audio\']', 
                    'button[aria-label*=\'Audio challenge\']', 
                    'button[aria-label*=\'audio challenge\']', 
                    '.rc-button-audio', 
                    '[role=\'button\']:has-text(\'audio\')', 
                    '[role=\'button\']:has-text(\'Audio\')'
                ]
                
                audio_clicked = False
                for selector in audio_button_selectors:
                    try:
                        element = await target.query_selector(selector)
                        if element:
                            await element.click()
                            await asyncio.sleep(0.5)
                            audio_clicked = True
                            log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'BUTTON_CLICKED', {'selector': selector})
                            break
                    except Exception:
                        pass
                
                if not audio_clicked:
                    raise Exception('Audio captcha button not found')
                
                audio_selectors = [
                    'audio#audio-source[src]', 
                    'audio[src]', 
                    '.rc-audiochallenge-tdownload-link audio[src]', 
                    '[src*=\'.mp3\']', 
                    '[src*=\'.wav\']', 
                    '[src*=\'audio\']'
                ]
                
                audio_element = None
                audio_src = None
                
                for selector in audio_selectors:
                    try:
                        audio_element = await target.wait_for_selector(selector, timeout=2500)
                        if audio_element:
                            audio_src = await audio_element.get_attribute('src')
                            if audio_src:
                                log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'AUDIO_FOUND', {'selector': selector})
                                break
                    except Exception:
                        pass
                
                if not audio_src:
                    link_selectors = [
                        'a.rc-audiochallenge-tdownload-link', 
                        '#rc-audio .rc-audiochallenge-tdownload a', 
                        'a[href*=\'payload/audio.mp3\']', 
                        'a[href*=\'audio\']'
                    ]
                    
                    for selector in link_selectors:
                        try:
                            link = await target.query_selector(selector)
                            if link:
                                href = await link.get_attribute('href')
                                if href:
                                    audio_src = href
                                    log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'AUDIO_LINK_FOUND', {'selector': selector})
                                    break
                        except Exception:
                            pass
                
                if audio_src and self.captcha_solver:
                    log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'DOWNLOADING', {'audio_url': audio_src[:50] + '...'})
                    audio_bytes = None
                    
                    def is_audio_resp(resp):
                        url = (resp.url or '').lower()
                        ctype = (resp.headers.get('content-type') or '').lower()
                        return ('recaptcha' in url and ('audio' in url or url.endswith('.mp3') or '.mp3' in url)) or ('audio/' in ctype)
                    
                    try:
                        resp = await self.page.wait_for_response(is_audio_resp, timeout=6000)
                        body = await resp.body()
                        if body:
                            audio_bytes = body
                            log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'CAPTURED_NETWORK', {'size': len(audio_bytes), 'url': resp.url[:80]})
                    except Exception as e:
                        log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'CAPTURE_NETWORK_FAILED', {'error': str(e)})
                    
                    if audio_bytes is None:
                        try:
                            b64 = await target.evaluate('''
                                async (url) => {
                                  try {
                                    const res = await fetch(url, { credentials: 'include' });
                                    const buf = await res.arrayBuffer();
                                    const bytes = new Uint8Array(buf);
                                    let bin = '';
                                    for (let i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
                                    return btoa(bin);
                                  } catch (e) { return null; }
                                }
                                ''', audio_src)
                            
                            if isinstance(b64, str) and b64:
                                decoded = base64.b64decode(b64)
                                if not audio_bytes:
                                    audio_bytes = decoded
                                log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'FETCHED_IN_FRAME', {'size': len(decoded)})
                        except Exception as e:
                            log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'FETCH_IN_FRAME_FAILED', {'error': str(e)})
                    
                    if audio_bytes is None:
                        try:
                            import requests
                            r = requests.get(audio_src, timeout=15)
                            if r.ok:
                                audio_bytes = r.content
                                log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'FETCHED_REQUESTS', {'size': len(audio_bytes)})
                        except Exception as e:
                            log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'FETCH_REQUESTS_FAILED', {'error': str(e)})
                    
                    if not audio_bytes:
                        log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'ERROR', {'error': 'Unable to download audio'})
                        return False
                    
                    fmt = 'mp3' if '.mp3' in (audio_src or '').lower() else 'wav'
                    result = self.captcha_solver.solve_audio_captcha_from_bytes(audio_bytes, format=fmt)
                    
                    if result:
                        log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'SOLVED', {'result': result})
                        
                        input_selectors = [
                            'input[id=\'audio-response\']', 
                            'input[name=\'audio-response\']', 
                            '.rc-audiochallenge-response-field', 
                            'input[type=\'text\']:visible', 
                            'input[placeholder*=\'hear\']', 
                            'input[aria-label*=\'audio\']'
                        ]
                        
                        input_filled = False
                        for selector in input_selectors:
                            try:
                                text_input = await target.query_selector(selector)
                                if text_input:
                                    await text_input.fill(result)
                                    await asyncio.sleep(0.5)
                                    input_filled = True
                                    log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'INPUT_FILLED', {'selector': selector})
                                    break
                            except Exception:
                                pass
                        
                        if input_filled:
                            submit_selectors = [
                                'button[id=\'recaptcha-verify-button\']', 
                                'button:has-text(\'Verify\')', 
                                'button:has-text(\'Submit\')', 
                                '.rc-audiochallenge-verify-button', 
                                'input[type=\'submit\']', 
                                'button[type=\'submit\']'
                            ]
                            
                            for selector in submit_selectors:
                                try:
                                    submit_btn = await target.query_selector(selector)
                                    if submit_btn:
                                        await submit_btn.click()
                                        await asyncio.sleep(1.0)
                                        if await self._is_captcha_solved():
                                            log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'SUCCESS', {'result': result, 'attempt': attempt})
                                            return True
                                except Exception:
                                    pass
                            
                            log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'ERROR', {'error': 'Submit button not found'})
                        else:
                            log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'ERROR', {'error': 'Text input field not found'})
                    else:
                        log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'ERROR', {'error': 'Could not solve audio captcha'})
                else:
                    log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'ERROR', {'error': 'Audio source not found or captcha solver not available'})
                    return False
                
                # If we get here, verification failed, try to reload
                log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'VERIFY_FAILED', {'attempt': attempt})
                
                reload_selectors = ['.rc-button-reload', 'button#recaptcha-reload-button', 'button[aria-label*=\'reload\']', 'button:has-text(\'Get a new challenge\')']
                
                for rs in reload_selectors:
                    try:
                        rb = await target.query_selector(rs)
                        if rb:
                            await rb.click()
                            log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'RELOAD_CLICKED', {'selector': rs})
                            break
                    except Exception:
                        pass
                
                await asyncio.sleep(1.0)
            
            return False
        except Exception as e:
            log_automation_step(self.logger, 'AUDIO_CAPTCHA', 'ERROR', {'error': str(e)})
            return False

    async def _is_captcha_solved(self) -> bool:
        """Deteksi apakah reCAPTCHA sudah tercentang atau token tersedia."""
        try:
            token = await self.page.evaluate('''
                try {
                  const t = document.querySelector('textarea#g-recaptcha-response, textarea[name="g-recaptcha-response"]');
                  return t && t.value ? t.value : '';
                } catch(e) { return ''; }
                ''')
        except Exception:
            token = ''
        
        if isinstance(token, str) and token.strip():
            return True
        
        try:
            for fr in self.page.frames:
                if 'recaptcha' in fr.url or 'google.com/recaptcha' in fr.url:
                    el = await fr.query_selector('#recaptcha-anchor[aria-checked=\'true\'], span.recaptcha-checkbox-checked[role=\'checkbox\']')
                    if el:
                        return True
        except Exception:
            pass
        
        try:
            rec_iframe = await self.page.query_selector('iframe[title*=\'reCAPTCHA\'], iframe[src*=\'recaptcha\']')
            return rec_iframe is None
        except Exception:
            return False

    async def _submit_form(self):
        """Submit registration form"""
        log_automation_step(self.logger, 'FORM_SUBMIT', 'START')
        try:
            if not await self._is_captcha_solved():
                raise Exception('Attempted to submit while CAPTCHA not solved')
            
            next_button = await self.page.query_selector('button[id=\'accountDetailsNext\']')
            if not next_button:
                next_button = await self.page.query_selector('button:has-text(\'Next\')')
            if not next_button:
                next_button = await self.page.query_selector('button[type=\'submit\']')
            
            if next_button:
                await next_button.click()
                await asyncio.sleep(2)
                log_automation_step(self.logger, 'FORM_SUBMIT', 'SUCCESS')
            else:
                raise Exception('Submit button not found')
        except Exception as e:
            log_automation_step(self.logger, 'FORM_SUBMIT', 'ERROR', {'error': str(e)})
            raise

    async def _wait_for_result(self) -> Dict:
        """Wait untuk hasil registrasi"""
        log_automation_step(self.logger, 'RESULT_WAITING', 'START')
        try:
            await self.page.wait_for_load_state('networkidle', timeout=30000)
            current_url = self.page.url
            
            if 'signup' not in current_url.lower():
                log_automation_step(self.logger, 'RESULT_WAITING', 'SUCCESS', {'url': current_url})
                return {'success': True, 'message': 'Registration completed', 'url': current_url}
            
            error_elements = await self.page.query_selector_all('.VfPpkd-CmumD-MZAGBe-SIawsf')
            if error_elements:
                error_messages = []
                for element in error_elements:
                    text = await element.inner_text()
                    if text.strip():
                        error_messages.append(text.strip())
                
                if error_messages:
                    error_msg = '; '.join(error_messages)
                    log_automation_step(self.logger, 'RESULT_WAITING', 'ERROR', {'errors': error_messages})
                    return {'success': False, 'error': error_msg}
            
            log_automation_step(self.logger, 'RESULT_WAITING', 'UNKNOWN')
            return {'success': False, 'error': 'Unknown result - still on signup page'}
        except Exception as e:
            log_automation_step(self.logger, 'RESULT_WAITING', 'ERROR', {'error': str(e)})
            return {'success': False, 'error': f'Error waiting for result: {str(e)}'}

    async def _cleanup(self):
        """Cleanup browser resources"""
        log_automation_step(self.logger, 'CLEANUP', 'START')
        errors = []
        
        try:
            if self.context:
                state_path_str = self.get_default_pw_state_path()
                try:
                    os.makedirs(os.path.dirname(state_path_str), exist_ok=True)
                except Exception:
                    pass
                
                try:
                    await self.context.storage_state(path=str(state_path_str))
                except Exception as e:
                    errors.append(f'storage_state: {e}')
        except Exception as e:
            errors.append(f'storage_state: {e}')
        
        try:
            if self.page:
                try:
                    if not self.page.is_closed():
                        await self.page.close()
                except Exception as e:
                    errors.append(f'page.close: {e}')
        except Exception as e:
            errors.append(f'page.check: {e}')
        
        try:
            if self.context:
                try:
                    await self.context.close()
                except Exception as e:
                    errors.append(f'context.close: {e}')
        except Exception as e:
            errors.append(f'context.check: {e}')
        
        try:
            if self.browser:
                try:
                    await self.browser.close()
                except Exception as e:
                    errors.append(f'browser.close: {e}')
        except Exception as e:
            errors.append(f'browser.check: {e}')
        
        if errors:
            log_automation_step(self.logger, 'CLEANUP', 'PARTIAL', {'details': errors[:5]})
        else:
            log_automation_step(self.logger, 'CLEANUP', 'SUCCESS')

if __name__ == '__main__':
    test_data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com', 'company': 'TechCorp', 'password': 'SecurePass123!'}
    automation = CloudSkillAutomation(headless=False)
    result = automation.register_account(test_data)
    print(f'Registration result: {result}')