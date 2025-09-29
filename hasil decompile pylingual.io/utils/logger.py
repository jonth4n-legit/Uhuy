# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: utils\logger.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
Utility untuk logging
"""
import logging
import os
from datetime import datetime
from config.settings import settings

def setup_logger(name: str = 'autocloudskill') -> logging.Logger:
    """
    Setup logger dengan konfigurasi yang sesuai
    
    Args:
        name: Nama logger
        
    Returns:
        Logger instance
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    
    level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    logger.setLevel(level)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    if settings.AUTO_SAVE_LOGS:
        try:
            base_logs = None
            try:
                base_logs = os.environ.get('LOCALAPPDATA')
            except Exception:
                base_logs = None
            
            if not base_logs:
                try:
                    base_logs = os.path.join(os.path.expanduser('~'), 'AppData', 'Local')
                except Exception:
                    base_logs = None
            
            if not base_logs:
                base_logs = os.getcwd()
            
            logs_dir = os.path.join(base_logs, 'AutoCloudSkill', 'logs')
            if not os.path.exists(logs_dir):
                os.makedirs(logs_dir, exist_ok=True)
            
            timestamp = datetime.now().strftime('%Y%m%d')
            log_name = getattr(settings, 'LOG_FILE', 'app.log')
            log_file = os.path.join(logs_dir, f"{str(log_name).replace('.log', '')}_{timestamp}.log")
            
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except Exception as e:
            try:
                logger.warning(f'File logger disabled: {e}')
            except Exception:
                pass
    
    return logger

def log_user_action(logger: logging.Logger, action: str, details: dict = None):
    """
    Log user action dengan format yang konsisten
    
    Args:
        logger: Logger instance
        action: Aksi yang dilakukan
        details: Detail tambahan
    """
    log_msg = f'USER_ACTION: {action}'
    if details:
        detail_str = ', '.join([f'{k}={v}' for k, v in details.items()])
        log_msg = f'{log_msg} | {detail_str}'
    logger.info(log_msg)

def log_automation_step(logger: logging.Logger, step: str, status: str, details: dict = None):
    """
    Log step otomatisasi dengan format yang konsisten
    
    Args:
        logger: Logger instance  
        step: Step yang sedang dilakukan
        status: Status (START, SUCCESS, ERROR, etc)
        details: Detail tambahan
    """
    log_msg = f'AUTOMATION: {step} - {status}'
    if details:
        detail_str = ', '.join([f'{k}={v}' for k, v in details.items()])
        log_msg = f'{log_msg} | {detail_str}'
    
    if status == 'ERROR':
        logger.error(log_msg)
    elif status == 'SUCCESS':
        logger.info(log_msg)
    else:
        logger.debug(log_msg)

main_logger = setup_logger()