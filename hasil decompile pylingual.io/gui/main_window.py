"""
Main window untuk aplikasi Auto Cloud Skill Registration
"""
import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import threading
import json
import time
from datetime import datetime
from typing import Dict, Optional
import tempfile
from pathlib import Path
import sys
import asyncio
import hashlib

# Import services
try:
    from services.randomuser_service import RandomUserService
    from services.firefox_relay_service import FirefoxRelayService
    from services.captcha_service import CaptchaSolverService
    from automation.cloudskill_automation import CloudSkillAutomation
    from utils.logger import setup_logger, log_user_action
    from utils.validators import validate_user_data
    from config.settings import settings
    from config.constants import APP_NAME, VERSION, AUTHOR
except ImportError as e:
    print(f"Import error in main_window.py: {e}")
    # Create dummy classes for testing
    class RandomUserService:
        def get_random_user(self, **kwargs):
            return {'first_name': 'John', 'last_name': 'Doe', 'email': 'test@example.com'}
        def generate_company_name(self):
            return 'TechCorp'
        def generate_password(self, length=12):
            return 'TestPass123!'
    
    class CaptchaSolverService:
        pass
    
    class CloudSkillAutomation:
        def __init__(self, **kwargs):
            pass
        def register_account(self, user_data):
            return {'success': True, 'message': 'Test registration'}
    
    def setup_logger(name):
        import logging
        return logging.getLogger(name)
    
    def log_user_action(logger, action, details=None):
        pass
    
    def validate_user_data(data):
        return []
    
    class settings:
        DEFAULT_GENDER = 'female'
        DEFAULT_NATIONALITIES = 'gb,us,es'
        DEFAULT_PASSWORD_LENGTH = 12
    
    APP_NAME = 'Auto Cloud Skill'
    VERSION = '1.2.0'
    AUTHOR = 'SinyoRMX'

