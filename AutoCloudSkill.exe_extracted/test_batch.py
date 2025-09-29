#!/usr/bin/env python3
"""
Test batch with first 10 files
"""

import csv
import subprocess
import sys
import os

# Read first 10 files from inventory
files = []
with open('pyc_inventory.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        if i >= 10:  # Only first 10 files
            break
        files.append(row['relative_path'])

print(f"Testing with {len(files)} files:")
for f in files:
    print(f"  {f}")

# Run PyLingual
base_dir = os.getcwd()
cmd = [
    sys.executable, '-m', 'poetry', 'run', 'python',
    'pylingual/main.py',
    '-o', os.path.join(base_dir, 'decompiled'),
    '-v', '3.11',
    '--quiet'
] + [os.path.join(base_dir, f) for f in files]

print(f"\\nRunning PyLingual...")
print(f"Command: {' '.join(cmd[:8])} ... [+{len(files)} files]")

try:
    result = subprocess.run(
        cmd,
        cwd='pylingual',
        capture_output=True,
        text=True,
        timeout=600,  # 10 minute timeout
        env={**os.environ, 'PYTHONIOENCODING': 'utf-8', 'HF_HUB_DISABLE_SYMLINKS_WARNING': '1'}
    )

    print(f"\\nReturn code: {result.returncode}")
    if result.stdout:
        print(f"STDOUT: {result.stdout}")
    if result.stderr:
        print(f"STDERR: {result.stderr}")

    # Check output
    print("\\nChecking decompiled files:")
    for root, dirs, files_found in os.walk('decompiled'):
        for file in files_found:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                size = os.path.getsize(file_path)
                print(f"  {file_path} ({size} bytes)")

except Exception as e:
    print(f"Error: {e}")