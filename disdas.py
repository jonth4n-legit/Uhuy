import os
import subprocess
import sys

# Base folder asli
base_dir = r"C:\Users\hp_5c\Downloads\Uhuy-main\Uhuy-main\AutoCloudSkill.exe_extracted\PYZ.pyz_extracted"
# Lokasi dis.py (pastikan disimpan di salah satu folder, contoh services)
dis_script = os.path.join(base_dir, "services", "dis.py")
# Lokasi pycdas.exe
pycdas_exe = r"C:\Users\hp_5c\Downloads\Uhuy-main\Uhuy-main\pycdas.exe"
# Output base
output_dir = os.path.join(os.path.dirname(base_dir), "output")

# Folder target
target_folders = ["services", "gui", "automation", "config", "utils"]

for folder in target_folders:
    folder_path = os.path.join(base_dir, folder)
    if not os.path.exists(folder_path):
        print(f"[!] Folder tidak ditemukan: {folder_path}")
        continue

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pyc"):
                pyc_path = os.path.join(root, file)

                # Buat path output mirror
                rel_path = os.path.relpath(root, base_dir)
                out_folder = os.path.join(output_dir, rel_path)
                os.makedirs(out_folder, exist_ok=True)

                # File output
                dis_out = os.path.join(out_folder, file.replace(".pyc", ".dis.txt"))
                pycdas_out = os.path.join(out_folder, file.replace(".pyc", ".pycdas.txt"))

                print(f"[+] Processing {pyc_path}")
                
                # Jalankan dis.py
                with open(dis_out, "w", encoding="utf-8") as out_f:
                    subprocess.run(
                        [sys.executable, dis_script, pyc_path],
                        stdout=out_f,
                        stderr=subprocess.STDOUT
                    )

                # Jalankan pycdas.exe
                with open(pycdas_out, "w", encoding="utf-8") as out_f:
                    subprocess.run(
                        [pycdas_exe, pyc_path],
                        stdout=out_f,
                        stderr=subprocess.STDOUT
                    )

print("[✓] Selesai! Semua hasil ada di folder 'output'")
