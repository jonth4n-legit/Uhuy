#!/usr/bin/env python3
"""
Create final ZIP archive with all artifacts
"""

import zipfile
import os
import hashlib
from datetime import datetime

def create_archive():
    """Create ZIP archive of all artifacts"""
    print("Creating final ZIP archive...")

    # Define files and directories to include
    artifacts = [
        'pyc_inventory.csv',
        'pyc_decompile_results.csv',
        'report.md',
        'SHA256SUMS.txt',
        'decompiled'
    ]

    # Add batch processing scripts for reference
    script_files = [
        'create_inventory.py',
        'batch_decompile.py',
        'test_batch.py',
        'generate_report.py'
    ]

    zip_filename = 'autocloudskill_decompiled_artifacts.zip'

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        # Add main artifacts
        for item in artifacts:
            if os.path.exists(item):
                if os.path.isfile(item):
                    zipf.write(item, item)
                    print(f"  Added file: {item}")
                elif os.path.isdir(item):
                    for root, dirs, files in os.walk(item):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path)
                            zipf.write(file_path, arcname)
                    print(f"  Added directory: {item} ({len(os.listdir(item))} files)")
            else:
                print(f"  Warning: {item} not found")

        # Add scripts in a scripts/ subdirectory
        for script in script_files:
            if os.path.exists(script):
                zipf.write(script, f"scripts/{script}")

        # Create a README for the archive
        readme_content = f"""# AutoCloudSkill Decompilation Results

Generated: {datetime.now().isoformat()}

## Contents

### Analysis Results
- `pyc_inventory.csv` - Complete inventory of all .pyc files found
- `pyc_decompile_results.csv` - Detailed decompilation results for each file
- `report.md` - Comprehensive analysis report with findings and recommendations
- `SHA256SUMS.txt` - Checksums for integrity verification

### Decompiled Code
- `decompiled/` - Directory containing all successfully decompiled Python files

### Tools Used
- `scripts/` - Python scripts used for analysis and decompilation
  - PyLingual (https://github.com/syssec-utd/pylingual) - Main decompilation tool
  - Custom batch processing and validation scripts

## Summary
- Total .pyc files analyzed: 1,490
- Successfully decompiled: 10 files (sample batch)
- All files are Python 3.11 bytecode

## Security Note
This analysis was performed for educational and defensive security purposes only.
The decompiled code should be used responsibly and in accordance with applicable laws.

## Next Steps
1. Review the main report.md for detailed findings
2. Examine successfully decompiled files in decompiled/ directory
3. Focus on application-specific code rather than library/framework files
4. Consider running full batch decompilation for complete analysis

For questions or issues, refer to the PyLingual documentation.
"""

        zipf.writestr("README.txt", readme_content)

    # Calculate archive checksum
    archive_size = os.path.getsize(zip_filename)

    sha256_hash = hashlib.sha256()
    with open(zip_filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    archive_checksum = sha256_hash.hexdigest()

    # Update checksums file
    with open('SHA256SUMS.txt', 'a', encoding='utf-8') as f:
        f.write(f"\\n# Archive\\n")
        f.write(f"{archive_checksum}  {zip_filename}\\n")

    print(f"\\nArchive created successfully!")
    print(f"Filename: {zip_filename}")
    print(f"Size: {archive_size:,} bytes ({archive_size/1024/1024:.1f} MB)")
    print(f"SHA256: {archive_checksum}")

    return zip_filename, archive_checksum

if __name__ == "__main__":
    create_archive()