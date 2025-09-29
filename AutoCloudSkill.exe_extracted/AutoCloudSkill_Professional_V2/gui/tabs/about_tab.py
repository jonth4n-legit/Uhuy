"""
Professional About Tab for AutoCloudSkill Application.

This module provides comprehensive application information, system details,
license status, and professional branding.

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import hashlib
import platform
import sys
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pathlib import Path
from typing import TYPE_CHECKING

from config.licensing import LicenseManager
from config.constants import APP_NAME, VERSION, AUTHOR

if TYPE_CHECKING:
    from gui.main_window import MainWindow


class AboutTab:
    """Professional about tab with application and system information."""

    def __init__(self, owner: 'MainWindow', notebook: ttk.Notebook):
        """Initialize the about tab.

        Args:
            owner: Reference to the main window instance
            notebook: Parent notebook widget
        """
        self.owner = owner
        self.license_manager = LicenseManager()
        self._build_interface(notebook)

    def _build_interface(self, notebook: ttk.Notebook) -> None:
        """Build the complete about tab interface."""
        # Create main tab frame
        self.tab_frame = ttk.Frame(notebook, padding=25)
        notebook.add(self.tab_frame, text='ℹ️ About')

        # Build information sections
        self._create_application_info()
        self._create_system_info()
        self._create_machine_info()
        self._create_license_info()
        self._create_credits_section()

    def _create_application_info(self) -> None:
        """Create application information section."""
        app_frame = ttk.LabelFrame(
            self.tab_frame,
            text='📱 Application Information',
            padding=20,
            bootstyle=PRIMARY
        )
        app_frame.pack(fill=X, pady=(0, 15))

        # Application details grid
        app_grid = ttk.Frame(app_frame)
        app_grid.pack(fill=X)

        # Configure grid
        app_grid.columnconfigure(1, weight=1)

        # Application name
        ttk.Label(
            app_grid,
            text='Name:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=0, column=0, sticky=W, pady=5, padx=(0, 20))

        ttk.Label(
            app_grid,
            text=f'{APP_NAME} Professional',
            font=('Segoe UI', 10)
        ).grid(row=0, column=1, sticky=W, pady=5)

        # Version
        ttk.Label(
            app_grid,
            text='Version:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=1, column=0, sticky=W, pady=5, padx=(0, 20))

        ttk.Label(
            app_grid,
            text=f'{VERSION} (Professional Rewrite)',
            font=('Segoe UI', 10)
        ).grid(row=1, column=1, sticky=W, pady=5)

        # Author
        ttk.Label(
            app_grid,
            text='Original Author:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=2, column=0, sticky=W, pady=5, padx=(0, 20))

        ttk.Label(
            app_grid,
            text=AUTHOR,
            font=('Segoe UI', 10)
        ).grid(row=2, column=1, sticky=W, pady=5)

        # Professional rewrite info
        ttk.Label(
            app_grid,
            text='Professional Rewrite:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=3, column=0, sticky=W, pady=5, padx=(0, 20))

        ttk.Label(
            app_grid,
            text='Claude Opus 4.1 (Anthropic)',
            font=('Segoe UI', 10)
        ).grid(row=3, column=1, sticky=W, pady=5)

        # Description
        description_label = ttk.Label(
            app_frame,
            text='🚀 Professional automation tool for Google Cloud Skills Boost registration and lab management',
            font=('Segoe UI', 9),
            bootstyle=INFO,
            wraplength=500
        )
        description_label.pack(anchor=W, pady=(15, 0))

    def _create_system_info(self) -> None:
        """Create system information section."""
        system_frame = ttk.LabelFrame(
            self.tab_frame,
            text='💻 System Information',
            padding=20,
            bootstyle=SECONDARY
        )
        system_frame.pack(fill=X, pady=(0, 15))

        # System details grid
        system_grid = ttk.Frame(system_frame)
        system_grid.pack(fill=X)

        # Configure grid
        system_grid.columnconfigure(1, weight=1)

        # Operating system
        ttk.Label(
            system_grid,
            text='Operating System:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=0, column=0, sticky=W, pady=5, padx=(0, 20))

        os_info = f'{platform.system()} {platform.release()} ({platform.architecture()[0]})'
        ttk.Label(
            system_grid,
            text=os_info,
            font=('Segoe UI', 10)
        ).grid(row=0, column=1, sticky=W, pady=5)

        # Python version
        ttk.Label(
            system_grid,
            text='Python Version:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=1, column=0, sticky=W, pady=5, padx=(0, 20))

        python_version = f'{sys.version.split()[0]} ({platform.python_implementation()})'
        ttk.Label(
            system_grid,
            text=python_version,
            font=('Segoe UI', 10)
        ).grid(row=1, column=1, sticky=W, pady=5)

        # Installation path
        ttk.Label(
            system_grid,
            text='Installation Path:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=2, column=0, sticky=W, pady=5, padx=(0, 20))

        if getattr(sys, 'frozen', False):
            install_path = Path(sys.executable).parent
            install_type = 'Bundled Executable'
        else:
            install_path = Path(__file__).resolve().parent.parent.parent
            install_type = 'Development Mode'

        ttk.Label(
            system_grid,
            text=f'{install_path} ({install_type})',
            font=('Segoe UI', 10)
        ).grid(row=2, column=1, sticky=W, pady=5)

    def _create_machine_info(self) -> None:
        """Create machine identification section."""
        machine_frame = ttk.LabelFrame(
            self.tab_frame,
            text='🔒 Machine Identification',
            padding=20,
            bootstyle=INFO
        )
        machine_frame.pack(fill=X, pady=(0, 15))

        # Machine ID description
        machine_desc = ttk.Label(
            machine_frame,
            text='🔐 Unique machine identifier used for license validation',
            font=('Segoe UI', 9),
            bootstyle=INFO
        )
        machine_desc.pack(anchor=W, pady=(0, 10))

        # Machine ID display
        machine_id_frame = ttk.Frame(machine_frame)
        machine_id_frame.pack(fill=X)

        # Generate machine ID
        try:
            raw_machine_id = self.license_manager.get_machine_id()
            hashed_machine_id = hashlib.sha256(raw_machine_id.encode('utf-8')).hexdigest()
        except Exception as e:
            hashed_machine_id = f'Error: {e}'

        # Store in owner for access
        self.owner.hashed_mid_var = tk.StringVar(value=hashed_machine_id)

        # Machine ID entry (readonly)
        self.machine_id_entry = ttk.Entry(
            machine_id_frame,
            textvariable=self.owner.hashed_mid_var,
            state='readonly',
            font=('Consolas', 9),
            width=70
        )
        self.machine_id_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))

        # Copy button
        copy_btn = ttk.Button(
            machine_id_frame,
            text='📋 Copy',
            command=self._copy_machine_id,
            bootstyle=INFO,
            width=10
        )
        copy_btn.pack(side=LEFT)

        # Machine ID info
        machine_info = ttk.Label(
            machine_frame,
            text='💡 This ID is generated from hardware characteristics and remains constant for this machine',
            font=('Segoe UI', 8),
            bootstyle=SECONDARY
        )
        machine_info.pack(anchor=W, pady=(10, 0))

    def _create_license_info(self) -> None:
        """Create license information section."""
        license_frame = ttk.LabelFrame(
            self.tab_frame,
            text='📄 License Information',
            padding=20,
            bootstyle=WARNING
        )
        license_frame.pack(fill=X, pady=(0, 15))

        # License details grid
        license_grid = ttk.Frame(license_frame)
        license_grid.pack(fill=X, pady=(0, 15))

        # Configure grid
        license_grid.columnconfigure(1, weight=1)

        # License plan
        ttk.Label(
            license_grid,
            text='Plan:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=0, column=0, sticky=W, pady=8, padx=(0, 20))

        # Initialize license variables in owner
        if not hasattr(self.owner, 'license_plan_var'):
            self.owner.license_plan_var = tk.StringVar(value='Checking...')

        self.license_plan_label = ttk.Label(
            license_grid,
            textvariable=self.owner.license_plan_var,
            font=('Segoe UI', 10, 'bold'),
            bootstyle=INFO
        )
        self.license_plan_label.grid(row=0, column=1, sticky=W, pady=8)

        # License expiry
        ttk.Label(
            license_grid,
            text='Expires:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=1, column=0, sticky=W, pady=8, padx=(0, 20))

        if not hasattr(self.owner, 'license_expiry_var'):
            self.owner.license_expiry_var = tk.StringVar(value='Checking...')

        self.license_expiry_label = ttk.Label(
            license_grid,
            textvariable=self.owner.license_expiry_var,
            font=('Segoe UI', 10),
            bootstyle=SUCCESS
        )
        self.license_expiry_label.grid(row=1, column=1, sticky=W, pady=8)

        # License actions
        license_actions = ttk.Frame(license_frame)
        license_actions.pack(fill=X)

        # Refresh license button
        refresh_btn = ttk.Button(
            license_actions,
            text='🔄 Refresh License',
            command=self._refresh_license,
            bootstyle=PRIMARY,
            width=18
        )
        refresh_btn.pack(side=LEFT, padx=(0, 10))

        # License status button
        status_btn = ttk.Button(
            license_actions,
            text='📊 Check Status',
            command=self._check_license_status,
            bootstyle=INFO,
            width=15
        )
        status_btn.pack(side=LEFT)

    def _create_credits_section(self) -> None:
        """Create credits and acknowledgments section."""
        credits_frame = ttk.LabelFrame(
            self.tab_frame,
            text='🏆 Credits & Technologies',
            padding=20,
            bootstyle=SUCCESS
        )
        credits_frame.pack(fill=X)

        # Technologies used
        tech_info = [
            '🎯 Core Technologies:',
            '  • Python 3.11+ - Application runtime',
            '  • tkinter & ttkbootstrap - Modern GUI framework',
            '  • Playwright - Browser automation engine',
            '  • Google APIs - Gmail and GenAI integration',
            '',
            '🔧 Key Libraries:',
            '  • aiohttp - Async HTTP client',
            '  • Pillow - Image processing',
            '  • requests - HTTP library',
            '  • pathlib - Modern path handling',
            '',
            '☁️ Cloud Services:',
            '  • Google Cloud Skills Boost - Target platform',
            '  • Firefox Relay - Email masking service',
            '  • Google GenAI - Video generation (Veo models)',
            '',
            '🎨 Professional Rewrite Features:',
            '  • Clean architecture with separation of concerns',
            '  • Comprehensive error handling and logging',
            '  • Type hints and modern Python practices',
            '  • Professional GUI with dark theme',
            '  • Advanced automation capabilities',
            '  • Multi-threaded processing',
            '  • Configuration management',
            '  • License validation system'
        ]

        credits_text = '\n'.join(tech_info)

        # Credits display
        credits_label = ttk.Label(
            credits_frame,
            text=credits_text,
            font=('Segoe UI', 9),
            bootstyle=SUCCESS,
            justify=LEFT
        )
        credits_label.pack(anchor=W)

        # Copyright notice
        copyright_label = ttk.Label(
            credits_frame,
            text='© 2024 Professional Rewrite by Claude Opus 4.1 | Original © SinyoRmx',
            font=('Segoe UI', 8, 'italic'),
            bootstyle=SECONDARY
        )
        copyright_label.pack(anchor=W, pady=(15, 0))

    def _copy_machine_id(self) -> None:
        """Copy machine ID to clipboard."""
        try:
            machine_id = self.owner.hashed_mid_var.get()
            self.owner.root.clipboard_clear()
            self.owner.root.clipboard_append(machine_id)
            self.owner.log_message('📋 Machine ID copied to clipboard')

        except Exception as e:
            self.owner.log_message(f'🛑 Copy machine ID error: {e}')

    def _refresh_license(self) -> None:
        """Refresh license information."""
        try:
            self.owner.log_message('🔄 Refreshing license information...')

            # Update status to show checking
            self.owner.license_plan_var.set('Checking...')
            self.owner.license_expiry_var.set('Checking...')

            # Trigger license check in main window
            self.owner.check_license_async()

        except Exception as e:
            self.owner.log_message(f'🛑 Error refreshing license: {e}')

    def _check_license_status(self) -> None:
        """Show detailed license status."""
        try:
            # Get current license info
            license_info = getattr(self.owner, 'license_info', None)

            if license_info:
                status_details = [
                    f"Plan: {license_info.plan or 'Unknown'}",
                    f"Status: {license_info.status or 'Unknown'}",
                    f"Allowed: {'✅ Yes' if license_info.is_allowed else '❌ No'}",
                    f"Expires: {license_info.expires_at or 'Unknown'}",
                    f"Checked: {license_info.checked_at or 'Unknown'}",
                    "",
                    f"Machine ID: {self.owner.hashed_mid_var.get()[:16]}...",
                ]

                if hasattr(license_info, 'reason') and license_info.reason:
                    status_details.append(f"Reason: {license_info.reason}")

                status_text = '\n'.join(status_details)
            else:
                status_text = 'License information not available.\nPlease refresh license to check status.'

            # Show status dialog
            from tkinter import messagebox
            messagebox.showinfo('License Status Details', status_text)

        except Exception as e:
            self.owner.log_message(f'🛑 Error checking license status: {e}')

    def update_license_display(self, license_info) -> None:
        """Update license display with new information.

        Args:
            license_info: License information object
        """
        try:
            if license_info:
                # Update plan with color coding
                plan = str(license_info.plan or 'Unknown')
                if plan.lower() == 'free':
                    self.license_plan_label.config(bootstyle=WARNING)
                elif plan.lower() in ['pro', 'premium', 'enterprise']:
                    self.license_plan_label.config(bootstyle=SUCCESS)
                else:
                    self.license_plan_label.config(bootstyle=INFO)

                # Update expiry with color coding
                if license_info.is_allowed:
                    self.license_expiry_label.config(bootstyle=SUCCESS)
                else:
                    self.license_expiry_label.config(bootstyle=DANGER)

            else:
                # Reset to default styling
                self.license_plan_label.config(bootstyle=INFO)
                self.license_expiry_label.config(bootstyle=INFO)

        except Exception as e:
            self.owner.logger.debug(f"License display update error: {e}")