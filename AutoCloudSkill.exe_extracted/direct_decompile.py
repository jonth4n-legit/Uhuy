#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Direct Queue Decompiler (VERBOSE) — 25 threads × 15 files per batch (dinamis, no wave)
- Sumber file dari pyc_inventory.csv (kolom: relative_path) → base_dir + relative_path
- Work-queue: setiap thread ambil batch (15 file). Selesai -> ambil batch berikutnya.
- Auto-retry per-file (Attempt1 default → Attempt2 --trust-lnotab + -k → Attempt3 -v fallback).
- VERBOSE: output PyLingual tampil real-time di terminal + disalin ke log (tee).

Contoh:
  python direct_queue_25x15_verbose.py ^
    --base-dir . ^
    --out decompiled ^
    --threads 25 ^
    --batch-size 15 ^
    --timeout 900 ^
    --default-version 3.11 ^
    --top-k 5
"""

import argparse
import csv
import os
import threading
import subprocess
import sys
import time
from pathlib import Path
from typing import List, Dict, Tuple
from queue import Queue

PRINT_LOCK = threading.Lock()
def log(msg: str):
    with PRINT_LOCK:
        print(msg, flush=True)

# -------------------- Util dasar --------------------
def read_inventory(csv_path: Path) -> List[str]:
    rels = []
    with csv_path.open("r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            rel = row.get("relative_path") or row.get("relative") or row.get("file")
            if rel:
                rels.append(rel)
    return rels

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def out_py_path(out_dir: Path, rel_pyc: str) -> Path:
    rel = Path(rel_pyc)
    return (out_dir / rel.with_suffix(".py")).resolve()

def file_has_output(out_dir: Path, rels: List[str]) -> Dict[str, bool]:
    status = {}
    for r in rels:
        p = out_py_path(out_dir, r)
        status[r] = (p.exists() and p.stat().st_size > 0)
    return status

# -------------------- PyLingual runner --------------------
def detect_pylingual_python() -> str:
    """
    Prefer venv Poetry PyLingual (Windows), fallback Python 3.12 global.
    Ubah path default sesuai mesin Anda bila perlu.
    """
    # 1) venv Poetry spesifik (contoh dari sesi Anda — sesuaikan jika berbeda)
    default_poetry_venv = r"C:\Users\hp_5c\AppData\Local\pypoetry\Cache\virtualenvs\pylingual-Ujk83j76-py3.12"
    pyexe = os.path.join(default_poetry_venv, "Scripts", "python.exe")
    if os.path.exists(pyexe):
        return pyexe

    # 2) cari venv pylingual lain di cache pypoetry
    cache_dir = r"C:\Users\hp_5c\AppData\Local\pypoetry\Cache\virtualenvs"
    if os.path.exists(cache_dir):
        for name in os.listdir(cache_dir):
            if "pylingual" in name.lower():
                cand = os.path.join(cache_dir, name, "Scripts", "python.exe")
                if os.path.exists(cand):
                    return cand

    # 3) fallback: Python 3.12 global
    for p in [
        r"C:\Users\hp_5c\AppData\Local\Programs\Python\Python312\python.exe",
        "python3.12", "py -3.12"
    ]:
        try:
            pr = subprocess.run([p, "-c", "import sys;print(sys.executable)"],
                                capture_output=True, text=True, timeout=8)
            if pr.returncode == 0 and pr.stdout.strip():
                return pr.stdout.strip()
        except Exception:
            pass

    raise RuntimeError("Interpreter PyLingual (Poetry venv / py3.12) tidak ditemukan.")

def build_cmd(py_exe: str, base_dir: Path, out_dir: Path, rels: List[str],
              trust_lnotab=False, top_k:int=0, version:str|None=None, use_module=False) -> List[str]:
    """
    Bangun command PyLingual untuk sekelompok file (tanpa --quiet).
    - Default jalankan main.py dari repo lokal 'pylingual'
    - Jika use_module=True: pakai `-m pylingual` (bila paket terinstal di venv)
    """
    cmd = [py_exe]
    if use_module:
        cmd += ["-m", "pylingual"]
    else:
        main_py = base_dir / "pylingual" / "pylingual" / "main.py"
        cmd.append(str(main_py))

    cmd += ["-o", str(out_dir)]
    if trust_lnotab:
        cmd.append("--trust-lnotab")
    if isinstance(top_k, int) and top_k > 0:
        cmd += ["-k", str(top_k)]
    if version:
        cmd += ["-v", str(version)]

    # Tambahkan file absolut
    abs_files = [str((base_dir / r).resolve()) for r in rels]
    cmd += abs_files
    return cmd

# ----- streaming (tee) stdout/stderr real-time ke konsol + file -----
def popen_stream_tee(cmd: List[str], timeout: int, prefix: str, logfile: Path) -> int:
    """
    Jalankan proses, stream stdout & stderr baris-per-baris:
    - Tampilkan ke terminal dengan prefix [B#### A#]
    - Simpan juga ke logfile
    """
    with logfile.open("a", encoding="utf-8") as lf:
        lf.write(f"\n{'='*80}\nCMD: {' '.join(cmd[:20])}{' ...' if len(cmd)>20 else ''}\n")
        lf.flush()

        # text=True = universal_newlines; bufsize=1 untuk line-buffered
        p = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, bufsize=1,
            env={**os.environ, "PYTHONIOENCODING":"utf-8","HF_HUB_DISABLE_SYMLINKS_WARNING":"1"}
        )

        start = time.time()
        try:
            for line in p.stdout:
                line = line.rstrip("\n")
                with PRINT_LOCK:
                    print(f"{prefix} {line}")
                lf.write(line + "\n")
                lf.flush()
            rc = p.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            try:
                p.kill()
            except Exception:
                pass
            with PRINT_LOCK:
                print(f"{prefix} TIMEOUT after {time.time()-start:.1f}s")
            lf.write(f"{prefix} TIMEOUT\n")
            lf.flush()
            return 124
        return rc

# -------------------- Batch worker (auto-retry per-file) --------------------
def process_batch_verbose(batch_id: int,
                          py_exe: str,
                          base_dir: Path,
                          out_dir: Path,
                          files: List[str],
                          timeout: int,
                          top_k:int,
                          default_version:str|None) -> Dict:
    """
    Eksekusi batch (≤15 file) dengan 3 attempt maksimum.
    Setiap attempt di-stream real-time ke konsol + log.
    Setelah attempt, cek file yang belum menghasilkan .py → lanjut attempt berikutnya untuk sisa.
    """
    log_path = Path(f"queue_batch_{batch_id:05d}.log")
    err_path = Path(f"queue_batch_{batch_id:05d}.err")

    remaining = list(files)

    # Attempt 1 (default)
    cmd1 = build_cmd(py_exe, base_dir, out_dir, remaining)
    rc1 = popen_stream_tee(cmd1, timeout, prefix=f"[B{batch_id:05d} A1]", logfile=log_path)

    # Filter jadi
    status = file_has_output(out_dir, remaining)
    remaining = [r for r in remaining if not status.get(r, False)]

    # Attempt 2
    if remaining:
        cmd2 = build_cmd(py_exe, base_dir, out_dir, remaining,
                         trust_lnotab=True, top_k=max(5, top_k))
        rc2 = popen_stream_tee(cmd2, timeout, prefix=f"[B{batch_id:05d} A2]", logfile=log_path)
        status2 = file_has_output(out_dir, remaining)
        remaining = [r for r in remaining if not status2.get(r, False)]

    # Attempt 3 (fallback -v)
    if remaining and default_version:
        cmd3 = build_cmd(py_exe, base_dir, out_dir, remaining,
                         trust_lnotab=True, top_k=max(5, top_k), version=default_version)
        rc3 = popen_stream_tee(cmd3, timeout, prefix=f"[B{batch_id:05d} A3]", logfile=log_path)
        status3 = file_has_output(out_dir, remaining)
        remaining = [r for r in remaining if not status3.get(r, False)]

    # Tulis daftar yang masih gagal
    if remaining:
        with err_path.open("w", encoding="utf-8") as ef:
            ef.write(f"[Batch {batch_id}] FAILED after retries: {len(remaining)} files\n")
            ef.write("\n".join(remaining[:5000]))

    success_count = len(files) - len(remaining)
    return {"batch_id": batch_id, "total": len(files), "success": success_count, "fail": len(remaining)}

# -------------------- Orchestrator: Queue dinamis --------------------
def chunked(seq: List[str], n: int) -> List[List[str]]:
    return [seq[i:i+n] for i in range(0, len(seq), n)]

def main():
    ap = argparse.ArgumentParser(description="Direct Queue (VERBOSE) — 25×15, auto-retry per-file, streaming output.")
    ap.add_argument("--inventory", default="pyc_inventory.csv", help="CSV (kolom 'relative_path')")
    ap.add_argument("--base-dir", default=".", help="Folder dasar (default: CWD)")
    ap.add_argument("--out", default="decompiled_queue", help="Folder output hasil .py")
    ap.add_argument("--threads", type=int, default=25, help="Jumlah thread worker (default 25)")
    ap.add_argument("--batch-size", type=int, default=15, help="Jumlah file per batch (default 15)")
    ap.add_argument("--timeout", type=int, default=900, help="Timeout per batch (detik)")
    ap.add_argument("--top-k", type=int, default=3, help="Nilai -k untuk attempt 2/3 (min 5 akan dipakai)")
    ap.add_argument("--default-version", default=None, help="Fallback -v CPython (mis. 3.11) untuk attempt 3")
    args = ap.parse_args()

    base_dir = Path(args.base_dir).resolve()
    out_dir  = Path(args.out).resolve()
    ensure_dir(out_dir)

    rel_all = read_inventory(Path(args.inventory))
    if not rel_all:
        print(f"[ERROR] Inventory kosong/tidak valid: {args.inventory}")
        sys.exit(1)

    py_exe = detect_pylingual_python()
    log(f"Using Python : {py_exe}")
    log(f"Base dir     : {base_dir}")
    log(f"Output dir   : {out_dir}")
    log(f"Total files  : {len(rel_all)}")
    log(f"Threads      : {args.threads}, Batch size: {args.batch_size}")

    # Build antrean batch dari file yang belum punya output .py
    pending = [r for r in rel_all if not (out_py_path(out_dir, r).exists() and out_py_path(out_dir, r).stat().st_size > 0)]
    if not pending:
        log("Semua file sudah memiliki output .py. Selesai.")
        return

    batches = chunked(pending, args.batch_size)
    q: Queue[List[str]] = Queue()
    for b in batches:
        q.put(b)

    PROG_LOCK = threading.Lock()
    total_target = len(pending)
    processed_files = 0
    success_files = 0
    failed_files  = 0
    batch_counter = 0

    def worker(thread_id: int):
        nonlocal processed_files, success_files, failed_files, batch_counter
        while True:
            try:
                batch = q.get_nowait()
            except Exception:
                break
            batch_counter += 1
            batch_id = batch_counter
            res = process_batch_verbose(
                batch_id=batch_id,
                py_exe=py_exe,
                base_dir=base_dir,
                out_dir=out_dir,
                files=batch,
                timeout=args.timeout,
                top_k=args.top_k,
                default_version=args.default_version
            )
            with PROG_LOCK:
                processed_files += res["total"]
                success_files   += res["success"]
                failed_files    += res["fail"]
                log(f"[PROGRESS] OK:{success_files}/{total_target}  FAIL:{failed_files}  (Batch {batch_id} done)")
            q.task_done()

    threads = []
    for t in range(max(1, args.threads)):
        th = threading.Thread(target=worker, args=(t+1,), daemon=True)
        th.start()
        threads.append(th)
    for th in threads:
        th.join()

    log("\n=== SELESAI (VERBOSE) ===")
    log(f"Target files : {total_target}")
    log(f"OK          : {success_files}")
    log(f"FAIL        : {failed_files}")
    log(f"Output dir  : {out_dir}")

if __name__ == "__main__":
    main()
