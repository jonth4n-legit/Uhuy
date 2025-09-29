#!/usr/bin/env python3
"""
Setup script untuk AutoCloudSkill
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setup(
    name="autocloudskill",
    version="1.2.0",
    author="SinyoRMX",
    description="Auto Cloud Skill Registration Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=[
        "playwright>=1.47.0",
        "google-genai>=0.6.0",
        "google-api-python-client>=2.183.0",
        "google-auth>=2.23.0",
        "google-auth-oauthlib>=1.0.0",
        "google-auth-httplib2>=0.2.0",
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.0",
        "ttkbootstrap>=1.10.0",
        "speechrecognition>=3.10.0",
        "imageio-ffmpeg>=0.4.9",
        "moviepy>=1.0.3",
        "numpy>=1.24.0",
        "Pillow>=10.0.0",
        "pydantic>=2.0.0",
        "machineid>=0.3.0",
    ],
    entry_points={
        "console_scripts": [
            "autocloudskill=main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
