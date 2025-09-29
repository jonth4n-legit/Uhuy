"""
Utility helpers for structured logging across the application.
"""
import logging
import os
from datetime import datetime
from typing import Optional, Dict

from config.settings import settings


def _resolve_logs_dir() -> str:
    """Resolve a writable logs directory across platforms.

    Priority order:
    1) %LOCALAPPDATA%/AutoCloudSkill/logs (Windows)
    2) ~/AppData/Local/AutoCloudSkill/logs (Windows without env)
    3) CWD/AutoCloudSkill/logs (fallback)
    """
    base = os.environ.get('LOCALAPPDATA')
    if not base:
        try:
            base = os.path.join(os.path.expanduser('~'), 'AppData', 'Local')
        except Exception:
            base = os.getcwd()
    logs_dir = os.path.join(base, 'AutoCloudSkill', 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    return logs_dir


def setup_logger(name: str = 'autocloudskill') -> logging.Logger:
    """Create or return a configured logger.

    - Level is taken from settings.LOG_LEVEL
    - Logs go to console and (optionally) to a daily-rotated file
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    level_name = str(getattr(settings, 'LOG_LEVEL', 'INFO')).upper()
    level = getattr(logging, level_name, logging.INFO)
    logger.setLevel(level)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(formatter)
    logger.addHandler(console)

    if getattr(settings, 'AUTO_SAVE_LOGS', True):
        try:
            logs_dir = _resolve_logs_dir()
            timestamp = datetime.now().strftime('%Y%m%d')
            log_name = str(getattr(settings, 'LOG_FILE', 'app.log')).replace('.log', '')
            file_path = os.path.join(logs_dir, f'{log_name}_{timestamp}.log')
            file_handler = logging.FileHandler(file_path, encoding='utf-8')
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except Exception as e:
            logger.warning(f'File logger disabled: {e}')

    return logger


def log_user_action(logger: logging.Logger, action: str, details: Optional[Dict] = None) -> None:
    """Log a user action in a consistent structured format."""
    msg = f'USER_ACTION: {action}'
    if details:
        detail_str = ', '.join(f'{k}={v}' for k, v in details.items())
        msg = f'{msg} | {detail_str}'
    logger.info(msg)


def log_automation_step(logger: logging.Logger, step: str, status: str, details: Optional[Dict] = None) -> None:
    """Log an automation step in a consistent structured format."""
    msg = f'AUTOMATION: {step} - {status}'
    if details:
        detail_str = ', '.join(f'{k}={v}' for k, v in details.items())
        msg = f'{msg} | {detail_str}'
    if status == 'ERROR':
        logger.error(msg)
    elif status in {'SUCCESS', 'DONE'}:
        logger.info(msg)
    else:
        logger.debug(msg)


# A convenient default logger used by modules that import main_logger
main_logger = setup_logger('Main')