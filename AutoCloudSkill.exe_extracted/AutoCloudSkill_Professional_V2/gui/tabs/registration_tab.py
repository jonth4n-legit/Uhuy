"""
Professional Registration Tab for AutoCloudSkill Application.

This module provides a clean, professional registration form interface
with proper input validation, visual feedback, and intuitive user controls.

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gui.main_window import MainWindow


class RegistrationTab:
    """Professional registration form tab for user data entry."""

    def __init__(self, owner: 'MainWindow', notebook: ttk.Notebook):
        """Initialize the registration tab.

        Args:
            owner: Reference to the main window instance
            notebook: Parent notebook widget
        """
        self.owner = owner
        self._build_interface(notebook)

    def _build_interface(self, notebook: ttk.Notebook) -> None:
        """Build the complete registration tab interface."""
        # Create main tab frame
        self.tab_frame = ttk.Frame(notebook, padding=20)
        notebook.add(self.tab_frame, text='🔐 Registration Form')

        # Create main content areas
        self._create_form_section()
        self._create_password_controls()
        self._create_action_buttons()

    def _create_form_section(self) -> None:
        """Create the main registration form section."""
        # Main form frame
        form_frame = ttk.LabelFrame(
            self.tab_frame,
            text='Registration Information',
            padding=20,
            bootstyle=PRIMARY
        )
        form_frame.pack(fill=BOTH, expand=True, pady=(0, 10))

        # Configure grid weights for responsive layout
        form_frame.columnconfigure(1, weight=1)

        # First Name
        ttk.Label(
            form_frame,
            text='First Name:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=0, column=0, sticky=W, pady=8, padx=(0, 10))

        self.first_name_entry = ttk.Entry(
            form_frame,
            textvariable=self.owner.first_name_var,
            width=30,
            font=('Segoe UI', 10)
        )
        self.first_name_entry.grid(row=0, column=1, sticky=W+E, pady=8)

        # Last Name
        ttk.Label(
            form_frame,
            text='Last Name:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=1, column=0, sticky=W, pady=8, padx=(0, 10))

        self.last_name_entry = ttk.Entry(
            form_frame,
            textvariable=self.owner.last_name_var,
            width=30,
            font=('Segoe UI', 10)
        )
        self.last_name_entry.grid(row=1, column=1, sticky=W+E, pady=8)

        # Email
        ttk.Label(
            form_frame,
            text='Email:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=2, column=0, sticky=W, pady=8, padx=(0, 10))

        self.email_entry = ttk.Entry(
            form_frame,
            textvariable=self.owner.email_var,
            width=30,
            font=('Segoe UI', 10),
            state='readonly'  # Email is generated automatically
        )
        self.email_entry.grid(row=2, column=1, sticky=W+E, pady=8)

        # Email info label
        email_info = ttk.Label(
            form_frame,
            text='📧 Generated automatically from Firefox Relay',
            font=('Segoe UI', 9),
            bootstyle=INFO
        )
        email_info.grid(row=2, column=2, sticky=W, padx=(10, 0))

        # Company
        ttk.Label(
            form_frame,
            text='Company:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=3, column=0, sticky=W, pady=8, padx=(0, 10))

        self.company_entry = ttk.Entry(
            form_frame,
            textvariable=self.owner.company_var,
            width=30,
            font=('Segoe UI', 10)
        )
        self.company_entry.grid(row=3, column=1, sticky=W+E, pady=8)

    def _create_password_controls(self) -> None:
        """Create password input and control section."""
        # Password frame
        password_frame = ttk.LabelFrame(
            self.tab_frame,
            text='Password Configuration',
            padding=20,
            bootstyle=SECONDARY
        )
        password_frame.pack(fill=X, pady=(0, 10))

        # Configure grid weights
        password_frame.columnconfigure(1, weight=1)

        # Password
        ttk.Label(
            password_frame,
            text='Password:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=0, column=0, sticky=W, pady=8, padx=(0, 10))

        self.owner.password_entry = ttk.Entry(
            password_frame,
            textvariable=self.owner.password_var,
            show='*',
            width=30,
            font=('Segoe UI', 10)
        )
        self.owner.password_entry.grid(row=0, column=1, sticky=W+E, pady=8, padx=(0, 10))

        # Password controls frame
        pwd_controls_frame = ttk.Frame(password_frame)
        pwd_controls_frame.grid(row=0, column=2, sticky=W, padx=(0, 0))

        # Show password toggle
        self.show_password_check = ttk.Checkbutton(
            pwd_controls_frame,
            text='Show',
            variable=self.owner.show_password_var,
            command=self._toggle_password_visibility,
            bootstyle='round-toggle'
        )
        self.show_password_check.pack(side=LEFT, padx=(0, 5))

        # Copy password button
        self.copy_password_btn = ttk.Button(
            pwd_controls_frame,
            text='📋 Copy',
            command=self._copy_password,
            bootstyle=INFO,
            width=10
        )
        self.copy_password_btn.pack(side=LEFT)

        # Confirm Password
        ttk.Label(
            password_frame,
            text='Confirm Password:',
            font=('Segoe UI', 10, 'bold')
        ).grid(row=1, column=0, sticky=W, pady=8, padx=(0, 10))

        self.owner.password_confirm_entry = ttk.Entry(
            password_frame,
            textvariable=self.owner.password_confirm_var,
            show='*',
            width=30,
            font=('Segoe UI', 10)
        )
        self.owner.password_confirm_entry.grid(row=1, column=1, sticky=W+E, pady=8)

        # Password strength indicator
        self.password_strength_label = ttk.Label(
            password_frame,
            text='Password strength will be shown here',
            font=('Segoe UI', 9),
            bootstyle=INFO
        )
        self.password_strength_label.grid(row=2, column=1, sticky=W, pady=(5, 0))

        # Setup password validation
        self.owner.password_var.trace_add('write', self._validate_password)
        self.owner.password_confirm_var.trace_add('write', self._validate_password_match)

    def _create_action_buttons(self) -> None:
        """Create action buttons section."""
        # Action buttons frame
        action_frame = ttk.LabelFrame(
            self.tab_frame,
            text='Quick Actions',
            padding=15,
            bootstyle=SUCCESS
        )
        action_frame.pack(fill=X)

        # Button container
        button_container = ttk.Frame(action_frame)
        button_container.pack(fill=X)

        # Generate new data button
        self.generate_btn = ttk.Button(
            button_container,
            text='🔄 Generate New Data',
            command=self.owner.refresh_generated_data,
            bootstyle=INFO,
            width=20
        )
        self.generate_btn.pack(side=LEFT, padx=(0, 10))

        # Validate data button
        self.validate_btn = ttk.Button(
            button_container,
            text='✅ Validate Data',
            command=self._validate_all_data,
            bootstyle=SUCCESS,
            width=15
        )
        self.validate_btn.pack(side=LEFT, padx=(0, 10))

        # Clear form button
        self.clear_btn = ttk.Button(
            button_container,
            text='🗑️ Clear Form',
            command=self._clear_form,
            bootstyle=WARNING,
            width=15
        )
        self.clear_btn.pack(side=LEFT)

        # Info label
        info_label = ttk.Label(
            action_frame,
            text='💡 Data is automatically generated when the application starts',
            font=('Segoe UI', 9),
            bootstyle=INFO
        )
        info_label.pack(pady=(10, 0))

    def _toggle_password_visibility(self) -> None:
        """Toggle password visibility for both password fields."""
        try:
            show_char = '' if self.owner.show_password_var.get() else '*'

            if hasattr(self.owner, 'password_entry'):
                self.owner.password_entry.config(show=show_char)

            if hasattr(self.owner, 'password_confirm_entry'):
                self.owner.password_confirm_entry.config(show=show_char)

        except Exception as e:
            self.owner.log_message(f'⚠️ Password visibility toggle error: {e}')

    def _copy_password(self) -> None:
        """Copy password to clipboard."""
        try:
            password = self.owner.password_var.get()
            if password:
                self.owner.root.clipboard_clear()
                self.owner.root.clipboard_append(password)
                self.owner.log_message('📋 Password copied to clipboard')
            else:
                self.owner.log_message('⚠️ No password to copy')

        except Exception as e:
            self.owner.log_message(f'🛑 Copy password error: {e}')

    def _validate_password(self, *args) -> None:
        """Validate password strength and update indicator."""
        try:
            password = self.owner.password_var.get()

            if not password:
                self.password_strength_label.config(
                    text='Enter a password',
                    bootstyle=INFO
                )
                return

            # Calculate password strength
            score = 0
            feedback = []

            # Length check
            if len(password) >= 8:
                score += 1
            else:
                feedback.append('at least 8 characters')

            # Character variety checks
            if any(c.isupper() for c in password):
                score += 1
            else:
                feedback.append('uppercase letters')

            if any(c.islower() for c in password):
                score += 1
            else:
                feedback.append('lowercase letters')

            if any(c.isdigit() for c in password):
                score += 1
            else:
                feedback.append('numbers')

            if any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password):
                score += 1
            else:
                feedback.append('special characters')

            # Update strength indicator
            if score <= 2:
                strength_text = '🔴 Weak'
                strength_style = DANGER
            elif score <= 3:
                strength_text = '🟡 Fair'
                strength_style = WARNING
            elif score <= 4:
                strength_text = '🟢 Good'
                strength_style = SUCCESS
            else:
                strength_text = '🔵 Excellent'
                strength_style = INFO

            if feedback:
                strength_text += f' (Add: {", ".join(feedback[:2])})'

            self.password_strength_label.config(
                text=strength_text,
                bootstyle=strength_style
            )

        except Exception as e:
            self.owner.logger.debug(f"Password validation error: {e}")

    def _validate_password_match(self, *args) -> None:
        """Validate password confirmation match."""
        try:
            password = self.owner.password_var.get()
            confirm = self.owner.password_confirm_var.get()

            if not confirm:
                return

            if password == confirm:
                self.owner.password_confirm_entry.config(bootstyle=SUCCESS)
            else:
                self.owner.password_confirm_entry.config(bootstyle=DANGER)

        except Exception as e:
            self.owner.logger.debug(f"Password match validation error: {e}")

    def _validate_all_data(self) -> None:
        """Validate all form data and show results."""
        try:
            # Collect all data
            data = {
                'first_name': self.owner.first_name_var.get().strip(),
                'last_name': self.owner.last_name_var.get().strip(),
                'email': self.owner.email_var.get().strip(),
                'company': self.owner.company_var.get().strip(),
                'password': self.owner.password_var.get(),
                'password_confirm': self.owner.password_confirm_var.get()
            }

            # Validation results
            errors = []

            # Required field checks
            if not data['first_name']:
                errors.append('First name is required')
            if not data['last_name']:
                errors.append('Last name is required')
            if not data['company']:
                errors.append('Company is required')
            if not data['password']:
                errors.append('Password is required')

            # Email check
            if not data['email'] or data['email'] == 'Will be generated from Firefox Relay':
                errors.append('Email will be generated automatically during registration')

            # Password match check
            if data['password'] != data['password_confirm']:
                errors.append('Password confirmation does not match')

            # Password strength check
            if len(data['password']) < 8:
                errors.append('Password should be at least 8 characters')

            # Show results
            if errors:
                error_msg = '⚠️ Validation Issues:\n\n' + '\n'.join(f'• {error}' for error in errors)
                self.owner.log_message('⚠️ Form validation found issues')

                # Show in a message box
                from tkinter import messagebox
                messagebox.showwarning('Validation Results', error_msg)
            else:
                success_msg = '✅ All data is valid and ready for registration!'
                self.owner.log_message(success_msg)

                # Show success message
                from tkinter import messagebox
                messagebox.showinfo('Validation Results', success_msg)

        except Exception as e:
            self.owner.log_message(f'🛑 Validation error: {e}')

    def _clear_form(self) -> None:
        """Clear all form fields."""
        try:
            # Confirm before clearing
            from tkinter import messagebox
            if messagebox.askyesno(
                'Clear Form',
                'Are you sure you want to clear all form data?'
            ):
                # Clear all variables
                self.owner.first_name_var.set('')
                self.owner.last_name_var.set('')
                self.owner.email_var.set('')
                self.owner.company_var.set('')
                self.owner.password_var.set('')
                self.owner.password_confirm_var.set('')

                # Reset data generated flag
                self.owner.data_generated = False
                self.owner._update_ui_state()

                self.owner.log_message('🗑️ Form cleared')

        except Exception as e:
            self.owner.log_message(f'🛑 Clear form error: {e}')

    def update_validation_styles(self) -> None:
        """Update visual validation styles for all fields."""
        try:
            # Update field styles based on content
            fields = [
                (self.first_name_entry, self.owner.first_name_var.get().strip()),
                (self.last_name_entry, self.owner.last_name_var.get().strip()),
                (self.company_entry, self.owner.company_var.get().strip())
            ]

            for entry, value in fields:
                if value:
                    entry.config(bootstyle=SUCCESS)
                else:
                    entry.config(bootstyle=DEFAULT)

        except Exception as e:
            self.owner.logger.debug(f"Style update error: {e}")