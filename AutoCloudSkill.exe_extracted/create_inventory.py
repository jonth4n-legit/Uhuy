#!/usr/bin/env python3
"""
Simple PyC File Inventory Creator
"""

import os
import csv
import hashlib
from datetime import datetime
from pathlib import Path

# Python version magic number mappings
MAGIC_NUMBERS = {
    b'\x33\x0d\x0d\x0a': '3.7',
    b'\x42\x0d\x0d\x0a': '3.8',
    b'\x55\x0d\x0d\x0a': '3.9',
    b'\x6f\x0d\x0d\x0a': '3.10',
    b'\xa7\x0d\x0d\x0a': '3.11',
    b'\xcb\x0d\x0d\x0a': '3.12',
    b'\x0c\x0e\x0d\x0a': '3.13',
}

def get_pyc_info(file_path):
    """Get magic number and Python version from .pyc file"""
    try:
        with open(file_path, 'rb') as f:
            magic_bytes = f.read(4)
            hex_magic = magic_bytes.hex()
            detected_version = MAGIC_NUMBERS.get(magic_bytes, 'Unknown')
            return hex_magic, detected_version
    except Exception as e:
        return 'Error', f'Error: {str(e)}'

def calculate_sha256(file_path):
    """Calculate SHA256 hash"""
    try:
        sha256_hash = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except Exception as e:
        return f'Error: {str(e)}'

def main():
    print("Creating inventory of .pyc files...")

    # Find all .pyc files
    pyc_files = []

    # Search in current directory
    for file in os.listdir('.'):
        if file.endswith('.pyc'):
            pyc_files.append(file)

    # Search in PYZ.pyz_extracted
    if os.path.exists('PYZ.pyz_extracted'):
        for root, dirs, files in os.walk('PYZ.pyz_extracted'):
            for file in files:
                if file.endswith('.pyc'):
                    full_path = os.path.join(root, file)
                    pyc_files.append(full_path)

    # Search in _internal
    if os.path.exists('_internal'):
        for root, dirs, files in os.walk('_internal'):
            for file in files:
                if file.endswith('.pyc'):
                    full_path = os.path.join(root, file)
                    pyc_files.append(full_path)

    print(f"Found {len(pyc_files)} .pyc files")

    # Create inventory CSV
    with open('pyc_inventory.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            'relative_path', 'size_bytes', 'modified_time', 'sha256',
            'pyc_magic', 'detected_python_version'
        ])

        stats = {'total_files': 0, 'total_size': 0, 'versions': {}}

        for i, file_path in enumerate(pyc_files):
            try:
                stat = os.stat(file_path)
                size = stat.st_size
                mtime = datetime.fromtimestamp(stat.st_mtime).isoformat()
                sha256 = calculate_sha256(file_path)
                magic_hex, py_version = get_pyc_info(file_path)

                row = [file_path, size, mtime, sha256, magic_hex, py_version]
                writer.writerow(row)

                stats['total_files'] += 1
                stats['total_size'] += size

                if py_version in stats['versions']:
                    stats['versions'][py_version] += 1
                else:
                    stats['versions'][py_version] = 1

                if i % 50 == 0:
                    print(f"Processed {i}/{len(pyc_files)} files...")

            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")

    print(f"\\nInventory complete!")
    print(f"Total files: {stats['total_files']}")
    print(f"Total size: {stats['total_size']:,} bytes")
    print("Python versions found:")
    for version, count in sorted(stats['versions'].items()):
        print(f"  {version}: {count} files")

    return pyc_files

if __name__ == "__main__":
    pyc_files = main()