"""
Captcha Solver Service for Auto Cloud Skill Registration application.

Professional implementation of audio captcha solving using speech recognition
with proper error handling, multiple engines, and audio preprocessing.
"""

import speech_recognition as sr
import requests
import tempfile
import os
import subprocess
import shlex
from pathlib import Path
from typing import Optional, Union, List
import logging
from datetime import datetime
import io

from utils.logger import log_service_call
from utils.validators import validate_url, ValidationError

logger = logging.getLogger(__name__)

class CaptchaSolverService:
    """
    Service for solving audio captchas using speech recognition.

    This service provides robust audio captcha solving capabilities with
    multiple recognition engines and proper audio preprocessing.
    """

    def __init__(self):
        """Initialize the captcha solver service."""
        self.recognizer = sr.Recognizer()

        # Configure recognizer settings for better accuracy
        self.recognizer.energy_threshold = 200
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.5
        self.recognizer.operation_timeout = None
        self.recognizer.phrase_threshold = 0.2
        self.recognizer.non_speaking_duration = 0.5

        # Test available engines
        self.available_engines = self._test_recognition_engines()
        logger.info(f"Available recognition engines: {self.available_engines}")

    def solve_audio_captcha(self, audio_url: str) -> Optional[str]:
        """
        Solve audio captcha from URL.

        Args:
            audio_url: URL to the audio captcha file

        Returns:
            str: Recognized text or None if failed
        """
        start_time = datetime.now()

        try:
            # Validate URL
            validate_url(audio_url)

            # Download audio file
            logger.info(f"Downloading audio captcha from: {audio_url}")
            response = requests.get(audio_url, timeout=30)
            response.raise_for_status()

            if not response.content:
                raise ValueError("Empty audio file received")

            # Process the audio content
            result = self.solve_audio_captcha_from_bytes(
                response.content,
                self._detect_audio_format(response.headers.get('content-type', ''))
            )

            # Log result
            response_time = (datetime.now() - start_time).total_seconds()
            status = 'SUCCESS' if result else 'FAILED'
            log_service_call('CaptchaSolver', 'solve_audio_captcha', status, response_time)

            return result

        except ValidationError as e:
            logger.error(f"Invalid audio URL: {e}")
            log_service_call('CaptchaSolver', 'solve_audio_captcha', 'FAILED')
            return None

        except requests.RequestException as e:
            logger.error(f"Error downloading audio captcha: {e}")
            log_service_call('CaptchaSolver', 'solve_audio_captcha', 'FAILED')
            return None

        except Exception as e:
            logger.error(f"Error solving audio captcha: {e}")
            log_service_call('CaptchaSolver', 'solve_audio_captcha', 'ERROR')
            return None

    def solve_audio_captcha_from_file(self, file_path: Union[str, Path]) -> Optional[str]:
        """
        Solve audio captcha from local file.

        Args:
            file_path: Path to the audio file

        Returns:
            str: Recognized text or None if failed
        """
        try:
            file_path = Path(file_path)

            if not file_path.exists():
                logger.error(f"Audio file not found: {file_path}")
                return None

            if file_path.stat().st_size == 0:
                logger.error(f"Audio file is empty: {file_path}")
                return None

            logger.info(f"Processing audio file: {file_path}")
            return self._process_audio_file(str(file_path))

        except Exception as e:
            logger.error(f"Error solving audio captcha from file: {e}")
            return None

    def solve_audio_captcha_from_bytes(self, audio_bytes: bytes, format: str = 'wav') -> Optional[str]:
        """
        Solve audio captcha from bytes data.

        Args:
            audio_bytes: Audio data as bytes
            format: Audio format (wav, mp3, etc.)

        Returns:
            str: Recognized text or None if failed
        """
        if not audio_bytes:
            logger.error("Empty audio bytes provided")
            return None

        temp_file_path = None
        try:
            # Create temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{format}') as temp_file:
                temp_file.write(audio_bytes)
                temp_file_path = temp_file.name

            # Process the temporary file
            result = self._process_audio_file(temp_file_path)
            return result

        except Exception as e:
            logger.error(f"Error solving audio captcha from bytes: {e}")
            return None

        finally:
            # Clean up temporary file
            if temp_file_path and os.path.exists(temp_file_path):
                try:
                    os.unlink(temp_file_path)
                except Exception as e:
                    logger.warning(f"Failed to delete temp file {temp_file_path}: {e}")

    def _process_audio_file(self, file_path: str) -> Optional[str]:
        """
        Process audio file and extract text using speech recognition.

        Args:
            file_path: Path to the audio file

        Returns:
            str: Recognized text or None if failed
        """
        try:
            # Convert to WAV if necessary
            wav_path = self._ensure_wav_format(file_path)

            # Load audio file
            with sr.AudioFile(wav_path) as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

                # Record the audio
                audio = self.recognizer.record(source)

            # Try recognition with multiple engines
            for engine in self.available_engines:
                try:
                    result = self._recognize_with_engine(audio, engine)
                    if result:
                        logger.info(f"Captcha solved using {engine}: {result}")
                        return result.strip()
                except Exception as e:
                    logger.warning(f"Recognition failed with {engine}: {e}")
                    continue

            logger.warning("All recognition engines failed")
            return None

        except Exception as e:
            logger.error(f"Error processing audio file: {e}")
            return None

        finally:
            # Clean up converted file if it was created
            if 'wav_path' in locals() and wav_path != file_path:
                try:
                    os.unlink(wav_path)
                except Exception:
                    pass

    def _recognize_with_engine(self, audio: sr.AudioData, engine: str) -> Optional[str]:
        """
        Recognize audio using specified engine.

        Args:
            audio: Audio data
            engine: Recognition engine name

        Returns:
            str: Recognized text or None if failed
        """
        try:
            if engine == 'google':
                return self.recognizer.recognize_google(audio, language='en-US')
            elif engine == 'google_cloud':
                return self.recognizer.recognize_google_cloud(audio, language='en-US')
            elif engine == 'wit':
                return self.recognizer.recognize_wit(audio)
            elif engine == 'azure':
                return self.recognizer.recognize_azure(audio, language='en-US')
            elif engine == 'sphinx':
                return self.recognizer.recognize_sphinx(audio)
            else:
                logger.warning(f"Unknown recognition engine: {engine}")
                return None

        except sr.UnknownValueError:
            logger.debug(f"Could not understand audio with {engine}")
            return None
        except sr.RequestError as e:
            logger.error(f"Recognition service error with {engine}: {e}")
            return None

    def _test_recognition_engines(self) -> List[str]:
        """
        Test which recognition engines are available.

        Returns:
            List[str]: List of available engine names
        """
        available = []

        # Test Google (free, no API key required)
        try:
            # Create a short silence to test
            import numpy as np
            silence = np.zeros(1000, dtype=np.int16)
            audio_data = sr.AudioData(silence.tobytes(), 16000, 2)

            self.recognizer.recognize_google(audio_data)
            available.append('google')
        except sr.UnknownValueError:
            # This is expected for silence
            available.append('google')
        except Exception:
            logger.debug("Google Speech Recognition not available")

        # Test Sphinx (offline)
        try:
            import pocketsphinx
            available.append('sphinx')
        except ImportError:
            logger.debug("PocketSphinx not available")

        # Note: Other engines require API keys, so we don't test them here
        return available

    def _ensure_wav_format(self, file_path: str) -> str:
        """
        Ensure audio file is in WAV format for speech recognition.

        Args:
            file_path: Path to the audio file

        Returns:
            str: Path to WAV file (may be the same as input)
        """
        if file_path.lower().endswith('.wav'):
            return file_path

        try:
            # Try to convert using ffmpeg
            wav_path = file_path.rsplit('.', 1)[0] + '_converted.wav'

            command = [
                'ffmpeg', '-i', file_path,
                '-acodec', 'pcm_s16le',
                '-ar', '16000',
                '-ac', '1',
                '-y',  # Overwrite output file
                wav_path
            ]

            subprocess.run(command, check=True, capture_output=True)
            return wav_path

        except subprocess.CalledProcessError as e:
            logger.warning(f"FFmpeg conversion failed: {e}")
            # Return original file and hope speech_recognition can handle it
            return file_path

        except FileNotFoundError:
            logger.warning("FFmpeg not found, using original file format")
            return file_path

    def _detect_audio_format(self, content_type: str) -> str:
        """
        Detect audio format from content type.

        Args:
            content_type: HTTP content type header

        Returns:
            str: Audio format extension
        """
        if 'wav' in content_type:
            return 'wav'
        elif 'mp3' in content_type:
            return 'mp3'
        elif 'ogg' in content_type:
            return 'ogg'
        elif 'webm' in content_type:
            return 'webm'
        else:
            return 'wav'  # Default to WAV

    def test_service(self) -> bool:
        """
        Test if the captcha solver service is working.

        Returns:
            bool: True if service is functional
        """
        try:
            # Test with a short silence
            import numpy as np
            silence = np.zeros(1000, dtype=np.int16)

            # Create temporary WAV file
            with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
                # Write WAV header and data
                import wave
                with wave.open(temp_file.name, 'wb') as wav_file:
                    wav_file.setnchannels(1)
                    wav_file.setsampwidth(2)
                    wav_file.setframerate(16000)
                    wav_file.writeframes(silence.tobytes())

                # Test recognition (should fail gracefully with silence)
                result = self.solve_audio_captcha_from_file(temp_file.name)

                # Clean up
                os.unlink(temp_file.name)

                # Service is working if it didn't crash
                return True

        except Exception as e:
            logger.error(f"Service test failed: {e}")
            return False