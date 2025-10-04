# Auto Cloud Skill Registration Tool

**Version**: 1.2.0  
**Author**: SinyoRMX  
**Status**: Partially Restored from Decompilation

## ⚠️ Important Notice

This codebase has been decompiled from `AutoCloudSkill.exe` using PyLingual.io. Approximately **60% of the code is fully functional**, while **40% requires manual fixing** due to decompilation artifacts.

### ✅ Fully Functional Modules:
- Core configuration system
- All service integrations (Gmail, Firefox Relay, Captcha, etc.)
- Utility functions (logging, validation)
- Main entry point

### ⚠️ Requires Fixing:
- Automation system (`automation/` folder)
- GUI system (`gui/` folder)

## Features

- **Automated Registration**: Automatic Google Cloud Skills Boost account registration
- **Email Management**: Firefox Relay email masking integration
- **Gmail Integration**: Automated email confirmation monitoring
- **Lab Automation**: Auto-start labs and extract API keys
- **Captcha Handling**: Automatic checkbox click and audio solving
- **Video Generation**: AI-powered video generation with GenAI
- **License System**: Trial and paid plan support

## Installation

### Prerequisites
- Python 3.11+
- Google Chrome/Chromium browser

### Steps

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Playwright Browser**:
   ```bash
   playwright install chromium
   ```

3. **Configuration**:
   - Edit `config/constants.py` to set your API keys
   - Or configure via GUI when running the application

## Usage

### Running the Application
```bash
python main.py
```

**Note**: Currently, the GUI and automation modules need fixing before the application can run fully.

### Testing Individual Modules

```bash
# Test Random User Service
python -c "from services.randomuser_service import RandomUserService; print(RandomUserService().get_random_user())"

# Test Logger
python -c "from utils.logger import setup_logger; logger = setup_logger('test'); logger.info('Test message')"

# Test Gmail Service (requires credentials.json)
python -c "from services.gmail_service import GmailService; svc = GmailService(); print('Gmail service initialized')"

# Test Captcha Service
python -c "from services.captcha_service import CaptchaSolverService; print('Captcha service initialized')"
```

## Project Structure

```
.
├── main.py                 # Entry point ✅
├── requirements.txt        # Dependencies ✅
├── config/                 # Configuration ✅
│   ├── constants.py
│   ├── settings.py
│   └── licensing.py
├── utils/                  # Utilities ✅
│   ├── logger.py
│   └── validators.py
├── services/               # External services ✅
│   ├── randomuser_service.py
│   ├── firefox_relay_service.py
│   ├── gmail_service.py
│   ├── captcha_service.py
│   ├── genai_video_service.py
│   └── video_postprocess_service.py
├── automation/             # Automation logic ⚠️
│   ├── cloudskill_automation.py
│   ├── lab_actions_simple.py
│   └── confirm_actions.py
└── gui/                    # User interface ⚠️
    ├── main_window.py
    └── tabs/
        ├── registration_tab.py
        ├── settings_tab.py
        ├── logs_tab.py
        ├── video_generator_tab.py
        └── about_tab.py
```

## Configuration

### API Keys Required

1. **Firefox Relay API Key** (for email masking)
   - Get from: https://relay.firefox.com/
   - Set in GUI or `config/constants.py`

2. **Gmail OAuth Credentials** (for email monitoring)
   - Create OAuth 2.0 credentials in Google Cloud Console
   - Download `credentials.json`
   - Place in project root or specify path in GUI

3. **Google GenAI API Key** (for video generation)
   - Obtained automatically via lab automation
   - Or manually input in GUI

### License System

The application uses a license validation system:
- **Trial**: Automatically provisioned on first run
- **Paid**: Requires license key

License is validated against: `https://sinyormx.vercel.app/api/licenses/`

## Development

### Fixing Remaining Issues

See `/workspace/DECOMPILATION_ANALYSIS_REPORT.md` and `/workspace/FIXING_SUMMARY.md` for detailed analysis and recommendations.

**Priority order:**
1. Fix `automation/cloudskill_automation.py` (core automation)
2. Fix `automation/lab_actions_simple.py` (lab operations)
3. Fix `gui/main_window.py` (main interface)
4. Fix remaining GUI tabs

### Testing
```bash
# Run syntax check on all files
python -m py_compile main.py
python -m py_compile config/*.py
python -m py_compile utils/*.py
python -m py_compile services/*.py

# Run specific module tests
python -m services.randomuser_service
python -m services.captcha_service
```

## Dependencies

### Core Libraries
- **playwright**: Browser automation
- **google-api-python-client**: Gmail API
- **ttkbootstrap**: Modern GUI framework
- **SpeechRecognition**: Audio captcha solving
- **moviepy**: Video processing
- **requests**: HTTP client

### Full list
See `requirements.txt` for complete dependency list.

## Known Issues

1. **Automation Module**: Control flow errors from decompilation (requires manual fixing)
2. **GUI Module**: Syntax and control flow errors (requires manual fixing)
3. **Incomplete Functionality**: Some features may not work until automation/GUI modules are fixed

## License

This is a decompiled application. Original license terms apply.

## Support

For issues with the decompilation process, refer to:
- `/workspace/DECOMPILATION_ANALYSIS_REPORT.md`
- `/workspace/FIXING_SUMMARY.md`

## Changelog

### Current Version (Decompiled)
- ✅ Successfully restored all service modules
- ✅ Successfully restored configuration system
- ✅ Successfully restored utility modules
- ✅ Created complete requirements.txt
- ⚠️ Automation modules require fixing
- ⚠️ GUI modules require fixing

---
**Decompilation Date**: 2025-09-29  
**Decompiler**: PyLingual.io  
**Python Version**: 3.11a7e