class MainWindow:
    """Main window aplikasi"""

    def __init__(self):
        """Initialize main window"""
        self.logger = setup_logger('MainWindow')
        self.random_user_service = RandomUserService()
        self.captcha_service = CaptchaSolverService()
        
        try:
            self.firefox_relay_service = FirefoxRelayService()
        except Exception as e:
            self.firefox_relay_service = None
            self.logger.warning(f'Firefox Relay service not available: {e}')
        
        self.automation = None
        
        # Create main window
        self.root = ttk.Window(
            title='Auto Cloud Skill', 
            themename='darkly', 
            size=(650, 600), 
            resizable=(True, True)
        )
        
        self.center_window()
        self.setup_variables()
        self.build_ui()
        self.is_running = False
        self._genai_api_key_event = threading.Event()
        self._latest_genai_api_key = None
        
        # Auto generate initial data
        self.root.after(5000, self.auto_generate_initial_data)
        log_user_action(self.logger, 'APPLICATION_START')

    def center_window(self):
        """Center window di layar"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

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
        
        # Registration Tab
        self.create_registration_tab(notebook)
        
        # Settings Tab
        self.create_settings_tab(notebook)
        
        # Logs Tab
        self.create_logs_tab(notebook)
        
        # About Tab
        self.create_about_tab(notebook)
        
        # Bottom buttons
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill=X, pady=(10, 0))
        
        # Status
        status_frame = ttk.Frame(bottom_frame)
        status_frame.pack(fill=X, pady=(0, 10))
        ttk.Label(status_frame, text='Status:', bootstyle=INFO).pack(side=LEFT)
        status_label = ttk.Label(status_frame, textvariable=self.status_var, bootstyle=SUCCESS)
        status_label.pack(side=LEFT, padx=(5, 0))
        
        # Buttons
        button_frame = ttk.Frame(bottom_frame)
        button_frame.pack(fill=X)
        
        refresh_btn = ttk.Button(
            button_frame, 
            text='Refresh Data', 
            command=self.refresh_generated_data, 
            bootstyle=INFO, 
            width=15
        )
        refresh_btn.pack(side=LEFT, padx=(0, 5))
        
        self.start_btn = ttk.Button(
            button_frame, 
            text='Start Registration', 
            command=self.start_automation, 
            bootstyle=SUCCESS, 
            width=20, 
            state=DISABLED
        )
        self.start_btn.pack(side=LEFT, padx=5)
        
        self.stop_btn = ttk.Button(
            button_frame, 
            text='Stop', 
            command=self.stop_automation, 
            bootstyle=DANGER, 
            width=15, 
            state=DISABLED
        )
        self.stop_btn.pack(side=LEFT, padx=5)
        
        exit_btn = ttk.Button(
            button_frame, 
            text='Exit', 
            command=self.on_closing, 
            bootstyle=DANGER, 
            width=15
        )
        exit_btn.pack(side=RIGHT)

    def create_registration_tab(self, notebook):
        """Create registration tab"""
        reg_frame = ttk.Frame(notebook)
        notebook.add(reg_frame, text='Registration')
        
        # User data frame
        user_frame = ttk.LabelFrame(reg_frame, text='User Information', padding=10)
        user_frame.pack(fill=X, pady=(0, 10))
        
        # First Name
        ttk.Label(user_frame, text='First Name:').grid(row=0, column=0, sticky=W, pady=2)
        ttk.Entry(user_frame, textvariable=self.first_name_var, width=30).grid(row=0, column=1, sticky=W, pady=2, padx=(5, 0))
        
        # Last Name
        ttk.Label(user_frame, text='Last Name:').grid(row=1, column=0, sticky=W, pady=2)
        ttk.Entry(user_frame, textvariable=self.last_name_var, width=30).grid(row=1, column=1, sticky=W, pady=2, padx=(5, 0))
        
        # Email
        ttk.Label(user_frame, text='Email:').grid(row=2, column=0, sticky=W, pady=2)
        ttk.Entry(user_frame, textvariable=self.email_var, width=30).grid(row=2, column=1, sticky=W, pady=2, padx=(5, 0))
        
        # Company
        ttk.Label(user_frame, text='Company:').grid(row=3, column=0, sticky=W, pady=2)
        ttk.Entry(user_frame, textvariable=self.company_var, width=30).grid(row=3, column=1, sticky=W, pady=2, padx=(5, 0))
        
        # Password
        ttk.Label(user_frame, text='Password:').grid(row=4, column=0, sticky=W, pady=2)
        self.password_entry = ttk.Entry(user_frame, textvariable=self.password_var, width=30, show='*')
        self.password_entry.grid(row=4, column=1, sticky=W, pady=2, padx=(5, 0))
        
        # Password Confirm
        ttk.Label(user_frame, text='Confirm Password:').grid(row=5, column=0, sticky=W, pady=2)
        self.password_confirm_entry = ttk.Entry(user_frame, textvariable=self.password_confirm_var, width=30, show='*')
        self.password_confirm_entry.grid(row=5, column=1, sticky=W, pady=2, padx=(5, 0))
        
        # Show password checkbox
        ttk.Checkbutton(
            user_frame, 
            text='Show passwords', 
            variable=self.show_password_var,
            command=self.toggle_password_visibility
        ).grid(row=6, column=1, sticky=W, pady=5, padx=(5, 0))

    def create_settings_tab(self, notebook):
        """Create settings tab"""
        settings_frame = ttk.Frame(notebook)
        notebook.add(settings_frame, text='Settings')
        
        # Firefox Relay settings
        relay_frame = ttk.LabelFrame(settings_frame, text='Firefox Relay Settings', padding=10)
        relay_frame.pack(fill=X, pady=(0, 10))
        
        ttk.Label(relay_frame, text='API Key:').grid(row=0, column=0, sticky=W, pady=2)
        ttk.Entry(relay_frame, textvariable=self.firefox_api_key_var, width=50).grid(row=0, column=1, sticky=W, pady=2, padx=(5, 0))
        
        ttk.Button(
            relay_frame, 
            text='Test API Key', 
            command=self.test_firefox_api_key
        ).grid(row=1, column=1, sticky=W, pady=5, padx=(5, 0))
        
        # Status label
        self.firefox_status_label = ttk.Label(relay_frame, text='Firefox Relay: Not configured', bootstyle=WARNING)
        self.firefox_status_label.grid(row=2, column=1, sticky=W, pady=2, padx=(5, 0))

    def create_logs_tab(self, notebook):
        """Create logs tab"""
        logs_frame = ttk.Frame(notebook)
        notebook.add(logs_frame, text='Logs')
        
        # Logs text area
        self.log_text = scrolledtext.ScrolledText(logs_frame, height=20, width=80)
        self.log_text.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Logs buttons
        logs_btn_frame = ttk.Frame(logs_frame)
        logs_btn_frame.pack(fill=X, padx=10, pady=(0, 10))
        
        ttk.Button(logs_btn_frame, text='Clear Logs', command=self.clear_logs).pack(side=LEFT, padx=(0, 5))
        ttk.Button(logs_btn_frame, text='Save Logs', command=self.save_logs).pack(side=LEFT)

    def create_about_tab(self, notebook):
        """Create about tab"""
        about_frame = ttk.Frame(notebook)
        notebook.add(about_frame, text='About')
        
        about_text = f"""
{APP_NAME} v{VERSION}
Created by: {AUTHOR}

