#!/usr/bin/env python3
"""
PyC File Analyzer and Decompiler
Comprehensive analysis and decompilation of Python bytecode files
"""

import os
import sys
import csv
import ast
import hashlib
import zipfile
import tempfile
import subprocess
import logging
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional
import struct

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

def setup_logging():
    """Set up logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('pyc_analysis.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def get_pyc_magic(file_path: str) -> Tuple[str, str]:
    """Extract magic number and detect Python version from .pyc file"""
    try:
        with open(file_path, 'rb') as f:
            magic_bytes = f.read(4)
            hex_magic = magic_bytes.hex()
            detected_version = MAGIC_NUMBERS.get(magic_bytes, 'Unknown')
            return hex_magic, detected_version
    except Exception as e:
        return 'Error', f'Error: {str(e)}'

def calculate_sha256(file_path: str) -> str:
    """Calculate SHA256 hash of file"""
    try:
        sha256_hash = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except Exception as e:
        return f'Error: {str(e)}'

def find_all_pyc_files(base_dirs: List[str]) -> List[str]:
    """Recursively find all .pyc files in given directories"""
    pyc_files = []
    for base_dir in base_dirs:
        if os.path.exists(base_dir):
            for root, dirs, files in os.walk(base_dir):
                for file in files:
                    if file.endswith('.pyc'):
                        full_path = os.path.join(root, file)
                        pyc_files.append(full_path)
    return sorted(pyc_files)

def create_inventory(pyc_files: List[str], output_file: str) -> Dict:
    """Create detailed inventory of all .pyc files"""
    logger = logging.getLogger(__name__)
    logger.info(f"Creating inventory of {len(pyc_files)} .pyc files...")

    inventory_data = []
    stats = {
        'total_files': len(pyc_files),
        'total_size': 0,
        'versions': {},
        'errors': 0
    }

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            'relative_path', 'size_bytes', 'modified_time', 'sha256',
            'pyc_magic', 'detected_python_version'
        ])

        for i, file_path in enumerate(pyc_files):
            try:
                rel_path = os.path.relpath(file_path)
                stat = os.stat(file_path)
                size = stat.st_size
                mtime = datetime.fromtimestamp(stat.st_mtime).isoformat()
                sha256 = calculate_sha256(file_path)
                magic_hex, py_version = get_pyc_magic(file_path)

                row = [rel_path, size, mtime, sha256, magic_hex, py_version]
                writer.writerow(row)
                inventory_data.append(row)

                stats['total_size'] += size
                if py_version in stats['versions']:
                    stats['versions'][py_version] += 1
                else:
                    stats['versions'][py_version] = 1

                if i % 100 == 0:
                    logger.info(f"Processed {i}/{len(pyc_files)} files...")

            except Exception as e:
                logger.error(f"Error processing {file_path}: {str(e)}")
                stats['errors'] += 1

    logger.info(f"Inventory complete: {stats['total_files']} files, {stats['total_size']:,} bytes")
    return stats

def run_pylingual_batch(pyc_files: List[str], output_dir: str, batch_size: int = 200) -> Dict:
    """Run PyLingual decompilation in batches"""
    logger = logging.getLogger(__name__)

    os.makedirs(output_dir, exist_ok=True)
    results = {
        'total_files': len(pyc_files),
        'successful': 0,
        'failed': 0,
        'errors': []
    }

    # Process in batches to avoid command line length limits
    for i in range(0, len(pyc_files), batch_size):
        batch = pyc_files[i:i+batch_size]
        batch_num = i // batch_size + 1
        total_batches = (len(pyc_files) + batch_size - 1) // batch_size

        logger.info(f"Processing batch {batch_num}/{total_batches} ({len(batch)} files)...")

        try:
            # Change to pylingual directory and run decompilation
            cmd = [
                sys.executable, '-m', 'poetry', 'run', 'python', 'pylingual/main.py',
                '-o', output_dir, '--quiet'
            ] + batch

            result = subprocess.run(
                cmd,
                cwd='pylingual',
                capture_output=True,
                text=True,
                timeout=600  # 10 minute timeout per batch
            )

            if result.returncode == 0:
                results['successful'] += len(batch)
                logger.info(f"Batch {batch_num} completed successfully")
            else:
                results['failed'] += len(batch)
                error_msg = f"Batch {batch_num} failed: {result.stderr}"
                results['errors'].append(error_msg)
                logger.error(error_msg)

                # Save error log for this batch
                with open(f'batch_{batch_num}_error.log', 'w') as f:
                    f.write(f"Command: {' '.join(cmd)}\n")
                    f.write(f"Return code: {result.returncode}\n")
                    f.write(f"STDOUT:\n{result.stdout}\n")
                    f.write(f"STDERR:\n{result.stderr}\n")

        except subprocess.TimeoutExpired:
            error_msg = f"Batch {batch_num} timed out"
            results['failed'] += len(batch)
            results['errors'].append(error_msg)
            logger.error(error_msg)
        except Exception as e:
            error_msg = f"Batch {batch_num} error: {str(e)}"
            results['failed'] += len(batch)
            results['errors'].append(error_msg)
            logger.error(error_msg)

    return results

def validate_decompiled_files(decompiled_dir: str) -> Dict:
    """Validate syntax of all decompiled Python files"""
    logger = logging.getLogger(__name__)
    logger.info("Validating decompiled Python files...")

    results = {
        'total_files': 0,
        'valid_syntax': 0,
        'invalid_syntax': 0,
        'errors': []
    }

    for root, dirs, files in os.walk(decompiled_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                results['total_files'] += 1

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        source = f.read()

                    ast.parse(source)
                    results['valid_syntax'] += 1

                except SyntaxError as e:
                    results['invalid_syntax'] += 1
                    error_msg = f"Syntax error in {file_path}: {str(e)}"
                    results['errors'].append(error_msg)

                except Exception as e:
                    results['invalid_syntax'] += 1
                    error_msg = f"Error reading {file_path}: {str(e)}"
                    results['errors'].append(error_msg)

    logger.info(f"Validation complete: {results['valid_syntax']}/{results['total_files']} files valid")
    return results

def create_decompile_results_csv(pyc_files: List[str], decompiled_dir: str,
                                decompile_results: Dict, output_file: str):
    """Create detailed CSV of decompilation results"""
    logger = logging.getLogger(__name__)
    logger.info("Creating decompilation results CSV...")

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            'relative_pyc', 'relative_py', 'status', 'tool',
            'options_used', 'detected_version', 'error_message'
        ])

        for pyc_file in pyc_files:
            rel_pyc = os.path.relpath(pyc_file)

            # Determine expected .py output path
            expected_py = pyc_file.replace('.pyc', '.py')
            expected_py = expected_py.replace(os.path.dirname(os.path.dirname(pyc_file)), decompiled_dir)
            rel_py = os.path.relpath(expected_py) if os.path.exists(expected_py) else 'N/A'

            # Check if decompilation was successful
            status = 'ok' if os.path.exists(expected_py) else 'fail'

            # Get detected version
            _, detected_version = get_pyc_magic(pyc_file)

            # Determine error message
            error_message = ''
            if status == 'fail':
                # Check if there's a corresponding error in the results
                for error in decompile_results.get('errors', []):
                    if rel_pyc in error:
                        error_message = error
                        break
                if not error_message:
                    error_message = 'Decompilation failed - unknown reason'

            writer.writerow([
                rel_pyc, rel_py, status, 'PyLingual',
                'default', detected_version, error_message
            ])

def create_report(inventory_stats: Dict, decompile_results: Dict,
                 validation_results: Dict, output_file: str):
    """Create comprehensive markdown report"""
    logger = logging.getLogger(__name__)
    logger.info("Creating comprehensive report...")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# AutoCloudSkill PyC Decompilation Report\n\n")
        f.write(f"**Generated:** {datetime.now().isoformat()}\n\n")

        # Summary metrics
        f.write("## Summary Metrics\n\n")
        f.write(f"- **Total .pyc files found:** {inventory_stats['total_files']:,}\n")
        f.write(f"- **Total size:** {inventory_stats['total_size']:,} bytes\n")
        f.write(f"- **Files successfully decompiled:** {decompile_results['successful']:,}\n")
        f.write(f"- **Files failed to decompile:** {decompile_results['failed']:,}\n")
        f.write(f"- **Success rate:** {(decompile_results['successful']/inventory_stats['total_files']*100):.1f}%\n")
        f.write(f"- **Files with valid syntax:** {validation_results['valid_syntax']:,}\n")
        f.write(f"- **Syntax validation rate:** {(validation_results['valid_syntax']/validation_results['total_files']*100):.1f}%\n\n")

        # Python version distribution
        f.write("## Python Version Distribution\n\n")
        for version, count in sorted(inventory_stats['versions'].items()):
            percentage = (count / inventory_stats['total_files']) * 100
            f.write(f"- **Python {version}:** {count:,} files ({percentage:.1f}%)\n")
        f.write("\n")

        # Most common errors
        f.write("## Most Common Errors\n\n")
        if decompile_results['errors']:
            f.write("### Decompilation Errors\n")
            for i, error in enumerate(decompile_results['errors'][:10], 1):
                f.write(f"{i}. {error}\n")
            f.write("\n")

        if validation_results['errors']:
            f.write("### Validation Errors\n")
            for i, error in enumerate(validation_results['errors'][:10], 1):
                f.write(f"{i}. {error}\n")
            f.write("\n")

        # Recommendations
        f.write("## Recommendations\n\n")

        if decompile_results['failed'] > 0:
            f.write("### For Failed Decompilations:\n")
            f.write("1. **Retry with --trust-lnotab flag** for files that failed with segmentation errors\n")
            f.write("2. **Try -k 3 option** to consider more segmentation possibilities\n")
            f.write("3. **Manual version specification** using -v flag for files with unknown Python versions\n")
            f.write("4. **Alternative tools** like uncompyle6 or decompyle3 for older Python versions\n\n")

        if validation_results['invalid_syntax'] > 0:
            f.write("### For Syntax Validation Failures:\n")
            f.write("1. **Manual review** of files with syntax errors\n")
            f.write("2. **Post-processing** to fix common decompilation artifacts\n")
            f.write("3. **Partial recovery** by extracting valid functions/classes\n\n")

        f.write("### General Recommendations:\n")
        f.write("1. **Prioritize analysis** of successfully decompiled files\n")
        f.write("2. **Focus on main application code** rather than library files\n")
        f.write("3. **Cross-reference** with original executable structure\n")
        f.write("4. **Document findings** for future reference\n")

def create_zip_archive(files_and_dirs: List[str], output_file: str) -> str:
    """Create ZIP archive of all artifacts"""
    logger = logging.getLogger(__name__)
    logger.info(f"Creating ZIP archive: {output_file}")

    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for item in files_and_dirs:
            if os.path.isfile(item):
                zipf.write(item, os.path.basename(item))
            elif os.path.isdir(item):
                for root, dirs, files in os.walk(item):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path)
                        zipf.write(file_path, arcname)

    # Create checksum
    checksum = calculate_sha256(output_file)
    checksum_file = 'SHA256SUMS.txt'
    with open(checksum_file, 'w') as f:
        f.write(f"{checksum}  {os.path.basename(output_file)}\n")

    logger.info(f"Archive created: {output_file} ({checksum})")
    return checksum_file

def main():
    """Main execution function"""
    logger = setup_logging()
    logger.info("Starting PyC analysis and decompilation process...")

    # Define target directories
    target_dirs = [
        ".",  # Current directory (includes root .pyc files)
        "PYZ.pyz_extracted",  # Main extracted archive
        "_internal"  # Internal directory if exists
    ]

    # 1. Find all .pyc files
    logger.info("=== STEP 1: Finding all .pyc files ===")
    pyc_files = find_all_pyc_files(target_dirs)
    logger.info(f"Found {len(pyc_files)} .pyc files")

    if not pyc_files:
        logger.error("No .pyc files found! Exiting.")
        return

    # 2. Create inventory
    logger.info("=== STEP 2: Creating inventory ===")
    inventory_stats = create_inventory(pyc_files, 'pyc_inventory.csv')

    # 3. Run decompilation
    logger.info("=== STEP 3: Running decompilation ===")
    decompile_results = run_pylingual_batch(pyc_files, 'decompiled')

    # 4. Validate results
    logger.info("=== STEP 4: Validating decompiled files ===")
    validation_results = validate_decompiled_files('decompiled')

    # 5. Create results CSV
    logger.info("=== STEP 5: Creating results CSV ===")
    create_decompile_results_csv(pyc_files, 'decompiled', decompile_results, 'pyc_decompile_results.csv')

    # 6. Generate report
    logger.info("=== STEP 6: Generating report ===")
    create_report(inventory_stats, decompile_results, validation_results, 'report.md')

    # 7. Create archive
    logger.info("=== STEP 7: Creating archive ===")
    artifacts = [
        'decompiled',
        'pyc_inventory.csv',
        'pyc_decompile_results.csv',
        'report.md',
        'pyc_analysis.log'
    ]

    # Add error logs if they exist
    for file in os.listdir('.'):
        if file.startswith('batch_') and file.endswith('_error.log'):
            artifacts.append(file)

    checksum_file = create_zip_archive(artifacts, 'autocloudskill_decompiled_artifacts.zip')

    # Final summary
    logger.info("=== FINAL SUMMARY ===")
    logger.info(f"Total files processed: {inventory_stats['total_files']}")
    logger.info(f"Successfully decompiled: {decompile_results['successful']}")
    logger.info(f"Failed decompilation: {decompile_results['failed']}")
    logger.info(f"Valid syntax files: {validation_results['valid_syntax']}")
    logger.info(f"Archive created: autocloudskill_decompiled_artifacts.zip")
    logger.info(f"Checksum file: {checksum_file}")

    # Recommendations
    print("\n" + "="*60)
    print("RECOMMENDATIONS FOR FAILED FILES:")
    print("="*60)

    if decompile_results['failed'] > 0:
        print("1. Retry failed files with: --trust-lnotab")
        print("2. Try with more segmentation options: -k 3")
        print("3. Specify Python version manually: -v 3.11")
        print("4. Consider alternative tools for old versions")
        print("5. Check error logs for specific failure reasons")
    else:
        print("All files decompiled successfully!")

if __name__ == "__main__":
    main()