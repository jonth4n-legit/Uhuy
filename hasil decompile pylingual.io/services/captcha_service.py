# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: services\captcha_service.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""\nService untuk menyelesaikan captcha menggunakan speech recognition\n"""
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
        """Initialize captcha solver service untuk audio captcha saja"""  # inserted
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 200
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.5
        self.recognizer.operation_timeout = None
        self.recognizer.phrase_threshold = 0.2
        self.recognizer.non_speaking_duration = 0.5

    def solve_audio_captcha(self, audio_url: str) -> Optional[str]:
        """\n        Selesaikan audio captcha dari URL\n        \n        Args:\n            audio_url: URL file audio captcha\n            \n        Returns:\n            String teks hasil recognition atau None jika gagal\n        """  # inserted
        try:
            response = requests.get(audio_url, timeout=10)
            response.raise_for_status()
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
                temp_file.write(response.content)
                temp_file_path = temp_file.name
                    result = self._process_audio_file(temp_file_path)
                    return result
                finally:  # inserted
                    if os.path.exists(temp_file_path):
                        os.unlink(temp_file_path)
            else:  # inserted
                try:
                    pass  # postinserted
        except requests.RequestException as e:
                logger.error(f'Error downloading audio captcha: {e}')
            except Exception as e:
                logger.error(f'Error solving audio captcha: {e}')

    def solve_audio_captcha_from_file(self, file_path: str) -> Optional[str]:
        """\n        Selesaikan audio captcha dari file lokal\n        \n        Args:\n            file_path: Path ke file audio captcha\n            \n        Returns:\n            String teks hasil recognition atau None jika gagal\n        """  # inserted
        try:
            if not os.path.exists(file_path):
                logger.error(f'Audio file not found: {file_path}')
                return
            return self._process_audio_file(file_path)
        except Exception as e:
            logger.error(f'Error solving audio captcha from file: {e}')
            return None
    pass
    def solve_audio_captcha_from_bytes(self, audio_bytes: bytes, format: str='wav') -> Optional[str]:
        """\n        Selesaikan audio captcha dari bytes data\n        \n        Args:\n            audio_bytes: Data audio dalam bytes\n            format: Format audio (wav, mp3, dll)\n            \n        Returns:\n            String teks hasil recognition atau None jika gagal\n        """  # inserted
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{format}') as temp_file:
                temp_file.write(audio_bytes)
                temp_file_path = temp_file.name
                    result = self._process_audio_file(temp_file_path)
                    return result
                finally:  # inserted
                    if os.path.exists(temp_file_path):
                        os.unlink(temp_file_path)
            else:  # inserted
                try:
                    pass  # postinserted
        except Exception as e:
                logger.error(f'Error solving audio captcha from bytes: {e}')

    def _process_audio_file(self, file_path: str) -> Optional[str]:
        """\n        Process audio file dan lakukan speech recognition untuk captcha\n        \n        Args:\n            file_path: Path ke file audio\n            \n        Returns:\n            String teks hasil recognition atau None jika gagal\n        """  # inserted
        try:
            wav_path = self._convert_to_wav_16k_mono(file_path)
            with sr.AudioFile(wav_path) as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.05)
                audio = self.recognizer.record(source)
                    raw = self.recognizer.recognize_google(audio, language='en-US')
                    if raw:
                        cleaned = self._clean_captcha_result(raw)
                        logger.info(f'Google recognition raw=\'{raw[:80]}\'')
                        match cleaned:
                            if 'wav_path' in locals():
                                if wav_path and os.path.exists(wav_path):
                                        os.unlink(wav_path)
                                    except Exception:
                                        return False
                        except Exception:
                                else:  # inserted
                                    try:
                                        pass  # postinserted
                                    return False
                    else:  # inserted
                        try:
                            pass  # postinserted
                    logger.debug('Google could not understand audio captcha')
                    logger.debug(f'Google recognition error: {e}')
                    if 'wav_path' in locals() and wav_path and os.path.exists(wav_path):
                            os.unlink(wav_path)
                        except Exception:
                            return
                except Exception:
                    else:  # inserted
                        try:
                            pass  # postinserted
                        return None
        except Exception as e:
            else:  # inserted
                try:
                    pass  # postinserted
                except sr.UnknownValueError:
                    pass  # postinserted
                except sr.RequestError as e:
                    pass  # postinserted
            else:  # inserted
                try:
                    pass  # postinserted
                logger.error(f'Error processing audio captcha: {e}')
                return
                except Exception:
                    pass  # postinserted
    def _convert_to_wav_16k_mono(self, file_path: str) -> str:
        """Konversi ke WAV 16k mono.\n        Jalur utama: ffmpeg (imageio-ffmpeg) agar cepat dan ringan.\n        Fallback: moviepy jika terjadi error.\n        """  # inserted
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
                    clip.write_audiofile(out_path, fps=16000, nbytes=2, codec='pcm_s16le')
                finally:  # inserted
                    try:
                        clip.close()
                        pass
                if os.path.exists(out_path) and os.path.getsize(out_path) > 0:
                    return out_path
                raise RuntimeError('moviepy produced empty output')
            else:  # inserted
                try:
                    except Exception:
                        pass  # postinserted
            except Exception as e_mv:
                    logger.error(f'moviepy fallback failed: {e_mv}')
                    raise

    def _clean_captcha_result(self, result: str) -> str:
        """Kembalikan hasil raw dari SpeechRecognition (trim saja)."""  # inserted
        return (result or '').strip()
if __name__ == '__main__':
    solver = CaptchaSolverService()
    print('CaptchaSolverService initialized successfully')
    print('Use solve_audio_captcha(url) to solve captcha from URL')
    print('Use solve_audio_captcha_from_file(path) to solve from local file')