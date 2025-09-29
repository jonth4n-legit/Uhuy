"""
GUI Tab: Logs Tab
"""
import tkinter as tk
from tkinter import messagebox, filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class LogsTab:
    def __init__(self, main_window, notebook):
        self.main_window = main_window
        self.notebook = notebook
        self._build_ui()

    def _build_ui(self):
        """Build logs tab UI"""
        self.frame = ttk.Frame(self.notebook)
        self.notebook.add(self.frame, text='Logs')
        
        # Log controls
        controls_frame = ttk.Frame(self.frame)
        controls_frame.pack(fill=X, padx=10, pady=(10, 5))
        
        ttk.Button(controls_frame, text='Clear Logs', command=self.main_window.clear_logs, bootstyle=WARNING).pack(side=LEFT, padx=(0, 5))
        ttk.Button(controls_frame, text='Save Logs', command=self.main_window.save_logs, bootstyle=INFO).pack(side=LEFT)
        
        # Log text area
        log_frame = ttk.Frame(self.frame)
        log_frame.pack(fill=BOTH, expand=True, padx=10, pady=(0, 10))
        
        self.main_window.log_text = tk.Text(log_frame, wrap=tk.WORD, height=20, font=('Consolas', 10))
        scrollbar = ttk.Scrollbar(log_frame, orient=tk.VERTICAL, command=self.main_window.log_text.yview)
        self.main_window.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.main_window.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)