# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: gui\tabs\registration_tab.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
Registration tab UI for Auto Cloud Skill.
This tab builds the Registration Form and binds to variables/methods of MainWindow (owner).
"""
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class RegistrationTab:

    def __init__(self, owner, notebook):
        self.owner = owner
        self._build(notebook)

    def _build(self, notebook):
        frame = ttk.Frame(notebook, padding=20)
        notebook.add(frame, text='Registration Form')
        form_frame = ttk.LabelFrame(frame, text='Registration Data', padding=15)
        form_frame.pack(fill=BOTH, expand=True)
        ttk.Label(form_frame, text='First Name:').grid(row=0, column=0, sticky=W, pady=5)
        first_name_entry = ttk.Entry(form_frame, textvariable=self.owner.first_name_var, width=30)
        first_name_entry.grid(row=0, column=1, sticky=W + E, padx=(10, 0), pady=5)
        ttk.Label(form_frame, text='Last Name:').grid(row=1, column=0, sticky=W, pady=5)
        last_name_entry = ttk.Entry(form_frame, textvariable=self.owner.last_name_var, width=30)
        last_name_entry.grid(row=1, column=1, sticky=W + E, padx=(10, 0), pady=5)
        ttk.Label(form_frame, text='Email:').grid(row=2, column=0, sticky=W, pady=5)
        email_entry = ttk.Entry(form_frame, textvariable=self.owner.email_var, width=30)
        email_entry.grid(row=2, column=1, sticky=W + E, padx=(10, 0), pady=5)
        ttk.Label(form_frame, text='Company:').grid(row=3, column=0, sticky=W, pady=5)
        company_entry = ttk.Entry(form_frame, textvariable=self.owner.company_var, width=30)
        company_entry.grid(row=3, column=1, sticky=W + E, padx=(10, 0), pady=5)
        ttk.Label(form_frame, text='Password:').grid(row=4, column=0, sticky=W, pady=5)
        self.owner.password_entry = ttk.Entry(form_frame, textvariable=self.owner.password_var, show='*', width=30)
        self.owner.password_entry.grid(row=4, column=1, sticky=W + E, padx=(10, 0), pady=5)
        show_pw_check = ttk.Checkbutton(form_frame, text='Show', variable=self.owner.show_password_var, command=self.owner.toggle_password_visibility, bootstyle='round-toggle')
        show_pw_check.grid(row=4, column=2, padx=(10, 0), sticky=W)
        copy_pw_btn = ttk.Button(form_frame, text='Copy', command=self.owner.copy_password, bootstyle=INFO, width=8)
        copy_pw_btn.grid(row=4, column=3, padx=(10, 0), sticky=W)
        ttk.Label(form_frame, text='Confirm Password:').grid(row=5, column=0, sticky=W, pady=5)
        self.owner.password_confirm_entry = ttk.Entry(form_frame, textvariable=self.owner.password_confirm_var, show='*', width=30)
        self.owner.password_confirm_entry.grid(row=5, column=1, sticky=W + E, padx=(10, 0), pady=5)
        form_frame.columnconfigure(1, weight=1)