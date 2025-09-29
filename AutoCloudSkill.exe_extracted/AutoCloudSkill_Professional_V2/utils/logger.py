"""
Professional logging utilities for AutoCloudSkill application.

This module provides comprehensive logging capabilities with:
- Multiple output formats (console, file, structured)
- Automatic log rotation and cleanup
- Performance monitoring
- User action tracking
- Automation step logging
- Security-aware logging (credential filtering)

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import logging
import logging.handlers
import os
import sys
import traceback
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, Optional, List
import json
import time
from functools import wraps

# Color codes for console output
class LogColors:
    """ANSI color codes for console logging."""
    RESET = '\033[0m'
    BOLD = '\033[1m'

    # Colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Background colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'

class ColoredFormatter(logging.Formatter):
    """Custom formatter with color support for console output."""

    COLORS = {
        'DEBUG': LogColors.CYAN,
        'INFO': LogColors.GREEN,
        'WARNING': LogColors.YELLOW,
        'ERROR': LogColors.RED,
        'CRITICAL': LogColors.BG_RED + LogColors.WHITE + LogColors.BOLD
    }

    def format(self, record):
        # Create a copy to avoid modifying the original record
        record_copy = logging.makeLogRecord(record.__dict__)

        # Add color if terminal supports it
        if hasattr(sys.stderr, 'isatty') and sys.stderr.isatty():
            color = self.COLORS.get(record.levelname, '')
            if color:
                record_copy.levelname = f"{color}{record.levelname}{LogColors.RESET}"
                record_copy.name = f"{LogColors.BOLD}{record.name}{LogColors.RESET}"

        return super().format(record_copy)

class SecurityFilter(logging.Filter):
    """Filter to remove sensitive information from logs."""

    SENSITIVE_PATTERNS = [
        r'password["\']?\s*[:=]\s*["\']?([^"\'\\s]+)',
        r'api[_-]?key["\']?\s*[:=]\s*["\']?([^"\'\\s]+)',
        r'token["\']?\s*[:=]\s*["\']?([^"\'\\s]+)',
        r'secret["\']?\s*[:=]\s*["\']?([^"\'\\s]+)',
        r'auth["\']?\s*[:=]\s*["\']?([^"\'\\s]+)',
        r'bearer\s+([a-zA-Z0-9\-_\.]+)',
    ]

    def filter(self, record):
        """Filter sensitive information from log records."""
        import re

        # Check message
        message = str(record.getMessage())
        for pattern in self.SENSITIVE_PATTERNS:
            message = re.sub(pattern, r'***REDACTED***', message, flags=re.IGNORECASE)

        # Update the record
        record.msg = message
        record.args = ()

        return True

class PerformanceLogger:
    """Context manager for performance monitoring."""

    def __init__(self, logger: logging.Logger, operation: str, threshold: float = 1.0):
        self.logger = logger
        self.operation = operation
        self.threshold = threshold
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        self.logger.debug(f"🚀 Starting: {self.operation}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time

        if exc_type:
            self.logger.error(f"❌ Failed: {self.operation} ({duration:.2f}s) - {exc_val}")
        elif duration > self.threshold:
            self.logger.warning(f"⚠️ Slow: {self.operation} ({duration:.2f}s)")
        else:
            self.logger.info(f"✅ Completed: {self.operation} ({duration:.2f}s)")

def get_logs_directory() -> Path:
    """
    Get the appropriate logs directory based on platform.

    Returns:
        Path to logs directory
    """
    try:
        if sys.platform.startswith('win'):
            # Windows: Use LOCALAPPDATA
            base_dir = os.environ.get('LOCALAPPDATA')
            if not base_dir:
                base_dir = Path.home() / 'AppData' / 'Local'
        else:
            # Unix-like: Use XDG_DATA_HOME or ~/.local/share
            base_dir = os.environ.get('XDG_DATA_HOME')
            if not base_dir:
                base_dir = Path.home() / '.local' / 'share'

        logs_dir = Path(base_dir) / 'AutoCloudSkill' / 'logs'
        logs_dir.mkdir(parents=True, exist_ok=True)
        return logs_dir

    except Exception:
        # Fallback to current directory
        fallback = Path.cwd() / 'logs'
        fallback.mkdir(exist_ok=True)
        return fallback

def cleanup_old_logs(logs_dir: Path, keep_days: int = 7) -> None:
    """
    Remove log files older than specified days.

    Args:
        logs_dir: Directory containing log files
        keep_days: Number of days to keep logs
    """
    try:
        cutoff_date = datetime.now() - timedelta(days=keep_days)

        for log_file in logs_dir.glob('*.log'):
            try:
                file_mtime = datetime.fromtimestamp(log_file.stat().st_mtime)
                if file_mtime < cutoff_date:
                    log_file.unlink()
            except Exception:
                continue  # Skip problematic files

    except Exception:
        pass  # Silent cleanup failure

def setup_application_logging(
    name: str = 'autocloudskill',
    level: str = 'INFO',
    enable_file_logging: bool = True,
    enable_console_colors: bool = True,
    max_file_size: int = 10 * 1024 * 1024,  # 10MB
    backup_count: int = 5
) -> logging.Logger:
    """
    Setup comprehensive application logging.

    Args:
        name: Logger name
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        enable_file_logging: Enable file logging
        enable_console_colors: Enable colored console output
        max_file_size: Maximum file size before rotation
        backup_count: Number of backup files to keep

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)

    # Avoid duplicate handlers
    if logger.handlers:
        return logger

    # Set logging level
    log_level = getattr(logging, level.upper(), logging.INFO)
    logger.setLevel(log_level)

    # Console handler with colors
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)

    if enable_console_colors:
        console_formatter = ColoredFormatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )
    else:
        console_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    console_handler.setFormatter(console_formatter)
    console_handler.addFilter(SecurityFilter())
    logger.addHandler(console_handler)

    # File handler with rotation
    if enable_file_logging:
        try:
            logs_dir = get_logs_directory()

            # Clean up old logs
            cleanup_old_logs(logs_dir)

            # Create rotating file handler
            log_file = logs_dir / f'{name}.log'
            file_handler = logging.handlers.RotatingFileHandler(
                log_file,
                maxBytes=max_file_size,
                backupCount=backup_count,
                encoding='utf-8'
            )

            file_handler.setLevel(log_level)
            file_formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            file_handler.setFormatter(file_formatter)
            file_handler.addFilter(SecurityFilter())
            logger.addHandler(file_handler)

            logger.info(f"📁 File logging enabled: {log_file}")

        except Exception as e:
            logger.warning(f"⚠️ File logging disabled: {e}")

    return logger

