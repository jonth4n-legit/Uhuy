"""
GUI Tab: Registration Tab
"""
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class RegistrationTab:
    def __init__(self, main_window, notebook):
        self.main_window = main_window
        self.notebook = notebook
        self._build_ui()

    def _build_ui(self):
        """Build registration tab UI"""
        self.frame = ttk.Frame(self.notebook)
        self.notebook.add(self.frame, text='Registration')
        
        # Registration form
        form_frame = ttk.LabelFrame(self.frame, text='Registration Form', padding=20)
        form_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # First Name
        ttk.Label(form_frame, text='First Name:').grid(row=0, column=0, sticky=W, pady=5)
        first_name_entry = ttk.Entry(form_frame, textvariable=self.main_window.first_name_var, width=30)
        first_name_entry.grid(row=0, column=1, sticky=EW, padx=(10, 0), pady=5)
        
        # Last Name
        ttk.Label(form_frame, text='Last Name:').grid(row=1, column=0, sticky=W, pady=5)
        last_name_entry = ttk.Entry(form_frame, textvariable=self.main_window.last_name_var, width=30)
        last_name_entry.grid(row=1, column=1, sticky=EW, padx=(10, 0), pady=5)
        
        # Email
        ttk.Label(form_frame, text='Email:').grid(row=2, column=0, sticky=W, pady=5)
        email_entry = ttk.Entry(form_frame, textvariable=self.main_window.email_var, width=30, state='readonly')
        email_entry.grid(row=2, column=1, sticky=EW, padx=(10, 0), pady=5)
        
        # Company
        ttk.Label(form_frame, text='Company:').grid(row=3, column=0, sticky=W, pady=5)
        company_entry = ttk.Entry(form_frame, textvariable=self.main_window.company_var, width=30)
        company_entry.grid(row=3, column=1, sticky=EW, padx=(10, 0), pady=5)
        
        # Password
        ttk.Label(form_frame, text='Password:').grid(row=4, column=0, sticky=W, pady=5)
        password_frame = ttk.Frame(form_frame)
        password_frame.grid(row=4, column=1, sticky=EW, padx=(10, 0), pady=5)
        
        self.main_window.password_entry = ttk.Entry(password_frame, textvariable=self.main_window.password_var, width=25, show='*')
        self.main_window.password_entry.pack(side=LEFT, fill=X, expand=True)
        
        ttk.Button(password_frame, text='👁', width=3, command=self.main_window.toggle_password_visibility).pack(side=LEFT, padx=(5, 0))
        ttk.Button(password_frame, text='📋', width=3, command=self.main_window.copy_password).pack(side=LEFT, padx=(2, 0))
        
        # Password Confirm
        ttk.Label(form_frame, text='Confirm Password:').grid(row=5, column=0, sticky=W, pady=5)
        self.main_window.password_confirm_entry = ttk.Entry(form_frame, textvariable=self.main_window.password_confirm_var, width=30, show='*')
        self.main_window.password_confirm_entry.grid(row=5, column=1, sticky=EW, padx=(10, 0), pady=5)
        
        # Configure grid weights
        form_frame.columnconfigure(1, weight=1)
        
        # Firefox Relay Settings
        relay_frame = ttk.LabelFrame(self.frame, text='Firefox Relay Settings', padding=20)
        relay_frame.pack(fill=X, padx=10, pady=(0, 10))
        
        ttk.Label(relay_frame, text='API Key:').grid(row=0, column=0, sticky=W, pady=5)
        api_key_entry = ttk.Entry(relay_frame, textvariable=self.main_window.firefox_api_key_var, width=40, show='*')
        api_key_entry.grid(row=0, column=1, sticky=EW, padx=(10, 0), pady=5)
        
        button_frame = ttk.Frame(relay_frame)
        button_frame.grid(row=0, column=2, padx=(10, 0), pady=5)
        
        ttk.Button(button_frame, text='Test', command=self.main_window.test_firefox_api_key, bootstyle=INFO).pack(side=LEFT, padx=(0, 5))
        ttk.Button(button_frame, text='Delete All Masks', command=self.main_window.delete_all_firefox_masks, bootstyle=DANGER).pack(side=LEFT)
        
        # Status labels
        status_frame = ttk.Frame(relay_frame)
        status_frame.grid(row=1, column=0, columnspan=3, sticky=EW, pady=(10, 0))
        
        self.main_window.firefox_status_label = ttk.Label(status_frame, text='Firefox Relay: 🛑 Not configured', bootstyle=WARNING)
        self.main_window.firefox_status_label.pack(side=LEFT)
        
        relay_frame.columnconfigure(1, weight=1)
        
        # Lab Settings
        lab_frame = ttk.LabelFrame(self.frame, text='Lab Settings', padding=20)
        lab_frame.pack(fill=X, padx=10, pady=(0, 10))
        
        ttk.Label(lab_frame, text='Lab URL:').grid(row=0, column=0, sticky=W, pady=5)
        lab_url_entry = ttk.Entry(lab_frame, textvariable=self.main_window.lab_url_var, width=50)
        lab_url_entry.grid(row=0, column=1, sticky=EW, padx=(10, 0), pady=5)
        
        ttk.Checkbutton(lab_frame, text='Auto Start Lab', variable=self.main_window.auto_start_lab_var, bootstyle='round-toggle').grid(row=1, column=0, columnspan=2, sticky=W, pady=5)
        
        lab_frame.columnconfigure(1, weight=1)