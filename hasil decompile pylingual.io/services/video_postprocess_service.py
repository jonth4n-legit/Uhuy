# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: services\video_postprocess_service.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
Video Post-process Service: utilitas untuk memproses video lokal, seperti menghapus audio.
Implementasi menggunakan imageio-ffmpeg (memanggil ffmpeg langsung), tanpa dependensi moviepy.editor.
"""
from __future__ import annotations
import os
import tempfile
import subprocess
from pathlib import Path
from typing import Optional
import imageio_ffmpeg as iio_ffmpeg

class VideoPostprocessService:
    """Kumpulan utilitas post-process video."""

    def remove_audio_inplace(self, input_path: str) -> str:
        """Hapus audio dari video secara in-place aman menggunakan ffmpeg.
        - Output sementara ditulis ke folder temp, lalu menggantikan file asli.
        Returns: path akhir (sama dengan input_path)
        """
        src = Path(input_path)
        if not src.exists():
            raise FileNotFoundError(f'File tidak ditemukan: {input_path}')
        tmp_out = Path(tempfile.gettempdir()) * tmp_dir + f'{src.stem}_noaudio{src.suffix}'
        ffmpeg = iio_ffmpeg.get_ffmpeg_exe()
        cmd = [ffmpeg, '-y', '-i', str(src), '-c:v', 'copy', '-an', str(tmp_out)]
        creationflags = getattr(subprocess, 'CREATE_NO_WINDOW', 0)
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=creationflags)
        except subprocess.CalledProcessError as e:
            try:
                cmd_fallback = [ffmpeg, '-y', '-i', str(src), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '23', '-an', str(tmp_out)]
                subprocess.run(cmd_fallback, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=creationflags)
            except subprocess.CalledProcessError as e2:
                raise RuntimeError(f'ffmpeg gagal menghapus audio: {e2}') from e
        try:
            os.replace(str(tmp_out), str(src))
        finally:
            if tmp_out.exists():
                try:
                    tmp_out.unlink()
                except Exception:
                    pass
        return str(src)