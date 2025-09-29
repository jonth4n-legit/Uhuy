"""
GUI Tab: About Tab
"""
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class AboutTab:
    def __init__(self, main_window, notebook):
        self.main_window = main_window
        self.notebook = notebook
        self._build_ui()

    def _build_ui(self):
        """Build about tab UI"""
        self.frame = ttk.Frame(self.notebook)
        self.notebook.add(self.frame, text='About')
        
        # About content
        about_frame = ttk.Frame(self.frame)
        about_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = ttk.Label(about_frame, text='Auto Cloud Skill Registration', font=('Arial', 16, 'bold'))
        title_label.pack(pady=(0, 10))
        
        # Version
        version_label = ttk.Label(about_frame, text='Version 1.2.0', font=('Arial', 12))
        version_label.pack(pady=(0, 20))
        
        # Description
        description_text = """
This application automates Google Cloud Skills Boost registration with the following features:

🤖 Automated Account Registration
📧 Email Management via Firefox Relay
🎥 AI Video Generation using Google GenAI
🔧 Lab Automation with API Key Extraction
📊 Comprehensive Logging and Monitoring

Requirements:
• Firefox Relay API Key
• Google GenAI API Key (for video generation)
• Gmail API Credentials (optional)

The application uses Playwright for browser automation and integrates
with various Google APIs for enhanced functionality.
        """
        
        description_label = ttk.Label(about_frame, text=description_text, justify=tk.LEFT)
        description_label.pack(pady=(0, 20))
        
        # Author
        author_label = ttk.Label(about_frame, text='Author: SinyoRMX', font=('Arial', 10, 'italic'))
        author_label.pack(pady=(0, 10))
        
        # License info
        license_label = ttk.Label(about_frame, text='This software is provided as-is for educational purposes.', font=('Arial', 9))
        license_label.pack()