This application automates the registration process for Google Cloud Skills Boost.

Features:
- Automatic user data generation
- Firefox Relay email integration
- Captcha solving support
- Lab automation

License: MIT License
        """.strip()
        
        ttk.Label(about_frame, text=about_text, justify=LEFT, font=('Segoe UI', 10)).pack(padx=20, pady=20)

    def toggle_password_visibility(self):
        """Toggle masking untuk input password dan confirm password."""
        try:
            show_char = '' if self.show_password_var.get() else '*'
            if hasattr(self, 'password_entry') and self.password_entry:
                self.password_entry.config(show=show_char)
            if hasattr(self, 'password_confirm_entry') and self.password_confirm_entry:
                self.password_confirm_entry.config(show=show_char)
        except Exception as e:
            self.log_message(f'⚠️ Toggle password visibility error: {e}')

    def copy_password(self):
        """Salin password utama ke clipboard."""
        try:
            pwd = self.password_var.get()
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            self.log_message('ℹ️ Password copied to clipboard.')
        except Exception as e:
            self.log_message(f'🛑 Copy password error: {e}')

    def auto_generate_initial_data(self):
        """Auto-generate data saat aplikasi start"""
        self.log_message('✅ Auto-generating initial data...')
        self.status_var.set('Generating data...')
        
        try:
            user_data = self.random_user_service.get_random_user(
                gender=settings.DEFAULT_GENDER, 
                nationalities=settings.DEFAULT_NATIONALITIES
            )
            
            if not user_data:
                raise Exception('Failed to get random user data')
                
            self.first_name_var.set(user_data['first_name'])
            self.last_name_var.set(user_data['last_name'])
            
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
                'first_name': user_data['first_name'], 
                'last_name': user_data['last_name'], 
                'company': company
            })
            
        except Exception as e:
            error_msg = f'Error generating initial data: {str(e)}'
            self.log_message(f'🛑 {error_msg}')
            self.status_var.set('Error generating data')

    def refresh_generated_data(self):
        """Refresh/regenerate data secara manual"""
        self.log_message('🔄️ Refreshing data...')
        self.status_var.set('Refreshing...')
        self.auto_generate_initial_data()

    def test_firefox_api_key(self):
        """Test Firefox Relay API key dengan berbagai auth format"""
        api_key = self.firefox_api_key_var.get().strip()
        if not api_key:
            messagebox.showwarning('Warning', 'Please enter Firefox Relay API key first')
            return
            
        self.log_message('⏳ Testing Firefox Relay API key...')
        self.log_message('⚙️ Trying different authentication formats...')
        
        try:
            from services.firefox_relay_service import FirefoxRelayService
            test_service = FirefoxRelayService(api_key=api_key)
            results = test_service.test_connection()
            
            if results['success']:
                self.firefox_status_label.config(text='Firefox Relay: ✅ Connected', bootstyle=SUCCESS)
                self.log_message('✅ Firefox Relay API key is valid!')
                self.log_message(f"✅ Using URL: {results.get('working_url', 'N/A')}")
                self.log_message(f"⏳ Auth format: {results['auth_format']}")
                self.log_message(f"🔊 Found {results['masks_count']} existing email masks")
                
                self.firefox_relay_service = test_service
                
                if self.data_generated:
                    self.status_var.set('Ready')
                    self.update_start_button_state()
                    
                messagebox.showinfo('Success', 
                    f"Firefox Relay API key is valid!\n"
                    f"URL: {results.get('working_url', 'N/A')}\n"
                    f"Auth: {results['auth_format']}\n"
                    f"Existing masks: {results['masks_count']}")
            else:
                self.firefox_status_label.config(text='Firefox Relay: 🛑 Invalid API Key', bootstyle=DANGER)
                error_msg = results.get('error', 'Unknown error')
                self.log_message(f'🛑 Firefox Relay API key test failed: {error_msg}')
                messagebox.showerror('Error', f'API key test failed:\n{error_msg}')
                
        except Exception as e:
            self.firefox_status_label.config(text='Firefox Relay: 🛑 Connection Error', bootstyle=DANGER)
            self.log_message(f'🛑 Firefox Relay connection error: {str(e)}')
            messagebox.showerror('Error', f'Connection error:\n{str(e)}')

    def start_automation(self):
        """Start automation process"""
        if self.is_running:
            return
            
        if not self.firefox_relay_service:
            api_key = (self.firefox_api_key_var.get() or '').strip()
            if not api_key:
                messagebox.showerror('Error', 'Please set and test Firefox Relay API key first!')
                return
                
            try:
                from services.firefox_relay_service import FirefoxRelayService
                self.firefox_relay_service = FirefoxRelayService(api_key=api_key)
            except Exception as e:
                messagebox.showerror('Error', f'Failed to initialize Firefox Relay service:\n{e}')
                return
                
        # Create relay email
        self.log_message('🔊 Creating Firefox Relay email...')
        self.status_var.set('Creating email...')
        
        try:
            mask = self.firefox_relay_service.create_relay_mask(
                f"Auto registration - {datetime.now().strftime('%Y%m%d_%H%M%S')}"
            )
            if not mask:
                raise Exception('Failed to create Firefox Relay email')
                
            relay_email = mask['full_address']
            self.email_var.set(relay_email)
            self.log_message(f'✅ Created relay email: {relay_email}')
            
        except Exception as e:
            error_msg = f'Failed to create relay email: {str(e)}'
            self.log_message(f'🛑 {error_msg}')
            messagebox.showerror('Error', error_msg)
            return
            
        # Validate user data
        user_data = {
            'first_name': self.first_name_var.get().strip(),
            'last_name': self.last_name_var.get().strip(),
            'email': self.email_var.get().strip(),
            'company': self.company_var.get().strip(),
            'password': self.password_var.get(),
            'password_confirm': self.password_confirm_var.get()
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
        """Run automation process"""
        try:
            keep_open = False  # Simplified for now
            
            self.automation = CloudSkillAutomation(
                headless=False, 
                captcha_solver=self.captcha_service, 
                keep_browser_open=keep_open, 
                extension_mode=self.extension_mode_var.get()
            )
            
            result = self.automation.register_account(user_data)
            
            if result.get('success'):
                self.log_message('✅ Registration completed successfully!')
                self.root.after(0, lambda: self.status_var.set('Registration completed'))
            else:
                error_msg = f'Automation error: {result.get("error", "Unknown error")}'
                self.log_message(f'🛑 {error_msg}')
                self.root.after(0, lambda: self.status_var.set('Error'))
                self.root.after(0, lambda: messagebox.showerror('Error', error_msg))
                
        except Exception as e:
            error_msg = f'Automation error: {str(e)}'
            self.log_message(f'🛑 {error_msg}')
            self.root.after(0, lambda: self.status_var.set('Error'))
            self.root.after(0, lambda: messagebox.showerror('Error', error_msg))
        finally:
            self.root.after(0, self.automation_finished)

    def stop_automation(self):
        """Stop automation process"""
        self.log_message('⛔ Stopping automation...')
        self.is_running = False
        self.automation_finished()

    def automation_finished(self):
        """Reset UI after automation finished"""
        self.is_running = False
        self.update_start_button_state()
        self.stop_btn.config(state=DISABLED)
        if self.status_var.get() in ['Running...', 'Error']:
            self.status_var.set('Ready')

    def update_start_button_state(self):
        """Set state Start button berdasarkan data_generated dan is_running."""
        try:
            state = NORMAL if self.data_generated and (not self.is_running) else DISABLED
            self.start_btn.config(state=state)
        except Exception:
            pass

    def log_message(self, message: str):
        """Add message to log"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        log_entry = f'[{timestamp}] {message}\n'
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        self.logger.info(message)

    def clear_logs(self):
        """Clear log text"""
        self.log_text.delete('1.0', tk.END)
        self.log_message('Logs cleared')

    def save_logs(self):
        """Save logs to file"""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension='.txt',
                filetypes=[('Text files', '*.txt'), ('All files', '*.*')],
                title='Save Logs'
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

    def on_closing(self):
        """Handle window closing"""
        if self.is_running:
            if messagebox.askokcancel('Quit', 'Automation is running. Are you sure you want to quit?'):
                self.stop_automation()
                self.root.after(1000, self.root.destroy)
        else:
            log_user_action(self.logger, 'APPLICATION_EXIT')
            self.root.destroy()

    def run(self):
        """Run the application"""
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.mainloop()

if __name__ == '__main__':
    app = MainWindow()
    app.run()