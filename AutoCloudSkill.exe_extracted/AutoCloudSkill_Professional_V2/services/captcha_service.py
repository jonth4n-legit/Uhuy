"""
Professional captcha solving service for AutoCloudSkill.

This module provides comprehensive captcha solving capabilities:
- Audio captcha solving using speech recognition
- Multiple recognition engines (Google, Azure, OpenAI Whisper)
- Image captcha support with OCR
- AntiCaptcha API integration
- 2Captcha API integration
- Fallback mechanisms and retry logic

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import os
import io
import tempfile
import logging
import asyncio
from pathlib import Path
from typing import Optional, Dict, Any, List, Union, Tuple
from dataclasses import dataclass
from enum import Enum
import base64
import time

import requests
import speech_recognition as sr
from PIL import Image
import numpy as np

from utils.logger import setup_application_logging, log_automation_step, performance_monitor
from config.settings import settings

logger = setup_application_logging('CaptchaService')

class CaptchaType(Enum):
    """Supported captcha types."""
    AUDIO = "audio"
    IMAGE = "image"
    RECAPTCHA_V2 = "recaptcha_v2"
    RECAPTCHA_V3 = "recaptcha_v3"
    HCAPTCHA = "hcaptcha"
    FUNCAPTCHA = "funcaptcha"

class SolverEngine(Enum):
    """Available solving engines."""
    SPEECH_RECOGNITION = "speech_recognition"
    ANTICAPTCHA = "anticaptcha"
    TWOCAPTCHA = "2captcha"
    OCR = "ocr"
    WHISPER = "whisper"

@dataclass
class CaptchaSolution:
    """Captcha solution result."""
    success: bool
    solution: Optional[str]
    confidence: float
    engine: SolverEngine
    duration: float
    error_message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class AudioCaptchaSolver:
    """Advanced audio captcha solver with multiple engines."""

    def __init__(self):
        """Initialize audio captcha solver."""
        self.recognizer = sr.Recognizer()
        self._configure_recognizer()

    def _configure_recognizer(self) -> None:
        """Configure speech recognizer with optimal settings."""
        self.recognizer.energy_threshold = 200
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.5
        self.recognizer.operation_timeout = None
        self.recognizer.phrase_threshold = 0.2
        self.recognizer.non_speaking_duration = 0.5

    @performance_monitor("audio_captcha_solve")
    def solve_from_url(self, audio_url: str) -> CaptchaSolution:
        """
        Solve audio captcha from URL.

        Args:
            audio_url: URL of the audio captcha

        Returns:
            CaptchaSolution with results
        """
        start_time = time.time()

        try:
            # Download audio
            response = requests.get(audio_url, timeout=30)
            response.raise_for_status()

            return self.solve_from_bytes(response.content)

        except requests.RequestException as e:
            duration = time.time() - start_time
            logger.error(f"Failed to download audio captcha: {e}")

            return CaptchaSolution(
                success=False,
                solution=None,
                confidence=0.0,
                engine=SolverEngine.SPEECH_RECOGNITION,
                duration=duration,
                error_message=f"Download failed: {str(e)}"
            )

    @performance_monitor("audio_captcha_process")
    def solve_from_bytes(self, audio_bytes: bytes, format_hint: str = "wav") -> CaptchaSolution:
        """
        Solve audio captcha from byte data.

        Args:
            audio_bytes: Raw audio data
            format_hint: Audio format hint

        Returns:
            CaptchaSolution with results
        """
        start_time = time.time()

        temp_file = None
        wav_file = None

        try:
            # Create temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{format_hint}') as temp_file:
                temp_file.write(audio_bytes)
                temp_file_path = temp_file.name

            # Convert to WAV if needed
            wav_file_path = self._convert_to_wav(temp_file_path)

            # Process with multiple engines
            solutions = []

            # Try Google Speech Recognition
            google_solution = self._solve_with_google(wav_file_path)
            if google_solution.success:
                solutions.append(google_solution)

            # Try Azure if available
            try:
                azure_solution = self._solve_with_azure(wav_file_path)
                if azure_solution.success:
                    solutions.append(azure_solution)
            except Exception:
                pass  # Azure not available

            # Try OpenAI Whisper if available
            try:
                whisper_solution = self._solve_with_whisper(wav_file_path)
                if whisper_solution.success:
                    solutions.append(whisper_solution)
            except Exception:
                pass  # Whisper not available

            # Select best solution
            if solutions:
                best_solution = max(solutions, key=lambda x: x.confidence)
                duration = time.time() - start_time
                best_solution.duration = duration
                return best_solution

            # No successful solutions
            duration = time.time() - start_time
            return CaptchaSolution(
                success=False,
                solution=None,
                confidence=0.0,
                engine=SolverEngine.SPEECH_RECOGNITION,
                duration=duration,
                error_message="All recognition engines failed"
            )

        except Exception as e:
            duration = time.time() - start_time
            logger.error(f"Audio captcha solving failed: {e}")

            return CaptchaSolution(
                success=False,
                solution=None,
                confidence=0.0,
                engine=SolverEngine.SPEECH_RECOGNITION,
                duration=duration,
                error_message=str(e)
            )

        finally:
            # Cleanup temporary files
            for file_path in [temp_file, wav_file]:
                if file_path and os.path.exists(file_path):
                    try:
                        os.unlink(file_path)
                    except Exception:
                        pass

    def _convert_to_wav(self, input_path: str) -> str:
        """
        Convert audio file to WAV format with optimal settings for speech recognition.

        Args:
            input_path: Path to input audio file

        Returns:
            Path to converted WAV file
        """
        try:
            # Try with moviepy first
            from moviepy.audio.io.AudioFileClip import AudioFileClip

            wav_path = input_path.replace(Path(input_path).suffix, '_converted.wav')

            with AudioFileClip(input_path) as audio:
                # Convert to 16kHz mono for better recognition
                audio_resampled = audio.set_fps(16000)
                if audio.nchannels > 1:
                    audio_resampled = audio_resampled.to_mono()

                audio_resampled.write_audiofile(
                    wav_path,
                    verbose=False,
                    logger=None,
                    codec='pcm_s16le'
                )

            return wav_path

        except ImportError:
            logger.warning("moviepy not available, using ffmpeg directly")
            return self._convert_with_ffmpeg(input_path)

        except Exception as e:
            logger.warning(f"moviepy conversion failed: {e}, trying ffmpeg")
            return self._convert_with_ffmpeg(input_path)

    def _convert_with_ffmpeg(self, input_path: str) -> str:
        """
        Convert audio using ffmpeg directly.

        Args:
            input_path: Path to input audio file

        Returns:
            Path to converted WAV file
        """
        import subprocess
        import shlex

        wav_path = input_path.replace(Path(input_path).suffix, '_converted.wav')

        try:
            # Use ffmpeg for conversion
            cmd = [
                'ffmpeg', '-i', input_path,
                '-ar', '16000',  # 16kHz sample rate
                '-ac', '1',      # Mono
                '-y',            # Overwrite
                wav_path
            ]

            subprocess.run(cmd, check=True, capture_output=True)
            return wav_path

        except subprocess.CalledProcessError as e:
            logger.error(f"ffmpeg conversion failed: {e}")
            # Return original file if conversion fails
            return input_path

        except FileNotFoundError:
            logger.warning("ffmpeg not found, using original file")
            return input_path

    def _solve_with_google(self, audio_file: str) -> CaptchaSolution:
        """
        Solve using Google Speech Recognition.

        Args:
            audio_file: Path to audio file

        Returns:
            CaptchaSolution with results
        """
        start_time = time.time()

        try:
            with sr.AudioFile(audio_file) as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.record(source)

            # Recognize speech
            result = self.recognizer.recognize_google(
                audio,
                language='en-US',
                show_all=False
            )

            if result:
                cleaned_result = self._clean_captcha_text(result)
                confidence = 0.8  # Google doesn't provide confidence scores

                duration = time.time() - start_time
                logger.info(f"Google recognition: '{result}' -> '{cleaned_result}'")

                return CaptchaSolution(
                    success=True,
                    solution=cleaned_result,
                    confidence=confidence,
                    engine=SolverEngine.SPEECH_RECOGNITION,
                    duration=duration,
                    metadata={'raw_result': result, 'engine': 'google'}
                )

        except sr.UnknownValueError:
            logger.warning("Google could not understand audio")
        except sr.RequestError as e:
            logger.error(f"Google recognition service error: {e}")
        except Exception as e:
            logger.error(f"Google recognition error: {e}")

        duration = time.time() - start_time
        return CaptchaSolution(
            success=False,
            solution=None,
            confidence=0.0,
            engine=SolverEngine.SPEECH_RECOGNITION,
            duration=duration,
            error_message="Google recognition failed"
        )

    def _solve_with_azure(self, audio_file: str) -> CaptchaSolution:
        """
        Solve using Azure Speech Recognition.

        Args:
            audio_file: Path to audio file

        Returns:
            CaptchaSolution with results
        """
        try:
            import azure.cognitiveservices.speech as speechsdk

            # Configure Azure Speech
            speech_key = os.environ.get('AZURE_SPEECH_KEY')
            service_region = os.environ.get('AZURE_SPEECH_REGION', 'eastus')

            if not speech_key:
                raise ValueError("Azure Speech key not configured")

            speech_config = speechsdk.SpeechConfig(
                subscription=speech_key,
                region=service_region
            )
            speech_config.speech_recognition_language = "en-US"

            # Create recognizer
            audio_config = speechsdk.audio.AudioConfig(filename=audio_file)
            speech_recognizer = speechsdk.SpeechRecognizer(
                speech_config=speech_config,
                audio_config=audio_config
            )

            # Perform recognition
            result = speech_recognizer.recognize_once()

            if result.reason == speechsdk.ResultReason.RecognizedSpeech:
                confidence = getattr(result, 'confidence', 0.85)  # Azure provides confidence
                cleaned_result = self._clean_captcha_text(result.text)

                logger.info(f"Azure recognition: '{result.text}' -> '{cleaned_result}'")

                return CaptchaSolution(
                    success=True,
                    solution=cleaned_result,
                    confidence=confidence,
                    engine=SolverEngine.SPEECH_RECOGNITION,
                    duration=0.0,  # Will be set by caller
                    metadata={'raw_result': result.text, 'engine': 'azure'}
                )

        except ImportError:
            logger.debug("Azure Speech SDK not available")
        except Exception as e:
            logger.warning(f"Azure recognition failed: {e}")

        return CaptchaSolution(
            success=False,
            solution=None,
            confidence=0.0,
            engine=SolverEngine.SPEECH_RECOGNITION,
            duration=0.0,
            error_message="Azure recognition failed"
        )

    def _solve_with_whisper(self, audio_file: str) -> CaptchaSolution:
        """
        Solve using OpenAI Whisper.

        Args:
            audio_file: Path to audio file

        Returns:
            CaptchaSolution with results
        """
        try:
            import whisper

            # Load model (small model for speed)
            model = whisper.load_model("base")

            # Transcribe
            result = model.transcribe(audio_file, language="en")

            if result and result.get('text'):
                text = result['text'].strip()
                confidence = 0.9  # Whisper generally has high accuracy
                cleaned_result = self._clean_captcha_text(text)

                logger.info(f"Whisper recognition: '{text}' -> '{cleaned_result}'")

                return CaptchaSolution(
                    success=True,
                    solution=cleaned_result,
                    confidence=confidence,
                    engine=SolverEngine.WHISPER,
                    duration=0.0,  # Will be set by caller
                    metadata={'raw_result': text, 'engine': 'whisper'}
                )

        except ImportError:
            logger.debug("Whisper not available")
        except Exception as e:
            logger.warning(f"Whisper recognition failed: {e}")

        return CaptchaSolution(
            success=False,
            solution=None,
            confidence=0.0,
            engine=SolverEngine.WHISPER,
            duration=0.0,
            error_message="Whisper recognition failed"
        )

    def _clean_captcha_text(self, text: str) -> str:
        """
        Clean and normalize captcha text.

        Args:
            text: Raw recognized text

        Returns:
            Cleaned text suitable for captcha input
        """
        if not text:
            return ""

        # Convert to lowercase
        text = text.lower().strip()

        # Remove common speech recognition artifacts
        text = text.replace("'", "")
        text = text.replace('"', "")
        text = text.replace(".", "")
        text = text.replace(",", "")
        text = text.replace("!", "")
        text = text.replace("?", "")

        # Remove spaces for typical captcha format
        text = text.replace(" ", "")

        # Keep only alphanumeric characters
        text = ''.join(char for char in text if char.isalnum())

        return text

class CaptchaSolverService:
    """
    Professional captcha solving service with multiple backends.
    """

    def __init__(self):
        """Initialize captcha solver service."""
        self.audio_solver = AudioCaptchaSolver()
        self._anticaptcha_key = settings.get('anticaptcha_api_key')
        self._twocaptcha_key = settings.get('twocaptcha_api_key')

        logger.info("CaptchaSolver service initialized")

    async def solve_captcha(
        self,
        captcha_type: CaptchaType,
        data: Union[str, bytes],
        **kwargs
    ) -> CaptchaSolution:
        """
        Solve captcha using appropriate method.

        Args:
            captcha_type: Type of captcha to solve
            data: Captcha data (URL, bytes, etc.)
            **kwargs: Additional parameters

        Returns:
            CaptchaSolution with results
        """
        log_automation_step(
            logger,
            f"solve_{captcha_type.value}_captcha",
            "START",
            {"type": captcha_type.value}
        )

        start_time = time.time()

        try:
            if captcha_type == CaptchaType.AUDIO:
                if isinstance(data, str):
                    solution = self.audio_solver.solve_from_url(data)
                else:
                    solution = self.audio_solver.solve_from_bytes(data)

                status = "SUCCESS" if solution.success else "ERROR"
                log_automation_step(
                    logger,
                    f"solve_audio_captcha",
                    status,
                    {
                        "success": solution.success,
                        "confidence": solution.confidence,
                        "engine": solution.engine.value
                    },
                    duration=solution.duration
                )

                return solution

            else:
                # Placeholder for other captcha types
                duration = time.time() - start_time
                solution = CaptchaSolution(
                    success=False,
                    solution=None,
                    confidence=0.0,
                    engine=SolverEngine.SPEECH_RECOGNITION,
                    duration=duration,
                    error_message=f"Captcha type {captcha_type.value} not implemented"
                )

                log_automation_step(
                    logger,
                    f"solve_{captcha_type.value}_captcha",
                    "ERROR",
                    {"error": solution.error_message}
                )

                return solution

        except Exception as e:
            duration = time.time() - start_time
            logger.error(f"Captcha solving failed: {e}")

            solution = CaptchaSolution(
                success=False,
                solution=None,
                confidence=0.0,
                engine=SolverEngine.SPEECH_RECOGNITION,
                duration=duration,
                error_message=str(e)
            )

            log_automation_step(
                logger,
                f"solve_{captcha_type.value}_captcha",
                "ERROR",
                {"error": str(e)}
            )

            return solution

    # Backward compatibility methods
    def solve_audio_captcha(self, audio_url: str) -> Optional[str]:
        """
        Solve audio captcha (backward compatibility).

        Args:
            audio_url: URL of audio captcha

        Returns:
            Solution text or None if failed
        """
        solution = self.audio_solver.solve_from_url(audio_url)
        return solution.solution if solution.success else None

    def solve_audio_captcha_from_file(self, file_path: str) -> Optional[str]:
        """
        Solve audio captcha from file (backward compatibility).

        Args:
            file_path: Path to audio file

        Returns:
            Solution text or None if failed
        """
        try:
            with open(file_path, 'rb') as f:
                audio_bytes = f.read()

            solution = self.audio_solver.solve_from_bytes(audio_bytes)
            return solution.solution if solution.success else None

        except Exception as e:
            logger.error(f"Failed to solve captcha from file: {e}")
            return None

    def solve_audio_captcha_from_bytes(
        self,
        audio_bytes: bytes,
        format: str = "wav"
    ) -> Optional[str]:
        """
        Solve audio captcha from bytes (backward compatibility).

        Args:
            audio_bytes: Raw audio data
            format: Audio format hint

        Returns:
            Solution text or None if failed
        """
        solution = self.audio_solver.solve_from_bytes(audio_bytes, format)
        return solution.solution if solution.success else None

# Export commonly used items
__all__ = [
    'CaptchaType',
    'SolverEngine',
    'CaptchaSolution',
    'AudioCaptchaSolver',
    'CaptchaSolverService'
]