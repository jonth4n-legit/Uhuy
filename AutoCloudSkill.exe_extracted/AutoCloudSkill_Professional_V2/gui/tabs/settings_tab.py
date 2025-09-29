"""
Professional Settings Tab for AutoCloudSkill Application.

This module provides a comprehensive settings interface for configuring
all application services and preferences with proper validation and status indicators.

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gui.main_window import MainWindow


class SettingsTab:
    """Professional settings tab for application configuration."""

    def __init__(self, owner: 'MainWindow', notebook: ttk.Notebook):
        """Initialize the settings tab.

        Args:
            owner: Reference to the main window instance
            notebook: Parent notebook widget
        """
        self.owner = owner
        self._build_interface(notebook)

    def _build_interface(self, notebook: ttk.Notebook) -> None:
        """Build the complete settings tab interface."""
        # Create scrollable container
        self.tab_frame = ttk.Frame(notebook)
        notebook.add(self.tab_frame, text='⚙️ Settings')

        # Create scrollable canvas
        self._create_scrollable_container()

        # Build settings sections
        self._create_api_configuration()
        self._create_browser_settings()
        self._create_gmail_configuration()
        self._create_lab_settings()
        self._create_license_information()
        self._create_service_status()

        # Setup scrolling
        self._setup_scrolling()

    def _create_scrollable_container(self) -> None:
        """Create scrollable container for settings."""
        # Canvas for scrolling
        self.canvas = tk.Canvas(self.tab_frame, highlightthickness=0)
        self.v_scrollbar = ttk.Scrollbar(
            self.tab_frame,
            orient='vertical',
            command=self.canvas.yview
        )

        self.canvas.configure(yscrollcommand=self.v_scrollbar.set)

        # Pack scrollbar and canvas
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollable frame
        self.scrollable_frame = ttk.Frame(self.canvas, padding=20)
        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor='nw'
        )

    def _setup_scrolling(self) -> None:
        """Setup canvas scrolling functionality."""
        def on_frame_configure(event=None):
            """Update scroll region when frame size changes."""
            self.canvas.configure(scrollregion=self.canvas.bbox('all'))
            try:
                # Update canvas window width
                canvas_width = self.canvas.winfo_width()
                self.canvas.itemconfig(self.canvas_window, width=canvas_width)
            except Exception:
                pass

        def on_mousewheel(event):
            """Handle mouse wheel scrolling."""
            delta = event.delta
            if delta == 0 and hasattr(event, 'num'):
                delta = 120 if event.num == 4 else -120
            try:
                self.canvas.yview_scroll(int(-delta / 120), 'units')
            except Exception:
                pass

        def bind_mousewheel(event):
            """Bind mouse wheel events."""
            self.canvas.bind_all('<MouseWheel>', on_mousewheel)
            self.canvas.bind_all('<Button-4>', on_mousewheel)
            self.canvas.bind_all('<Button-5>', on_mousewheel)

        def unbind_mousewheel(event):
            """Unbind mouse wheel events."""
            self.canvas.unbind_all('<MouseWheel>')
            self.canvas.unbind_all('<Button-4>')
            self.canvas.unbind_all('<Button-5>')

        # Bind events
        self.scrollable_frame.bind('<Configure>', on_frame_configure)
        self.canvas.bind('<Enter>', bind_mousewheel)
        self.canvas.bind('<Leave>', unbind_mousewheel)

        # Update scroll region after tab changes
        def on_tab_changed(event):
            try:
                current = event.widget.nametowidget(event.widget.select())
                if current is self.tab_frame:
                    self.canvas.update_idletasks()
                    on_frame_configure()
            except Exception:
                pass

        # Bind to notebook tab changes
        try:
            notebook = self.tab_frame.master
            notebook.bind('<<NotebookTabChanged>>', on_tab_changed)
        except Exception:
            pass

    def _create_api_configuration(self) -> None:
        """Create API configuration section."""
        api_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text='🔑 API Configuration',
            padding=20,
            bootstyle=PRIMARY
        )
        api_frame.pack(fill=X, pady=(0, 15))

        # Firefox Relay API Key
        ttk.Label(
            api_frame,
            text='Firefox Relay API Key:',
            font=('Segoe UI', 10, 'bold')
        ).pack(anchor=W, pady=(0, 5))

        # API Key input frame
        api_input_frame = ttk.Frame(api_frame)
        api_input_frame.pack(fill=X, pady=(0, 10))

        self.api_key_entry = ttk.Entry(
            api_input_frame,
            textvariable=self.owner.firefox_api_key_var,
            show='*',
            font=('Segoe UI', 10)
        )
        self.api_key_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))

        # Show API key toggle
        self.show_api_key_var = tk.BooleanVar()
        show_api_check = ttk.Checkbutton(
            api_input_frame,
            text='Show',
            variable=self.show_api_key_var,
            command=self._toggle_api_key_visibility,
            bootstyle='round-toggle'
        )
        show_api_check.pack(side=RIGHT)

        # API Key actions
        api_actions_frame = ttk.Frame(api_frame)
        api_actions_frame.pack(fill=X, pady=(0, 10))

        self.test_api_btn = ttk.Button(
            api_actions_frame,
            text='🧪 Test API Key',
            command=self._test_firefox_api_key,
            bootstyle=SUCCESS,
            width=18
        )
        self.test_api_btn.pack(side=LEFT, padx=(0, 10))

        self.delete_masks_btn = ttk.Button(
            api_actions_frame,
            text='🗑️ Delete All Masks',
            command=self._delete_all_firefox_masks,
            bootstyle=DANGER,
            width=20
        )
        self.delete_masks_btn.pack(side=LEFT)

        # API Key status
        self.firefox_status_label = ttk.Label(
            api_frame,
            text='Firefox Relay: 🛑 API Key Required',
            font=('Segoe UI', 9),
            bootstyle=DANGER
        )
        self.firefox_status_label.pack(anchor=W)

        # API Key info
        api_info = ttk.Label(
            api_frame,
            text='💡 Get your Firefox Relay API key from relay.firefox.com',
            font=('Segoe UI', 9),
            bootstyle=INFO
        )
        api_info.pack(anchor=W, pady=(5, 0))

    def _create_browser_settings(self) -> None:
        """Create browser and captcha settings section."""
        browser_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text='🌐 Browser & Captcha Settings',
            padding=20,
            bootstyle=SECONDARY
        )
        browser_frame.pack(fill=X, pady=(0, 15))

        # Extension mode setting
        ext_frame = ttk.Frame(browser_frame)
        ext_frame.pack(fill=X, pady=(0, 10))

        self.extension_mode_check = ttk.Checkbutton(
            ext_frame,
            text='Use reCAPTCHA Extension (Manual Mode)',
            variable=self.owner.extension_mode_var,
            bootstyle='warning-round-toggle'
        )
        self.extension_mode_check.pack(side=LEFT)

        # Extension info
        ext_info = ttk.Label(
            browser_frame,
            text='⚠️ Extension mode requires manual captcha solving when automated solving fails',
            font=('Segoe UI', 9),
            bootstyle=WARNING
        )
        ext_info.pack(anchor=W)

        # Captcha solver info
        captcha_info_frame = ttk.Frame(browser_frame)
        captcha_info_frame.pack(fill=X, pady=(10, 0))

        ttk.Label(
            captcha_info_frame,
            text='🔊 Audio Captcha Solver: Multi-engine (Google Speech, Azure, Whisper)',
            font=('Segoe UI', 9),
            bootstyle=SUCCESS
        ).pack(anchor=W)

    def _create_gmail_configuration(self) -> None:
        """Create Gmail configuration section."""
        gmail_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text='📧 Gmail Configuration',
            padding=20,
            bootstyle=INFO
        )
        gmail_frame.pack(fill=X, pady=(0, 15))

        # Gmail grid setup
        gmail_grid = ttk.Frame(gmail_frame)
        gmail_grid.pack(fill=X)

        # Configure grid weights
        gmail_grid.columnconfigure(1, weight=1)

        button_width = 16

        # Credentials file
        ttk.Label(
            gmail_grid,
            text='Credentials File:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=0, column=0, sticky=W, pady=(0, 8), padx=(0, 10))

        self.gmail_credentials_entry = ttk.Entry(
            gmail_grid,
            textvariable=self.owner.gmail_credentials_path_var,
            font=('Segoe UI', 9)
        )
        self.gmail_credentials_entry.grid(
            row=0, column=1, sticky=EW, padx=(0, 10), pady=(0, 8)
        )

        ttk.Button(
            gmail_grid,
            text='📁 Browse',
            width=button_width,
            command=self._browse_gmail_credentials,
            bootstyle=INFO
        ).grid(row=0, column=2, padx=(0, 10), pady=(0, 8))

        ttk.Button(
            gmail_grid,
            text='🔗 Get Auth URL',
            width=button_width,
            command=self._generate_gmail_auth_url,
            bootstyle=SUCCESS
        ).grid(row=0, column=3, pady=(0, 8))

        # Auth URL
        ttk.Label(
            gmail_grid,
            text='Auth URL:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=1, column=0, sticky=W, pady=(0, 8), padx=(0, 10))

        self.gmail_auth_url_entry = ttk.Entry(
            gmail_grid,
            textvariable=self.owner.gmail_auth_url_var,
            font=('Segoe UI', 9),
            state='readonly'
        )
        self.gmail_auth_url_entry.grid(
            row=1, column=1, sticky=EW, padx=(0, 10), pady=(0, 8)
        )

        ttk.Button(
            gmail_grid,
            text='📋 Copy URL',
            width=button_width,
            command=self._copy_gmail_auth_url,
            bootstyle=INFO
        ).grid(row=1, column=2, padx=(0, 10), pady=(0, 8))

        # Verification code
        ttk.Label(
            gmail_grid,
            text='Verification Code:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=2, column=0, sticky=W, padx=(0, 10))

        self.gmail_auth_code_entry = ttk.Entry(
            gmail_grid,
            textvariable=self.owner.gmail_auth_code_var,
            font=('Segoe UI', 10)
        )
        self.gmail_auth_code_entry.grid(
            row=2, column=1, sticky=EW, padx=(0, 10)
        )

        ttk.Button(
            gmail_grid,
            text='✅ Complete Auth',
            width=button_width,
            command=self._complete_gmail_auth,
            bootstyle=PRIMARY
        ).grid(row=2, column=2, padx=(0, 10))

        ttk.Button(
            gmail_grid,
            text='🚀 Auto Auth',
            width=button_width,
            command=self._authenticate_gmail_auto,
            bootstyle=SUCCESS
        ).grid(row=2, column=3)

        # Gmail status
        self.gmail_status_label = ttk.Label(
            gmail_frame,
            text='Gmail: 🛑 Not configured',
            font=('Segoe UI', 9),
            bootstyle=WARNING
        )
        self.gmail_status_label.pack(anchor=W, pady=(15, 5))

        # Gmail info
        gmail_info = ttk.Label(
            gmail_frame,
            text='💡 Gmail is used for automatic email confirmation. Configure credentials.json from Google Cloud Console.',
            font=('Segoe UI', 9),
            bootstyle=INFO
        )
        gmail_info.pack(anchor=W)

    def _create_lab_settings(self) -> None:
        """Create lab settings section."""
        lab_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text='🧪 Lab Settings',
            padding=20,
            bootstyle=WARNING
        )
        lab_frame.pack(fill=X, pady=(0, 15))

        # Lab URL
        ttk.Label(
            lab_frame,
            text='Lab URL (cloudskillsboost.google/focuses/...):',
            font=('Segoe UI', 10, 'bold')
        ).pack(anchor=W, pady=(0, 5))

        lab_url_frame = ttk.Frame(lab_frame)
        lab_url_frame.pack(fill=X, pady=(0, 10))

        self.lab_url_entry = ttk.Entry(
            lab_url_frame,
            textvariable=self.owner.lab_url_var,
            font=('Segoe UI', 10)
        )
        self.lab_url_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))

        ttk.Button(
            lab_url_frame,
            text='📋 Paste',
            command=self._paste_lab_url,
            bootstyle=INFO,
            width=10
        ).pack(side=RIGHT)

        # Auto start setting
        auto_start_frame = ttk.Frame(lab_frame)
        auto_start_frame.pack(fill=X)

        self.auto_start_check = ttk.Checkbutton(
            auto_start_frame,
            text='🚀 Auto-start lab after email confirmation',
            variable=self.owner.auto_start_lab_var,
            bootstyle='success-round-toggle'
        )
        self.auto_start_check.pack(side=LEFT)

        # Lab info
        lab_info = ttk.Label(
            lab_frame,
            text='💡 Lab will be automatically started after successful registration and email confirmation',
            font=('Segoe UI', 9),
            bootstyle=INFO
        )
        lab_info.pack(anchor=W, pady=(10, 0))

    def _create_license_information(self) -> None:
        """Create license information section."""
        license_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text='📄 License Information',
            padding=20,
            bootstyle=DARK
        )
        license_frame.pack(fill=X, pady=(0, 15))

        # License grid
        license_grid = ttk.Frame(license_frame)
        license_grid.pack(fill=X)

        # License plan
        ttk.Label(
            license_grid,
            text='License Plan:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=0, column=0, sticky=W, pady=5, padx=(0, 20))

        self.license_plan_label = ttk.Label(
            license_grid,
            textvariable=self.owner.license_plan_var,
            font=('Segoe UI', 10),
            bootstyle=INFO
        )
        self.license_plan_label.grid(row=0, column=1, sticky=W, pady=5)

        # License expiry
        ttk.Label(
            license_grid,
            text='Expires:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=1, column=0, sticky=W, pady=5, padx=(0, 20))

        self.license_expiry_label = ttk.Label(
            license_grid,
            textvariable=self.owner.license_expiry_var,
            font=('Segoe UI', 10),
            bootstyle=INFO
        )
        self.license_expiry_label.grid(row=1, column=1, sticky=W, pady=5)

        # Refresh license button
        ttk.Button(
            license_frame,
            text='🔄 Refresh License',
            command=self._refresh_license,
            bootstyle=PRIMARY,
            width=18
        ).pack(anchor=W, pady=(10, 0))

    def _create_service_status(self) -> None:
        """Create service status section."""
        status_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text='📊 Service Status',
            padding=20,
            bootstyle=SUCCESS
        )
        status_frame.pack(fill=X)

        # Service status labels
        self.randomuser_status_label = ttk.Label(
            status_frame,
            text='RandomUser API: ✅ Available',
            font=('Segoe UI', 9),
            bootstyle=SUCCESS
        )
        self.randomuser_status_label.pack(anchor=W, pady=2)

        self.captcha_status_label = ttk.Label(
            status_frame,
            text='Audio Captcha Solver: ✅ Ready (Multi-engine)',
            font=('Segoe UI', 9),
            bootstyle=SUCCESS
        )
        self.captcha_status_label.pack(anchor=W, pady=2)

        # Test all services button
        ttk.Button(
            status_frame,
            text='🧪 Test All Services',
            command=self._test_all_services,
            bootstyle=INFO,
            width=20
        ).pack(anchor=W, pady=(10, 0))

    # Event handlers and utility methods

    def _toggle_api_key_visibility(self) -> None:
        """Toggle Firefox Relay API key visibility."""
        try:
            show_char = '' if self.show_api_key_var.get() else '*'
            self.api_key_entry.config(show=show_char)
        except Exception as e:
            self.owner.log_message(f'⚠️ API key visibility toggle error: {e}')

    def _test_firefox_api_key(self) -> None:
        """Test Firefox Relay API key."""
        api_key = self.owner.firefox_api_key_var.get().strip()
        if not api_key:
            from tkinter import messagebox
            messagebox.showwarning('Warning', 'Please enter Firefox Relay API key first')
            return

        self.owner.log_message('🧪 Testing Firefox Relay API key...')

        def worker():
            try:
                from services.firefox_relay_service import FirefoxRelayService
                test_service = FirefoxRelayService(api_key=api_key)
                results = test_service.test_connection()

                def on_result():
                    if results['success']:
                        self.firefox_status_label.config(
                            text='Firefox Relay: ✅ Connected',
                            bootstyle=SUCCESS
                        )
                        self.owner.log_message('✅ Firefox Relay API key is valid!')
                        self.owner.log_message(f"🔗 Using URL: {results.get('working_url', 'N/A')}")
                        self.owner.firefox_relay_service = test_service
                        self.owner._save_firefox_relay_key(api_key)

                        from tkinter import messagebox
                        messagebox.showinfo(
                            'Success',
                            f"Firefox Relay API key is valid!\n"
                            f"URL: {results.get('working_url', 'N/A')}\n"
                            f"Auth: {results['auth_format']}\n"
                            f"Existing masks: {results['masks_count']}"
                        )
                    else:
                        self.firefox_status_label.config(
                            text='Firefox Relay: 🛑 Invalid API Key',
                            bootstyle=DANGER
                        )
                        error_msg = results.get('error', 'Unknown error')
                        self.owner.log_message(f'🛑 Firefox Relay API key test failed: {error_msg}')

                        from tkinter import messagebox
                        messagebox.showerror('Error', f'API key test failed:\n{error_msg}')

                self.owner.root.after(0, on_result)

            except Exception as e:
                def on_error():
                    self.firefox_status_label.config(
                        text='Firefox Relay: 🛑 Connection Error',
                        bootstyle=DANGER
                    )
                    self.owner.log_message(f'🛑 Firefox Relay connection error: {str(e)}')

                    from tkinter import messagebox
                    messagebox.showerror('Error', f'Connection error:\n{str(e)}')

                self.owner.root.after(0, on_error)

        import threading
        threading.Thread(target=worker, daemon=True).start()

    def _delete_all_firefox_masks(self) -> None:
        """Delete all Firefox Relay masks."""
        from tkinter import messagebox

        if not messagebox.askyesno(
            'Confirm',
            'Are you sure you want to delete ALL email masks?\n'
            'This action cannot be undone.'
        ):
            return

        if not self.owner.firefox_relay_service:
            messagebox.showerror('Error', 'Please test Firefox Relay API key first')
            return

        self.owner.log_message('🗑️ Deleting all Firefox Relay masks...')

        def worker():
            try:
                result = self.owner.firefox_relay_service.delete_all_masks()
                requested = result.get('requested', 0)
                deleted = result.get('deleted', 0)
                failed = len(result.get('failed_ids', []))

                def on_result():
                    self.owner.log_message(
                        f'✅ Delete summary: requested={requested}, deleted={deleted}, failed={failed}'
                    )
                    messagebox.showinfo(
                        'Delete All Masks',
                        f'Requested: {requested}\nDeleted: {deleted}\nFailed: {failed}'
                    )

                self.owner.root.after(0, on_result)

            except Exception as e:
                def on_error():
                    self.owner.log_message(f'🛑 Delete all masks error: {e}')
                    messagebox.showerror('Error', f'Delete error:\n{e}')

                self.owner.root.after(0, on_error)

        import threading
        threading.Thread(target=worker, daemon=True).start()

    def _browse_gmail_credentials(self) -> None:
        """Browse for Gmail credentials file."""
        try:
            from tkinter import filedialog
            filename = filedialog.askopenfilename(
                title='Select Gmail credentials.json',
                filetypes=[('JSON files', '*.json'), ('All files', '*.*')]
            )

            if filename:
                self.owner.gmail_credentials_path_var.set(filename)
                self.owner.log_message(f'✅ Gmail credentials set: {filename}')
                self.owner._save_gmail_credentials_path(filename)
                self.owner.update_gmail_status()

        except Exception as e:
            self.owner.log_message(f'🛑 Error selecting Gmail credentials: {e}')

    def _generate_gmail_auth_url(self) -> None:
        """Generate Gmail OAuth URL."""
        try:
            cred_path = self.owner.gmail_credentials_path_var.get().strip()
            if not cred_path:
                from tkinter import messagebox
                messagebox.showwarning('Gmail', 'Please select credentials.json first.')
                return

            self.owner.gmail_auth_code_var.set('')
            self.owner.gmail_auth_url_var.set('')

            from google_auth_oauthlib.flow import InstalledAppFlow
            from services.gmail_service import SCOPES

            self.owner._gmail_oauth_flow = InstalledAppFlow.from_client_secrets_file(
                cred_path, SCOPES
            )
            self.owner._gmail_oauth_flow.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'

            auth_url, _ = self.owner._gmail_oauth_flow.authorization_url(
                access_type='offline',
                include_granted_scopes='true',
                prompt='consent'
            )

            self.owner.gmail_auth_url_var.set(auth_url)
            self.owner.log_message('🔗 Gmail Auth URL generated. Copy URL and authenticate in your browser.')

        except Exception as e:
            self.owner.log_message(f'🛑 Failed to generate Gmail Auth URL: {e}')

    def _copy_gmail_auth_url(self) -> None:
        """Copy Gmail auth URL to clipboard."""
        try:
            url = self.owner.gmail_auth_url_var.get().strip()
            if not url:
                return

            self.owner.root.clipboard_clear()
            self.owner.root.clipboard_append(url)
            self.owner.log_message('📋 Auth URL copied to clipboard.')

        except Exception as e:
            self.owner.log_message(f'🛑 Clipboard error: {e}')

    def _complete_gmail_auth(self) -> None:
        """Complete Gmail authentication with verification code."""
        code = self.owner.gmail_auth_code_var.get().strip()
        if not code:
            from tkinter import messagebox
            messagebox.showwarning('Gmail', 'Please paste verification code first.')
            return

        import threading
        threading.Thread(target=self._complete_gmail_auth_worker, args=(code,), daemon=True).start()

    def _complete_gmail_auth_worker(self, code: str) -> None:
        """Worker thread for completing Gmail authentication."""
        try:
            if not self.owner._gmail_oauth_flow:
                self.owner.root.after(0, lambda: self.owner.log_message('🛑 Please click \'Get Auth URL\' first.'))
                return

            self.owner._gmail_oauth_flow.fetch_token(code=code)
            creds = self.owner._gmail_oauth_flow.credentials

            from services.gmail_service import GmailService
            cred_path = self.owner.gmail_credentials_path_var.get().strip()
            service = GmailService(credentials_path=cred_path)

            # Save token
            import os
            os.makedirs(os.path.dirname(service.token_path), exist_ok=True)
            with open(service.token_path, 'w', encoding='utf-8') as f:
                f.write(creds.to_json())

            def on_success():
                self.owner.log_message('✅ Gmail authenticated and token stored.')
                self.owner.update_gmail_status()

                from tkinter import messagebox
                messagebox.showinfo('Gmail', 'Authentication successful! Token saved for future use.')

            self.owner.root.after(0, on_success)

        except Exception as e:
            def on_error():
                self.owner.log_message(f'🛑 Gmail authentication error: {e}')

                from tkinter import messagebox
                messagebox.showerror('Gmail', f'Authentication failed:\n{e}')

            self.owner.root.after(0, on_error)

    def _authenticate_gmail_auto(self) -> None:
        """Auto-authenticate Gmail (opens browser)."""
        cred_path = self.owner.gmail_credentials_path_var.get().strip()
        if not cred_path:
            from tkinter import messagebox
            messagebox.showwarning('Gmail', 'Please select credentials.json first.')
            return

        self.owner.log_message('🚀 Starting Gmail OAuth authentication...')

        import threading
        threading.Thread(target=self._authenticate_gmail_auto_worker, args=(cred_path,), daemon=True).start()

    def _authenticate_gmail_auto_worker(self, cred_path: str) -> None:
        """Worker thread for auto Gmail authentication."""
        try:
            from services.gmail_service import GmailService
            service = GmailService(credentials_path=cred_path)
            gmail_service = service.get_service()

            # Test the service
            gmail_service.users().labels().list(userId='me').execute()

            def on_success():
                self.owner.log_message('✅ Gmail authenticated and token stored.')
                self.owner.update_gmail_status()
                self.owner._save_gmail_credentials_path(cred_path)

                from tkinter import messagebox
                messagebox.showinfo('Gmail', 'Authentication successful! Token saved for future use.')

            self.owner.root.after(0, on_success)

        except Exception as e:
            def on_error():
                self.owner.log_message(f'🛑 Gmail authentication error: {e}')

                from tkinter import messagebox
                messagebox.showerror('Gmail', f'Authentication failed:\n{e}')

            self.owner.root.after(0, on_error)

    def _paste_lab_url(self) -> None:
        """Paste lab URL from clipboard."""
        try:
            clipboard_content = self.owner.root.clipboard_get()
            if clipboard_content:
                self.owner.lab_url_var.set(clipboard_content.strip())
                self.owner.log_message('📋 Lab URL pasted from clipboard')
        except Exception as e:
            self.owner.log_message(f'⚠️ Could not paste from clipboard: {e}')

    def _refresh_license(self) -> None:
        """Refresh license information."""
        self.owner.log_message('🔄 Refreshing license information...')
        self.owner.check_license_async()

    def _test_all_services(self) -> None:
        """Test all services and update status."""
        self.owner.log_message('🧪 Testing all services...')

        def worker():
            results = []

            # Test RandomUser API
            try:
                user_data = self.owner.random_user_service.get_random_user()
                if user_data:
                    results.append('✅ RandomUser API: Available')
                else:
                    results.append('🛑 RandomUser API: Failed to get data')
            except Exception as e:
                results.append(f'🛑 RandomUser API: Error - {e}')

            # Test Captcha Service
            try:
                # Basic initialization test
                if self.owner.captcha_service:
                    results.append('✅ Audio Captcha Solver: Ready (Multi-engine)')
                else:
                    results.append('🛑 Audio Captcha Solver: Not initialized')
            except Exception as e:
                results.append(f'🛑 Audio Captcha Solver: Error - {e}')

            # Test Firefox Relay if configured
            if self.owner.firefox_relay_service:
                try:
                    test_result = self.owner.firefox_relay_service.test_connection()
                    if test_result['success']:
                        results.append('✅ Firefox Relay: Connected')
                    else:
                        results.append(f"🛑 Firefox Relay: {test_result.get('error', 'Unknown error')}")
                except Exception as e:
                    results.append(f'🛑 Firefox Relay: Error - {e}')
            else:
                results.append('⚠️ Firefox Relay: Not configured')

            # Update UI
            def update_ui():
                for result in results:
                    self.owner.log_message(result)

                from tkinter import messagebox
                messagebox.showinfo('Service Test Results', '\n'.join(results))

            self.owner.root.after(0, update_ui)

        import threading
        threading.Thread(target=worker, daemon=True).start()