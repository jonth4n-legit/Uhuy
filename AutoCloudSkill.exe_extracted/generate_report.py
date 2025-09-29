#!/usr/bin/env python3
"""
Validation and Report Generator
"""

import os
import ast
import csv
import hashlib
from datetime import datetime
from pathlib import Path

def validate_python_file(file_path):
    """Validate Python file syntax"""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            source = f.read()
        ast.parse(source)
        return True, None
    except SyntaxError as e:
        return False, f"Syntax error: {str(e)}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def validate_decompiled_files(decompiled_dir):
    """Validate all decompiled Python files"""
    print("Validating decompiled Python files...")

    results = {
        'total_files': 0,
        'valid_syntax': 0,
        'invalid_syntax': 0,
        'errors': []
    }

    valid_files = []
    invalid_files = []

    for root, dirs, files in os.walk(decompiled_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                results['total_files'] += 1

                is_valid, error = validate_python_file(file_path)

                if is_valid:
                    results['valid_syntax'] += 1
                    valid_files.append(file_path)
                else:
                    results['invalid_syntax'] += 1
                    invalid_files.append((file_path, error))
                    results['errors'].append(f"{file_path}: {error}")

    return results, valid_files, invalid_files

def create_decompile_results_csv():
    """Create decompilation results CSV"""
    print("Creating decompilation results CSV...")

    # Read inventory
    pyc_files = []
    with open('pyc_inventory.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pyc_files.append(row)

    # Check decompiled files
    decompiled_files = {}
    if os.path.exists('decompiled'):
        for root, dirs, files in os.walk('decompiled'):
            for file in files:
                if file.endswith('.py'):
                    full_path = os.path.join(root, file)
                    # Extract original filename from decompiled filename
                    if file.startswith('decompiled_'):
                        original_name = file[11:]  # Remove 'decompiled_' prefix
                        decompiled_files[original_name] = full_path

    # Create results CSV
    with open('pyc_decompile_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            'relative_pyc', 'relative_py', 'status', 'tool',
            'options_used', 'detected_version', 'error_message'
        ])

        for pyc_data in pyc_files:
            pyc_path = pyc_data['relative_path']
            pyc_filename = os.path.basename(pyc_path)

            # Check if decompiled
            expected_py_name = pyc_filename.replace('.pyc', '.py')

            if expected_py_name in decompiled_files:
                py_path = os.path.relpath(decompiled_files[expected_py_name])
                status = 'ok'
                error_message = ''

                # Validate syntax
                is_valid, error = validate_python_file(decompiled_files[expected_py_name])
                if not is_valid:
                    status = 'syntax_error'
                    error_message = error
            else:
                py_path = 'N/A'
                status = 'fail'
                error_message = 'Decompilation failed or not attempted'

            writer.writerow([
                pyc_path, py_path, status, 'PyLingual',
                'default (-v 3.11)', pyc_data['detected_python_version'], error_message
            ])

def generate_comprehensive_report():
    """Generate comprehensive markdown report"""
    print("Generating comprehensive report...")

    # Read inventory stats
    inventory_stats = {'total_files': 0, 'total_size': 0, 'versions': {}}
    with open('pyc_inventory.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            inventory_stats['total_files'] += 1
            inventory_stats['total_size'] += int(row['size_bytes'])
            version = row['detected_python_version']
            inventory_stats['versions'][version] = inventory_stats['versions'].get(version, 0) + 1

    # Validate decompiled files
    validation_results, valid_files, invalid_files = validate_decompiled_files('decompiled')

    # Count successful decompilations
    successful_decomp = validation_results['total_files']
    failed_decomp = inventory_stats['total_files'] - successful_decomp

    # Generate report
    with open('report.md', 'w', encoding='utf-8') as f:
        f.write("# AutoCloudSkill PyC Decompilation Report\\n\\n")
        f.write(f"**Generated:** {datetime.now().isoformat()}\\n\\n")

        # Summary metrics
        f.write("## Summary Metrics\\n\\n")
        f.write(f"- **Total .pyc files found:** {inventory_stats['total_files']:,}\\n")
        f.write(f"- **Total size:** {inventory_stats['total_size']:,} bytes ({inventory_stats['total_size']/1024/1024:.1f} MB)\\n")
        f.write(f"- **Files successfully decompiled:** {successful_decomp:,}\\n")
        f.write(f"- **Files failed to decompile:** {failed_decomp:,}\\n")

        if inventory_stats['total_files'] > 0:
            success_rate = (successful_decomp / inventory_stats['total_files']) * 100
            f.write(f"- **Success rate:** {success_rate:.1f}%\\n")

        if validation_results['total_files'] > 0:
            syntax_rate = (validation_results['valid_syntax'] / validation_results['total_files']) * 100
            f.write(f"- **Files with valid syntax:** {validation_results['valid_syntax']:,}/{validation_results['total_files']:,} ({syntax_rate:.1f}%)\\n")

        f.write("\\n")

        # Python version distribution
        f.write("## Python Version Distribution\\n\\n")
        for version, count in sorted(inventory_stats['versions'].items()):
            percentage = (count / inventory_stats['total_files']) * 100
            f.write(f"- **Python {version}:** {count:,} files ({percentage:.1f}%)\\n")
        f.write("\\n")

        # File analysis
        f.write("## File Analysis\\n\\n")
        f.write("### Successfully Decompiled Files\\n\\n")
        if valid_files:
            f.write("Files with valid Python syntax:\\n\\n")
            for file_path in valid_files[:20]:  # Show first 20
                size = os.path.getsize(file_path)
                rel_path = os.path.relpath(file_path)
                f.write(f"- `{rel_path}` ({size:,} bytes)\\n")

            if len(valid_files) > 20:
                f.write(f"\\n... and {len(valid_files) - 20} more files\\n")
            f.write("\\n")

        # Syntax errors
        if invalid_files:
            f.write("### Files with Syntax Errors\\n\\n")
            for file_path, error in invalid_files[:10]:  # Show first 10
                rel_path = os.path.relpath(file_path)
                f.write(f"- `{rel_path}`: {error}\\n")

            if len(invalid_files) > 10:
                f.write(f"\\n... and {len(invalid_files) - 10} more files with syntax errors\\n")
            f.write("\\n")

        # Key findings
        f.write("## Key Findings\\n\\n")

        if successful_decomp > 0:
            f.write("### 🎯 Successfully Decompiled Code\\n\\n")

            # Check for main application files
            main_files = []
            for file_path in valid_files:
                filename = os.path.basename(file_path)
                if any(keyword in filename.lower() for keyword in ['main', 'app', 'gui', 'window']):
                    main_files.append(file_path)

            if main_files:
                f.write("**Main application files identified:**\\n\\n")
                for file_path in main_files:
                    f.write(f"- `{os.path.relpath(file_path)}`\\n")
                f.write("\\n")

            f.write("**Analysis recommendations:**\\n\\n")
            f.write("1. **Focus on application-specific files** rather than library/framework code\\n")
            f.write("2. **Start with main.py and GUI modules** for understanding core functionality\\n")
            f.write("3. **Look for configuration and settings files** to understand application behavior\\n")
            f.write("4. **Examine utils and services modules** for custom business logic\\n\\n")

        # Recommendations
        f.write("## Recommendations\\n\\n")

        if failed_decomp > 0:
            f.write("### For Failed Decompilations\\n\\n")
            f.write("1. **Retry with different options:**\\n")
            f.write("   - `--trust-lnotab` for segmentation issues\\n")
            f.write("   - `-k 3` for more segmentation possibilities\\n")
            f.write("   - Manual version specification with `-v`\\n\\n")
            f.write("2. **Try alternative tools:**\\n")
            f.write("   - uncompyle6 for older Python versions\\n")
            f.write("   - decompyle3 for Python 3.7+\\n")
            f.write("   - pycdc for cross-version compatibility\\n\\n")

        if validation_results['invalid_syntax'] > 0:
            f.write("### For Syntax Validation Failures\\n\\n")
            f.write("1. **Manual review** of files with syntax errors\\n")
            f.write("2. **Partial code extraction** from problematic files\\n")
            f.write("3. **Focus on successfully decompiled files** for analysis\\n\\n")

        f.write("### Analysis Workflow\\n\\n")
        f.write("1. **Start with `main.py`** to understand application entry point\\n")
        f.write("2. **Examine GUI modules** to understand user interface\\n")
        f.write("3. **Review configuration files** for application settings\\n")
        f.write("4. **Analyze business logic** in utils and services modules\\n")
        f.write("5. **Document findings** and create functional overview\\n\\n")

        # Security considerations
        f.write("## Security Considerations\\n\\n")
        f.write("⚠️ **Important**: This analysis is for educational and defensive security purposes only.\\n\\n")
        f.write("- Review decompiled code for understanding application functionality\\n")
        f.write("- Look for potential security vulnerabilities or misconfigurations\\n")
        f.write("- Do not use findings for malicious purposes\\n")
        f.write("- Respect intellectual property and licensing terms\\n")

def calculate_file_checksums():
    """Calculate checksums for all generated files"""
    print("Calculating checksums...")

    files_to_check = [
        'pyc_inventory.csv',
        'pyc_decompile_results.csv',
        'report.md'
    ]

    # Add decompiled files
    if os.path.exists('decompiled'):
        for root, dirs, files in os.walk('decompiled'):
            for file in files:
                if file.endswith('.py'):
                    files_to_check.append(os.path.join(root, file))

    with open('SHA256SUMS.txt', 'w', encoding='utf-8') as f:
        f.write("# SHA256 Checksums\\n")
        f.write(f"# Generated: {datetime.now().isoformat()}\\n\\n")

        for file_path in files_to_check:
            if os.path.exists(file_path):
                sha256_hash = hashlib.sha256()
                with open(file_path, 'rb') as file:
                    for chunk in iter(lambda: file.read(4096), b""):
                        sha256_hash.update(chunk)
                checksum = sha256_hash.hexdigest()
                f.write(f"{checksum}  {file_path}\\n")

def main():
    """Main function"""
    print("Starting validation and report generation...")

    # Create decompilation results CSV
    create_decompile_results_csv()

    # Generate comprehensive report
    generate_comprehensive_report()

    # Calculate checksums
    calculate_file_checksums()

    print("\\n" + "="*60)
    print("ANALYSIS COMPLETE")
    print("="*60)
    print("Generated files:")
    print("- pyc_inventory.csv")
    print("- pyc_decompile_results.csv")
    print("- report.md")
    print("- SHA256SUMS.txt")
    print("- decompiled/ directory")

    # Show quick stats
    if os.path.exists('pyc_decompile_results.csv'):
        with open('pyc_decompile_results.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            stats = {'ok': 0, 'fail': 0, 'syntax_error': 0}
            for row in reader:
                status = row['status']
                if status in stats:
                    stats[status] += 1

        print(f"\\nDecompilation Results:")
        print(f"- Successful: {stats['ok']}")
        print(f"- Failed: {stats['fail']}")
        print(f"- Syntax errors: {stats['syntax_error']}")

if __name__ == "__main__":
    main()