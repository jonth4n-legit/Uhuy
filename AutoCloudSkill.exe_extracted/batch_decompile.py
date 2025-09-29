#!/usr/bin/env python3
"""
Batch PyC Decompiler using PyLingual
Processes all .pyc files in batches
"""

import csv
import os
import subprocess
import sys
from pathlib import Path

def read_pyc_inventory(csv_file):
    """Read the inventory CSV and return list of files"""
    files = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            files.append(row['relative_path'])
    return files

def decompile_batch(files, output_dir, batch_size=100):
    """Decompile files in batches"""
    total_files = len(files)
    successful = 0
    failed = 0
    errors = []

    print(f"Starting decompilation of {total_files} files...")
    print(f"Output directory: {output_dir}")

    os.makedirs(output_dir, exist_ok=True)

    # Convert relative paths to absolute paths
    base_dir = os.getcwd()

    for i in range(0, total_files, batch_size):
        batch = files[i:i+batch_size]
        batch_num = i // batch_size + 1
        total_batches = (total_files + batch_size - 1) // batch_size

        print(f"\\n[Batch {batch_num}/{total_batches}] Processing {len(batch)} files...")

        # Build command - use Python 3.12 explicitly
        cmd = [
            r"C:\Users\hp_5c\AppData\Local\Programs\Python\Python312\python.exe",
            '-m', 'poetry', 'run', 'python',
            'pylingual/main.py',
            '-o', os.path.join(base_dir, output_dir),
            '-v', '3.11',
            '--quiet'
        ]

        # Add files to command
        cmd.extend([os.path.join(base_dir, f) for f in batch])

        try:
            # Run decompilation
            result = subprocess.run(
                cmd,
                cwd='pylingual',
                capture_output=True,
                text=True,
                timeout=1800,  # 30 minute timeout per batch
                env={
                    **os.environ,
                    'PYTHONIOENCODING': 'utf-8',
                    'HF_HUB_DISABLE_SYMLINKS_WARNING': '1'
                }
            )

            if result.returncode == 0:
                print(f"  ✓ Batch {batch_num} completed successfully")
                successful += len(batch)
            else:
                print(f"  ✗ Batch {batch_num} failed")
                failed += len(batch)
                error_msg = f"Batch {batch_num}: {result.stderr[:200]}"
                errors.append(error_msg)

                # Save detailed error log
                with open(f'batch_{batch_num}_error.log', 'w', encoding='utf-8') as ef:
                    ef.write(f"Batch {batch_num} Error Log\\n")
                    ef.write("=" * 60 + "\\n")
                    ef.write(f"Files processed: {len(batch)}\\n")
                    ef.write(f"Return code: {result.returncode}\\n\\n")
                    ef.write("STDOUT:\\n")
                    ef.write(result.stdout + "\\n\\n")
                    ef.write("STDERR:\\n")
                    ef.write(result.stderr + "\\n")

        except subprocess.TimeoutExpired:
            print(f"  ⏱ Batch {batch_num} timed out")
            failed += len(batch)
            errors.append(f"Batch {batch_num}: Timeout after 30 minutes")

        except Exception as e:
            print(f"  ✗ Batch {batch_num} error: {str(e)}")
            failed += len(batch)
            errors.append(f"Batch {batch_num}: {str(e)}")

        # Progress update
        processed = min(i + batch_size, total_files)
        progress = (processed / total_files) * 100
        print(f"Progress: {processed}/{total_files} files ({progress:.1f}%)")
        print(f"Successful: {successful}, Failed: {failed}")

    print("\\n" + "="*60)
    print("DECOMPILATION COMPLETE")
    print("="*60)
    print(f"Total files: {total_files}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Success rate: {(successful/total_files*100):.1f}%")

    if errors:
        print(f"\\nErrors encountered: {len(errors)}")
        print("Check batch_*_error.log files for details")

    return {
        'total': total_files,
        'successful': successful,
        'failed': failed,
        'errors': errors
    }

def main():
    """Main function"""
    # Read inventory
    print("Reading pyc_inventory.csv...")
    files = read_pyc_inventory('pyc_inventory.csv')
    print(f"Found {len(files)} files to decompile")

    # Decompile
    results = decompile_batch(files, 'decompiled', batch_size=50)

    # Save results summary
    with open('decompile_summary.txt', 'w', encoding='utf-8') as f:
        f.write("PyC Decompilation Summary\\n")
        f.write("=" * 60 + "\\n\\n")
        f.write(f"Total files: {results['total']}\\n")
        f.write(f"Successful: {results['successful']}\\n")
        f.write(f"Failed: {results['failed']}\\n")
        f.write(f"Success rate: {(results['successful']/results['total']*100):.1f}%\\n\\n")

        if results['errors']:
            f.write("Errors:\\n")
            for error in results['errors']:
                f.write(f"- {error}\\n")

    print("\\nResults saved to decompile_summary.txt")

if __name__ == "__main__":
    main()