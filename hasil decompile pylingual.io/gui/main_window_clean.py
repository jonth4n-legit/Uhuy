"""
Clean MainWindow rebuilt from decompiled sources to ensure a runnable GUI.
Focuses on Settings, Registration, Logs, and About tabs with core actions.
"""
from __future__ import annotations

import tempfile
from datetime import datetime
from pathlib import Path
from typing import Optional

import tkinter as tk
from tkinter import messagebox, filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from services.randomuser_service import RandomUserService
from services.firefox_relay_service import FirefoxRelayService
from utils.logger import setup_logger, log_user_action
from config.settings import settings
from gui.tabs.registration_tab import RegistrationTab
from gui.tabs.settings_tab import SettingsTab
from gui.tabs.logs_tab import LogsTab
from gui.tabs.about_tab import AboutTab


class MainWindow:
    def __init__(self) -> None:
        self.logger = setup_logger('MainWindow')
        self.random_user_service = RandomUserService()
        self.firefox_relay_service: Optional[FirefoxRelayService] = None

        self.root = ttk.Window(title='Auto Cloud Skill', themename='darkly', size=(800, 650), resizable=(True, True))
        self._init_variables()
        self._build_ui()
        self._center_window()

        # Load API key from temp if exists
        try:
            key = self._load_relay_key_from_temp()
            if key:
                self.firefox_api_key_var.set(key)
        except Exception:
            pass

        self.is_running = False
        self.root.after(300, self.auto_generate_initial_data)
        log_user_action(self.logger, 'APPLICATION_START')

    def _center_window(self) -> None:
        self.root.update_idletasks()
        w = self.root.winfo_width() or 800
        h = self.root.winfo_height() or 650
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = int((sw - w) / 2)
        y = int((sh - h) / 3)
        self.root.geometry(f'{w}x{h}+{x}+{y}')

    def _init_variables(self) -> None:
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
        self.show_password_var = tk.BooleanVar(value=False)
        self.status_var = tk.StringVar(value='Initializing...')
        self.data_generated = False
        self.lab_url_var = tk.StringVar()
        self.auto_start_lab_var = tk.BooleanVar(value=False)

    def _build_ui(self) -> None:
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=BOTH, expand=True)

        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=BOTH, expand=True)

        self.settings_tab = SettingsTab(self, notebook)
        self.logs_tab = LogsTab(self, notebook)
        self.registration_tab = RegistrationTab(self, notebook)
        self.about_tab = AboutTab(self, notebook)

        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill=X, pady=(10, 0))
        status_frame = ttk.Frame(bottom_frame)
        status_frame.pack(fill=X, pady=(0, 10))
        ttk.Label(status_frame, text='Status:', bootstyle=INFO).pack(side=LEFT)
        ttk.Label(status_frame, textvariable=self.status_var, bootstyle=SUCCESS).pack(side=LEFT, padx=(5, 0))

        button_frame = ttk.Frame(bottom_frame)
        button_frame.pack(fill=X)
        ttk.Button(button_frame, text='Refresh Data', command=self.refresh_generated_data, bootstyle=INFO, width=15).pack(side=LEFT, padx=(0, 5))
        self.start_btn = ttk.Button(button_frame, text='Start Registration', command=self.start_automation, bootstyle=SUCCESS, width=20, state=DISABLED)
        self.start_btn.pack(side=LEFT, padx=5)
        self.stop_btn = ttk.Button(button_frame, text='Stop', command=self.stop_automation, bootstyle=DANGER, width=15, state=DISABLED)
        self.stop_btn.pack(side=LEFT, padx=5)
        ttk.Button(button_frame, text='Exit', command=self.on_closing, bootstyle=DANGER, width=15).pack(side=RIGHT)

    # Registration Tab helpers
    def toggle_password_visibility(self) -> None:
        show_char = '' if self.show_password_var.get() else '*'
        try:
            if hasattr(self, 'password_entry') and self.password_entry:
                self.password_entry.config(show=show_char)
            if hasattr(self, 'password_confirm_entry') and self.password_confirm_entry:
                self.password_confirm_entry.config(show=show_char)
        except Exception as e:
            self.log_message(f'⚠️ Toggle password visibility error: {e}')

    def copy_password(self) -> None:
        try:
            pwd = self.password_var.get()
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            self.log_message('ℹ️ Password copied to clipboard.')
        except Exception as e:
            self.log_message(f'🛑 Copy password error: {e}')

    # Settings Tab actions
    def test_firefox_api_key(self) -> None:
        api_key = self.firefox_api_key_var.get().strip()
        if not api_key:
            messagebox.showwarning('Warning', 'Please enter Firefox Relay API key first')
            return
        self.log_message('⏳ Testing Firefox Relay API key...')
        try:
            svc = FirefoxRelayService(api_key=api_key)
            res = svc.test_connection()
            if res.get('success'):
                self.firefox_relay_service = svc
                self.status_var.set('Ready')
                self._save_relay_key_to_temp(api_key)
                if hasattr(self, 'firefox_status_label'):
                    self.firefox_status_label.config(text='Firefox Relay: ✅ Connected', bootstyle=SUCCESS)
                self.log_message('✅ Firefox Relay API key is valid!')
                self.update_start_button_state()
            else:
                if hasattr(self, 'firefox_status_label'):
                    self.firefox_status_label.config(text='Firefox Relay: 🛑 Invalid API Key', bootstyle=DANGER)
                messagebox.showerror('Error', res.get('error') or 'All authentication formats and URLs failed')
        except Exception as e:
            if hasattr(self, 'firefox_status_label'):
                self.firefox_status_label.config(text='Firefox Relay: 🛑 Connection Error', bootstyle=DANGER)
            self.log_message(f'🛑 Firefox Relay connection error: {e}')

    def delete_all_firefox_masks(self) -> None:
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
        if not messagebox.askyesno('Confirm', 'Yakin ingin menghapus SEMUA email masks?'):
            return
        try:
            result = self.firefox_relay_service.delete_all_masks()
            requested = int(result.get('requested', 0))
            deleted = int(result.get('deleted', 0))
            failed = len(result.get('failed_ids', []) or [])
            messagebox.showinfo('Delete All Masks', f'Requested: {requested}\nDeleted: {deleted}\nFailed: {failed}')
        except Exception as e:
            messagebox.showerror('Error', f'Delete error:\n{e}')

    # Data generation
    def auto_generate_initial_data(self) -> None:
        self.status_var.set('Generating data...')
        try:
            user_data = self.random_user_service.get_random_user(
                gender=settings.DEFAULT_GENDER,
                nationalities=settings.DEFAULT_NATIONALITIES,
            )
            if not user_data:
                raise RuntimeError('Failed to get random user data')
            self.first_name_var.set(user_data.get('first_name',''))
            self.last_name_var.set(user_data.get('last_name',''))
            self.company_var.set(self.random_user_service.generate_company_name())
            pwd = self.random_user_service.generate_password(settings.DEFAULT_PASSWORD_LENGTH)
            self.password_var.set(pwd)
            self.password_confirm_var.set(pwd)
            self.email_var.set('Will be generated from Firefox Relay')
            self.status_var.set('Ready')
            self.data_generated = True
            self.update_start_button_state()
            self.log_message('✅ Initial data generated successfully!')
        except Exception as e:
            self.status_var.set('Error generating data')
            self.log_message(f'🛑 Error generating initial data: {e}')

    def refresh_generated_data(self) -> None:
        self.log_message('🔄 Refreshing data...')
        self.auto_generate_initial_data()

    # Start/Stop (simplified)
    def start_automation(self) -> None:
        if self.is_running:
            return
        if not self.firefox_relay_service:
            api_key = self.firefox_api_key_var.get().strip()
            if not api_key:
                messagebox.showerror('Error', 'Please set and test Firefox Relay API key first!')
                return
            try:
                self.firefox_relay_service = FirefoxRelayService(api_key=api_key)
            except Exception as e:
                messagebox.showerror('Error', f'Failed to initialize Firefox Relay service:\n{e}')
                return
        self.is_running = True
        self.start_btn.config(state=DISABLED)
        self.stop_btn.config(state=NORMAL)
        self.status_var.set('Creating email...')
        try:
            mask = self.firefox_relay_service.create_relay_mask(f"Auto registration - {datetime.now().strftime('%Y%m%d_%H%M%S')}")
            if not mask:
                raise RuntimeError('Failed to create Firefox Relay email')
            relay_email = mask.get('full_address') or f"{mask.get('address','')}@{mask.get('domain','')}"
            self.email_var.set(relay_email)
            self.log_message(f'✅ Created relay email: {relay_email}')
            self.status_var.set('Ready')
        except Exception as e:
            self.log_message(f'🛑 Failed to create relay email: {e}')
            messagebox.showerror('Error', f'Failed to create relay email:\n{e}')
        finally:
            self.automation_finished()

    def stop_automation(self) -> None:
        self.log_message('⛔ Stopping...')
        self.automation_finished()

    def automation_finished(self) -> None:
        self.is_running = False
        self.update_start_button_state()
        self.stop_btn.config(state=DISABLED)
        if self.status_var.get() in ['Running...', 'Error']:
            self.status_var.set('Ready')

    def update_start_button_state(self) -> None:
        state = NORMAL if self.data_generated and (not self.is_running) else DISABLED
        try:
            self.start_btn.config(state=state)
        except Exception:
            pass

    # Logs helpers (used by LogsTab)
    def log_message(self, message: str) -> None:
        ts = datetime.now().strftime('%H:%M:%S')
        line = f'[{ts}] {message}\n'
        try:
            self.log_text.insert(tk.END, line)
            self.log_text.see(tk.END)
        except Exception:
            pass
        self.logger.info(message)

    def clear_logs(self) -> None:
        try:
            self.log_text.delete('1.0', tk.END)
        except Exception:
            pass

    def save_logs(self) -> None:
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
            self.log_message(f'🛑 Error saving logs: {e}')

    # Gmail status stub for SettingsTab
    def update_gmail_status_label(self) -> None:
        try:
            if hasattr(self, 'gmail_status_label'):
                self.gmail_status_label.config(text='Gmail: 🛑 Not configured', bootstyle=WARNING)
        except Exception:
            pass

    # Placeholder Gmail actions used by SettingsTab (safe stubs)
    def browse_gmail_credentials(self) -> None:
        try:
            filename = filedialog.askopenfilename(title='Select Gmail credentials.json', filetypes=[('JSON files', '*.json'), ('All files', '*.*')])
            if filename:
                self.gmail_credentials_path_var.set(filename)
                self.log_message(f'✅ Gmail credentials set: {filename}')
                self.update_gmail_status_label()
        except Exception as e:
            self.log_message(f'🛑 Error selecting Gmail credentials: {e}')

    def generate_gmail_auth_url(self) -> None:
        self.log_message('ℹ️ Gmail Auth URL flow is not enabled in this build.')

    def copy_gmail_auth_url(self) -> None:
        url = self.gmail_auth_url_var.get().strip()
        if not url:
            return
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(url)
            self.log_message('ℹ️ Auth URL copied to clipboard.')
        except Exception as e:
            self.log_message(f'🛑 Clipboard error: {e}')

    def complete_gmail_auth_async(self) -> None:
        self.log_message('ℹ️ Complete Gmail Auth is not enabled in this build.')

    # Temp storage helpers
    def _relay_key_temp_path(self) -> Path:
        return Path(tempfile.gettempdir()) / 'autocloudskill_firefox_api_key.txt'

    def _save_relay_key_to_temp(self, api_key: str) -> None:
        try:
            p = self._relay_key_temp_path()
            p.write_text((api_key or '').strip(), encoding='utf-8')
        except Exception:
            pass

    def _load_relay_key_from_temp(self):
        p = self._relay_key_temp_path()
        if p.exists():
            return p.read_text(encoding='utf-8').strip()
        return None

    # App run/exit
    def on_closing(self) -> None:
        log_user_action(self.logger, 'APPLICATION_EXIT')
        try:
            self.root.destroy()
        except Exception:
            pass

    def run(self) -> None:
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.mainloop()


if __name__ == '__main__':
    MainWindow().run()

