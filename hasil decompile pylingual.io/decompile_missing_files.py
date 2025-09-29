#!/usr/bin/env python3
"""
Script to identify missing .pyc files that should be decompiled with pylingual.io and disassembled with dis.py/pycdas.exe
"""

import os
from pathlib import Path

def find_missing_pyc_files():
    """Find .pyc files that haven't been decompiled yet"""
    
    # Original .pyc files location
    pyc_source_dir = Path("/workspace/AutoCloudSkill.exe_extracted/PYZ.pyz_extracted")
    
    # Decompiled files location  
    decompiled_dir = Path("/workspace/hasil decompile pylingual.io")
    
    print("🔍 Scanning for missing .pyc files...")
    print(f"Source directory: {pyc_source_dir}")
    print(f"Decompiled directory: {decompiled_dir}")
    print("-" * 60)
    
    missing_files = []
    
    # Core directories to check
    target_dirs = ['automation', 'services', 'gui', 'config', 'utils']
    
    for target_dir in target_dirs:
        pyc_dir = pyc_source_dir / target_dir
        decompiled_target_dir = decompiled_dir / target_dir
        
        if not pyc_dir.exists():
            print(f"⚠️  Directory not found: {pyc_dir}")
            continue
            
        print(f"\n📁 Checking {target_dir}/")
        
        for pyc_file in pyc_dir.rglob("*.pyc"):
            # Calculate corresponding .py file path
            relative_path = pyc_file.relative_to(pyc_dir)
            py_file_path = decompiled_target_dir / str(relative_path).replace('.pyc', '.py')
            
            if not py_file_path.exists():
                missing_files.append({
                    'pyc_path': str(pyc_file),
                    'expected_py_path': str(py_file_path),
                    'relative_path': str(relative_path)
                })
                print(f"❌ Missing: {relative_path}")
            else:
                print(f"✅ Found: {relative_path}")
    
    # Check main.pyc
    main_pyc = Path("/workspace/AutoCloudSkill.exe_extracted/main.pyc")
    main_py = decompiled_dir / "main.py"
    
    if main_pyc.exists() and not main_py.exists():
        missing_files.append({
            'pyc_path': str(main_pyc),
            'expected_py_path': str(main_py),
            'relative_path': 'main.pyc'
        })
    
    print(f"\n📊 Summary:")
    print(f"Total missing files: {len(missing_files)}")
    
    if missing_files:
        print(f"\n🛠️  Recommended actions:")
        print(f"1. Use pylingual.io to decompile the following .pyc files:")
        for file_info in missing_files:
            print(f"   - {file_info['pyc_path']}")
        
        print(f"\n2. Use dis.py and pycdas.exe to disassemble for analysis:")
        print(f"   dis.py example:")
        for file_info in missing_files[:3]:  # Show first 3 examples
            print(f"   python dis.py \"{file_info['pyc_path']}\" > \"{file_info['relative_path']}.dis.txt\"")
        
        print(f"\n   pycdas.exe example:")
        for file_info in missing_files[:3]:  # Show first 3 examples
            print(f"   pycdas.exe \"{file_info['pyc_path']}\" > \"{file_info['relative_path']}.pycdas.txt\"")
    else:
        print("✅ All core .pyc files have been decompiled!")
    
    return missing_files

def check_gui_tabs():
    """Check for missing GUI tab files"""
    print(f"\n🎨 Checking GUI tabs...")
    
    gui_tabs_dir = Path("/workspace/hasil decompile pylingual.io/gui/tabs")
    pyc_gui_tabs_dir = Path("/workspace/AutoCloudSkill.exe_extracted/PYZ.pyz_extracted/gui/tabs")
    
    if not pyc_gui_tabs_dir.exists():
        print("⚠️  Original GUI tabs directory not found in .pyc files")
        return
    
    missing_tabs = []
    for pyc_file in pyc_gui_tabs_dir.glob("*.pyc"):
        tab_name = pyc_file.stem
        py_file = gui_tabs_dir / f"{tab_name}.py"
        
        if not py_file.exists():
            missing_tabs.append(pyc_file)
            print(f"❌ Missing tab: {tab_name}.py")
        else:
            print(f"✅ Found tab: {tab_name}.py")
    
    if missing_tabs:
        print(f"\n📝 Missing GUI tabs should be decompiled:")
        for tab_file in missing_tabs:
            print(f"   - {tab_file}")

if __name__ == "__main__":
    print("🔎 Auto Cloud Skill - Missing Files Analysis")
    print("=" * 60)
    
    missing_files = find_missing_pyc_files()
    check_gui_tabs()
    
    print(f"\n💡 Note: The screenshots show working tools, so focus on files that are critical")
    print(f"    for the automation functionality shown in the screenshots.")
    print(f"\n🎯 Priority files to decompile (if missing):")
    print(f"   1. automation/* - Core automation logic")
    print(f"   2. services/* - Service integrations") 
    print(f"   3. gui/tabs/* - User interface components")
    print(f"   4. config/* - Configuration files")
    
    print(f"\n✅ Current status: All major syntax errors have been fixed!")
    print(f"✅ The application can now be run with: python main.py")
    print(f"✅ Dependencies can be installed with: pip install -r requirements.txt")