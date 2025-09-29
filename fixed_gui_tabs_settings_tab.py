"""
GUI Tab: Settings Tab
"""
import tkinter as tk
from tkinter import messagebox, filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class SettingsTab:
    def __init__(self, main_window, notebook):
        self.main_window = main_window
        self.notebook = notebook
        self._build_ui()

    def _build_ui(self):
        """Build settings tab UI"""
        self.frame = ttk.Frame(self.notebook)
        self.notebook.add(self.frame, text='Settings')
        
        # Gmail Settings
        gmail_frame = ttk.LabelFrame(self.frame, text='Gmail Settings', padding=20)
        gmail_frame.pack(fill=X, padx=10, pady=10)
        
        ttk.Label(gmail_frame, text='Credentials Path:').grid(row=0, column=0, sticky=W, pady=5)
        cred_path_frame = ttk.Frame(gmail_frame)
        cred_path_frame.grid(row=0, column=1, sticky=EW, padx=(10, 0), pady=5)
        
        cred_entry = ttk.Entry(cred_path_frame, textvariable=self.main_window.gmail_credentials_path_var, width=40)
        cred_entry.pack(side=LEFT, fill=X, expand=True)
        
        ttk.Button(cred_path_frame, text='Browse', command=self.main_window.browse_gmail_credentials, bootstyle=INFO).pack(side=LEFT, padx=(5, 0))
        
        # Gmail Auth Section
        auth_frame = ttk.Frame(gmail_frame)
        auth_frame.grid(row=1, column=0, columnspan=2, sticky=EW, pady=(10, 0))
        
        ttk.Button(auth_frame, text='Get Auth URL', command=self.main_window.generate_gmail_auth_url, bootstyle=INFO).pack(side=LEFT, padx=(0, 5))
        ttk.Button(auth_frame, text='Copy URL', command=self.main_window.copy_gmail_auth_url, bootstyle=SECONDARY).pack(side=LEFT, padx=(0, 5))
        
        # Auth URL
        ttk.Label(gmail_frame, text='Auth URL:').grid(row=2, column=0, sticky=W, pady=5)
        auth_url_entry = ttk.Entry(gmail_frame, textvariable=self.main_window.gmail_auth_url_var, width=50, state='readonly')
        auth_url_entry.grid(row=2, column=1, sticky=EW, padx=(10, 0), pady=5)
        
        # Auth Code
        ttk.Label(gmail_frame, text='Auth Code:').grid(row=3, column=0, sticky=W, pady=5)
        auth_code_frame = ttk.Frame(gmail_frame)
        auth_code_frame.grid(row=3, column=1, sticky=EW, padx=(10, 0), pady=5)
        
        auth_code_entry = ttk.Entry(auth_code_frame, textvariable=self.main_window.gmail_auth_code_var, width=30)
        auth_code_entry.pack(side=LEFT, fill=X, expand=True)
        
        ttk.Button(auth_code_frame, text='Authenticate', command=self.main_window.complete_gmail_auth_async, bootstyle=SUCCESS).pack(side=LEFT, padx=(5, 0))
        
        # Status labels
        status_frame = ttk.Frame(gmail_frame)
        status_frame.grid(row=4, column=0, columnspan=2, sticky=EW, pady=(10, 0))
        
        self.main_window.gmail_status_label = ttk.Label(status_frame, text='Gmail: 🛑 Not configured', bootstyle=WARNING)
        self.main_window.gmail_status_label.pack(side=LEFT)
        
        gmail_frame.columnconfigure(1, weight=1)
        
        # Browser Settings
        browser_frame = ttk.LabelFrame(self.frame, text='Browser Settings', padding=20)
        browser_frame.pack(fill=X, padx=10, pady=(0, 10))
        
        ttk.Checkbutton(browser_frame, text='Use reCAPTCHA Extension Mode', variable=self.main_window.extension_mode_var, bootstyle='round-toggle').pack(anchor=W, pady=5)
        
        # License Information
        license_frame = ttk.LabelFrame(self.frame, text='License Information', padding=20)
        license_frame.pack(fill=X, padx=10, pady=(0, 10))
        
        ttk.Label(license_frame, text='Plan:').grid(row=0, column=0, sticky=W, pady=5)
        self.main_window.license_plan_var = tk.StringVar(value='Unknown')
        ttk.Label(license_frame, textvariable=self.main_window.license_plan_var, bootstyle=INFO).grid(row=0, column=1, sticky=W, padx=(10, 0), pady=5)
        
        ttk.Label(license_frame, text='Expires:').grid(row=1, column=0, sticky=W, pady=5)
        self.main_window.license_expiry_var = tk.StringVar(value='Unknown')
        ttk.Label(license_frame, textvariable=self.main_window.license_expiry_var, bootstyle=INFO).grid(row=1, column=1, sticky=W, padx=(10, 0), pady=5)