def log_user_action(
    logger: logging.Logger,
    action: str,
    details: Optional[Dict[str, Any]] = None,
    user_id: Optional[str] = None
) -> None:
    """
    Log user action with consistent formatting and optional details.

    Args:
        logger: Logger instance
        action: Action performed by user
        details: Additional details about the action
        user_id: User identifier (optional)
    """
    log_data = {
        'type': 'USER_ACTION',
        'action': action,
        'timestamp': datetime.now().isoformat(),
    }

    if user_id:
        log_data['user_id'] = user_id

    if details:
        log_data['details'] = details

    # Format for human readability
    msg_parts = [f"👤 USER: {action}"]

    if user_id:
        msg_parts.append(f"(ID: {user_id})")

    if details:
        detail_str = ', '.join([f'{k}={v}' for k, v in details.items()])
        msg_parts.append(f"| {detail_str}")

    logger.info(' '.join(msg_parts))

def log_automation_step(
    logger: logging.Logger,
    step: str,
    status: str,
    details: Optional[Dict[str, Any]] = None,
    duration: Optional[float] = None
) -> None:
    """
    Log automation step with status and optional performance data.

    Args:
        logger: Logger instance
        step: Step being performed
        status: Status (START, SUCCESS, ERROR, WARNING, INFO)
        details: Additional step details
        duration: Step duration in seconds
    """
    # Status icons
    status_icons = {
        'START': '🚀',
        'SUCCESS': '✅',
        'ERROR': '❌',
        'WARNING': '⚠️',
        'INFO': 'ℹ️',
        'PROGRESS': '🔄'
    }

    icon = status_icons.get(status.upper(), '📍')

    log_data = {
        'type': 'AUTOMATION',
        'step': step,
        'status': status.upper(),
        'timestamp': datetime.now().isoformat(),
    }

    msg_parts = [f"{icon} AUTO: {step} - {status.upper()}"]

    if duration is not None:
        log_data['duration'] = duration
        msg_parts.append(f"({duration:.2f}s)")

    if details:
        log_data['details'] = details
        detail_str = ', '.join([f'{k}={v}' for k, v in details.items()])
        msg_parts.append(f"| {detail_str}")

    log_message = ' '.join(msg_parts)

    # Log at appropriate level based on status
    if status.upper() == 'ERROR':
        logger.error(log_message)
    elif status.upper() == 'WARNING':
        logger.warning(log_message)
    elif status.upper() in ['SUCCESS', 'START']:
        logger.info(log_message)
    else:
        logger.debug(log_message)

def log_performance_metrics(
    logger: logging.Logger,
    operation: str,
    metrics: Dict[str, Any]
) -> None:
    """
    Log performance metrics for analysis.

    Args:
        logger: Logger instance
        operation: Operation name
        metrics: Performance metrics dictionary
    """
    metrics_str = ', '.join([f'{k}={v}' for k, v in metrics.items()])
    logger.info(f"📊 PERF: {operation} | {metrics_str}")

def performance_monitor(operation: str, threshold: float = 1.0):
    """
    Decorator for automatic performance monitoring.

    Args:
        operation: Operation name for logging
        threshold: Warning threshold in seconds

    Returns:
        Decorated function
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__module__)

            start_time = time.time()
            try:
                logger.debug(f"🚀 Starting: {operation}")
                result = func(*args, **kwargs)
                duration = time.time() - start_time

                if duration > threshold:
                    logger.warning(f"⚠️ Slow: {operation} ({duration:.2f}s)")
                else:
                    logger.debug(f"✅ Completed: {operation} ({duration:.2f}s)")

                return result

            except Exception as e:
                duration = time.time() - start_time
                logger.error(f"❌ Failed: {operation} ({duration:.2f}s) - {e}")
                raise

        return wrapper
    return decorator

def setup_logger(name: str = 'autocloudskill') -> logging.Logger:
    """
    Backward compatibility function for existing code.

    Args:
        name: Logger name

    Returns:
        Logger instance
    """
    return setup_application_logging(name)

# Create main application logger
main_logger = setup_application_logging('autocloudskill')

# Export commonly used items
__all__ = [
    'setup_application_logging',
    'setup_logger',
    'log_user_action',
    'log_automation_step',
    'log_performance_metrics',
    'performance_monitor',
    'PerformanceLogger',
    'main_logger'
]