#!/usr/bin/env python3
"""
Setup script untuk Auto Cloud Skill Registration
Install dependencies dan setup environment
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run command dengan error handling"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Error: {e.stderr}")
        return False

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    return True

def install_dependencies():
    """Install Python dependencies"""
    if not run_command("pip install --upgrade pip", "Upgrading pip"):
        return False
    
    if not run_command("pip install -r requirements.txt", "Installing Python dependencies"):
        return False
    
    return True

def install_playwright():
    """Install Playwright browsers"""
    if not run_command("playwright install chromium", "Installing Playwright Chromium browser"):
        return False
    
    return True

def create_directories():
    """Create necessary directories"""
    directories = [
        'logs',
        'temp', 
        'output',
        'assets',
        'config',
        'services',
        'gui',
        'gui/tabs',
        'automation',
        'utils'
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"📁 Created directory: {directory}")
    
    return True

def create_config_files():
    """Create default configuration files"""
    
    # Create .env file template
    env_content = """# Auto Cloud Skill Configuration
# Copy this file to .env and fill in your API keys

# Firefox Relay API Key (required)
FIREFOX_RELAY_API_KEY=your_firefox_relay_api_key_here

# Google Cloud Skills Boost Registration URL
CLOUDSKILL_REGISTER_URL=https://www.cloudskillsboost.google/users/sign_up

# Debug mode (true/false)
DEBUG=false

# Log level (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL=INFO

# Auto save logs (true/false)
AUTO_SAVE_LOGS=true

# Playwright settings
PLAYWRIGHT_HEADLESS=false
PLAYWRIGHT_TIMEOUT=30000

# Default user generation settings
DEFAULT_GENDER=female
DEFAULT_NATIONALITIES=gb,us,es
DEFAULT_PASSWORD_LENGTH=12

# Browser user agent
BROWSER_USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
"""
    
    with open('.env.template', 'w') as f:
        f.write(env_content)
    
    print("📄 Created .env.template file")
    
    # Create README
    readme_content = """# Auto Cloud Skill Registration

Automated Google Cloud Skills Boost registration tool with video generation capabilities.

## Features

- 🤖 Automated account registration
- 📧 Email confirmation handling via Firefox Relay
- 🎥 Video generation using Google GenAI
- 🔧 Lab automation with API key extraction
- 📊 Comprehensive logging and monitoring

## Setup

1. Install dependencies:
   ```bash
   python setup.py
   ```

2. Configure API keys:
   ```bash
   cp .env.template .env
   # Edit .env with your API keys
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Requirements

- Python 3.8+
- Firefox Relay API key
- Google GenAI API key (for video generation)
- Gmail API credentials (optional, for email confirmation)

## API Keys

### Firefox Relay API Key
1. Go to https://relay.firefox.com/
2. Sign in with your Firefox account
3. Go to Settings > API Keys
4. Generate a new API key
5. Add to .env file

### Google GenAI API Key
1. Go to https://ai.google.dev/
2. Sign in with your Google account
3. Create a new project
4. Enable GenAI API
5. Generate API key
6. Add to .env file

### Gmail API Credentials (Optional)
1. Go to Google Cloud Console
2. Create a new project
3. Enable Gmail API
4. Create OAuth 2.0 credentials
5. Download credentials.json
6. Place in project root

## Usage

1. Start the application
2. Enter your Firefox Relay API key
3. Configure Gmail credentials (optional)
4. Set lab URL for auto-start
5. Click "Start Registration"
6. Monitor progress in logs tab
7. Use Video Generator tab for AI video creation

## Troubleshooting

- Check logs in the logs tab
- Verify API keys are correct
- Ensure all dependencies are installed
- Check internet connection
- Verify Playwright browsers are installed

## Support

For issues and support, check the logs and error messages in the application.
"""
    
    with open('README.md', 'w') as f:
        f.write(readme_content)
    
    print("📄 Created README.md file")
    
    return True

def main():
    """Main setup function"""
    print("🚀 Auto Cloud Skill Registration Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Create directories
    if not create_directories():
        return 1
    
    # Install dependencies
    if not install_dependencies():
        return 1
    
    # Install Playwright
    if not install_playwright():
        return 1
    
    # Create config files
    if not create_config_files():
        return 1
    
    print("\n✅ Setup completed successfully!")
    print("\nNext steps:")
    print("1. Copy .env.template to .env")
    print("2. Edit .env with your API keys")
    print("3. Run: python main.py")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())