"""
Professional main window for AutoCloudSkill Application.

This module provides the primary GUI interface for the AutoCloudSkill application:
- Professional dark-themed interface using ttkbootstrap
- Multi-tab interface for organized functionality
- Real-time status updates and logging
- Professional automation control
- Comprehensive error handling and user feedback

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import asyncio
import threading
import time
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, Any
import sys

import tkinter as tk
from tkinter import messagebox, filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from automation.cloudskill_automation import (
    CloudSkillAutomation,
    RegistrationData,
    RegistrationMethod
)
from services.randomuser_service import RandomUserService
from services.firefox_relay_service import FirefoxRelayService
from services.captcha_service import CaptchaSolverService
from services.gmail_service import GmailService, SCOPES
from utils.logger import setup_application_logging, log_user_action, performance_monitor
from utils.validators import validate_user_data
from config.settings import settings
from config.licensing import LicenseManager
from config.constants import APP_NAME, VERSION, AUTHOR

# Import tab modules
from gui.tabs.video_generator_tab import VideoGeneratorTab
from gui.tabs.registration_tab import RegistrationTab
from gui.tabs.settings_tab import SettingsTab
from gui.tabs.logs_tab import LogsTab
from gui.tabs.about_tab import AboutTab


class MainWindow:
    """Professional main window for AutoCloudSkill application."""

    def __init__(self):
        """Initialize the main application window."""
        # Setup logging
        self.logger = setup_application_logging('MainWindow')

        # Initialize services
        self._initialize_services()

        # Initialize license manager
        self.license_manager = LicenseManager()
        self.license_info = None

        # Create main window
        self._create_main_window()

        # Setup variables and state
        self._setup_variables()
        self._setup_state()

        # Load persistent settings
        self._load_persistent_settings()

        # Build user interface
        self._build_interface()

        # Setup event handlers
        self._setup_event_handlers()

        # Initialize application
        self._initialize_application()

        log_user_action(self.logger, 'APPLICATION_START')

    def _initialize_services(self) -> None:
        """Initialize all required services."""
        try:
            self.random_user_service = RandomUserService()
            self.captcha_service = CaptchaSolverService()

            # Initialize Firefox Relay service
            try:
                self.firefox_relay_service = FirefoxRelayService()
            except ValueError as e:
                self.firefox_relay_service = None
                self.logger.warning(f'Firefox Relay service not available: {e}')

            self.automation = None

        except Exception as e:
            self.logger.error(f"Failed to initialize services: {e}")
            raise

    def _create_main_window(self) -> None:
        """Create and configure the main window."""
        self.root = ttk.Window(
            title=f'{APP_NAME} Professional v{VERSION}',
            themename='darkly',
            size=(800, 700),
            resizable=(True, True)
        )

        # Set window icon if available
        self._set_window_icon()

        # Center window on screen
        self._center_window()

    def _set_window_icon(self) -> None:
        """Set application icon from assets directory."""
        try:
            base_dir = self._get_application_path()
            assets_dir = base_dir / 'assets'

            # Try .ico first (Windows preferred)
            ico_path = assets_dir / 'logo.ico'
            if ico_path.exists():
                try:
                    self.root.iconbitmap(str(ico_path))
                    self.logger.info(f'Application icon set: {ico_path}')
                    return
                except Exception as e:
                    self.logger.debug(f'Failed to set .ico icon: {e}')

            # Try .png as fallback
            png_path = assets_dir / 'logo.png'
            if png_path.exists():
                try:
                    icon_image = tk.PhotoImage(file=str(png_path))
                    self._icon_image = icon_image  # Keep reference to prevent GC
                    self.root.iconphoto(True, icon_image)
                    self.logger.info(f'Application icon set: {png_path}')
                    return
                except Exception as e:
                    self.logger.debug(f'Failed to set .png icon: {e}')

            self.logger.debug('No application icon found in assets directory')

        except Exception as e:
            self.logger.debug(f'Icon setup failed: {e}')

    def _get_application_path(self) -> Path:
        """Get application base path (compatible with PyInstaller)."""
        if getattr(sys, 'frozen', False):
            # Running as bundled executable
            if hasattr(sys, '_MEIPASS'):
                return Path(sys._MEIPASS)
            else:
                return Path(sys.executable).parent
        else:
            # Running as script
            return Path(__file__).resolve().parent.parent

    def _center_window(self) -> None:
        """Center window on screen."""
        self.root.update_idletasks()

        # Get window dimensions
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        # Calculate center position
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)

        # Set window position
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def _setup_variables(self) -> None:
        """Setup all tkinter variables."""
        # User data variables
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.company_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.password_confirm_var = tk.StringVar()

        # Service configuration variables
        self.firefox_api_key_var = tk.StringVar()
        self.gmail_credentials_path_var = tk.StringVar()
        self.gmail_auth_url_var = tk.StringVar()
        self.gmail_auth_code_var = tk.StringVar()

        # Settings variables
        self.extension_mode_var = tk.BooleanVar(value=False)
        self.show_password_var = tk.BooleanVar(value=False)
        self.lab_url_var = tk.StringVar()
        self.auto_start_lab_var = tk.BooleanVar(value=False)

        # Application state variables
        self.status_var = tk.StringVar(value='Initializing...')

        # License variables
        self.license_plan_var = tk.StringVar(value='Checking...')
        self.license_expiry_var = tk.StringVar(value='Checking...')

    def _setup_state(self) -> None:
        """Setup application state."""
        self.is_running = False
        self.data_generated = False

        # Gmail OAuth state
        self._gmail_oauth_flow = None

        # GenAI API key event handling
        self._genai_api_key_event = threading.Event()
        self._latest_genai_api_key = None

        # Progress tracking
        self.gmail_progress_running = False
        self.gmail_progress_job = None

    def _load_persistent_settings(self) -> None:
        """Load persistent settings from temporary storage."""
        try:
            # Load Firefox Relay API key
            relay_key = self._load_firefox_relay_key()
            if relay_key:
                self.firefox_api_key_var.set(relay_key)

            # Load Gmail credentials path
            gmail_cred = self._load_gmail_credentials_path()
            if gmail_cred:
                self.gmail_credentials_path_var.set(gmail_cred)

            # Load lab URL
            lab_url = self._load_lab_url()
            if lab_url:
                self.lab_url_var.set(lab_url)

            # Load auto start lab setting
            auto_start = self._load_auto_start_lab()
            if auto_start is not None:
                self.auto_start_lab_var.set(auto_start)

            # Load extension mode setting
            extension_mode = self._load_extension_mode()
            if extension_mode is not None:
                self.extension_mode_var.set(extension_mode)

        except Exception as e:
            self.logger.warning(f"Failed to load persistent settings: {e}")

    def _build_interface(self) -> None:
        """Build the complete user interface."""
        # Main container
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=BOTH, expand=True)

        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=BOTH, expand=True)

        # Create tabs
        self._create_tabs()

        # Create bottom controls
        self._create_bottom_controls(main_frame)

    def _create_tabs(self) -> None:
        """Create all application tabs."""
        try:
            # Registration tab
            self.registration_tab = RegistrationTab(self, self.notebook)

            # Video Generator tab
            self.video_tab = VideoGeneratorTab(
                self.root,
                self.notebook,
                self.log_message,
                self.request_new_api_key_and_wait
            )

            # Settings tab
            self.settings_tab = SettingsTab(self, self.notebook)

            # Logs tab
            self.logs_tab = LogsTab(self, self.notebook)

            # About tab
            self.about_tab = AboutTab(self, self.notebook)

        except Exception as e:
            self.logger.error(f"Failed to create tabs: {e}")
            self.log_message(f'🛑 Failed to create application tabs: {e}')

    def _create_bottom_controls(self, parent: ttk.Frame) -> None:
        """Create bottom control panel."""
        bottom_frame = ttk.Frame(parent)
        bottom_frame.pack(fill=X, pady=(10, 0))

        # Status frame
        status_frame = ttk.Frame(bottom_frame)
        status_frame.pack(fill=X, pady=(0, 10))

        ttk.Label(status_frame, text='Status:', bootstyle=INFO).pack(side=LEFT)
        self.status_label = ttk.Label(
            status_frame,
            textvariable=self.status_var,
            bootstyle=SUCCESS
        )
        self.status_label.pack(side=LEFT, padx=(5, 0))

        # Button frame
        button_frame = ttk.Frame(bottom_frame)
        button_frame.pack(fill=X)

        # Control buttons
        self.refresh_btn = ttk.Button(
            button_frame,
            text='Refresh Data',
            command=self.refresh_generated_data,
            bootstyle=INFO,
            width=15
        )
        self.refresh_btn.pack(side=LEFT, padx=(0, 5))

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

        # Exit button
        exit_btn = ttk.Button(
            button_frame,
            text='Exit',
            command=self.on_closing,
            bootstyle=DANGER,
            width=15
        )
        exit_btn.pack(side=RIGHT)

    def _setup_event_handlers(self) -> None:
        """Setup event handlers and variable traces."""
        try:
            # Variable traces for persistent storage
            self.lab_url_var.trace_add(
                'write',
                lambda *args: self._save_lab_url(self.lab_url_var.get())
            )

            self.auto_start_lab_var.trace_add(
                'write',
                lambda *args: self._save_auto_start_lab(self.auto_start_lab_var.get())
            )

            self.extension_mode_var.trace_add(
                'write',
                lambda *args: self._save_extension_mode(self.extension_mode_var.get())
            )

        except Exception as e:
            self.logger.warning(f"Failed to setup event handlers: {e}")

    def _initialize_application(self) -> None:
        """Initialize application after UI is built."""
        # Update Gmail status
        self.root.after(200, self.update_gmail_status)

        # Auto-initialize Firefox Relay if API key is available
        self.root.after(500, self.auto_initialize_firefox_relay)

        # Check license asynchronously
        self.root.after(1000, self.check_license_async)

        # Auto-generate initial data
        self.root.after(2000, self.auto_generate_initial_data)

    @performance_monitor("auto_generate_data")
    def auto_generate_initial_data(self) -> None:
        """Auto-generate initial user data."""
        self.log_message('🔄 Auto-generating initial data...')
        self.status_var.set('Generating data...')

        try:
            # Generate random user data
            user_data = self.random_user_service.get_random_user(
                gender=settings.DEFAULT_GENDER,
                nationalities=settings.DEFAULT_NATIONALITIES
            )

            if not user_data:
                raise Exception('Failed to get random user data')

            # Set user data
            self.first_name_var.set(user_data['first_name'])
            self.last_name_var.set(user_data['last_name'])

            # Generate company name
            company = self.random_user_service.generate_company_name()
            self.company_var.set(company)

            # Generate password
            password = self.random_user_service.generate_password(
                settings.DEFAULT_PASSWORD_LENGTH
            )
            self.password_var.set(password)
            self.password_confirm_var.set(password)

            # Email will be generated from Firefox Relay
            self.email_var.set('Will be generated from Firefox Relay')

            self.log_message('✅ Initial data generated successfully!')

            # Update state
            self.data_generated = True
            self._update_ui_state()

            log_user_action(
                self.logger,
                'AUTO_GENERATE_DATA',
                {
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                    'company': company
                }
            )

        except Exception as e:
            error_msg = f'Error generating initial data: {str(e)}'
            self.log_message(f'🛑 {error_msg}')
            self.status_var.set('Error generating data')
            self.logger.error(error_msg)

    def refresh_generated_data(self) -> None:
        """Refresh/regenerate user data manually."""
        self.log_message('🔄 Refreshing data...')
        self.status_var.set('Refreshing...')
        self.auto_generate_initial_data()

    def auto_initialize_firefox_relay(self) -> None:
        """Auto-initialize Firefox Relay service if API key is available."""
        api_key = self.firefox_api_key_var.get().strip()
        if not api_key:
            return

        def worker():
            try:
                # Test the API key
                test_service = FirefoxRelayService(api_key=api_key)
                results = test_service.test_connection()

                if results.get('success'):
                    def on_success():
                        self.firefox_relay_service = test_service
                        self.log_message('✅ Firefox Relay auto-initialized successfully')
                        self.log_message(f"✅ Using URL: {results.get('working_url', 'N/A')}")
                        self._update_ui_state()

                    self.root.after(0, on_success)
                else:
                    def on_failure():
                        self.log_message('⚠️ Firefox Relay auto-initialization failed')

                    self.root.after(0, on_failure)

            except Exception as e:
                self.root.after(0, lambda: self.log_message(f'⚠️ Auto-init Firefox Relay failed: {e}'))

        threading.Thread(target=worker, daemon=True).start()

    def check_license_async(self) -> None:
        """Check license status asynchronously."""
        def worker():
            try:
                license_info = self.license_manager.ensure_license()

                def apply_license():
                    self.license_info = license_info

                    # Update license display variables
                    plan = str(license_info.plan or 'Unknown')
                    self.license_plan_var.set(plan)

                    if license_info.expires_at:
                        try:
                            expiry_date = datetime.fromisoformat(
                                license_info.expires_at.replace('Z', '+00:00')
                            )
                            self.license_expiry_var.set(expiry_date.strftime('%d/%m/%Y'))
                        except Exception:
                            self.license_expiry_var.set('Unknown')
                    else:
                        self.license_expiry_var.set('Unknown')

                    # Log license status
                    if license_info.is_allowed:
                        if plan.lower() == 'free':
                            self.log_message('🔒 License plan is \'free\' - limited functionality')
                        else:
                            self.log_message('🔓 License validated successfully')
                    else:
                        self.log_message(f"🔒 License not allowed: {license_info.status}")

                    self._update_ui_state()

                self.root.after(0, apply_license)

            except Exception as e:
                def on_error():
                    self.license_info = None
                    self.license_plan_var.set('Error')
                    self.license_expiry_var.set('Error')
                    self.log_message(f'🛑 License check failed: {e}')
                    self._update_ui_state()

                self.root.after(0, on_error)

        threading.Thread(target=worker, daemon=True).start()

    def _update_ui_state(self) -> None:
        """Update UI state based on current conditions."""
        try:
            # Check if registration is allowed
            allowed = True
            if self.license_info:
                plan = str(self.license_info.plan or '').lower()
                allowed = self.license_info.is_allowed and plan != 'free'

            # Update start button state
            can_start = (
                allowed and
                self.data_generated and
                not self.is_running and
                self.firefox_relay_service is not None
            )

            self.start_btn.config(state=NORMAL if can_start else DISABLED)

            # Update status
            if not allowed:
                self.status_var.set('License required')
            elif not self.data_generated:
                self.status_var.set('Generating data...')
            elif not self.firefox_relay_service:
                self.status_var.set('Firefox Relay API key required')
            elif self.is_running:
                self.status_var.set('Running...')
            else:
                self.status_var.set('Ready')

        except Exception as e:
            self.logger.error(f"Failed to update UI state: {e}")

    def update_gmail_status(self) -> None:
        """Update Gmail service status display."""
        try:
            # Check for existing token
            gmail_service = GmailService()
            token_exists = Path(gmail_service.token_path).exists()

            cred_path = self.gmail_credentials_path_var.get().strip()

            if token_exists:
                status_text = 'Gmail: ✅ Ready (token found)'
                status_style = SUCCESS
            elif cred_path:
                status_text = 'Gmail: ⚙️ Credentials set (authenticate to enable)'
                status_style = INFO
            else:
                status_text = 'Gmail: 🛑 Not configured'
                status_style = WARNING

            # Update status in settings tab if available
            if hasattr(self, 'settings_tab') and hasattr(self.settings_tab, 'gmail_status_label'):
                self.settings_tab.gmail_status_label.config(
                    text=status_text,
                    bootstyle=status_style
                )

        except Exception as e:
            self.logger.warning(f"Failed to update Gmail status: {e}")

    @performance_monitor("start_automation")
    def start_automation(self) -> None:
        """Start the automation process."""
        if self.is_running:
            return

        # Validate Firefox Relay service
        if not self.firefox_relay_service:
            api_key = self.firefox_api_key_var.get().strip()
            if not api_key:
                messagebox.showerror(
                    'Error',
                    'Please set and test Firefox Relay API key first!'
                )
                return

            try:
                self.firefox_relay_service = FirefoxRelayService(api_key=api_key)
            except Exception as e:
                messagebox.showerror(
                    'Error',
                    f'Failed to initialize Firefox Relay service:\n{e}'
                )
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
            messagebox.showerror('Error', 'Password confirmation does not match!')
            return

        # Create Firefox Relay email
        self.log_message('🔄 Creating Firefox Relay email...')
        self.status_var.set('Creating email...')

        try:
            # Auto-purge old masks if needed
            purge_result = self.firefox_relay_service.auto_purge_if_limit_reached(limit=5)
            if purge_result.get('purged'):
                self.log_message(
                    f"🧹 Auto purge triggered: "
                    f"deleted={purge_result.get('deleted', 0)}, "
                    f"failed={len(purge_result.get('failed_ids', []))}"
                )

            # Create new mask
            mask = self.firefox_relay_service.create_relay_mask(
                f"AutoCloudSkill - {datetime.now().strftime('%Y%m%d_%H%M%S')}"
            )

            if not mask:
                raise Exception('Failed to create Firefox Relay email')

            relay_email = mask['full_address']
            user_data['email'] = relay_email
            self.email_var.set(relay_email)

            self.log_message(f'✅ Created relay email: {relay_email}')

        except Exception as e:
            error_msg = f'Failed to create relay email: {str(e)}'
            self.log_message(f'🛑 {error_msg}')
            messagebox.showerror('Error', error_msg)
            return

        # Start automation
        self.is_running = True
        self.start_btn.config(state=DISABLED)
        self.stop_btn.config(state=NORMAL)
        self.status_var.set('Running...')

        self.log_message('▶️ Starting automation...')

        # Run automation in separate thread
        thread = threading.Thread(
            target=self._run_automation_worker,
            args=(user_data,),
            daemon=True
        )
        thread.start()

    def _run_automation_worker(self, user_data: Dict[str, str]) -> None:
        """Run automation process in worker thread."""
        try:
            # Check Gmail configuration
            cred_path = self.gmail_credentials_path_var.get().strip()
            gmail_service = GmailService(credentials_path=cred_path if cred_path else None)
            gmail_ready = Path(gmail_service.token_path).exists() or bool(cred_path)

            # Initialize automation
            registration_data = RegistrationData(
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                email=user_data['email'],
                company=user_data['company'],
                password=user_data['password'],
                method=RegistrationMethod.FIREFOX_RELAY
            )

            self.automation = CloudSkillAutomation(
                headless=False,
                captcha_solver=self.captcha_service,
                keep_browser_open=gmail_ready,
                extension_mode=self.extension_mode_var.get()
            )

            # Run registration
            result = asyncio.run(self.automation.register_account_async(registration_data))

            if result.success:
                self.log_message('✅ Registration completed successfully!')
                self.root.after(0, lambda: self.status_var.set('Registration completed'))

                # Handle email confirmation if Gmail is ready
                if gmail_ready:
                    self._handle_email_confirmation(user_data, gmail_service)
                else:
                    self.log_message('ℹ️ Gmail not configured - skipping email confirmation')

            else:
                error_msg = result.error_message or 'Unknown registration error'
                self.log_message(f'🛑 Registration failed: {error_msg}')
                self.root.after(0, lambda: self.status_var.set('Registration failed'))
                self.root.after(0, lambda: messagebox.showerror('Error', error_msg))

        except Exception as e:
            error_msg = f'Automation error: {str(e)}'
            self.log_message(f'🛑 {error_msg}')
            self.root.after(0, lambda: self.status_var.set('Error'))
            self.root.after(0, lambda: messagebox.showerror('Error', error_msg))

        finally:
            self.root.after(0, self._automation_finished)

    def _handle_email_confirmation(self, user_data: Dict[str, str], gmail_service: GmailService) -> None:
        """Handle email confirmation process."""
        try:
            self.log_message('⏳ Checking Gmail inbox for confirmation email...')

            # Wait for confirmation email
            timeout_sec = 300  # 5 minutes
            poll_interval_sec = 5

            self.root.after(0, lambda: self._start_gmail_progress(timeout_sec, poll_interval_sec))

            try:
                message = gmail_service.wait_for_email(
                    target_email=user_data['email'],
                    subject_contains='Welcome to Google Cloud Skills Boost',
                    from_contains='noreply@cloudskillsboost.google',
                    timeout_sec=timeout_sec,
                    poll_interval_sec=poll_interval_sec
                )
            finally:
                self.root.after(0, self._stop_gmail_progress)

            if message:
                # Extract confirmation links
                links = gmail_service.extract_links(message)
                self.log_message(f"✅ Confirmation email found. Links: {len(links)}")

                if links:
                    # Choose best confirmation link
                    chosen_link = self._choose_confirmation_link(links)

                    self.log_message(f'🔗 Opening confirmation link: {chosen_link[:100]}...')

                    # Process confirmation
                    confirm_result = asyncio.run(
                        self.automation.confirm_via_link_async(
                            chosen_link,
                            user_data['password'],
                            user_data['email']
                        )
                    )

                    if confirm_result.success:
                        self.log_message('✅ Email confirmation completed successfully!')

                        # Auto-start lab if configured
                        if self.auto_start_lab_var.get():
                            self._auto_start_lab()

                    else:
                        error_msg = confirm_result.error_message or 'Unknown confirmation error'
                        self.log_message(f'🛑 Email confirmation failed: {error_msg}')

                else:
                    self.log_message('⚠️ No confirmation links found in email')

            else:
                self.log_message('🛑 No confirmation email received within timeout')

        except Exception as e:
            self.log_message(f'🛑 Email confirmation error: {e}')

    def _choose_confirmation_link(self, links: list) -> str:
        """Choose the best confirmation link from available links."""
        # Prefer Google redirect links
        for link in links:
            if 'notifications.googleapis.com/email/redirect' in link.lower():
                return link

        # Fall back to CloudSkills links
        for link in links:
            link_lower = link.lower()
            if ('cloudskillsboost.google' in link_lower or
                '/users/confirmation' in link_lower or
                'confirm' in link_lower):
                return link

        # Use first link as last resort
        return links[0] if links else ""

    def _auto_start_lab(self) -> None:
        """Auto-start lab if URL is configured."""
        try:
            lab_url = self.lab_url_var.get().strip()
            if not lab_url:
                self.log_message('⚠️ Lab URL not configured - skipping auto-start')
                return

            self.log_message('🚀 Starting lab automatically...')

            # Start lab
            lab_result = asyncio.run(self.automation.start_lab_async(lab_url))

            if lab_result.success:
                self.log_message(f"✅ Lab started successfully: {lab_result.lab_url}")

                # Handle API key if provided
                if lab_result.api_key:
                    self.root.after(0, lambda: self.set_genai_api_key(lab_result.api_key))
                    self.log_message('🔑 GenAI API key received and forwarded to Video Generator')

            else:
                error_msg = lab_result.error_message or 'Unknown lab start error'
                self.log_message(f'🛑 Lab start failed: {error_msg}')

        except Exception as e:
            self.log_message(f'🛑 Auto-start lab error: {e}')

    def _start_gmail_progress(self, total_sec: int, interval_sec: int) -> None:
        """Start Gmail progress indicator."""
        try:
            self.gmail_poll_total = max(1, int(total_sec))
            self.gmail_poll_interval = max(1, int(interval_sec))
            self.gmail_poll_start = time.time()
            self.gmail_progress_running = True

            # Update progress in logs tab if available
            if hasattr(self, 'logs_tab'):
                self.logs_tab.start_progress_indicator(total_sec)

            self._update_gmail_progress()

        except Exception as e:
            self.logger.warning(f"Could not start Gmail progress: {e}")

    def _update_gmail_progress(self) -> None:
        """Update Gmail progress indicator."""
        if not self.gmail_progress_running:
            return

        try:
            now = time.time()
            elapsed = now - getattr(self, 'gmail_poll_start', now)
            total = getattr(self, 'gmail_poll_total', 1)

            remaining = max(0, total - elapsed)

            # Update logs tab progress if available
            if hasattr(self, 'logs_tab'):
                self.logs_tab.update_progress(elapsed, total, remaining)

            if elapsed < total and self.gmail_progress_running:
                self.gmail_progress_job = self.root.after(500, self._update_gmail_progress)
            else:
                self._stop_gmail_progress()

        except Exception as e:
            self.logger.warning(f"Gmail progress update error: {e}")

    def _stop_gmail_progress(self) -> None:
        """Stop Gmail progress indicator."""
        self.gmail_progress_running = False

        if self.gmail_progress_job:
            try:
                self.root.after_cancel(self.gmail_progress_job)
            except Exception:
                pass
            self.gmail_progress_job = None

        # Stop progress in logs tab if available
        if hasattr(self, 'logs_tab'):
            self.logs_tab.stop_progress_indicator()

    def stop_automation(self) -> None:
        """Stop automation process."""
        self.log_message('⛔ Stopping automation...')
        self.is_running = False

        if self.automation:
            try:
                self.automation.shutdown()
            except Exception as e:
                self.logger.warning(f"Error stopping automation: {e}")

        self._automation_finished()

    def _automation_finished(self) -> None:
        """Handle automation completion."""
        self.is_running = False
        self.stop_btn.config(state=DISABLED)
        self._update_ui_state()

        if self.status_var.get() in ['Running...', 'Error']:
            self.status_var.set('Ready')

    def set_genai_api_key(self, api_key: str) -> None:
        """Set GenAI API key and forward to Video Generator tab."""
        try:
            if hasattr(self, 'video_tab') and self.video_tab:
                self.video_tab.set_api_key(api_key)
                self.log_message('🔑 GenAI API key forwarded to Video Generator tab')

                # Notify waiting threads
                self._latest_genai_api_key = api_key.strip()
                self._genai_api_key_event.set()
            else:
                self.log_message('⚠️ Video Generator tab not initialized - API key not forwarded')

        except Exception as e:
            self.log_message(f'🛑 Failed to set GenAI API key: {e}')

    def request_new_api_key_and_wait(self, reason: str, timeout_seconds: int = 600) -> Optional[str]:
        """Request new API key and wait for it (blocking call for Video Generator)."""
        try:
            # Clear previous event
            self._genai_api_key_event.clear()
            self._latest_genai_api_key = None

            # Request new registration
            self.root.after(0, lambda: self.log_message(
                f'⏸️ Video tab paused: {reason}. Re-registering for new API key...'
            ))
            self.root.after(0, self.refresh_generated_data)
            self.root.after(0, self.start_automation)

            # Wait for new API key
            success = self._genai_api_key_event.wait(timeout=max(1, int(timeout_seconds)))

            if success:
                return self._latest_genai_api_key
            else:
                self.root.after(0, lambda: self.log_message('🛑 Timeout waiting for new GenAI API key'))
                return None

        except Exception as e:
            self.root.after(0, lambda: self.log_message(f'🛑 API key request error: {e}'))
            return None

    def log_message(self, message: str) -> None:
        """Log message to application log."""
        try:
            timestamp = datetime.now().strftime('%H:%M:%S')
            log_entry = f'[{timestamp}] {message}'

            # Log to application logger
            self.logger.info(message)

            # Forward to logs tab if available
            if hasattr(self, 'logs_tab'):
                self.logs_tab.add_log_message(log_entry)

        except Exception as e:
            self.logger.error(f"Failed to log message: {e}")

    # Persistent settings methods
    def _get_temp_file_path(self, filename: str) -> Path:
        """Get path for temporary settings file."""
        return Path(tempfile.gettempdir()) / f'autocloudskill_{filename}.txt'

    def _load_firefox_relay_key(self) -> Optional[str]:
        """Load Firefox Relay API key from temporary storage."""
        try:
            path = self._get_temp_file_path('firefox_api_key')
            if path.exists():
                return path.read_text(encoding='utf-8').strip()
        except Exception:
            pass
        return None

    def _save_firefox_relay_key(self, api_key: str) -> None:
        """Save Firefox Relay API key to temporary storage."""
        try:
            path = self._get_temp_file_path('firefox_api_key')
            path.write_text(api_key.strip(), encoding='utf-8')
        except Exception:
            pass

    def _load_gmail_credentials_path(self) -> Optional[str]:
        """Load Gmail credentials path from temporary storage."""
        try:
            path = self._get_temp_file_path('gmail_credentials_path')
            if path.exists():
                return path.read_text(encoding='utf-8').strip()
        except Exception:
            pass
        return None

    def _save_gmail_credentials_path(self, cred_path: str) -> None:
        """Save Gmail credentials path to temporary storage."""
        try:
            path = self._get_temp_file_path('gmail_credentials_path')
            path.write_text(cred_path.strip(), encoding='utf-8')
        except Exception:
            pass

    def _load_lab_url(self) -> Optional[str]:
        """Load lab URL from temporary storage."""
        try:
            path = self._get_temp_file_path('lab_url')
            if path.exists():
                return path.read_text(encoding='utf-8').strip()
        except Exception:
            pass
        return None

    def _save_lab_url(self, url: str) -> None:
        """Save lab URL to temporary storage."""
        try:
            path = self._get_temp_file_path('lab_url')
            path.write_text(url.strip(), encoding='utf-8')
        except Exception:
            pass

    def _load_auto_start_lab(self) -> Optional[bool]:
        """Load auto start lab setting from temporary storage."""
        try:
            path = self._get_temp_file_path('auto_start_lab')
            if path.exists():
                value = path.read_text(encoding='utf-8').strip().lower()
                return value in ['1', 'true', 'yes', 'on']
        except Exception:
            pass
        return None

    def _save_auto_start_lab(self, value: bool) -> None:
        """Save auto start lab setting to temporary storage."""
        try:
            path = self._get_temp_file_path('auto_start_lab')
            path.write_text('1' if value else '0', encoding='utf-8')
        except Exception:
            pass

    def _load_extension_mode(self) -> Optional[bool]:
        """Load extension mode setting from temporary storage."""
        try:
            path = self._get_temp_file_path('extension_mode')
            if path.exists():
                value = path.read_text(encoding='utf-8').strip().lower()
                return value in ['1', 'true', 'yes', 'on']
        except Exception:
            pass
        return None

    def _save_extension_mode(self, value: bool) -> None:
        """Save extension mode setting to temporary storage."""
        try:
            path = self._get_temp_file_path('extension_mode')
            path.write_text('1' if value else '0', encoding='utf-8')
        except Exception:
            pass

    def on_closing(self) -> None:
        """Handle application closing."""
        if self.is_running:
            if messagebox.askokcancel(
                'Quit',
                'Automation is running. Are you sure you want to quit?'
            ):
                self.stop_automation()
                self.root.after(1000, self.root.destroy)
        else:
            log_user_action(self.logger, 'APPLICATION_EXIT')
            self.root.destroy()

    def run(self) -> None:
        """Run the application main loop."""
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.root.mainloop()


if __name__ == '__main__':
    app = MainWindow()
    app.run()