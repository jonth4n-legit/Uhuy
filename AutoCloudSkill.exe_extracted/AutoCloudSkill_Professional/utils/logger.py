"""
Professional logging utilities for Auto Cloud Skill Registration application.

This module provides centralized logging configuration with proper formatting,
file rotation, and integration with the application's debugging capabilities.
"""

import logging
import logging.handlers
import sys
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime
from config.constants import LOG_LEVEL, LOG_FILE, AUTO_SAVE_LOGS

class ColoredFormatter(logging.Formatter):
    """Custom formatter that adds colors to console output."""

    # Color codes for different log levels
    COLORS = {
        'DEBUG': '\033[36m',      # Cyan
        'INFO': '\033[32m',       # Green
        'WARNING': '\033[33m',    # Yellow
        'ERROR': '\033[31m',      # Red
        'CRITICAL': '\033[35m',   # Magenta
        'RESET': '\033[0m'        # Reset
    }

    def format(self, record):
        """Format log record with colors for console output."""
        # Get the original formatted message
        formatted = super().format(record)

        # Add color if this is a console handler
        if hasattr(record, 'levelname') and record.levelname in self.COLORS:
            color = self.COLORS[record.levelname]
            reset = self.COLORS['RESET']
            return f"{color}{formatted}{reset}"

        return formatted

def setup_logger(name: str, level: Optional[str] = None) -> logging.Logger:
    """
    Setup a logger with console and file handlers.

    Args:
        name: Logger name (usually module name)
        level: Logging level override

    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)

    # Avoid duplicate handlers
    if logger.handlers:
        return logger

    # Set log level
    log_level = getattr(logging, (level or LOG_LEVEL).upper(), logging.INFO)
    logger.setLevel(log_level)

    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    console_formatter = ColoredFormatter(
        '%(levelname)s - %(name)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # File handler (if enabled)
    if AUTO_SAVE_LOGS:
        try:
            # Create logs directory if it doesn't exist
            log_path = Path(LOG_FILE)
            log_path.parent.mkdir(parents=True, exist_ok=True)

            # Use rotating file handler to prevent huge log files
            file_handler = logging.handlers.RotatingFileHandler(
                log_path,
                maxBytes=10 * 1024 * 1024,  # 10MB
                backupCount=5,
                encoding='utf-8'
            )
            file_handler.setLevel(log_level)
            file_handler.setFormatter(detailed_formatter)
            logger.addHandler(file_handler)

        except Exception as e:
            logger.warning(f"Could not setup file logging: {e}")

    return logger

def log_user_action(action: str, details: Optional[Dict[str, Any]] = None) -> None:
    """
    Log user actions for audit trail.

    Args:
        action: Description of the action
        details: Additional details dictionary
    """
    logger = logging.getLogger('UserActions')

    detail_str = ""
    if details:
        detail_parts = [f"{k}={v}" for k, v in details.items()]
        detail_str = f" ({', '.join(detail_parts)})"

    logger.info(f"USER ACTION: {action}{detail_str}")

def log_automation_step(step: str, status: str, details: Optional[str] = None) -> None:
    """
    Log automation steps for debugging.

    Args:
        step: Description of the automation step
        status: Status (SUCCESS, FAILED, STARTED, etc.)
        details: Additional details
    """
    logger = logging.getLogger('Automation')

    detail_str = f" - {details}" if details else ""
    logger.info(f"AUTOMATION [{status}]: {step}{detail_str}")

def log_service_call(service: str, method: str, status: str,
                    response_time: Optional[float] = None) -> None:
    """
    Log external service calls.

    Args:
        service: Service name (e.g., 'Firefox Relay', 'Gmail')
        method: Method called
        status: Status of the call
        response_time: Response time in seconds
    """
    logger = logging.getLogger('Services')

    time_str = f" ({response_time:.2f}s)" if response_time else ""
    logger.info(f"SERVICE [{status}]: {service}.{method}{time_str}")

# Global logger for main application
main_logger = setup_logger('Main')