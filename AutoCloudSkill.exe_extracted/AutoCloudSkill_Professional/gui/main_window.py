"""
Main Window for Auto Cloud Skill Registration application.

Professional implementation of the main GUI window with clean architecture,
proper event handling, and comprehensive tab management.
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import threading
import asyncio
from pathlib import Path
import json
import tempfile
from typing import Dict, Optional, Any
import logging

from config.constants import APP_NAME, VERSION, AUTHOR
from config.licensing import ensure_license, get_machine_id, get_license_info
from services.randomuser_service import RandomUserService
from services.firefox_relay_service import FirefoxRelayService
from services.captcha_service import CaptchaSolverService
from automation.cloudskill_automation import CloudSkillAutomation
from utils.logger import setup_logger, log_user_action
from utils.validators import validate_user_data, ValidationError

logger = logging.getLogger(__name__)

class MainWindow:
    """
    Main application window with professional GUI implementation.

    This class provides the primary user interface for the Auto Cloud Skill
    Registration application with clean tab-based navigation and proper
    state management.
    """

    def __init__(self):
        """Initialize the main window and all components."""
        self.logger = setup_logger('MainWindow')
        self.logger.info("Initializing main window")

        # Initialize services
        self._initialize_services()

        # Initialize GUI
        self._initialize_gui()

        # Setup variables and state
        self._setup_variables()

        # Load saved settings
        self._load_settings()

        # Build UI
        self._build_interface()

        # Setup event handlers
        self._setup_event_handlers()

        self.logger.info("Main window initialization complete")

    def _initialize_services(self) -> None:
        """Initialize all external services."""
        try:
            # Random user service
            self.random_user_service = RandomUserService()

            # Captcha solver service
            self.captcha_service = CaptchaSolverService()

            # Firefox Relay service (may fail if no API key)
            try:
                self.firefox_relay_service = FirefoxRelayService()
            except ValueError as e:
                self.firefox_relay_service = None
                self.logger.warning(f"Firefox Relay service not available: {e}")

            # Automation service (initialized on demand)
            self.automation = None

            self.logger.info("Services initialized successfully")

        except Exception as e:
            self.logger.error(f"Service initialization failed: {e}")

    def _initialize_gui(self) -> None:
        """Initialize the main GUI window."""
        try:
            # Create main window
            self.root = ttk.Window(
                title=f"{APP_NAME} v{VERSION}",
                themename='darkly',
                size=(1000, 700),
                resizable=(True, True)
            )

            # Set window icon if available
            self._set_application_icon()

            # Center window on screen
            self._center_window()

            self.logger.info("GUI window initialized")

        except Exception as e:
            self.logger.error(f"GUI initialization failed: {e}")
            raise

    def _setup_variables(self) -> None:
        """Setup tkinter variables for data binding."""
        # API Configuration
        self.firefox_api_key_var = tk.StringVar()
        self.gmail_credentials_path_var = tk.StringVar()

        # Automation Settings
        self.lab_url_var = tk.StringVar()
        self.auto_start_lab_var = tk.BooleanVar()
        self.extension_mode_var = tk.BooleanVar()
        self.headless_mode_var = tk.BooleanVar()

        # User Data
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.company_var = tk.StringVar()

        # Status
        self.status_var = tk.StringVar(value="Ready")
        self.progress_var = tk.DoubleVar()

        self.logger.debug("Variables initialized")

    def _load_settings(self) -> None:
        """Load saved settings from temporary storage."""
        try:
            # Load Firefox Relay API key
            api_key = self._load_temp_setting('firefox_api_key')
            if api_key:
                self.firefox_api_key_var.set(api_key)
                if self.firefox_relay_service:
                    self.firefox_relay_service.set_api_key(api_key)

            # Load Gmail credentials path
            gmail_creds = self._load_temp_setting('gmail_credentials_path')
            if gmail_creds:
                self.gmail_credentials_path_var.set(gmail_creds)

            # Load lab URL
            lab_url = self._load_temp_setting('lab_url')
            if lab_url:
                self.lab_url_var.set(lab_url)

            # Load boolean settings
            auto_start = self._load_temp_setting('auto_start_lab')
            if auto_start is not None:
                self.auto_start_lab_var.set(bool(auto_start))

            extension_mode = self._load_temp_setting('extension_mode')
            if extension_mode is not None:
                self.extension_mode_var.set(bool(extension_mode))

            self.logger.info("Settings loaded successfully")

        except Exception as e:
            self.logger.warning(f"Could not load settings: {e}")

    def _build_interface(self) -> None:
        """Build the complete user interface."""
        try:
            # Create main container
            main_frame = ttk.Frame(self.root, padding=10)
            main_frame.pack(fill=BOTH, expand=True)

            # Create header
            self._create_header(main_frame)

            # Create tab notebook
            self._create_tab_notebook(main_frame)

            # Create status bar
            self._create_status_bar(main_frame)

            self.logger.info("Interface built successfully")

        except Exception as e:
            self.logger.error(f"Interface building failed: {e}")
            raise

    def _create_header(self, parent: ttk.Frame) -> None:
        """Create application header."""
        header_frame = ttk.Frame(parent)
        header_frame.pack(fill=X, pady=(0, 10))

        # Application title
        title_label = ttk.Label(
            header_frame,
            text=f"{APP_NAME} v{VERSION}",
            font=("Arial", 16, "bold")
        )
        title_label.pack(side=LEFT)

        # License info
        license_info = get_license_info()
        machine_id = license_info.get('machine_id', '')[:8]
        license_label = ttk.Label(
            header_frame,
            text=f"Machine ID: {machine_id}... | Plan: {license_info.get('plan', 'Unknown')}",
            font=("Arial", 9)
        )
        license_label.pack(side=RIGHT)

    def _create_tab_notebook(self, parent: ttk.Frame) -> None:
        """Create the main tab notebook."""
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack(fill=BOTH, expand=True, pady=(0, 10))

        # Create tabs
        self._create_registration_tab()
        self._create_settings_tab()
        self._create_logs_tab()
        self._create_about_tab()

    def _create_registration_tab(self) -> None:
        """Create the registration tab."""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="Registration")

        # Create two-column layout
        left_frame = ttk.Frame(tab_frame)
        left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

        right_frame = ttk.Frame(tab_frame)
        right_frame.pack(side=RIGHT, fill=Y, padx=(10, 0))

        # Left column: User data form
        self._create_user_data_form(left_frame)

        # Right column: Actions and status
        self._create_action_panel(right_frame)

    def _create_user_data_form(self, parent: ttk.Frame) -> None:
        """Create user data input form."""
        # Form header
        form_label = ttk.Label(parent, text="User Registration Data", font=("Arial", 12, "bold"))
        form_label.pack(anchor=W, pady=(0, 10))

        # Auto-generate button
        generate_frame = ttk.Frame(parent)
        generate_frame.pack(fill=X, pady=(0, 10))

        generate_btn = ttk.Button(
            generate_frame,
            text="Generate Random User",
            command=self._generate_random_user,
            bootstyle=SUCCESS
        )
        generate_btn.pack(side=LEFT)

        # Clear button
        clear_btn = ttk.Button(
            generate_frame,
            text="Clear Form",
            command=self._clear_form,
            bootstyle=SECONDARY
        )
        clear_btn.pack(side=LEFT, padx=(10, 0))

        # Form fields
        form_frame = ttk.LabelFrame(parent, text="Personal Information", padding=15)
        form_frame.pack(fill=X, pady=(0, 10))

        # First Name
        ttk.Label(form_frame, text="First Name:").grid(row=0, column=0, sticky=W, pady=5)
        first_name_entry = ttk.Entry(form_frame, textvariable=self.first_name_var, width=30)
        first_name_entry.grid(row=0, column=1, sticky=EW, pady=5, padx=(10, 0))

        # Last Name
        ttk.Label(form_frame, text="Last Name:").grid(row=1, column=0, sticky=W, pady=5)
        last_name_entry = ttk.Entry(form_frame, textvariable=self.last_name_var, width=30)
        last_name_entry.grid(row=1, column=1, sticky=EW, pady=5, padx=(10, 0))

        # Email
        ttk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky=W, pady=5)
        email_entry = ttk.Entry(form_frame, textvariable=self.email_var, width=30)
        email_entry.grid(row=2, column=1, sticky=EW, pady=5, padx=(10, 0))

        # Company
        ttk.Label(form_frame, text="Company:").grid(row=3, column=0, sticky=W, pady=5)
        company_entry = ttk.Entry(form_frame, textvariable=self.company_var, width=30)
        company_entry.grid(row=3, column=1, sticky=EW, pady=5, padx=(10, 0))

        # Configure grid weights
        form_frame.columnconfigure(1, weight=1)

    def _create_action_panel(self, parent: ttk.Frame) -> None:
        """Create action buttons and status panel."""
        # Action buttons
        action_frame = ttk.LabelFrame(parent, text="Actions", padding=15)
        action_frame.pack(fill=X, pady=(0, 10))

        # Register button
        self.register_btn = ttk.Button(
            action_frame,
            text="Start Registration",
            command=self._start_registration,
            bootstyle=PRIMARY,
            width=20
        )
        self.register_btn.pack(fill=X, pady=5)

        # Stop button
        self.stop_btn = ttk.Button(
            action_frame,
            text="Stop Process",
            command=self._stop_registration,
            bootstyle=DANGER,
            width=20,
            state=DISABLED
        )
        self.stop_btn.pack(fill=X, pady=5)

        # Progress frame
        progress_frame = ttk.LabelFrame(parent, text="Progress", padding=15)
        progress_frame.pack(fill=X, pady=(0, 10))

        # Progress bar
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            variable=self.progress_var,
            mode='determinate',
            length=200
        )
        self.progress_bar.pack(fill=X, pady=5)

        # Progress label
        self.progress_label = ttk.Label(progress_frame, text="Ready")
        self.progress_label.pack(fill=X, pady=5)

    def _create_settings_tab(self) -> None:
        """Create the settings tab."""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="Settings")

        # Create scrollable frame
        canvas = tk.Canvas(tab_frame)
        scrollbar = ttk.Scrollbar(tab_frame, orient=VERTICAL, command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # API Settings
        api_frame = ttk.LabelFrame(scrollable_frame, text="API Configuration", padding=15)
        api_frame.pack(fill=X, pady=10, padx=10)

        # Firefox Relay API Key
        ttk.Label(api_frame, text="Firefox Relay API Key:").grid(row=0, column=0, sticky=W, pady=5)
        api_key_entry = ttk.Entry(api_frame, textvariable=self.firefox_api_key_var, width=50, show="*")
        api_key_entry.grid(row=0, column=1, sticky=EW, pady=5, padx=(10, 0))

        test_api_btn = ttk.Button(
            api_frame,
            text="Test",
            command=self._test_firefox_api,
            bootstyle=INFO,
            width=10
        )
        test_api_btn.grid(row=0, column=2, pady=5, padx=(10, 0))

        # Gmail Credentials
        ttk.Label(api_frame, text="Gmail Credentials:").grid(row=1, column=0, sticky=W, pady=5)
        gmail_entry = ttk.Entry(api_frame, textvariable=self.gmail_credentials_path_var, width=50)
        gmail_entry.grid(row=1, column=1, sticky=EW, pady=5, padx=(10, 0))

        browse_btn = ttk.Button(
            api_frame,
            text="Browse",
            command=self._browse_gmail_credentials,
            bootstyle=SECONDARY,
            width=10
        )
        browse_btn.grid(row=1, column=2, pady=5, padx=(10, 0))

        api_frame.columnconfigure(1, weight=1)

        # Automation Settings
        auto_frame = ttk.LabelFrame(scrollable_frame, text="Automation Settings", padding=15)
        auto_frame.pack(fill=X, pady=10, padx=10)

        # Extension mode
        ttk.Checkbutton(
            auto_frame,
            text="Use reCAPTCHA extension (manual)",
            variable=self.extension_mode_var
        ).pack(anchor=W, pady=5)

        # Headless mode
        ttk.Checkbutton(
            auto_frame,
            text="Run browser in headless mode",
            variable=self.headless_mode_var
        ).pack(anchor=W, pady=5)

        # Pack canvas and scrollbar
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

    def _create_logs_tab(self) -> None:
        """Create the logs tab."""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="Logs")

        # Create log display
        log_frame = ttk.Frame(tab_frame)
        log_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Log text widget with scrollbar
        self.log_text = tk.Text(
            log_frame,
            wrap=tk.WORD,
            font=("Consolas", 10),
            bg="#2b2b2b",
            fg="#ffffff",
            insertbackground="#ffffff"
        )

        log_scrollbar = ttk.Scrollbar(log_frame, orient=VERTICAL, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=log_scrollbar.set)

        self.log_text.pack(side=LEFT, fill=BOTH, expand=True)
        log_scrollbar.pack(side=RIGHT, fill=Y)

        # Log control buttons
        button_frame = ttk.Frame(tab_frame)
        button_frame.pack(fill=X, padx=10, pady=(0, 10))

        clear_log_btn = ttk.Button(
            button_frame,
            text="Clear Logs",
            command=self._clear_logs,
            bootstyle=SECONDARY
        )
        clear_log_btn.pack(side=LEFT)

        save_log_btn = ttk.Button(
            button_frame,
            text="Save Logs",
            command=self._save_logs,
            bootstyle=INFO
        )
        save_log_btn.pack(side=LEFT, padx=(10, 0))

    def _create_about_tab(self) -> None:
        """Create the about tab."""
        tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(tab_frame, text="About")

        # Center frame
        center_frame = ttk.Frame(tab_frame)
        center_frame.pack(expand=True, fill=BOTH)

        # Application info
        info_frame = ttk.Frame(center_frame)
        info_frame.pack(expand=True)

        # App icon (if available)
        ttk.Label(
            info_frame,
            text=APP_NAME,
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        ttk.Label(
            info_frame,
            text=f"Version {VERSION}",
            font=("Arial", 12)
        ).pack(pady=5)

        ttk.Label(
            info_frame,
            text=f"By {AUTHOR}",
            font=("Arial", 10)
        ).pack(pady=5)

        # License info
        license_info = get_license_info()
        ttk.Label(
            info_frame,
            text=f"Machine ID: {license_info.get('machine_id', 'Unknown')}",
            font=("Arial", 9)
        ).pack(pady=20)

        ttk.Label(
            info_frame,
            text="Professional Python implementation with clean architecture",
            font=("Arial", 9, "italic")
        ).pack(pady=5)

    def _create_status_bar(self, parent: ttk.Frame) -> None:
        """Create status bar at bottom."""
        status_frame = ttk.Frame(parent)
        status_frame.pack(fill=X)

        # Status label
        self.status_label = ttk.Label(
            status_frame,
            textvariable=self.status_var,
            relief=SUNKEN,
            anchor=W
        )
        self.status_label.pack(side=LEFT, fill=X, expand=True)

        # Service status indicators
        self._create_service_indicators(status_frame)

    def _create_service_indicators(self, parent: ttk.Frame) -> None:
        """Create service status indicators."""
        # Firefox Relay status
        self.relay_status = ttk.Label(
            parent,
            text="Relay: ❌",
            foreground="red"
        )
        self.relay_status.pack(side=RIGHT, padx=5)

        # Random User status
        self.user_status = ttk.Label(
            parent,
            text="RandomUser: ✅",
            foreground="green"
        )
        self.user_status.pack(side=RIGHT, padx=5)

        # Update status
        self._update_service_status()

    def _setup_event_handlers(self) -> None:
        """Setup event handlers for GUI components."""
        # API key change handler
        self.firefox_api_key_var.trace_add('write', self._on_api_key_change)

        # Settings change handlers
        self.lab_url_var.trace_add('write', lambda *args: self._save_temp_setting('lab_url', self.lab_url_var.get()))
        self.auto_start_lab_var.trace_add('write', lambda *args: self._save_temp_setting('auto_start_lab', self.auto_start_lab_var.get()))
        self.extension_mode_var.trace_add('write', lambda *args: self._save_temp_setting('extension_mode', self.extension_mode_var.get()))

        # Window close handler
        self.root.protocol("WM_DELETE_WINDOW", self._on_window_close)

    def _generate_random_user(self) -> None:
        """Generate random user data."""
        try:
            self.status_var.set("Generating random user data...")
            self.root.update()

            user_data = self.random_user_service.get_random_user()
            if user_data:
                self.first_name_var.set(user_data.get('first_name', ''))
                self.last_name_var.set(user_data.get('last_name', ''))
                self.email_var.set(user_data.get('email', ''))
                self.company_var.set(user_data.get('company', ''))

                self.status_var.set("Random user data generated")
                log_user_action("Generated random user data", {"email": user_data.get('email')})
            else:
                self.status_var.set("Failed to generate user data")
                messagebox.showerror("Error", "Failed to generate random user data")

        except Exception as e:
            self.logger.error(f"Random user generation failed: {e}")
            self.status_var.set("Error generating user data")
            messagebox.showerror("Error", f"Failed to generate user data: {e}")

    def _clear_form(self) -> None:
        """Clear all form fields."""
        self.first_name_var.set('')
        self.last_name_var.set('')
        self.email_var.set('')
        self.company_var.set('')
        self.status_var.set("Form cleared")
        log_user_action("Cleared registration form")

    def _start_registration(self) -> None:
        """Start the registration process."""
        try:
            # Validate form data
            user_data = {
                'first_name': self.first_name_var.get().strip(),
                'last_name': self.last_name_var.get().strip(),
                'email': self.email_var.get().strip(),
                'company': self.company_var.get().strip(),
                'password': 'TempPassword123!'  # Will be generated
            }

            # Validate required fields
            validate_user_data(user_data)

            # Update UI state
            self.register_btn.config(state=DISABLED)
            self.stop_btn.config(state=NORMAL)
            self.progress_var.set(0)
            self.status_var.set("Starting registration process...")

            # Start registration in background thread
            thread = threading.Thread(
                target=self._run_registration_async,
                args=(user_data,),
                daemon=True
            )
            thread.start()

            log_user_action("Started registration process", {"email": user_data['email']})

        except ValidationError as e:
            messagebox.showerror("Validation Error", str(e))
        except Exception as e:
            self.logger.error(f"Registration start failed: {e}")
            messagebox.showerror("Error", f"Failed to start registration: {e}")

    def _run_registration_async(self, user_data: Dict[str, Any]) -> None:
        """Run registration process in async context."""
        try:
            # Create new event loop for this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            # Run the registration
            result = loop.run_until_complete(self._run_registration(user_data))

            # Update UI on main thread
            self.root.after(0, self._registration_completed, result)

        except Exception as e:
            self.logger.error(f"Async registration failed: {e}")
            self.root.after(0, self._registration_failed, str(e))

    async def _run_registration(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Run the actual registration process."""
        # Initialize automation
        self.automation = CloudSkillAutomation(
            headless=self.headless_mode_var.get(),
            captcha_solver=self.captcha_service,
            extension_mode=self.extension_mode_var.get()
        )

        # Update progress
        self.root.after(0, lambda: self.progress_var.set(20))
        self.root.after(0, lambda: self.status_var.set("Initializing browser..."))

        # Run registration
        result = await self.automation.register_account(user_data)

        return result

    def _registration_completed(self, result: Dict[str, Any]) -> None:
        """Handle registration completion."""
        try:
            self.progress_var.set(100)

            if result.get('success'):
                self.status_var.set("Registration completed successfully!")
                messagebox.showinfo("Success", "Account registration completed successfully!")
            else:
                error_msg = result.get('message', 'Unknown error')
                self.status_var.set(f"Registration failed: {error_msg}")
                messagebox.showerror("Registration Failed", error_msg)

            log_user_action("Registration completed", {
                "success": result.get('success'),
                "email": result.get('email'),
                "steps": result.get('steps_completed', [])
            })

        finally:
            self._reset_ui_state()

    def _registration_failed(self, error_msg: str) -> None:
        """Handle registration failure."""
        self.status_var.set(f"Registration failed: {error_msg}")
        messagebox.showerror("Error", f"Registration failed: {error_msg}")
        self._reset_ui_state()

    def _stop_registration(self) -> None:
        """Stop the registration process."""
        # Note: In a full implementation, this would signal the automation to stop
        self.status_var.set("Stopping registration...")
        self._reset_ui_state()
        log_user_action("Stopped registration process")

    def _reset_ui_state(self) -> None:
        """Reset UI to initial state."""
        self.register_btn.config(state=NORMAL)
        self.stop_btn.config(state=DISABLED)
        self.progress_var.set(0)

    def _test_firefox_api(self) -> None:
        """Test Firefox Relay API connection."""
        try:
            if not self.firefox_relay_service:
                messagebox.showerror("Error", "Firefox Relay service not configured")
                return

            api_key = self.firefox_api_key_var.get().strip()
            if not api_key:
                messagebox.showerror("Error", "Please enter an API key")
                return

            self.firefox_relay_service.set_api_key(api_key)

            if self.firefox_relay_service.test_connection():
                messagebox.showinfo("Success", "Firefox Relay API connection successful!")
                self._update_service_status()
            else:
                messagebox.showerror("Error", "Firefox Relay API connection failed")

        except Exception as e:
            messagebox.showerror("Error", f"API test failed: {e}")

    def _browse_gmail_credentials(self) -> None:
        """Browse for Gmail credentials file."""
        filename = filedialog.askopenfilename(
            title="Select Gmail Credentials File",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            self.gmail_credentials_path_var.set(filename)
            self._save_temp_setting('gmail_credentials_path', filename)

    def _on_api_key_change(self, *args) -> None:
        """Handle API key change."""
        api_key = self.firefox_api_key_var.get().strip()
        if api_key and self.firefox_relay_service:
            self.firefox_relay_service.set_api_key(api_key)
            self._save_temp_setting('firefox_api_key', api_key)
        self._update_service_status()

    def _update_service_status(self) -> None:
        """Update service status indicators."""
        # Firefox Relay status
        if self.firefox_relay_service and self.firefox_api_key_var.get().strip():
            self.relay_status.config(text="Relay: ✅", foreground="green")
        else:
            self.relay_status.config(text="Relay: ❌", foreground="red")

    def _clear_logs(self) -> None:
        """Clear the log display."""
        self.log_text.delete(1.0, tk.END)

    def _save_logs(self) -> None:
        """Save logs to file."""
        filename = filedialog.asksaveasfilename(
            title="Save Logs",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.log_text.get(1.0, tk.END))
            messagebox.showinfo("Success", f"Logs saved to {filename}")

    def _save_temp_setting(self, key: str, value: Any) -> None:
        """Save setting to temporary storage."""
        try:
            temp_dir = Path(tempfile.gettempdir()) / "AutoCloudSkill"
            temp_dir.mkdir(exist_ok=True)

            settings_file = temp_dir / "settings.json"

            # Load existing settings
            settings = {}
            if settings_file.exists():
                with open(settings_file, 'r', encoding='utf-8') as f:
                    settings = json.load(f)

            # Update setting
            settings[key] = value

            # Save settings
            with open(settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2)

        except Exception as e:
            self.logger.warning(f"Could not save setting {key}: {e}")

    def _load_temp_setting(self, key: str) -> Any:
        """Load setting from temporary storage."""
        try:
            temp_dir = Path(tempfile.gettempdir()) / "AutoCloudSkill"
            settings_file = temp_dir / "settings.json"

            if settings_file.exists():
                with open(settings_file, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                return settings.get(key)

        except Exception as e:
            self.logger.debug(f"Could not load setting {key}: {e}")

        return None

    def _set_application_icon(self) -> None:
        """Set application icon if available."""
        try:
            # Try to find icon in various locations
            icon_paths = [
                Path(__file__).parent / "assets" / "icon.ico",
                Path.cwd() / "assets" / "icon.ico"
            ]

            for icon_path in icon_paths:
                if icon_path.exists():
                    self.root.iconbitmap(str(icon_path))
                    break

        except Exception as e:
            self.logger.debug(f"Could not set application icon: {e}")

    def _center_window(self) -> None:
        """Center window on screen."""
        try:
            self.root.update_idletasks()
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            x = (self.root.winfo_screenwidth() // 2) - (width // 2)
            y = (self.root.winfo_screenheight() // 2) - (height // 2)
            self.root.geometry(f"{width}x{height}+{x}+{y}")
        except Exception as e:
            self.logger.debug(f"Could not center window: {e}")

    def _on_window_close(self) -> None:
        """Handle window close event."""
        try:
            # Cleanup automation if running
            if self.automation:
                # Note: In a full implementation, this would properly clean up async resources
                pass

            # Log application shutdown
            log_user_action("Application shutdown")
            self.logger.info("Application closing")

            # Destroy window
            self.root.destroy()

        except Exception as e:
            self.logger.error(f"Error during window close: {e}")
            self.root.destroy()

    def run(self) -> None:
        """Start the application main loop."""
        try:
            # Ensure license is valid
            if not ensure_license():
                messagebox.showerror("License Error", "License validation failed")
                return

            self.logger.info("Starting application main loop")
            self.root.mainloop()

        except Exception as e:
            self.logger.error(f"Application run failed: {e}")
            messagebox.showerror("Fatal Error", f"Application failed to start: {e}")
            raise