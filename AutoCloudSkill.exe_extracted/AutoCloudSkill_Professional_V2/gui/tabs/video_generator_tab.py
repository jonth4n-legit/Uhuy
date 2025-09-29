"""
Professional Video Generator Tab for AutoCloudSkill Application.

This module provides a comprehensive video generation interface using Google's GenAI
Veo models with advanced features like bulk processing, image-to-video conversion,
and professional video post-processing.

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import os
import threading
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pathlib import Path
from datetime import datetime
from typing import Optional, Callable, List, Dict, Any, TYPE_CHECKING
import json

from services.genai_video_service import GenAIVideoService
from services.video_postprocess_service import VideoPostprocessService

if TYPE_CHECKING:
    pass


class VideoGeneratorTab:
    """Professional video generator tab using Google GenAI Veo models."""

    def __init__(
        self,
        root: tk.Misc,
        notebook: ttk.Notebook,
        log_fn: Callable[[str], None],
        request_new_api_key_and_wait: Optional[Callable[[str, int], Optional[str]]] = None
    ):
        """Initialize the video generator tab.

        Args:
            root: Root tkinter widget
            notebook: Parent notebook widget
            log_fn: Logging function
            request_new_api_key_and_wait: Function to request new API key
        """
        self.root = root
        self.notebook = notebook
        self.log = log_fn
        self.request_new_api_key_and_wait = request_new_api_key_and_wait

        # Initialize variables
        self._initialize_variables()

        # Initialize services
        self.video_service: Optional[GenAIVideoService] = None
        self.postprocess_service = VideoPostprocessService()

        # Thread management
        self._stop_event = None
        self._worker_thread = None

        # Build interface
        self._build_interface()

    def _initialize_variables(self) -> None:
        """Initialize all tkinter variables."""
        # API configuration
        self.api_key_var = tk.StringVar()

        # Model configuration
        self.model_var = tk.StringVar(value='veo-3.0-generate-001')
        self.aspect_ratio_var = tk.StringVar(value='16:9')
        self.resolution_var = tk.StringVar(value='720p')

        # Prompt configuration
        self.neg_prompt_var = tk.StringVar()
        self.prompt_count_var = tk.StringVar(value='Prompts: 0')

        # Output configuration
        self.output_dir_var = tk.StringVar(value=str(Path.home() / 'Downloads' / 'AutoCloudSkill_Videos'))

        # Feature toggles
        self.image_to_video_var = tk.BooleanVar(value=False)
        self.veo2_double_var = tk.BooleanVar(value=False)
        self.veo3_audio_var = tk.BooleanVar(value=True)
        self.auto_enhance_var = tk.BooleanVar(value=True)

        # UI references
        self.prompts_text = None
        self.progress_label = None
        self.progress_bar = None
        self.start_btn = None
        self.stop_btn = None

    def _build_interface(self) -> None:
        """Build the complete video generator interface."""
        # Create scrollable container
        self._create_scrollable_container()

        # Build interface sections
        self._create_api_section()
        self._create_model_configuration()
        self._create_prompt_section()
        self._create_feature_toggles()
        self._create_output_configuration()
        self._create_progress_section()
        self._create_control_buttons()

        # Setup scrolling
        self._setup_scrolling()

    def _create_scrollable_container(self) -> None:
        """Create scrollable container for the tab."""
        # Main tab frame
        self.tab_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_frame, text='🎬 Video Generator')

        # Canvas for scrolling
        self.canvas = tk.Canvas(self.tab_frame, highlightthickness=0)
        self.v_scrollbar = ttk.Scrollbar(
            self.tab_frame,
            orient='vertical',
            command=self.canvas.yview
        )

        self.canvas.configure(yscrollcommand=self.v_scrollbar.set)

        # Pack scrollbar and canvas
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollable frame
        self.scrollable_frame = ttk.Frame(self.canvas, padding=20)
        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor='nw'
        )

    def _setup_scrolling(self) -> None:
        """Setup canvas scrolling functionality."""
        def on_frame_configure(event=None):
            """Update scroll region when frame size changes."""
            self.canvas.configure(scrollregion=self.canvas.bbox('all'))
            try:
                canvas_width = self.canvas.winfo_width()
                self.canvas.itemconfig(self.canvas_window, width=canvas_width)
            except Exception:
                pass

        def on_mousewheel(event):
            """Handle mouse wheel scrolling."""
            delta = event.delta
            if delta == 0 and hasattr(event, 'num'):
                delta = 120 if event.num == 4 else -120
            try:
                self.canvas.yview_scroll(int(-delta / 120), 'units')
            except Exception:
                pass

        def bind_mousewheel(event):
            """Bind mouse wheel events."""
            self.canvas.bind_all('<MouseWheel>', on_mousewheel)
            self.canvas.bind_all('<Button-4>', on_mousewheel)
            self.canvas.bind_all('<Button-5>', on_mousewheel)

        def unbind_mousewheel(event):
            """Unbind mouse wheel events."""
            self.canvas.unbind_all('<MouseWheel>')
            self.canvas.unbind_all('<Button-4>')
            self.canvas.unbind_all('<Button-5>')

        # Bind events
        self.scrollable_frame.bind('<Configure>', on_frame_configure)
        self.canvas.bind('<Enter>', bind_mousewheel)
        self.canvas.bind('<Leave>', unbind_mousewheel)

    def _create_api_section(self) -> None:
        """Create API key configuration section."""
        api_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text='🔑 Google GenAI API Configuration',
            padding=15,
            bootstyle=PRIMARY
        )
        api_frame.pack(fill=X, pady=(0, 15))

        # API key display
        api_row = ttk.Frame(api_frame)
        api_row.pack(fill=X, pady=(0, 10))

        self.api_key_entry = ttk.Entry(
            api_row,
            textvariable=self.api_key_var,
            width=60,
            state='readonly',
            font=('Consolas', 10)
        )
        self.api_key_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))

        # Copy API key button
        ttk.Button(
            api_row,
            text='📋 Copy',
            width=10,
            command=self._copy_api_key,
            bootstyle=SECONDARY
        ).pack(side=LEFT)

        # API key status
        self.api_status_label = ttk.Label(
            api_frame,
            text='🔑 API Key: Not available - complete registration first',
            font=('Segoe UI', 9),
            bootstyle=WARNING
        )
        self.api_status_label.pack(anchor=W)

        # API key info
        api_info = ttk.Label(
            api_frame,
            text='💡 API key is automatically provided after successful lab registration',
            font=('Segoe UI', 9),
            bootstyle=INFO
        )
        api_info.pack(anchor=W, pady=(5, 0))

    def _create_model_configuration(self) -> None:
        """Create model configuration section."""
        model_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text='🤖 Model Configuration',
            padding=15,
            bootstyle=SECONDARY
        )
        model_frame.pack(fill=X, pady=(0, 15))

        # Model selection
        model_row = ttk.Frame(model_frame)
        model_row.pack(fill=X, pady=(0, 10))

        ttk.Label(
            model_row,
            text='AI Model:',
            font=('Segoe UI', 10, 'bold')
        ).pack(side=LEFT, padx=(0, 10))

        model_combo = ttk.Combobox(
            model_row,
            textvariable=self.model_var,
            values=[
                'veo-3.0-generate-001',
                'veo-3.0-fast-generate-001',
                'veo-2.0-generate-001'
            ],
            state='readonly',
            width=25
        )
        model_combo.pack(side=LEFT, padx=(0, 20))

        # Aspect ratio
        ttk.Label(
            model_row,
            text='Aspect Ratio:',
            font=('Segoe UI', 10, 'bold')
        ).pack(side=LEFT, padx=(0, 10))

        aspect_combo = ttk.Combobox(
            model_row,
            textvariable=self.aspect_ratio_var,
            values=['16:9', '9:16', '1:1', '4:3', '3:4'],
            state='readonly',
            width=10
        )
        aspect_combo.pack(side=LEFT)

        # Resolution selection
        resolution_row = ttk.Frame(model_frame)
        resolution_row.pack(fill=X, pady=(0, 10))

        ttk.Label(
            resolution_row,
            text='Resolution:',
            font=('Segoe UI', 10, 'bold')
        ).pack(side=LEFT, padx=(0, 10))

        resolution_combo = ttk.Combobox(
            resolution_row,
            textvariable=self.resolution_var,
            values=['720p', '1080p', '4K'],
            state='readonly',
            width=10
        )
        resolution_combo.pack(side=LEFT)

        # Negative prompt
        neg_prompt_row = ttk.Frame(model_frame)
        neg_prompt_row.pack(fill=X)

        ttk.Label(
            neg_prompt_row,
            text='Negative Prompt:',
            font=('Segoe UI', 10, 'bold')
        ).pack(anchor=W, pady=(0, 5))

        self.neg_prompt_entry = ttk.Entry(
            neg_prompt_row,
            textvariable=self.neg_prompt_var,
            font=('Segoe UI', 10)
        )
        self.neg_prompt_entry.pack(fill=X)

    def _create_prompt_section(self) -> None:
        """Create prompt input section."""
        prompt_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text='📝 Video Prompts',
            padding=15,
            bootstyle=INFO
        )
        prompt_frame.pack(fill=X, pady=(0, 15))

        # Prompt count and controls
        prompt_header = ttk.Frame(prompt_frame)
        prompt_header.pack(fill=X, pady=(0, 10))

        self.prompt_count_label = ttk.Label(
            prompt_header,
            textvariable=self.prompt_count_var,
            font=('Segoe UI', 10, 'bold'),
            bootstyle=INFO
        )
        self.prompt_count_label.pack(side=LEFT)

        # Load prompts button
        ttk.Button(
            prompt_header,
            text='📁 Load from File',
            command=self._load_prompts_from_file,
            bootstyle=SUCCESS,
            width=15
        ).pack(side=RIGHT, padx=(5, 0))

        # Save prompts button
        ttk.Button(
            prompt_header,
            text='💾 Save to File',
            command=self._save_prompts_to_file,
            bootstyle=INFO,
            width=15
        ).pack(side=RIGHT)

        # Prompts text area
        self.prompts_text = scrolledtext.ScrolledText(
            prompt_frame,
            wrap=tk.WORD,
            width=80,
            height=12,
            font=('Segoe UI', 10),
            bg='#f8f9fa',
            fg='#212529'
        )
        self.prompts_text.pack(fill=BOTH, expand=True, pady=(0, 10))

        # Bind text change event
        self.prompts_text.bind('<KeyRelease>', self._update_prompt_count)
        self.prompts_text.bind('<ButtonRelease>', self._update_prompt_count)

        # Prompt templates
        template_frame = ttk.Frame(prompt_frame)
        template_frame.pack(fill=X)

        ttk.Label(
            template_frame,
            text='Quick Templates:',
            font=('Segoe UI', 9, 'bold')
        ).pack(side=LEFT, padx=(0, 10))

        # Template buttons
        templates = [
            ('🌅 Nature', 'A serene landscape with mountains and flowing water'),
            ('🏃 Action', 'Dynamic action scene with movement and energy'),
            ('🎨 Abstract', 'Abstract artistic visualization with flowing colors'),
            ('🏙️ Urban', 'Modern city scene with architecture and lights')
        ]

        for name, template in templates:
            ttk.Button(
                template_frame,
                text=name,
                command=lambda t=template: self._add_template(t),
                bootstyle=OUTLINE,
                width=12
            ).pack(side=LEFT, padx=(0, 5))

    def _create_feature_toggles(self) -> None:
        """Create feature toggle section."""
        features_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text='🚀 Advanced Features',
            padding=15,
            bootstyle=WARNING
        )
        features_frame.pack(fill=X, pady=(0, 15))

        # Feature toggles grid
        features_grid = ttk.Frame(features_frame)
        features_grid.pack(fill=X)

        # Image-to-Video
        self.image_to_video_check = ttk.Checkbutton(
            features_grid,
            text='🖼️ Image-to-Video (via Imagen 4 Ultra)',
            variable=self.image_to_video_var,
            bootstyle='info-round-toggle'
        )
        self.image_to_video_check.grid(row=0, column=0, sticky=W, pady=5)

        # Veo 2 Double Generation
        self.veo2_double_check = ttk.Checkbutton(
            features_grid,
            text='🔄 Veo 2: Generate 2 videos per prompt',
            variable=self.veo2_double_var,
            bootstyle='warning-round-toggle'
        )
        self.veo2_double_check.grid(row=1, column=0, sticky=W, pady=5)

        # Veo 3 Audio
        self.veo3_audio_check = ttk.Checkbutton(
            features_grid,
            text='🔊 Veo 3: Generate with audio (default ON)',
            variable=self.veo3_audio_var,
            bootstyle='success-round-toggle'
        )
        self.veo3_audio_check.grid(row=2, column=0, sticky=W, pady=5)

        # Auto Enhancement
        self.auto_enhance_check = ttk.Checkbutton(
            features_grid,
            text='✨ Auto-enhance video quality',
            variable=self.auto_enhance_var,
            bootstyle='primary-round-toggle'
        )
        self.auto_enhance_check.grid(row=3, column=0, sticky=W, pady=5)

    def _create_output_configuration(self) -> None:
        """Create output configuration section."""
        output_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text='💾 Output Configuration',
            padding=15,
            bootstyle=SUCCESS
        )
        output_frame.pack(fill=X, pady=(0, 15))

        # Output directory
        output_row = ttk.Frame(output_frame)
        output_row.pack(fill=X, pady=(0, 10))

        ttk.Label(
            output_row,
            text='Output Directory:',
            font=('Segoe UI', 10, 'bold')
        ).pack(anchor=W, pady=(0, 5))

        dir_input_row = ttk.Frame(output_row)
        dir_input_row.pack(fill=X)

        self.output_dir_entry = ttk.Entry(
            dir_input_row,
            textvariable=self.output_dir_var,
            font=('Segoe UI', 10)
        )
        self.output_dir_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))

        ttk.Button(
            dir_input_row,
            text='📁 Browse',
            command=self._browse_output_directory,
            bootstyle=INFO,
            width=12
        ).pack(side=LEFT, padx=(0, 5))

        ttk.Button(
            dir_input_row,
            text='📂 Open',
            command=self._open_output_directory,
            bootstyle=SUCCESS,
            width=10
        ).pack(side=LEFT)

        # Output format info
        format_info = ttk.Label(
            output_frame,
            text='💡 Videos are saved as MP4 files with timestamps and quality indicators',
            font=('Segoe UI', 9),
            bootstyle=INFO
        )
        format_info.pack(anchor=W)

    def _create_progress_section(self) -> None:
        """Create progress tracking section."""
        progress_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text='📊 Generation Progress',
            padding=15,
            bootstyle=DARK
        )
        progress_frame.pack(fill=X, pady=(0, 15))

        # Progress label
        self.progress_label = ttk.Label(
            progress_frame,
            text='Ready to generate videos',
            font=('Segoe UI', 10),
            bootstyle=INFO
        )
        self.progress_label.pack(anchor=W, pady=(0, 10))

        # Progress bar
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            orient='horizontal',
            mode='determinate',
            length=400,
            bootstyle='info-striped'
        )
        self.progress_bar.pack(fill=X, pady=(0, 10))

        # Statistics display
        stats_frame = ttk.Frame(progress_frame)
        stats_frame.pack(fill=X)

        self.stats_label = ttk.Label(
            stats_frame,
            text='Videos: 0 | Success: 0 | Failed: 0 | Total Size: 0 MB',
            font=('Segoe UI', 9),
            bootstyle=SECONDARY
        )
        self.stats_label.pack(anchor=W)

    def _create_control_buttons(self) -> None:
        """Create control buttons section."""
        controls_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text='🎮 Controls',
            padding=15,
            bootstyle=PRIMARY
        )
        controls_frame.pack(fill=X)

        # Button container
        button_container = ttk.Frame(controls_frame)
        button_container.pack(fill=X)

        # Start generation button
        self.start_btn = ttk.Button(
            button_container,
            text='🎬 Start Generation',
            command=self._start_generation,
            bootstyle=SUCCESS,
            width=20,
            state=DISABLED
        )
        self.start_btn.pack(side=LEFT, padx=(0, 10))

        # Stop generation button
        self.stop_btn = ttk.Button(
            button_container,
            text='⏹️ Stop',
            command=self._stop_generation,
            bootstyle=DANGER,
            width=15,
            state=DISABLED
        )
        self.stop_btn.pack(side=LEFT, padx=(0, 10))

        # Preview button
        self.preview_btn = ttk.Button(
            button_container,
            text='👁️ Preview Setup',
            command=self._preview_generation_setup,
            bootstyle=INFO,
            width=15
        )
        self.preview_btn.pack(side=LEFT, padx=(0, 10))

        # Clear results button
        self.clear_btn = ttk.Button(
            button_container,
            text='🗑️ Clear Results',
            command=self._clear_results,
            bootstyle=WARNING,
            width=15
        )
        self.clear_btn.pack(side=LEFT)

        # Queue status
        self.queue_status_label = ttk.Label(
            controls_frame,
            text='Queue: Ready',
            font=('Segoe UI', 9),
            bootstyle=SECONDARY
        )
        self.queue_status_label.pack(anchor=W, pady=(10, 0))

    def set_api_key(self, api_key: str) -> None:
        """Set the GenAI API key.

        Args:
            api_key: The API key to set
        """
        try:
            self.api_key_var.set(api_key)

            if api_key and api_key.strip():
                # Initialize video service
                self.video_service = GenAIVideoService(api_key.strip())

                # Update status
                self.api_status_label.config(
                    text='🔑 API Key: ✅ Active and ready',
                    bootstyle=SUCCESS
                )

                # Enable start button if prompts are available
                self._update_ui_state()

                self.log('✅ GenAI API key set successfully')
            else:
                self.api_status_label.config(
                    text='🔑 API Key: ❌ Invalid or empty',
                    bootstyle=DANGER
                )
                self.start_btn.config(state=DISABLED)

        except Exception as e:
            self.log(f'🛑 Error setting API key: {e}')
            self.api_status_label.config(
                text='🔑 API Key: ❌ Error setting key',
                bootstyle=DANGER
            )

    def _copy_api_key(self) -> None:
        """Copy API key to clipboard."""
        try:
            api_key = self.api_key_var.get()
            if api_key:
                self.root.clipboard_clear()
                self.root.clipboard_append(api_key)
                self.log('📋 API key copied to clipboard')
            else:
                self.log('⚠️ No API key to copy')
        except Exception as e:
            self.log(f'🛑 Copy API key error: {e}')

    def _update_prompt_count(self, event=None) -> None:
        """Update prompt count display."""
        try:
            text_content = self.prompts_text.get('1.0', tk.END).strip()
            prompts = [p.strip() for p in text_content.split('\n') if p.strip()]
            count = len(prompts)

            self.prompt_count_var.set(f'Prompts: {count}')
            self._update_ui_state()

        except Exception as e:
            self.log(f'🛑 Error updating prompt count: {e}')

    def _update_ui_state(self) -> None:
        """Update UI state based on current conditions."""
        try:
            # Check if generation can start
            has_api_key = bool(self.api_key_var.get().strip())
            has_prompts = bool(self._get_prompts())
            is_running = bool(self._worker_thread and self._worker_thread.is_alive())

            # Enable/disable start button
            can_start = has_api_key and has_prompts and not is_running
            self.start_btn.config(state=NORMAL if can_start else DISABLED)

            # Enable/disable stop button
            self.stop_btn.config(state=NORMAL if is_running else DISABLED)

            # Update queue status
            if is_running:
                self.queue_status_label.config(text='Queue: Running...', bootstyle=SUCCESS)
            elif has_prompts:
                prompt_count = len(self._get_prompts())
                self.queue_status_label.config(
                    text=f'Queue: {prompt_count} prompts ready',
                    bootstyle=INFO
                )
            else:
                self.queue_status_label.config(text='Queue: No prompts', bootstyle=WARNING)

        except Exception as e:
            self.log(f'🛑 Error updating UI state: {e}')

    def _get_prompts(self) -> List[str]:
        """Get list of prompts from text area.

        Returns:
            List of non-empty prompt strings
        """
        try:
            text_content = self.prompts_text.get('1.0', tk.END).strip()
            return [p.strip() for p in text_content.split('\n') if p.strip()]
        except Exception:
            return []

    def _load_prompts_from_file(self) -> None:
        """Load prompts from a text file."""
        try:
            filename = filedialog.askopenfilename(
                title='Load Prompts',
                filetypes=[
                    ('Text files', '*.txt'),
                    ('JSON files', '*.json'),
                    ('All files', '*.*')
                ]
            )

            if filename:
                with open(filename, 'r', encoding='utf-8') as f:
                    if filename.endswith('.json'):
                        data = json.load(f)
                        if isinstance(data, list):
                            content = '\n'.join(data)
                        elif isinstance(data, dict) and 'prompts' in data:
                            content = '\n'.join(data['prompts'])
                        else:
                            content = str(data)
                    else:
                        content = f.read()

                self.prompts_text.delete('1.0', tk.END)
                self.prompts_text.insert('1.0', content)
                self._update_prompt_count()

                self.log(f'📁 Prompts loaded from: {filename}')

        except Exception as e:
            self.log(f'🛑 Error loading prompts: {e}')
            messagebox.showerror('Error', f'Failed to load prompts:\n{e}')

    def _save_prompts_to_file(self) -> None:
        """Save prompts to a text file."""
        try:
            prompts = self._get_prompts()
            if not prompts:
                messagebox.showwarning('Warning', 'No prompts to save')
                return

            filename = filedialog.asksaveasfilename(
                title='Save Prompts',
                defaultextension='.txt',
                filetypes=[
                    ('Text files', '*.txt'),
                    ('JSON files', '*.json'),
                    ('All files', '*.*')
                ],
                initialname=f'video_prompts_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
            )

            if filename:
                if filename.endswith('.json'):
                    data = {
                        'prompts': prompts,
                        'model': self.model_var.get(),
                        'aspect_ratio': self.aspect_ratio_var.get(),
                        'resolution': self.resolution_var.get(),
                        'negative_prompt': self.neg_prompt_var.get(),
                        'created_at': datetime.now().isoformat()
                    }
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                else:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write('\n'.join(prompts))

                self.log(f'💾 Prompts saved to: {filename}')

        except Exception as e:
            self.log(f'🛑 Error saving prompts: {e}')
            messagebox.showerror('Error', f'Failed to save prompts:\n{e}')

    def _add_template(self, template: str) -> None:
        """Add a template prompt to the text area.

        Args:
            template: Template prompt to add
        """
        try:
            current_content = self.prompts_text.get('1.0', tk.END).strip()
            if current_content:
                new_content = f'{current_content}\n{template}'
            else:
                new_content = template

            self.prompts_text.delete('1.0', tk.END)
            self.prompts_text.insert('1.0', new_content)
            self._update_prompt_count()

            self.log(f'➕ Template added: {template[:50]}...')

        except Exception as e:
            self.log(f'🛑 Error adding template: {e}')

    def _browse_output_directory(self) -> None:
        """Browse for output directory."""
        try:
            directory = filedialog.askdirectory(
                title='Select Output Directory',
                initialdir=self.output_dir_var.get()
            )

            if directory:
                self.output_dir_var.set(directory)
                self.log(f'📁 Output directory set: {directory}')

        except Exception as e:
            self.log(f'🛑 Error browsing output directory: {e}')

    def _open_output_directory(self) -> None:
        """Open output directory in file explorer."""
        try:
            output_dir = Path(self.output_dir_var.get())
            if output_dir.exists():
                os.startfile(str(output_dir))  # Windows
                self.log(f'📂 Opened output directory: {output_dir}')
            else:
                self.log('⚠️ Output directory does not exist')

        except Exception as e:
            self.log(f'🛑 Error opening output directory: {e}')

    def _preview_generation_setup(self) -> None:
        """Preview the generation setup."""
        try:
            prompts = self._get_prompts()
            if not prompts:
                messagebox.showwarning('Warning', 'No prompts to preview')
                return

            # Prepare preview info
            setup_info = [
                f"Model: {self.model_var.get()}",
                f"Aspect Ratio: {self.aspect_ratio_var.get()}",
                f"Resolution: {self.resolution_var.get()}",
                f"Prompts: {len(prompts)}",
                f"Output Directory: {self.output_dir_var.get()}",
                "",
                "Features:",
                f"  • Image-to-Video: {'✅' if self.image_to_video_var.get() else '❌'}",
                f"  • Veo 2 Double: {'✅' if self.veo2_double_var.get() else '❌'}",
                f"  • Veo 3 Audio: {'✅' if self.veo3_audio_var.get() else '❌'}",
                f"  • Auto Enhancement: {'✅' if self.auto_enhance_var.get() else '❌'}",
                "",
                "Sample Prompts:",
            ]

            # Add first few prompts
            for i, prompt in enumerate(prompts[:5]):
                setup_info.append(f"  {i+1}. {prompt[:80]}{'...' if len(prompt) > 80 else ''}")

            if len(prompts) > 5:
                setup_info.append(f"  ... and {len(prompts) - 5} more")

            preview_text = '\n'.join(setup_info)

            # Show preview
            messagebox.showinfo('Generation Setup Preview', preview_text)

        except Exception as e:
            self.log(f'🛑 Error generating preview: {e}')

    def _start_generation(self) -> None:
        """Start video generation process."""
        try:
            # Validate setup
            if not self.video_service:
                messagebox.showerror('Error', 'No API key configured')
                return

            prompts = self._get_prompts()
            if not prompts:
                messagebox.showerror('Error', 'No prompts provided')
                return

            # Create output directory
            output_dir = Path(self.output_dir_var.get())
            output_dir.mkdir(parents=True, exist_ok=True)

            # Initialize progress
            self.progress_bar.configure(maximum=len(prompts), value=0)
            self.progress_label.config(text='Initializing generation...')

            # Create stop event
            self._stop_event = threading.Event()

            # Start worker thread
            self._worker_thread = threading.Thread(
                target=self._generation_worker,
                args=(prompts, output_dir),
                daemon=True
            )
            self._worker_thread.start()

            # Update UI
            self._update_ui_state()
            self.log(f'🎬 Started video generation for {len(prompts)} prompts')

        except Exception as e:
            self.log(f'🛑 Error starting generation: {e}')
            messagebox.showerror('Error', f'Failed to start generation:\n{e}')

    def _generation_worker(self, prompts: List[str], output_dir: Path) -> None:
        """Worker thread for video generation.

        Args:
            prompts: List of prompts to process
            output_dir: Output directory for videos
        """
        try:
            success_count = 0
            failed_count = 0
            total_size = 0

            for i, prompt in enumerate(prompts):
                if self._stop_event.is_set():
                    break

                # Update progress
                self.root.after(0, lambda p=prompt: self.progress_label.config(
                    text=f'Generating: {p[:50]}...'
                ))
                self.root.after(0, lambda v=i: self.progress_bar.configure(value=v))

                try:
                    # Generate video
                    result = self._generate_single_video(prompt, output_dir, i + 1)

                    if result['success']:
                        success_count += 1
                        total_size += result.get('file_size', 0)
                        self.root.after(0, lambda: self.log(
                            f'✅ Video {i+1}/{len(prompts)} generated successfully'
                        ))
                    else:
                        failed_count += 1
                        self.root.after(0, lambda e=result.get('error', 'Unknown error'): self.log(
                            f'🛑 Video {i+1}/{len(prompts)} failed: {e}'
                        ))

                except Exception as e:
                    failed_count += 1
                    self.root.after(0, lambda err=str(e): self.log(
                        f'🛑 Video {i+1}/{len(prompts)} error: {err}'
                    ))

                # Update statistics
                self.root.after(0, lambda s=success_count, f=failed_count, size=total_size:
                    self.stats_label.config(
                        text=f'Videos: {s+f} | Success: {s} | Failed: {f} | Total Size: {size//1024//1024} MB'
                    ))

            # Completion
            if not self._stop_event.is_set():
                self.root.after(0, lambda: self.progress_label.config(
                    text=f'Generation complete! Success: {success_count}, Failed: {failed_count}'
                ))
                self.root.after(0, lambda: self.progress_bar.configure(value=len(prompts)))
                self.root.after(0, lambda: self.log(
                    f'🎉 Generation complete! {success_count} successful, {failed_count} failed'
                ))
            else:
                self.root.after(0, lambda: self.progress_label.config(text='Generation stopped by user'))
                self.root.after(0, lambda: self.log('⏹️ Generation stopped by user'))

        except Exception as e:
            self.root.after(0, lambda err=str(e): self.log(f'🛑 Generation worker error: {err}'))

        finally:
            # Reset UI state
            self._worker_thread = None
            self.root.after(0, self._update_ui_state)

    def _generate_single_video(self, prompt: str, output_dir: Path, index: int) -> Dict[str, Any]:
        """Generate a single video.

        Args:
            prompt: Video prompt
            output_dir: Output directory
            index: Video index

        Returns:
            Result dictionary with success status and details
        """
        try:
            # Video generation parameters
            params = {
                'prompt': prompt,
                'model': self.model_var.get(),
                'aspect_ratio': self.aspect_ratio_var.get(),
                'negative_prompt': self.neg_prompt_var.get() or None,
                'image_to_video': self.image_to_video_var.get(),
                'generate_audio': self.veo3_audio_var.get() if 'veo-3' in self.model_var.get() else False
            }

            # Generate video using service
            result = self.video_service.generate_video(**params)

            if result['success']:
                # Download and save video
                video_url = result['video_url']
                filename = f"video_{index:03d}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
                output_path = output_dir / filename

                # Download video
                download_result = self.video_service.download_video(video_url, str(output_path))

                if download_result['success']:
                    file_size = output_path.stat().st_size if output_path.exists() else 0

                    # Post-process if needed
                    if self.auto_enhance_var.get():
                        self.postprocess_service.enhance_video(str(output_path))

                    return {
                        'success': True,
                        'file_path': str(output_path),
                        'file_size': file_size
                    }
                else:
                    return {
                        'success': False,
                        'error': f"Download failed: {download_result.get('error', 'Unknown error')}"
                    }
            else:
                return {
                    'success': False,
                    'error': result.get('error', 'Generation failed')
                }

        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def _stop_generation(self) -> None:
        """Stop video generation."""
        try:
            if self._stop_event:
                self._stop_event.set()
                self.log('⏹️ Stopping video generation...')
                self._update_ui_state()

        except Exception as e:
            self.log(f'🛑 Error stopping generation: {e}')

    def _clear_results(self) -> None:
        """Clear generation results and reset progress."""
        try:
            if messagebox.askyesno('Clear Results', 'Clear all generation progress and statistics?'):
                self.progress_bar.configure(value=0)
                self.progress_label.config(text='Ready to generate videos')
                self.stats_label.config(text='Videos: 0 | Success: 0 | Failed: 0 | Total Size: 0 MB')
                self.log('🗑️ Generation results cleared')

        except Exception as e:
            self.log(f'🛑 Error clearing results: {e}')