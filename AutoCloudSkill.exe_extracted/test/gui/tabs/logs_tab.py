# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: gui\tabs\logs_tab.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
Logs tab UI for Auto Cloud Skill.
This tab builds the Logs UI and binds necessary widgets/vars on the MainWindow (owner).
"""
import tkinter as tk
from tkinter import scrolledtext
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class LogsTab:

    def __init__(self, owner, notebook):
        self.owner = owner
        self._build(notebook)

    def _build(self, notebook):
        frame = ttk.Frame(notebook, padding=20)
        notebook.add(frame, text='Logs')
        self.owner.log_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=80, height=25, font=('Consolas', 9), bg='#2b3e50', fg='#ecf0f1', insertbackground='#ecf0f1')
        self.owner.log_text.pack(fill=BOTH, expand=True)
        self.owner.gmail_progress_container = ttk.Frame(frame)
        self.owner.gmail_progress_label = ttk.Label(self.owner.gmail_progress_container, text='', bootstyle=INFO)
        self.owner.gmail_progress_label.pack(side=LEFT)
        self.owner.gmail_progress = ttk.Progressbar(self.owner.gmail_progress_container, orient='horizontal', mode='determinate', length=250)
        self.owner.gmail_progress.pack(side=RIGHT, padx=(10, 0))
        self.owner.gmail_progress_job = None
        self.owner.gmail_progress_running = False
        log_controls = ttk.Frame(frame)
        log_controls.pack(fill=X, pady=(10, 0))
        ttk.Button(log_controls, text='Clear Logs', command=self.owner.clear_logs, bootstyle=WARNING).pack(side=LEFT)
        ttk.Button(log_controls, text='Save Logs', command=self.owner.save_logs, bootstyle=INFO).pack(side=LEFT, padx=(10, 0))