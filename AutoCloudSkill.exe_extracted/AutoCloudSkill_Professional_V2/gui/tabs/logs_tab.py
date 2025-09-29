"""
Professional Logs Tab for AutoCloudSkill Application.

This module provides a comprehensive logging interface with real-time updates,
progress indicators, and advanced log management features.

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import datetime
from typing import TYPE_CHECKING, Optional
import threading
import time

if TYPE_CHECKING:
    from gui.main_window import MainWindow


class LogsTab:
    """Professional logs tab for real-time application monitoring."""

    def __init__(self, owner: 'MainWindow', notebook: ttk.Notebook):
        """Initialize the logs tab.

        Args:
            owner: Reference to the main window instance
            notebook: Parent notebook widget
        """
        self.owner = owner
        self._build_interface(notebook)

    def _build_interface(self, notebook: ttk.Notebook) -> None:
        """Build the complete logs tab interface."""
        # Create main tab frame
        self.tab_frame = ttk.Frame(notebook, padding=15)
        notebook.add(self.tab_frame, text='📋 Logs')

        # Create log display area
        self._create_log_display()

        # Create progress indicators
        self._create_progress_indicators()

        # Create log controls
        self._create_log_controls()

        # Initialize log display
        self._initialize_log_display()

    def _create_log_display(self) -> None:
        """Create the main log display area."""
        # Log display frame
        log_display_frame = ttk.LabelFrame(
            self.tab_frame,
            text='📝 Application Logs',
            padding=10,
            bootstyle=PRIMARY
        )
        log_display_frame.pack(fill=BOTH, expand=True, pady=(0, 10))

        # Create log text widget with professional styling
        self.owner.log_text = scrolledtext.ScrolledText(
            log_display_frame,
            wrap=tk.WORD,
            width=90,
            height=30,
            font=('Consolas', 10),
            bg='#1e1e1e',          # Dark background
            fg='#d4d4d4',          # Light text
            insertbackground='#ffffff',  # White cursor
            selectbackground='#264f78',  # Selection highlight
            selectforeground='#ffffff'   # Selection text
        )
        self.owner.log_text.pack(fill=BOTH, expand=True)

        # Configure text tags for different log levels
        self._configure_log_tags()

    def _configure_log_tags(self) -> None:
        """Configure text tags for different log levels and types."""
        try:
            # Success messages (green)
            self.owner.log_text.tag_configure(
                'success',
                foreground='#4EC9B0',  # Green
                font=('Consolas', 10, 'normal')
            )

            # Error messages (red)
            self.owner.log_text.tag_configure(
                'error',
                foreground='#F44747',  # Red
                font=('Consolas', 10, 'bold')
            )

            # Warning messages (yellow)
            self.owner.log_text.tag_configure(
                'warning',
                foreground='#FFCC02',  # Yellow
                font=('Consolas', 10, 'normal')
            )

            # Info messages (blue)
            self.owner.log_text.tag_configure(
                'info',
                foreground='#569CD6',  # Blue
                font=('Consolas', 10, 'normal')
            )

            # Debug messages (gray)
            self.owner.log_text.tag_configure(
                'debug',
                foreground='#808080',  # Gray
                font=('Consolas', 9, 'italic')
            )

            # Timestamp styling
            self.owner.log_text.tag_configure(
                'timestamp',
                foreground='#9CDCFE',  # Light blue
                font=('Consolas', 9, 'normal')
            )

        except Exception as e:
            # Fallback if tag configuration fails
            pass

    def _create_progress_indicators(self) -> None:
        """Create progress indicator section."""
        # Progress container
        self.owner.gmail_progress_container = ttk.LabelFrame(
            self.tab_frame,
            text='📊 Progress Indicators',
            padding=10,
            bootstyle=INFO
        )

        # Gmail progress frame
        gmail_progress_frame = ttk.Frame(self.owner.gmail_progress_container)
        gmail_progress_frame.pack(fill=X, pady=(0, 5))

        # Gmail progress label
        self.owner.gmail_progress_label = ttk.Label(
            gmail_progress_frame,
            text='Gmail polling status: Ready',
            font=('Segoe UI', 9),
            bootstyle=INFO
        )
        self.owner.gmail_progress_label.pack(side=LEFT)

        # Gmail progress bar
        self.owner.gmail_progress = ttk.Progressbar(
            gmail_progress_frame,
            orient='horizontal',
            mode='determinate',
            length=300,
            bootstyle='info-striped'
        )
        self.owner.gmail_progress.pack(side=RIGHT, padx=(10, 0))

        # Initialize progress state
        self.owner.gmail_progress_job = None
        self.owner.gmail_progress_running = False

        # Hide progress container initially
        # Will be shown when progress starts

    def _create_log_controls(self) -> None:
        """Create log control buttons."""
        # Log controls frame
        log_controls_frame = ttk.LabelFrame(
            self.tab_frame,
            text='🎛️ Log Controls',
            padding=10,
            bootstyle=SECONDARY
        )
        log_controls_frame.pack(fill=X, pady=(10, 0))

        # Button container
        button_container = ttk.Frame(log_controls_frame)
        button_container.pack(fill=X)

        # Clear logs button
        self.clear_logs_btn = ttk.Button(
            button_container,
            text='🗑️ Clear Logs',
            command=self._clear_logs,
            bootstyle=WARNING,
            width=15
        )
        self.clear_logs_btn.pack(side=LEFT, padx=(0, 10))

        # Save logs button
        self.save_logs_btn = ttk.Button(
            button_container,
            text='💾 Save Logs',
            command=self._save_logs,
            bootstyle=SUCCESS,
            width=15
        )
        self.save_logs_btn.pack(side=LEFT, padx=(0, 10))

        # Export logs button
        self.export_logs_btn = ttk.Button(
            button_container,
            text='📤 Export Logs',
            command=self._export_logs,
            bootstyle=INFO,
            width=15
        )
        self.export_logs_btn.pack(side=LEFT, padx=(0, 10))

        # Auto-scroll toggle
        self.auto_scroll_var = tk.BooleanVar(value=True)
        self.auto_scroll_check = ttk.Checkbutton(
            button_container,
            text='🔄 Auto-scroll',
            variable=self.auto_scroll_var,
            bootstyle='success-round-toggle'
        )
        self.auto_scroll_check.pack(side=LEFT, padx=(20, 10))

        # Search frame
        search_frame = ttk.Frame(button_container)
        search_frame.pack(side=RIGHT, fill=X, expand=True)

        # Search entry
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(
            search_frame,
            textvariable=self.search_var,
            placeholder_text='Search logs...',
            width=25
        )
        self.search_entry.pack(side=RIGHT, padx=(0, 5))

        # Search button
        self.search_btn = ttk.Button(
            search_frame,
            text='🔍',
            command=self._search_logs,
            bootstyle=INFO,
            width=3
        )
        self.search_btn.pack(side=RIGHT)

        # Bind search on Enter
        self.search_entry.bind('<Return>', lambda e: self._search_logs())

    def _initialize_log_display(self) -> None:
        """Initialize the log display with welcome message."""
        welcome_msg = (
            f"AutoCloudSkill Professional v2.0.0 - Logs\n"
            f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"{'=' * 60}\n\n"
        )

        self.owner.log_text.insert(tk.END, welcome_msg)
        self.owner.log_text.see(tk.END)

    def add_log_message(self, message: str) -> None:
        """Add a log message with appropriate styling.

        Args:
            message: The log message to add
        """
        try:
            # Add timestamp if not present
            if not message.startswith('['):
                timestamp = datetime.now().strftime('%H:%M:%S')
                formatted_message = f'[{timestamp}] {message}'
            else:
                formatted_message = message

            # Determine message type and apply appropriate tag
            tag = self._determine_message_tag(message)

            # Insert message with appropriate styling
            self.owner.log_text.insert(tk.END, formatted_message + '\n', tag)

            # Auto-scroll if enabled
            if self.auto_scroll_var.get():
                self.owner.log_text.see(tk.END)

            # Limit log size to prevent memory issues
            self._limit_log_size()

        except Exception as e:
            # Fallback: insert plain text
            try:
                self.owner.log_text.insert(tk.END, f'{message}\n')
                if self.auto_scroll_var.get():
                    self.owner.log_text.see(tk.END)
            except Exception:
                pass

    def _determine_message_tag(self, message: str) -> str:
        """Determine the appropriate tag for a log message.

        Args:
            message: The log message

        Returns:
            The tag name to apply
        """
        message_lower = message.lower()

        if any(indicator in message for indicator in ['✅', '🔓', 'success', 'completed', 'ready']):
            return 'success'
        elif any(indicator in message for indicator in ['🛑', '❌', 'error', 'failed', 'exception']):
            return 'error'
        elif any(indicator in message for indicator in ['⚠️', '🔒', 'warning', 'warn', 'caution']):
            return 'warning'
        elif any(indicator in message for indicator in ['ℹ️', '🔗', '📧', 'info', 'starting', 'loading']):
            return 'info'
        elif 'debug' in message_lower:
            return 'debug'
        else:
            return ''  # Default styling

    def _limit_log_size(self, max_lines: int = 1000) -> None:
        """Limit log size to prevent memory issues.

        Args:
            max_lines: Maximum number of lines to keep
        """
        try:
            total_lines = int(self.owner.log_text.index('end-1c').split('.')[0])

            if total_lines > max_lines:
                # Delete oldest lines
                lines_to_delete = total_lines - max_lines
                self.owner.log_text.delete('1.0', f'{lines_to_delete}.0')

        except Exception:
            pass

    def _clear_logs(self) -> None:
        """Clear all log content."""
        try:
            if messagebox.askyesno('Clear Logs', 'Are you sure you want to clear all logs?'):
                self.owner.log_text.delete('1.0', tk.END)
                self._initialize_log_display()
                self.owner.log_message('📋 Logs cleared')

        except Exception as e:
            messagebox.showerror('Error', f'Failed to clear logs: {e}')

    def _save_logs(self) -> None:
        """Save logs to a file."""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension='.txt',
                filetypes=[
                    ('Text files', '*.txt'),
                    ('Log files', '*.log'),
                    ('All files', '*.*')
                ],
                title='Save Logs',
                initialname=f'autocloudskill_logs_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
            )

            if filename:
                content = self.owner.log_text.get('1.0', tk.END)

                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)

                self.owner.log_message(f'💾 Logs saved to: {filename}')
                messagebox.showinfo('Success', f'Logs saved to:\n{filename}')

        except Exception as e:
            error_msg = f'Error saving logs: {str(e)}'
            self.owner.log_message(f'🛑 {error_msg}')
            messagebox.showerror('Error', error_msg)

    def _export_logs(self) -> None:
        """Export logs with metadata in JSON format."""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension='.json',
                filetypes=[
                    ('JSON files', '*.json'),
                    ('Text files', '*.txt'),
                    ('All files', '*.*')
                ],
                title='Export Logs',
                initialname=f'autocloudskill_export_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
            )

            if filename:
                # Prepare export data
                export_data = {
                    'application': 'AutoCloudSkill Professional',
                    'version': '2.0.0',
                    'export_timestamp': datetime.now().isoformat(),
                    'logs': self.owner.log_text.get('1.0', tk.END),
                    'metadata': {
                        'total_lines': int(self.owner.log_text.index('end-1c').split('.')[0]),
                        'auto_scroll_enabled': self.auto_scroll_var.get()
                    }
                }

                import json
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(export_data, f, indent=2, ensure_ascii=False)

                self.owner.log_message(f'📤 Logs exported to: {filename}')
                messagebox.showinfo('Success', f'Logs exported to:\n{filename}')

        except Exception as e:
            error_msg = f'Error exporting logs: {str(e)}'
            self.owner.log_message(f'🛑 {error_msg}')
            messagebox.showerror('Error', error_msg)

    def _search_logs(self) -> None:
        """Search for text in logs."""
        try:
            search_term = self.search_var.get().strip()
            if not search_term:
                return

            # Clear previous search highlights
            self.owner.log_text.tag_remove('search_highlight', '1.0', tk.END)

            # Configure search highlight tag
            self.owner.log_text.tag_configure(
                'search_highlight',
                background='#FFD700',  # Gold background
                foreground='#000000'   # Black text
            )

            # Search and highlight
            start_pos = '1.0'
            matches_found = 0

            while True:
                pos = self.owner.log_text.search(
                    search_term,
                    start_pos,
                    tk.END,
                    nocase=True
                )

                if not pos:
                    break

                # Calculate end position
                end_pos = f'{pos}+{len(search_term)}c'

                # Apply highlight
                self.owner.log_text.tag_add('search_highlight', pos, end_pos)

                # Move to next search
                start_pos = end_pos
                matches_found += 1

            if matches_found > 0:
                # Jump to first match
                first_match = self.owner.log_text.search(
                    search_term,
                    '1.0',
                    tk.END,
                    nocase=True
                )
                if first_match:
                    self.owner.log_text.see(first_match)

                self.owner.log_message(f'🔍 Found {matches_found} matches for "{search_term}"')
            else:
                self.owner.log_message(f'🔍 No matches found for "{search_term}"')

        except Exception as e:
            self.owner.log_message(f'🛑 Search error: {e}')

    def start_progress_indicator(self, total_seconds: int) -> None:
        """Start progress indicator for long-running operations.

        Args:
            total_seconds: Total duration in seconds
        """
        try:
            self.owner.gmail_progress_container.pack(fill=X, pady=(0, 10))

            self.gmail_poll_total = max(1, int(total_seconds))
            self.gmail_poll_start = time.time()
            self.owner.gmail_progress_running = True

            self.owner.gmail_progress.configure(
                maximum=self.gmail_poll_total,
                value=0
            )

            self.update_progress(0, self.gmail_poll_total, self.gmail_poll_total)

        except Exception as e:
            self.owner.logger.warning(f"Could not start progress indicator: {e}")

    def update_progress(self, elapsed: float, total: float, remaining: float) -> None:
        """Update progress indicator.

        Args:
            elapsed: Elapsed time in seconds
            total: Total time in seconds
            remaining: Remaining time in seconds
        """
        try:
            progress_percent = min(100, (elapsed / total) * 100) if total > 0 else 0

            self.owner.gmail_progress.configure(value=min(total, elapsed))

            self.owner.gmail_progress_label.config(
                text=f'Gmail polling: {progress_percent:.1f}% - {remaining:.0f}s remaining'
            )

        except Exception as e:
            self.owner.logger.debug(f"Progress update error: {e}")

    def stop_progress_indicator(self) -> None:
        """Stop progress indicator."""
        try:
            self.owner.gmail_progress_running = False
            self.owner.gmail_progress_container.pack_forget()

            self.owner.gmail_progress_label.config(
                text='Gmail polling status: Ready'
            )

        except Exception as e:
            self.owner.logger.debug(f"Progress stop error: {e}")

    def get_log_statistics(self) -> dict:
        """Get statistics about current logs.

        Returns:
            Dictionary with log statistics
        """
        try:
            content = self.owner.log_text.get('1.0', tk.END)
            lines = content.split('\n')

            stats = {
                'total_lines': len(lines),
                'total_characters': len(content),
                'success_messages': sum(1 for line in lines if any(indicator in line for indicator in ['✅', 'success', 'completed'])),
                'error_messages': sum(1 for line in lines if any(indicator in line for indicator in ['🛑', 'error', 'failed'])),
                'warning_messages': sum(1 for line in lines if any(indicator in line for indicator in ['⚠️', 'warning', 'warn'])),
                'info_messages': sum(1 for line in lines if any(indicator in line for indicator in ['ℹ️', 'info']))
            }

            return stats

        except Exception:
            return {
                'total_lines': 0,
                'total_characters': 0,
                'success_messages': 0,
                'error_messages': 0,
                'warning_messages': 0,
                'info_messages': 0
            }