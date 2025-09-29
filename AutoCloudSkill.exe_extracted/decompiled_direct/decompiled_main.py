# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: 'main.py'
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

# irreducible cflow, using cdg fallback
"""\nMain entry point untuk aplikasi Auto Cloud Skill Registration\n"""
import sys
import os
import traceback
from pathlib import Path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
from gui.main_window import MainWindow
from config.settings import settings
from utils.logger import setup_logger, main_logger
def main():
    """Main function"""
    logger = setup_logger('Main')
    try:
        logger.info('Starting Auto Cloud Skill Registration application')
        logger.info('Skipping config validation - API key will be input via GUI')
        app = MainWindow()
        app.run()
        logger.info('Application terminated normally')
    except KeyboardInterrupt:
        logger.info('Application interrupted by user')
        return 0
    except Exception as e:
        logger.error(f'Unexpected error: {e}')
        logger.error(f'Traceback: {traceback.format_exc()}')
        print(f'\n❌ Unexpected error: {e}')
        print('Check logs for more details.')
        return 1
    else:
        return 0
if __name__ == '__main__':
    sys.exit(main())
        except ImportError as e:
                print(f'❌ Import error: {e}')
                print('\nPastikan semua dependencies sudah diinstall:')
                print('pip install -r requirements.txt')
                print('\nDan pastikan Playwright browser sudah diinstall:')
                print('playwright install chromium')
                sys.exit(1)
            except Exception as e:
                    print(f'❌ Fatal error: {e}')
                    print(f'Traceback: {traceback.format_exc()}')
                    sys.exit(1)