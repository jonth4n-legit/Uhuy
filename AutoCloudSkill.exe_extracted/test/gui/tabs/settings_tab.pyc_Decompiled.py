# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: gui\tabs\settings_tab.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
Settings tab UI for Auto Cloud Skill.
This tab builds the Settings UI and binds to variables/methods of MainWindow (owner).
"""
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class SettingsTab:

    def __init__(self, owner, notebook):
        self.owner = owner
        self._build(notebook)

    def _build(self, notebook):
        canvas_window = ttk.Frame(notebook)
        notebook.add(canvas_window, text='Settings')
        _update_scrollregion = tk.Canvas(canvas_window, highlightthickness=0)
        vscroll = ttk.Scrollbar(canvas_window, orient='vertical', command=_update_scrollregion.yview)
        _update_scrollregion.configure(yscrollcommand=vscroll.set)
        _update_scrollregion.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vscroll.pack(side=tk.RIGHT, fill=tk.Y)
        frame = ttk.Frame(_update_scrollregion, padding=20)
        canvas = _update_scrollregion.create_window((0, 0), window=frame, anchor='nw')

        def _on_frame_configure(event=None):
            canvas.configure(scrollregion=canvas.bbox('all'))
            try:
                canvas.itemconfig(canvas_window, width=canvas.winfo_width())
            except Exception:
                return None

        def _on_mousewheel(event):
            delta = event.delta
            if delta == 0 and hasattr(event, 'num'):
                delta = 120 if event.num == 4 else -120
            try:
                canvas.yview_scroll(int(-delta + 120), 'units')
            except Exception:
                return None
        frame.bind('<Configure>', self)

        def _bind_wheel(_):
            canvas.bind_all('<MouseWheel>', _on_mousewheel)
            canvas.bind_all('<Button-4>', _on_mousewheel)
            canvas.bind_all('<Button-5>', _on_mousewheel)

        def _unbind_wheel(_):
            canvas.unbind_all('<MouseWheel>')
            canvas.unbind_all('<Button-4>')
            canvas.unbind_all('<Button-5>')
        _update_scrollregion.bind('<Enter>', _bind_wheel)
        _update_scrollregion.bind('<Leave>', _unbind_wheel)

        def _update_scrollregion():
            try:
                outer.update_idletasks()
                _on_frame_configure()
                canvas.yview_moveto(0.0)
            except Exception:
                return None
        canvas_window.bind('<Visibility>', lambda e: _update_scrollregion())
        canvas_window.bind('<Configure>', lambda e: _update_scrollregion())
        canvas_window.after(0, _on_mousewheel)

        def _on_tab_changed(event):
            try:
                current = event.widget.nametowidget(event.widget.select())
                if current is outer:
                    _update_scrollregion()
            except Exception:
                return None
        try:
            notebook.bind('<<NotebookTabChanged>>', _on_tab_changed)
        except Exception:
            pass
        try:
            canvas_window.update_idletasks()
            _on_mousewheel()
        except Exception:
            pass
        api_frame = ttk.LabelFrame(frame, text='API Configuration', padding=15)
        api_frame.pack(fill=X, pady=(0, 10))
        ttk.Label(api_frame, text='Firefox Relay API Key:').pack(anchor=W)
        api_key_entry = ttk.Entry(api_frame, textvariable=self.owner.firefox_api_key_var, show='*', width=50)
        api_key_entry.pack(fill=X, pady=(5, 10))
        actions_frame = ttk.Frame(api_frame)
        actions_frame.pack(fill=X)
        test_api_btn = ttk.Button(actions_frame, text='Test API Key', command=self.owner.test_firefox_api_key, bootstyle=INFO, width=15)
        test_api_btn.pack(side=LEFT)
        delete_masks_btn = ttk.Button(actions_frame, text='Delete All Masks', command=self.owner.delete_all_firefox_masks, bootstyle=DANGER, width=18)
        delete_masks_btn.pack(side=LEFT, padx=(10, 0))
        browser_frame = ttk.LabelFrame(frame, text='Browser / Captcha Settings', padding=15)
        browser_frame.pack(fill=X, pady=(0, 10))
        ext_check = ttk.Checkbutton(browser_frame, text='Use reCAPTCHA extension (manual)', variable=self.owner.extension_mode_var, bootstyle='warning-round-toggle')
        ext_check.pack(anchor=W)
        gmail_frame = ttk.LabelFrame(frame, text='Gmail Settings', padding=15)
        gmail_frame.pack(fill=X, pady=(0, 10))
        ggrid = ttk.Frame(gmail_frame)
        ggrid.pack(fill=X)
        try:
            ggrid.columnconfigure(0, weight=0)
            ggrid.columnconfigure(1, weight=1)
            ggrid.columnconfigure(2, weight=0)
            ggrid.columnconfigure(3, weight=0)
        except Exception:
            pass
        BTN_W = 16
        ttk.Label(ggrid, text='credentials.json path:').grid(row=0, column=0, sticky=W, pady=(0, 6))
        gmail_entry = ttk.Entry(ggrid, textvariable=self.owner.gmail_credentials_path_var)
        gmail_entry.grid(row=0, column=1, sticky=EW, padx=(8, 8), pady=(0, 6))
        ttk.Button(ggrid, text='Browse...', width=BTN_W, command=self.owner.browse_gmail_credentials, bootstyle=INFO).grid(row=0, column=2, sticky=E, padx=(0, 6), pady=(0, 6))
        ttk.Button(ggrid, text='Get Auth URL', width=BTN_W, command=self.owner.generate_gmail_auth_url, bootstyle=SUCCESS).grid(row=0, column=3, sticky=E, pady=(0, 6))
        ttk.Label(ggrid, text='Auth URL:').grid(row=1, column=0, sticky=W, pady=(0, 6))
        url_entry = ttk.Entry(ggrid, textvariable=self.owner.gmail_auth_url_var)
        url_entry.grid(row=1, column=1, sticky=EW, padx=(8, 8), pady=(0, 6))
        ttk.Button(ggrid, text='Copy URL', width=BTN_W, command=self.owner.copy_gmail_auth_url, bootstyle=INFO).grid(row=1, column=2, sticky=E, padx=(0, 6), pady=(0, 6))
        ttk.Label(ggrid, text='').grid(row=1, column=3)
        ttk.Label(ggrid, text='Verification code:').grid(row=2, column=0, sticky=W)
        code_entry = ttk.Entry(ggrid, textvariable=self.owner.gmail_auth_code_var)
        code_entry.grid(row=2, column=1, sticky=EW, padx=(8, 8))
        ttk.Button(ggrid, text='Complete Auth', width=BTN_W, command=self.owner.complete_gmail_auth_async, bootstyle=PRIMARY).grid(row=2, column=2, sticky=E, padx=(0, 6))
        ttk.Label(ggrid, text='').grid(row=2, column=3)
        lab_frame = ttk.LabelFrame(frame, text='Lab Settings', padding=15)
        lab_frame.pack(fill=X, pady=(10, 10))
        ttk.Label(lab_frame, text='Lab URL (focuses/...):').pack(anchor=W)
        labrow = ttk.Frame(lab_frame)
        labrow.pack(fill=X, pady=(5, 0))
        lab_entry = ttk.Entry(labrow, textvariable=self.owner.lab_url_var)
        lab_entry.pack(side=LEFT, fill=X, expand=True)
        ttk.Button(labrow, text='Paste', command=lambda: self.owner.lab_url_var.set(self.owner.root.clipboard_get() or ''), bootstyle=INFO).pack(side=LEFT, padx=(8, 0))
        auto_row = ttk.Frame(lab_frame)
        auto_row.pack(fill=X, pady=(8, 0))
        ttk.Checkbutton(auto_row, text='Auto start lab after confirmation', variable=self.owner.auto_start_lab_var, bootstyle='round-toggle').pack(side=LEFT)
        status_frame = ttk.LabelFrame(frame, text='Service Status', padding=15)
        status_frame.pack(fill=X)
        self.owner.firefox_status_label = ttk.Label(status_frame, text='Firefox Relay: 🛑 API Key Required', bootstyle=DANGER)
        self.owner.firefox_status_label.pack(anchor=W)
        self.owner.gmail_status_label = ttk.Label(status_frame, text='Gmail: 🛑 Not configured', bootstyle=WARNING)
        self.owner.gmail_status_label.pack(anchor=W, pady=(5, 0))
        ttk.Label(status_frame, text='RandomUser API: ✅ Available', bootstyle=SUCCESS).pack(anchor=W, pady=(5, 0))
        ttk.Label(status_frame, text='Audio Captcha Solver: ✅ Ready', bootstyle=SUCCESS).pack(anchor=W, pady=(5, 0))
        try:
            self.owner.update_gmail_status_label()
        except Exception:
            return None