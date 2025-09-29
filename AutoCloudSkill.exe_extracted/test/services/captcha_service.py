# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: services\captcha_service.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
Service untuk menyelesaikan captcha menggunakan speech recognition
"""
import speech_recognition as sr
import requests
import tempfile
import os
from typing import Optional
import logging
from moviepy.audio.io.AudioFileClip import AudioFileClip
import imageio_ffmpeg
import subprocess
import shlex
import io

logger = logging.getLogger(__name__)

class CaptchaSolverService:
    """Service untuk menyelesaikan audio captcha menggunakan speech recognition"""

    def __init__(self):
        """Initialize captcha solver service untuk audio captcha saja"""
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 200
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.5
        self.recognizer.operation_timeout = None
        self.recognizer.phrase_threshold = 0.2
        self.recognizer.non_speaking_duration = 0.5

    def solve_audio_captcha(self, audio_url: str) -> Optional[str]:
        """
        Selesaikan audio captcha dari URL

        Args:
            audio_url: URL file audio captcha

        Returns:
            String teks hasil recognition atau None jika gagal
        """
        try:
            response = requests.get(audio_url, timeout=10)
            response.raise_for_status()
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
                temp_file.write(response.content)
                temp_file_path = temp_file.name
                try:
                    result = self._process_audio_file(temp_file_path)
                    return result
                finally:
                    if os.path.exists(temp_file_path):
                        os.unlink(temp_file_path)
        except requests.RequestException as e:
            logger.error(f'Error downloading audio captcha: {e}')
        except Exception as e:
            logger.error(f'Error solving audio captcha: {e}')
        return None

    def solve_audio_captcha_from_file(self, file_path: str) -> Optional[str]:
        """
        Selesaikan audio captcha dari file lokal

        Args:
            file_path: Path ke file audio captcha

        Returns:
            String teks hasil recognition atau None jika gagal
        """
        try:
            if not os.path.exists(file_path):
                logger.error(f'Audio file not found: {file_path}')
                return None
            return self._process_audio_file(file_path)
        except Exception as e:
            logger.error(f'Error solving audio captcha from file: {e}')
            return None

    def solve_audio_captcha_from_bytes(self, audio_bytes: bytes, format: str='wav') -> Optional[str]:
        """
        Selesaikan audio captcha dari bytes data

        Args:
            audio_bytes: Data audio dalam bytes
            format: Format audio (wav, mp3, dll)

        Returns:
            String teks hasil recognition atau None jika gagal
        """
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{format}') as temp_file:
                temp_file.write(audio_bytes)
                temp_file_path = temp_file.name
                try:
                    result = self._process_audio_file(temp_file_path)
                    return result
                finally:
                    if os.path.exists(temp_file_path):
                        os.unlink(temp_file_path)
        except Exception as e:
            logger.error(f'Error solving audio captcha from bytes: {e}')
            return None

    def _process_audio_file(self, file_path: str) -> Optional[str]:
        """
        Process audio file dan lakukan speech recognition untuk captcha

        Args:
            file_path: Path ke file audio

        Returns:
            String teks hasil recognition atau None jika gagal
        """
        wav_path = None
        try:
            wav_path = self._convert_to_wav_16k_mono(file_path)
            with sr.AudioFile(wav_path) as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.05)
                audio = self.recognizer.record(source)
                try:
                    raw = self.recognizer.recognize_google(audio, language='en-US')
                    if raw:
                        cleaned = self._clean_captcha_result(raw)
                        logger.info(f'Google recognition raw=\'{raw[:80]}\'')
                        return cleaned
                    else:
                        logger.debug('Google could not understand audio captcha')
                        return None
                except sr.UnknownValueError:
                    logger.debug('Google could not understand audio captcha')
                    return None
                except sr.RequestError as e:
                    logger.debug(f'Google recognition error: {e}')
                    return None
        except Exception as e:
            logger.error(f'Error processing audio captcha: {e}')
            return None
        finally:
            if wav_path and os.path.exists(wav_path):
                try:
                    os.unlink(wav_path)
                except Exception:
                    pass

    def _convert_to_wav_16k_mono(self, file_path: str) -> str:
        """
        Konversi ke WAV 16k mono.
        Jalur utama: ffmpeg (imageio-ffmpeg) agar cepat dan ringan.
        Fallback: moviepy jika terjadi error.
        """
        base, _ = os.path.splitext(file_path)
        out_path = base + '_16kmono.wav'
        try:
            ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
            cmd = [ffmpeg_exe, '-y', '-i', file_path, '-ac', '1', '-ar', '16000', '-acodec', 'pcm_s16le', out_path]
            creationflags = getattr(subprocess, 'CREATE_NO_WINDOW', 0)
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, creationflags=creationflags)
            if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
                return out_path
            raise RuntimeError('ffmpeg produced empty output')
        except Exception as e_ff:
            logger.warning(f'ffmpeg convert error: {e_ff}. Falling back to moviepy.')
            try:
                clip = AudioFileClip(file_path)
                try:
                    clip.write_audiofile(out_path, fps=16000, nbytes=2, codec='pcm_s16le')
                finally:
                    try:
                        clip.close()
                    except Exception:
                        pass
                if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
                    return out_path
                raise RuntimeError('moviepy produced empty output')
            except Exception as e_mv:
                logger.error(f'moviepy fallback failed: {e_mv}')
                raise

    def _clean_captcha_result(self, result: str) -> str:
        """Kembalikan hasil raw dari SpeechRecognition (trim saja)."""
        return (result or '').strip()

if __name__ == '__main__':
    solver = CaptchaSolverService()
    print('CaptchaSolverService initialized successfully')
    print('Use solve_audio_captcha(url) to solve captcha from URL')
    print('Use solve_audio_captcha_from_file(path) to solve from local file')