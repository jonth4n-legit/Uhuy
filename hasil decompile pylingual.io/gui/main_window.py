"""
Main window untuk aplikasi Auto Cloud Skill Registration
"""
import tkinter as tk
from tkinter import messagebox, filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import threading
import time
from datetime import datetime
from typing import Dict, Optional
import tempfile
from pathlib import Path
import sys

from services.randomuser_service import RandomUserService
from services.firefox_relay_service import FirefoxRelayService
from services.captcha_service import CaptchaSolverService
from utils.logger import setup_logger, log_user_action
from config.settings import settings
from gui.tabs.video_generator_tab import VideoGeneratorTab
from gui.tabs.registration_tab import RegistrationTab
from gui.tabs.settings_tab import SettingsTab
from gui.tabs.logs_tab import LogsTab
from gui.tabs.about_tab import AboutTab
from config.licensing import ensure_license


class MainWindow:
    """Main window aplikasi"""

    def __init__(self):
        self.logger = setup_logger('MainWindow')
        self.random_user_service = RandomUserService()
        self.captcha_service = CaptchaSolverService()
        try:
            self.firefox_relay_service = FirefoxRelayService()
        except Exception as e:
            self.firefox_relay_service = None
            self.logger.warning(f'Firefox Relay service not available: {e}')

        self.automation = None
        self.root = ttk.Window(title='Auto Cloud Skill', themename='darkly', size=(650, 600), resizable=(True, True))
        try:
            self.set_app_icon()
        except Exception:
            pass
        self.center_window()
        self.setup_variables()
        # Load persisted temp values
        try:
            key = self._load_relay_key_from_temp()
            if key:
                self.firefox_api_key_var.set(key)
        except Exception:
            pass
        try:
            gcred = self._load_gmail_cred_path_from_temp()
            if gcred:
                self.gmail_credentials_path_var.set(gcred)
        except Exception:
            pass
        try:
            lab = self._load_lab_url_from_temp()
            if lab:
                self.lab_url_var.set(lab)
        except Exception:
            pass
        try:
            v = self._load_auto_start_lab_from_temp()
            if v is not None:
                self.auto_start_lab_var.set(bool(v))
        except Exception:
            pass
        try:
            v = self._load_recaptcha_extension_from_temp()
            if v is not None:
                self.extension_mode_var.set(bool(v))
        except Exception:
            pass

        self.build_ui()
        try:
            self.lab_url_var.trace_add('write', lambda *a: self._save_lab_url_to_temp(self.lab_url_var.get()))
            self.auto_start_lab_var.trace_add('write', lambda *a: self._save_auto_start_lab_to_temp(bool(self.auto_start_lab_var.get())))
            self.extension_mode_var.trace_add('write', lambda *a: self._save_recaptcha_extension_to_temp(bool(self.extension_mode_var.get())))
        except Exception:
            pass
        try:
            self.update_gmail_status_label()
        except Exception:
            pass
        try:
            self.root.after(200, self.auto_init_firefox_relay_from_temp)
        except Exception:
            pass

        self.is_running = False
        self._genai_api_key_event = threading.Event()
        self._latest_genai_api_key: Optional[str] = None
        self.root.after(500, self.auto_generate_initial_data)
        try:
            self.root.after(200, self.check_and_apply_license_async)
        except Exception:
            pass
        log_user_action(self.logger, 'APPLICATION_START')

    def center_window(self):
        """Center window di layar"""
        self.root.update_idletasks()
        width = self.root.winfo_width() or 650
        height = self.root.winfo_height() or 600
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = max(0, (sw - width) // 2)
        y = max(0, (sh - height) // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def set_app_icon(self):
        """Set icon aplikasi dari assets/logo.ico atau assets/logo.png."""
        base_dir = self._resolve_base_dir()
        assets_dir = base_dir / 'assets'
        ico_path = assets_dir / 'logo.ico'
        png_path = assets_dir / 'logo.png'
        set_ok = False
        try:
            if ico_path.exists():
                try:
                    self.root.iconbitmap(default=str(ico_path))
                    set_ok = True
                    self.logger.info(f'App icon (.ico) applied: {ico_path}')
                except Exception:
                    pass
            if png_path.exists():
                try:
                    img = tk.PhotoImage(file=str(png_path))
                    self._icon_image = img  # keep reference
                    self.root.iconphoto(True, self._icon_image)
                    set_ok = True
                    self.logger.info(f'App icon (.png) applied via iconphoto: {png_path}')
                except Exception:
                    pass
            if not set_ok:
                self.logger.warning('App icon not set: assets/logo.ico or assets/logo.png not found or failed to load.')
        except Exception:
            return

    def _resolve_base_dir(self) -> Path:
        """Base directory untuk akses assets, kompatibel dengan PyInstaller."""
        base = getattr(sys, '_MEIPASS', None)
        if base:
            return Path(base)
        return Path(__file__).resolve().parent.parent

    def setup_variables(self):
        """Setup tkinter variables"""
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.company_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.password_confirm_var = tk.StringVar()
        self.firefox_api_key_var = tk.StringVar()
        self.extension_mode_var = tk.BooleanVar(value=False)
        self.gmail_credentials_path_var = tk.StringVar()
        self.gmail_auth_url_var = tk.StringVar()
        self.gmail_auth_code_var = tk.StringVar()
        self._gmail_oauth_flow = None
        self.show_password_var = tk.BooleanVar(value=False)
        self.status_var = tk.StringVar(value='Initializing...')
        self.data_generated = False
        self.lab_url_var = tk.StringVar()
        self.auto_start_lab_var = tk.BooleanVar(value=False)

    def build_ui(self):
        """Build user interface"""
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=BOTH, expand=True)

        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=BOTH, expand=True)

        self.video_tab = VideoGeneratorTab(self.root, notebook, self.log_message, self.request_new_api_key_and_wait)
        self.settings_tab = SettingsTab(self, notebook)
        self.logs_tab = LogsTab(self, notebook)
        self.registration_tab = RegistrationTab(self, notebook)
        self.about_tab = AboutTab(self, notebook)

        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill=X, pady=(10, 0))

        status_frame = ttk.Frame(bottom_frame)
        status_frame.pack(fill=X, pady=(0, 10))
        ttk.Label(status_frame, text='Status:', bootstyle=INFO).pack(side=LEFT)
        status_label = ttk.Label(status_frame, textvariable=self.status_var, bootstyle=SUCCESS)
        status_label.pack(side=LEFT, padx=(5, 0))

        button_frame = ttk.Frame(bottom_frame)
        button_frame.pack(fill=X)
        ttk.Button(button_frame, text='Refresh Data', command=self.refresh_generated_data, bootstyle=INFO, width=15).pack(side=LEFT, padx=(0, 5))
        self.start_btn = ttk.Button(button_frame, text='Start Registration', command=self.start_automation, bootstyle=SUCCESS, width=20, state=DISABLED)
        self.start_btn.pack(side=LEFT, padx=5)
        self.stop_btn = ttk.Button(button_frame, text='Stop', command=self.stop_automation, bootstyle=DANGER, width=15, state=DISABLED)
        self.stop_btn.pack(side=LEFT, padx=5)
        ttk.Button(button_frame, text='Exit', command=self.on_closing, bootstyle=DANGER, width=15).pack(side=RIGHT)

    def create_video_generator_tab(self, notebook):
        try:
            self.video_tab = VideoGeneratorTab(self.root, notebook, self.log_message, self.request_new_api_key_and_wait)
        except Exception as e:
            self.log_message(f'🛑 Gagal memuat Video Generator tab: {e}')

    def set_genai_api_key(self, key: str):
        """Terima API key hasil proses create API key dan teruskan ke tab Video Generator."""
        try:
            if hasattr(self, 'video_tab') and self.video_tab:
                self.video_tab.set_api_key(key)
                self.log_message('⏳ GenAI API key diteruskan ke Video Generator tab.')
                self._latest_genai_api_key = (key or '').strip()
                self._genai_api_key_event.set()
            else:
                self.log_message('⚠️ Video Generator tab belum terinisialisasi; API key belum dapat diatur.')
        except Exception as e:
            self.log_message(f'🛑 Gagal menerapkan GenAI API key: {e}')

    def request_new_api_key_and_wait(self, reason: str, timeout_seconds: int = 600) -> Optional[str]:
        """Minta proses registrasi ulang untuk mendapatkan API key baru dan tunggu atau timeout."""
        try:
            self._genai_api_key_event.clear()
            self._latest_genai_api_key = None
            self.root.after(0, lambda: self.log_message(f'⏸️ Pausing generation at Video tab: {reason}. Re-registering to obtain new API key...'))
            self.root.after(0, self.refresh_generated_data)
            self.root.after(0, self.start_automation)
            ok = self._genai_api_key_event.wait(timeout=max(1, int(timeout_seconds)))
            if ok:
                return self._latest_genai_api_key
            self.root.after(0, lambda: self.log_message('🛑 Timeout waiting for new GenAI API key.'))
        except Exception as e:
            self.root.after(0, lambda: self.log_message(f'🛑 request_new_api_key_and_wait error: {e}'))
        return None

    def toggle_password_visibility(self):
        try:
            show_char = '' if self.show_password_var.get() else '*'
            if hasattr(self, 'password_entry') and self.password_entry:
                self.password_entry.config(show=show_char)
            if hasattr(self, 'password_confirm_entry') and self.password_confirm_entry:
                self.password_confirm_entry.config(show=show_char)
        except Exception as e:
            self.log_message(f'⚠️ Toggle password visibility error: {e}')

    def copy_password(self):
        try:
            pwd = self.password_var.get()
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            self.log_message('ℹ️ Password copied to clipboard.')
        except Exception as e:
            self.log_message(f'🛑 Copy password error: {e}')

    def auto_init_firefox_relay_from_temp(self):
        key = (self.firefox_api_key_var.get() or '').strip()
        if not key:
            return

        def _worker():
            try:
                svc = FirefoxRelayService(api_key=key)
                self.log_message('✅ Detected Firefox Relay API key from temp. Validating...')
                results = svc.test_connection()
                if results.get('success'):
                    def _on_ok():
                        self.firefox_relay_service = svc
                        try:
                            self.firefox_status_label.config(text='Firefox Relay: ✅ Connected', bootstyle=SUCCESS)
                        except Exception:
                            pass
                        self.log_message('✅ Firefox Relay API key is valid (auto).')
                        self.log_message(f"✅ Using URL: {results.get('working_url', 'N/A')}")
                        try:
                            self.status_var.set('Ready')
                        except Exception:
                            pass
                        if self.data_generated:
                            try:
                                self.start_btn.config(state=NORMAL)
                            except Exception:
                                pass
                    self.root.after(0, _on_ok)
                else:
                    def _on_fail():
                        try:
                            self.firefox_status_label.config(text='Firefox Relay: 🛑 Invalid API Key', bootstyle=DANGER)
                        except Exception:
                            pass
                        self.log_message('⚠️ Auto-validate API key failed. Please click \"Test API Key\".')
                    self.root.after(0, _on_fail)
            except Exception as e:
                self.root.after(0, lambda: self.log_message(f'⚠️ Auto-init Relay failed: {e}'))
        threading.Thread(target=_worker, daemon=True).start()

    def start_gmail_progress(self, total_sec: int, interval_sec: int):
        try:
            self.gmail_poll_total = max(1, int(total_sec))
            self.gmail_poll_interval = max(1, int(interval_sec))
            self.gmail_poll_start = time.time()
            self.gmail_progress_running = True
            self.gmail_progress.configure(maximum=self.gmail_poll_total, value=0)
            self.gmail_progress_container.pack(fill=X, pady=(8, 0))
            self._update_gmail_progress()
        except Exception as e:
            self.log_message(f'⚠️ Could not start Gmail progress: {e}')

    def _update_gmail_progress(self):
        if not getattr(self, 'gmail_progress_running', False):
            return
        now = time.time()
        elapsed = int(now - getattr(self, 'gmail_poll_start', now))
        total = int(getattr(self, 'gmail_poll_total', 1))
        interval = int(getattr(self, 'gmail_poll_interval', 5))
        remaining = max(0, total - elapsed)
        attempt = max(0, (elapsed // max(1, interval))) + 1
        try:
            self.gmail_progress.configure(value=min(total, elapsed))
            self.gmail_progress_label.config(text=f'Gmail polling attempt={attempt} remaining={remaining}s')
        except Exception:
            pass
        if elapsed < total and self.gmail_progress_running:
            self.gmail_progress_job = self.root.after(500, self._update_gmail_progress)
        else:
            self.stop_gmail_progress()

    def stop_gmail_progress(self):
        self.gmail_progress_running = False
        if getattr(self, 'gmail_progress_job', None):
            try:
                self.root.after_cancel(self.gmail_progress_job)
            except Exception:
                pass
            self.gmail_progress_job = None
        try:
            self.gmail_progress_container.pack_forget()
        except Exception:
            pass

    def auto_generate_initial_data(self):
        self.log_message('✅ Auto-generating initial data...')
        self.status_var.set('Generating data...')
        try:
            user_data = self.random_user_service.get_random_user(gender=settings.DEFAULT_GENDER, nationalities=settings.DEFAULT_NATIONALITIES)
            if not user_data:
                raise Exception('Failed to get random user data')
            self.first_name_var.set(user_data.get('first_name', ''))
            self.last_name_var.set(user_data.get('last_name', ''))
            company = self.random_user_service.generate_company_name()
            self.company_var.set(company)
            password = self.random_user_service.generate_password(settings.DEFAULT_PASSWORD_LENGTH)
            self.password_var.set(password)
            self.password_confirm_var.set(password)
            self.email_var.set('Will be generated from Firefox Relay')
            self.log_message('✅ Initial data generated successfully!')
            self.log_message('✅ Email akan dibuat otomatis dari Firefox Relay saat registrasi')
            if getattr(self, 'firefox_relay_service', None):
                self.status_var.set('Ready')
                self.update_start_button_state()
            else:
                self.status_var.set('Ready - Please set Firefox Relay API Key')
            self.data_generated = True
            self.update_start_button_state()
            log_user_action(self.logger, 'AUTO_GENERATE_DATA', {
                'first_name': user_data.get('first_name', ''),
                'last_name': user_data.get('last_name', ''),
                'company': company,
            })
        except Exception as e:
            error_msg = f'Error generating initial data: {str(e)}'
            self.log_message(f'🛑 {error_msg}')
            self.status_var.set('Error generating data')

    def refresh_generated_data(self):
        self.log_message('🔄️ Refreshing data...')
        self.status_var.set('Refreshing...')
        self.auto_generate_initial_data()

    def test_firefox_api_key(self):
        api_key = self.firefox_api_key_var.get().strip()
        if not api_key:
            messagebox.showwarning('Warning', 'Please enter Firefox Relay API key first')
            return
        self.log_message('⏳ Testing Firefox Relay API key...')
        self.log_message('⚙️ Trying different authentication formats...')
        try:
            test_service = FirefoxRelayService(api_key=api_key)
            results = test_service.test_connection()
            if results.get('success'):
                self.firefox_status_label.config(text='Firefox Relay: ✅ Connected', bootstyle=SUCCESS)
                self.log_message('✅ Firefox Relay API key is valid!')
                self.log_message(f"✅ Using URL: {results.get('working_url', 'N/A')}")
                self.log_message(f"⏳ Auth format: {results.get('auth_format', 'N/A')}")
                self.log_message(f"🔊 Found {results.get('masks_count', 0)} existing email masks")
                self.firefox_relay_service = test_service
                try:
                    self._save_relay_key_to_temp(api_key)
                    self.log_message('📩 Firefox Relay API key saved to temp.')
                except Exception as e:
                    self.log_message(f'⚠️ Could not save API key to temp: {e}')
                if self.data_generated:
                    self.status_var.set('Ready')
                    self.update_start_button_state()
                messagebox.showinfo('Success', f"Firefox Relay API key is valid!\nURL: {results.get('working_url', 'N/A')}\nAuth: {results.get('auth_format', 'N/A')}\nExisting masks: {results.get('masks_count', 0)}")
            else:
                self.firefox_status_label.config(text='Firefox Relay: 🛑 Invalid API Key', bootstyle=DANGER)
                error_msg = results.get('error', 'Unknown error')
                self.log_message(f'🛑 Firefox Relay API key test failed: {error_msg}')
                messagebox.showerror('Error', f'API key test failed:\n{error_msg}')
        except Exception as e:
            self.firefox_status_label.config(text='Firefox Relay: 🛑 Connection Error', bootstyle=DANGER)
            self.log_message(f'🛑 Firefox Relay connection error: {str(e)}')
            messagebox.showerror('Error', f'Connection error:\n{str(e)}')

    def delete_all_firefox_masks(self):
        api_key = self.firefox_api_key_var.get().strip()
        if not api_key:
            messagebox.showwarning('Warning', 'Masukkan Firefox Relay API key terlebih dahulu')
            return
        if not self.firefox_relay_service:
            try:
                self.firefox_relay_service = FirefoxRelayService(api_key=api_key)
            except Exception as e:
                messagebox.showerror('Error', f'Gagal inisialisasi service:\n{e}')
                return
        if not messagebox.askyesno('Confirm', 'Yakin ingin menghapus SEMUA email masks? Tindakan ini tidak dapat dibatalkan.'):
            return
        self.log_message('🛑 Deleting all Firefox Relay masks...')
        try:
            result = self.firefox_relay_service.delete_all_masks()
            requested = result.get('requested', 0)
            deleted = result.get('deleted', 0)
            failed = len(result.get('failed_ids', []))
            self.log_message(f'✅ Delete summary: requested={requested}, deleted={deleted}, failed={failed}')
            messagebox.showinfo('Delete All Masks', f'Requested: {requested}\nDeleted: {deleted}\nFailed: {failed}')
        except Exception as e:
            self.log_message(f'🛑 Delete all masks error: {e}')
            messagebox.showerror('Error', f'Delete error:\n{e}')

    def start_automation(self):
        if self.is_running:
            return
        if not self.firefox_relay_service:
            api_key = (self.firefox_api_key_var.get() or '').strip()
            if not api_key:
                messagebox.showerror('Error', 'Please set and test Firefox Relay API key first!')
                return
            try:
                self.firefox_relay_service = FirefoxRelayService(api_key=api_key)
                try:
                    self.firefox_status_label.config(text='Firefox Relay: ⏳ Connecting...', bootstyle=INFO)
                except Exception:
                    pass
            except Exception as e:
                messagebox.showerror('Error', f'Failed to initialize Firefox Relay service:\n{e}')
                return
        try:
            purge_res = self.firefox_relay_service.auto_purge_if_limit_reached(limit=5)
            if purge_res.get('purged'):
                self.log_message(f"🧹 Auto purge masks triggered: requested={purge_res.get('requested', 0)}, deleted={purge_res.get('deleted', 0)}, failed={len(purge_res.get('failed_ids', []))}")
            else:
                self.log_message(f"ℹ️ Current masks count: {purge_res.get('count', 'N/A')}")
        except Exception as e:
            self.log_message(f'⚠️ Auto purge check failed: {e}')
        self.log_message('🔊 Creating Firefox Relay email...')
        self.status_var.set('Creating email...')
        try:
            mask = self.firefox_relay_service.create_relay_mask(f"Auto registration - {datetime.now().strftime('%Y%m%d_%H%M%S')}")
            if not mask:
                raise Exception('Failed to create Firefox Relay email')
            relay_email = mask.get('full_address') or mask.get('address')
            self.email_var.set(relay_email or '')
            self.log_message(f'✅ Created relay email: {relay_email}')
        except Exception as e:
            error_msg = f'Failed to create relay email: {str(e)}'
            self.log_message(f'🛑 {error_msg}')
            messagebox.showerror('Error', error_msg)
            return

        user_data = {
            'first_name': self.first_name_var.get().strip(),
            'last_name': self.last_name_var.get().strip(),
            'email': self.email_var.get().strip(),
            'company': self.company_var.get().strip(),
            'password': self.password_var.get(),
            'password_confirm': self.password_confirm_var.get(),
        }
        if not user_data['first_name'] or not user_data['last_name']:
            messagebox.showerror('Error', 'First name and last name are required!')
            return
        if user_data['password'] != user_data['password_confirm']:
            messagebox.showerror('Error', 'Password confirmation tidak cocok!')
            return

        self.is_running = True
        self.start_btn.config(state=DISABLED)
        self.stop_btn.config(state=NORMAL)
        self.status_var.set('Running...')
        self.log_message('▶️ Starting automation...')
        thread = threading.Thread(target=self.run_automation, args=(user_data,), daemon=True)
        thread.start()

    def run_automation(self, user_data: Dict):
        try:
            try:
                from automation.cloudskill_automation import CloudSkillAutomation
                from services.gmail_service import GmailService
            except Exception as e:  # import issues shouldn't crash the UI thread
                self.log_message(f'⚠️ Import error for automation services: {e}')
                self.root.after(0, self.automation_finished)
                return

            cred_path = self.gmail_credentials_path_var.get().strip()
            project_root = Path(__file__).resolve().parent.parent
            token_default = project_root / 'token.json'
            token_exists = token_default.exists()
            gmail_ready = bool(cred_path) or token_exists
            keep_open = gmail_ready

            self.automation = CloudSkillAutomation(
                headless=bool(settings.PLAYWRIGHT_HEADLESS),
                captcha_solver=self.captcha_service,
                keep_browser_open=keep_open,
                extension_mode=bool(self.extension_mode_var.get()),
            )
            result = self.automation.register_account(user_data)
            if result.get('success'):
                self.log_message('✅ Registration completed successfully!')
                self.root.after(0, lambda: self.status_var.set('Registration completed'))
                if gmail_ready:
                    try:
                        self.log_message('⏳ Checking Gmail inbox for confirmation email...')
                        svc = GmailService(credentials_path=cred_path) if cred_path else GmailService()
                        timeout_sec = 180
                        poll_interval_sec = 5
                        self.root.after(0, lambda: self.start_gmail_progress(timeout_sec, poll_interval_sec))
                        msg = svc.wait_for_email(
                            target_email=user_data.get('email', ''),
                            subject_contains='Welcome to Google Cloud Skills Boost',
                            from_contains='noreply@cloudskillsboost.google',
                            timeout_sec=timeout_sec,
                            poll_interval_sec=poll_interval_sec,
                        )
                    finally:
                        self.root.after(0, self.stop_gmail_progress)
                    if msg:
                        links = svc.extract_links(msg)
                        self.log_message(f"✅ Confirmation email found. Links: {(links[:3] if links else 'No links found')}")
                        if links:
                            chosen = None
                            notif_link = None
                            cloud_link = None
                            for u in links:
                                ul = (u or '').lower()
                                if 'notifications.googleapis.com/email/redirect' in ul:
                                    notif_link = u
                                    break
                            if not notif_link:
                                for u in links:
                                    ul = (u or '').lower()
                                    if 'cloudskillsboost.google' in ul or '/users/confirmation' in ul or 'confirm' in ul:
                                        cloud_link = u
                                        break
                            chosen = notif_link or cloud_link or (links[0] if links else None)
                            if chosen:
                                self.log_message(f'ℹ️ Opening confirmation link: {chosen}')
                                confirm_result = self.automation.confirm_via_link(chosen, user_data.get('password', ''), user_data.get('email', ''))
                                if confirm_result.get('success'):
                                    self.log_message('✅ Confirmation link processed successfully.')
                                    lab_url = (self.lab_url_var.get() or '').strip()
                                    if self.auto_start_lab_var.get() and lab_url:
                                        self.log_message('▶️ Starting lab (auto)')
                                        result_lab = self.automation.start_lab(lab_url)
                                        if result_lab.get('success'):
                                            self.log_message(f"✅ Lab started successfully. URL: {result_lab.get('url')}")
                                            api_key_val = (result_lab.get('api_key') or '').strip()
                                            if api_key_val:
                                                self.root.after(0, lambda k=api_key_val: self.set_genai_api_key(k))
                                                self.log_message('Received GenAI API key from Lab. Injected to Video Generator tab.')
                                        else:
                                            self.log_message(f"⚠️ Start Lab failed: {result_lab.get('error')}")
                                else:
                                    self.log_message(f"⚠️ Confirmation processing failed: {confirm_result.get('error')}")
                    else:
                        self.log_message('🛑 No matching email arrived within timeout.')
                else:
                    self.log_message('🛑 Gmail not configured (no credentials or token). Skipping email confirmation check.')
            else:
                self.log_message(f"🛑 Automation error: {result.get('error')}")
                self.root.after(0, lambda: self.status_var.set('Error'))
        except Exception as e:
            self.log_message(f'🛑 Automation error: {str(e)}')
            self.root.after(0, lambda: self.status_var.set('Error'))
        finally:
            self.root.after(0, self.automation_finished)

    def update_gmail_status_label(self):
        try:
            project_root = Path(__file__).resolve().parent.parent
            token_default = project_root / 'token.json'
            try:
                from services.gmail_service import GmailService
                token_local = Path(GmailService.get_default_token_path())
            except Exception:
                token_local = Path('')
            cred_path = (self.gmail_credentials_path_var.get() or '').strip()
            token_exists = (token_local.exists() if str(token_local) else False) or token_default.exists()
            if not token_exists and cred_path:
                cpath = Path(cred_path)
                token_alt = cpath.parent / 'token.json'
                token_exists = token_alt.exists()
            if token_exists:
                self.gmail_status_label.config(text='Gmail: ✅ Ready (token found)', bootstyle=SUCCESS)
            elif cred_path:
                self.gmail_status_label.config(text='Gmail: ✅ Credentials set (authenticate to enable)', bootstyle=INFO)
            else:
                self.gmail_status_label.config(text='Gmail: 🛑 Not configured', bootstyle=WARNING)
        except Exception:
            pass

    def stop_automation(self):
        self.log_message('⛔ Stopping automation...')
        self.is_running = False
        self.automation_finished()

    def automation_finished(self):
        self.is_running = False
        self.update_start_button_state()
        try:
            self.stop_btn.config(state=DISABLED)
        except Exception:
            pass
        if self.status_var.get() in ['Running...', 'Error']:
            self.status_var.set('Ready')

    def check_and_apply_license_async(self):
        def _worker():
            try:
                res = ensure_license()
            except Exception as e:
                res = {'is_allowed': False, 'plan': None, 'status': 'error', 'reason': str(e)}

            def _apply():
                self.license_info = res
                try:
                    if hasattr(self, 'license_plan_var'):
                        self.license_plan_var.set(str(res.get('plan') or 'Unknown'))
                    exp = res.get('expiresAt')
                    disp = 'Unknown'
                    try:
                        if isinstance(exp, str) and exp:
                            dt = datetime.fromisoformat(exp.replace('Z', '+00:00'))
                            disp = dt.strftime('%d/%m/%Y')
                    except Exception:
                        pass
                    if hasattr(self, 'license_expiry_var'):
                        self.license_expiry_var.set(disp)
                except Exception:
                    pass
                plan = str(res.get('plan') or '').lower()
                if plan == 'free':
                    self.log_message("🔒 License plan is 'free'.")
                else:
                    if not res.get('is_allowed', True):
                        self.log_message(f"🔒 License not allowed: {res.get('reason', 'unknown')}")
                    else:
                        self.log_message('🔓 License valid.')
                self.update_start_button_state()

            try:
                self.root.after(0, _apply)
            except Exception:
                pass
        threading.Thread(target=_worker, daemon=True).start()

    def update_start_button_state(self):
        try:
            allowed = True
            info = getattr(self, 'license_info', None)
            if info is not None:
                plan = str(info.get('plan') or '').lower()
                allowed = bool(info.get('is_allowed', True)) and plan != 'free'
            state = NORMAL if allowed and self.data_generated and (not self.is_running) else DISABLED
            self.start_btn.config(state=state)
        except Exception:
            pass

    def log_message(self, message: str):
        timestamp = datetime.now().strftime('%H:%M:%S')
        log_entry = f'[{timestamp}] {message}\n'
        try:
            self.log_text.insert(tk.END, log_entry)
            self.log_text.see(tk.END)
        except Exception:
            pass
        self.logger.info(message)

    def clear_logs(self):
        try:
            self.log_text.delete('1.0', tk.END)
            self.log_message('Logs cleared')
        except Exception:
            pass

    def save_logs(self):
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension='.txt',
                filetypes=[('Text files', '*.txt'), ('All files', '*.*')],
                title='Save Logs',
            )
            if filename:
                content = self.log_text.get('1.0', tk.END)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.log_message(f'Logs saved to: {filename}')
                messagebox.showinfo('Success', f'Logs saved to:\n{filename}')
        except Exception as e:
            error_msg = f'Error saving logs: {str(e)}'
            self.log_message(f'🛑 {error_msg}')
            messagebox.showerror('Error', error_msg)

    def browse_gmail_credentials(self):
        try:
            filename = filedialog.askopenfilename(
                title='Select Gmail credentials.json',
                filetypes=[('JSON files', '*.json'), ('All files', '*.*')],
            )
            if filename:
                self.gmail_credentials_path_var.set(filename)
                self.log_message(f'✅ Gmail credentials set: {filename}')
                try:
                    self._save_gmail_cred_path_to_temp(filename)
                except Exception:
                    pass
                self.update_gmail_status_label()
        except Exception as e:
            self.log_message(f'🛑 Error selecting Gmail credentials: {e}')

    def generate_gmail_auth_url(self):
        try:
            cred_path = self.gmail_credentials_path_var.get().strip()
            if not cred_path:
                messagebox.showwarning('Gmail', 'Silakan pilih credentials.json terlebih dahulu.')
                return
            self.gmail_auth_code_var.set('')
            self.gmail_auth_url_var.set('')
            from google_auth_oauthlib.flow import InstalledAppFlow
            from services.gmail_service import SCOPES
            self._gmail_oauth_flow = InstalledAppFlow.from_client_secrets_file(cred_path, SCOPES)
            self._gmail_oauth_flow.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
            auth_url, _ = self._gmail_oauth_flow.authorization_url(
                access_type='offline', include_granted_scopes='true', prompt='consent'
            )
            self.gmail_auth_url_var.set(auth_url)
            self.log_message('ℹ️ Gmail Auth URL generated. Copy URL and authenticate in your browser.')
        except Exception as e:
            self.log_message(f'🛑 Failed to generate Gmail Auth URL: {e}')

    def copy_gmail_auth_url(self):
        try:
            url = self.gmail_auth_url_var.get().strip()
            if not url:
                return
            self.root.clipboard_clear()
            self.root.clipboard_append(url)
            self.log_message('ℹ️ Auth URL copied to clipboard.')
        except Exception as e:
            self.log_message(f'🛑 Clipboard error: {e}')

    def complete_gmail_auth_async(self):
        code = self.gmail_auth_code_var.get().strip()
        if not code:
            messagebox.showwarning('Gmail', 'Silakan paste verification code terlebih dahulu.')
            return
        t = threading.Thread(target=self.complete_gmail_auth, args=(code,), daemon=True)
        t.start()

    def complete_gmail_auth(self, code: str):
        try:
            if not self._gmail_oauth_flow:
                self.root.after(0, lambda: messagebox.showwarning('Gmail', "Silakan klik 'Get Auth URL' terlebih dahulu."))
                return
            self._gmail_oauth_flow.fetch_token(code=code)
            creds = self._gmail_oauth_flow.credentials
            from services.gmail_service import GmailService
            cred_path = self.gmail_credentials_path_var.get().strip()
            svc = GmailService(credentials_path=cred_path)
            token_path = svc.token_path
            saved_ok = False
            import os as _os
            try:
                _os.makedirs(_os.path.dirname(token_path), exist_ok=True)
                with open(token_path, 'w', encoding='utf-8') as f:
                    f.write(creds.to_json())
                saved_ok = True
            except Exception as e:
                self.root.after(0, lambda: self.log_message(f'⚠️ Could not save token: {e}'))
            if cred_path:
                try:
                    self._save_gmail_cred_path_to_temp(cred_path)
                except Exception:
                    pass
            if saved_ok:
                self.root.after(0, lambda: self.log_message('✅ Gmail authenticated (manual) and token stored.'))
                self.root.after(0, lambda: messagebox.showinfo('Gmail', 'Authentication berhasil. Token disimpan untuk run berikutnya.'))
            else:
                self.root.after(0, lambda: messagebox.showwarning('Gmail', "Authentication berhasil, tetapi token tidak dapat disimpan. Coba ulangi atau jalankan proses 'Authenticate' (bukan manual code)."))
            self.root.after(0, self.update_gmail_status_label)
        except Exception as e:
            self.root.after(0, lambda: self.log_message(f'🛑 Complete Gmail auth error: {e}'))
            self.root.after(0, lambda: messagebox.showerror('Gmail', f'Authentication gagal:\n{e}'))

    def authenticate_gmail_async(self):
        cred_path = self.gmail_credentials_path_var.get().strip()
        if not cred_path:
            messagebox.showwarning('Gmail', 'Silakan pilih credentials.json terlebih dahulu.')
            return
        self.log_message('⏳ Starting Gmail OAuth authentication...')
        t = threading.Thread(target=self.authenticate_gmail, args=(cred_path,), daemon=True)
        t.start()

    def authenticate_gmail(self, cred_path: str):
        try:
            from services.gmail_service import GmailService
            svc = GmailService(credentials_path=cred_path)
            service = svc.get_service()
            _ = service.users().labels().list(userId='me').execute()
            if cred_path:
                try:
                    self._save_gmail_cred_path_to_temp(cred_path)
                except Exception:
                    pass
            self.root.after(0, lambda: self.log_message('✅ Gmail authenticated and token stored.'))
            self.root.after(0, lambda: messagebox.showinfo('Gmail', 'Authentication berhasil. Token disimpan untuk run berikutnya.'))
            self.root.after(0, self.update_gmail_status_label)
        except Exception as e:
            self.root.after(0, lambda: self.log_message(f'🛑 Gmail authentication error: {e}'))
            self.root.after(0, lambda: messagebox.showerror('Gmail', f'Authentication gagal:\n{e}'))

    def _relay_key_temp_path(self) -> Path:
        tmpdir = Path(tempfile.gettempdir())
        return tmpdir / 'autocloudskill_firefox_api_key.txt'

    def _save_relay_key_to_temp(self, api_key: str) -> None:
        p = self._relay_key_temp_path()
        p.write_text(api_key.strip(), encoding='utf-8')

    def _load_relay_key_from_temp(self) -> Optional[str]:
        p = self._relay_key_temp_path()
        if p.exists():
            return p.read_text(encoding='utf-8').strip()
        return None

    def _gmail_cred_temp_path(self) -> Path:
        tmpdir = Path(tempfile.gettempdir())
        return tmpdir / 'autocloudskill_gmail_credentials_path.txt'

    def _save_gmail_cred_path_to_temp(self, path_str: str) -> None:
        p = self._gmail_cred_temp_path()
        p.write_text(path_str.strip(), encoding='utf-8')

    def _lab_url_temp_path(self) -> Path:
        tmpdir = Path(tempfile.gettempdir())
        return tmpdir / 'autocloudskill_lab_url.txt'

    def _save_lab_url_to_temp(self, url: str) -> None:
        p = self._lab_url_temp_path()
        p.write_text((url or '').strip(), encoding='utf-8')

    def _load_lab_url_from_temp(self) -> Optional[str]:
        p = self._lab_url_temp_path()
        if p.exists():
            return p.read_text(encoding='utf-8').strip()
        return None

    def _auto_start_lab_temp_path(self) -> Path:
        tmpdir = Path(tempfile.gettempdir())
        return tmpdir / 'autocloudskill_auto_start_lab.txt'

    def _save_auto_start_lab_to_temp(self, value: bool) -> None:
        p = self._auto_start_lab_temp_path()
        p.write_text('1' if value else '0', encoding='utf-8')

    def _load_auto_start_lab_from_temp(self) -> Optional[bool]:
        p = self._auto_start_lab_temp_path()
        if p.exists():
            val = (p.read_text(encoding='utf-8').strip() or '0').lower()
            return val in ['1', 'true', 'yes', 'on']
        return None

    def _recaptcha_ext_temp_path(self) -> Path:
        tmpdir = Path(tempfile.gettempdir())
        return tmpdir / 'autocloudskill_recaptcha_extension.txt'

    def _save_recaptcha_extension_to_temp(self, value: bool) -> None:
        p = self._recaptcha_ext_temp_path()
        p.write_text('1' if value else '0', encoding='utf-8')

    def _load_recaptcha_extension_from_temp(self) -> Optional[bool]:
        p = self._recaptcha_ext_temp_path()
        if p.exists():
            val = (p.read_text(encoding='utf-8').strip() or '0').lower()
            return val in ['1', 'true', 'yes', 'on']
        return None

    def _load_gmail_cred_path_from_temp(self) -> Optional[str]:
        p = self._gmail_cred_temp_path()
        if p.exists():
            return p.read_text(encoding='utf-8').strip()
        return None

    def on_closing(self):
        if self.is_running:
            if messagebox.askokcancel('Quit', 'Automation is running. Are you sure you want to quit?'):
                self.stop_automation()
                self.root.after(1000, self.root.destroy)
        else:
            log_user_action(self.logger, 'APPLICATION_EXIT')
            self.root.destroy()

    def run(self):
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.mainloop()


if __name__ == '__main__':
    app = MainWindow()
    app.run()