# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: gui\tabs\about_tab.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
About tab UI for Auto Cloud Skill.
This tab shows application info, Machine ID, and License details (plan and expiry).
It binds StringVars on the owner (MainWindow) to be updated by license checker.
"""
import hashlib
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from config.licensing import get_machine_id
from config.constants import APP_NAME, VERSION, AUTHOR

class AboutTab:

    def __init__(self, owner, notebook):
        self.owner = owner
        self._build(notebook)

    def _build(self, notebook):
        frame = ttk.Frame(notebook, padding=20)
        notebook.add(frame, text='About')
        info = ttk.LabelFrame(frame, text='Application', padding=15)
        info.pack(fill=X)
        ttk.Label(info, text=f'Name: {APP_NAME}').pack(anchor=W)
        ttk.Label(info, text=f'Version: {VERSION}').pack(anchor=W)
        ttk.Label(info, text=f'Author: {AUTHOR}').pack(anchor=W)
        ttk.Label(info, text='© SinyoRmx').pack(anchor=W, pady=(4, 0))
        mid_frame = ttk.LabelFrame(frame, text='Machine ID', padding=15)
        mid_frame.pack(fill=X, pady=(12, 0))
        try:
            raw_mid = get_machine_id()
            hashed = hashlib.sha256(raw_mid.encode('utf-8')).hexdigest()
        except Exception as e:
            hashed = f'Error: {e}'
        self.owner.hashed_mid_var = tk.StringVar(value=hashed)
        entry = ttk.Entry(mid_frame, textvariable=self.owner.hashed_mid_var, state='readonly')
        entry.pack(side=LEFT, fill=X, expand=True)

        def _copy_mid():
            try:
                self.owner.root.clipboard_clear()
                self.owner.root.clipboard_append(self.owner.hashed_mid_var.get())
                self.owner.log_message('ℹ️ Machine ID copied to clipboard.')
            except Exception as e:
                self.owner.log_message(f'⚠️ Copy error: {e}')
        ttk.Button(mid_frame, text='Copy', command=_copy_mid, bootstyle=INFO).pack(side=LEFT, padx=(8, 0))
        license_frame = ttk.LabelFrame(frame, text='License', padding=15)
        license_frame.pack(fill=X, pady=(12, 0))
        self.owner.license_plan_var = tk.StringVar(value='Unknown')
        ttk.Label(license_frame, text='Plan:').pack(anchor=W)
        ttk.Label(license_frame, textvariable=self.owner.license_plan_var).pack(anchor=W)
        self.owner.license_expiry_var = tk.StringVar(value='Lifetime')
        ttk.Label(license_frame, text='Expires at:').pack(anchor=W)
        ttk.Label(license_frame, textvariable=self.owner.license_expiry_var).pack(anchor=W)