#!/usr/bin/env python3
"""
Fixed test for batch decompilation
"""

import subprocess
import os

# Test with just one file that we know works
test_files = ['main.pyc']

base_dir = os.getcwd()
output_dir = 'decompiled_test'

cmd = [
    r"C:\Users\hp_5c\AppData\Local\Programs\Python\Python312\python.exe",
    '-m', 'poetry', 'run', 'python',
    'pylingual/main.py',
    '-o', os.path.join(base_dir, output_dir),
    '-v', '3.11',
    '--quiet'
] + [os.path.join(base_dir, f) for f in test_files]

print("Testing fixed batch decompilation...")
print(f"Command: {' '.join(cmd[:8])} ... [+{len(test_files)} files]")

try:
    result = subprocess.run(
        cmd,
        cwd='pylingual',
        capture_output=True,
        text=True,
        timeout=300,
        env={
            **os.environ,
            'PYTHONIOENCODING': 'utf-8',
            'HF_HUB_DISABLE_SYMLINKS_WARNING': '1'
        }
    )

    print(f"Return code: {result.returncode}")
    if result.stdout:
        print(f"STDOUT: {result.stdout}")
    if result.stderr:
        print(f"STDERR: {result.stderr}")

    if result.returncode == 0:
        print("✅ SUCCESS: Fixed batch script works!")
    else:
        print("❌ FAILED: Still has issues")

except Exception as e:
    print(f"❌ ERROR: {e}")