"""
Root entrypoint to run the reconstructed Auto Cloud Skill app.
Falls back to a CLI mode when tkinter GUI is unavailable.
"""
import os
import sys
from pathlib import Path


def _cli_fallback() -> int:
    # Minimal non-GUI flow: generate user, test Firefox Relay, create a mask
    try:
        from services.randomuser_service import RandomUserService
        from services.firefox_relay_service import FirefoxRelayService
        from utils.logger import setup_logger
        from config.settings import settings
    except Exception as e:
        print(f"❌ Import failure in CLI fallback: {e}")
        return 1

    logger = setup_logger('CLI')
    try:
        rus = RandomUserService()
        user = rus.get_random_user(gender=settings.DEFAULT_GENDER, nationalities=settings.DEFAULT_NATIONALITIES) or {}
        api_key = os.environ.get('FIREFOX_RELAY_API_KEY') or getattr(settings, 'FIREFOX_RELAY_API_KEY', '')
        if not api_key or api_key == 'your_api_key_here':
            print('⚠️ Set env FIREFOX_RELAY_API_KEY to enable mask creation (skipping).')
            print(f"👤 Generated user: {user.get('first_name','')} {user.get('last_name','')}")
            return 0
        svc = FirefoxRelayService(api_key=api_key)
        test = svc.test_connection()
        if not test.get('success'):
            print(f"🛑 Firefox Relay test failed: {test.get('error','unknown error')}")
            return 2
        mask = svc.create_relay_mask('Auto registration - CLI')
        if not mask:
            print('🛑 Failed to create relay email mask')
            return 3
        print(f"✅ Created relay email: {mask.get('full_address')}")
        return 0
    except Exception as e:
        logger.error(f'CLI error: {e}')
        print(f'❌ CLI error: {e}')
        return 1


def main() -> int:
    # Ensure package path points to the reconstructed sources
    project_root = Path(__file__).parent / 'hasil decompile pylingual.io'
    sys.path.insert(0, str(project_root))

    try:
        # Prefer clean main window rebuild to avoid decompiler artifacts
        from gui.main_window_clean import MainWindow
        app = MainWindow()
        app.run()
        return 0
    except Exception as e:
        print(f"ℹ️ GUI not available or failed to start: {e}")
        print('➡️ Switching to CLI fallback...')
        return _cli_fallback()


if __name__ == '__main__':
    sys.exit(main())

