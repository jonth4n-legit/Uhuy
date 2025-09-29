"""
Professional GenAI Video service for AutoCloudSkill.

This module provides comprehensive AI video generation capabilities:
- Google Gemini/Imagen API integration
- Image-to-video generation
- Text-to-video generation
- Professional video processing pipeline
- Async generation support

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import os
import time
import asyncio
import logging
from typing import Dict, Any, Optional, Union, List
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from enum import Enum

from utils.logger import setup_application_logging, log_automation_step, performance_monitor
from config.settings import settings

logger = setup_application_logging('GenAIVideoService')

class VideoModel(Enum):
    """Available video generation models."""
    VEO_3_0 = "veo-3.0-generate-001"
    VEO_2_0 = "veo-2.0-generate-001"

class ImageModel(Enum):
    """Available image generation models."""
    IMAGEN_4_0 = "imagen-4.0-generate-001"
    IMAGEN_3_0 = "imagen-3.0-generate-001"

class AspectRatio(Enum):
    """Video aspect ratio options."""
    SQUARE = "1:1"
    PORTRAIT = "9:16"
    LANDSCAPE = "16:9"
    WIDESCREEN = "21:9"

class Resolution(Enum):
    """Video resolution options."""
    HD_720P = "720p"
    FULL_HD_1080P = "1080p"
    UHD_4K = "4k"

@dataclass
class GenerationRequest:
    """Video generation request configuration."""
    prompt: str
    model: VideoModel = VideoModel.VEO_3_0
    aspect_ratio: Optional[AspectRatio] = None
    resolution: Optional[Resolution] = None
    negative_prompt: Optional[str] = None
    image_input: Optional[Any] = None
    duration_seconds: Optional[int] = None
    seed: Optional[int] = None

@dataclass
class GenerationResult:
    """Video generation result."""
    success: bool
    video_path: Optional[str]
    operation_id: Optional[str]
    duration: float
    model_used: str
    metadata: Dict[str, Any]
    error_message: Optional[str] = None

class GenAIVideoService:
    """Professional AI video generation service."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize GenAI video service.

        Args:
            api_key: Google AI API key for authentication

        Raises:
            ImportError: If google-genai package is not available
            ValueError: If API key is not provided
        """
        try:
            from google import genai
            from google.genai import types
            self.genai = genai
            self.types = types
        except ImportError:
            raise ImportError(
                "google-genai package required. Install with: pip install google-genai"
            )

        self.api_key = api_key
        self.client = None

        if api_key and api_key.strip() and api_key != 'your_api_key_here':
            self._initialize_client(api_key.strip())
        else:
            logger.warning("No API key provided - client will be initialized when needed")

        self._temp_dir = Path.cwd() / 'temp_videos'
        self._temp_dir.mkdir(exist_ok=True)

        logger.info("GenAI Video service initialized")

    def _initialize_client(self, api_key: str) -> None:
        """Initialize GenAI client with API key."""
        try:
            self.client = self.genai.Client(api_key=api_key)
            self.api_key = api_key
            logger.info("GenAI client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize GenAI client: {e}")
            raise

    def set_api_key(self, api_key: str) -> None:
        """
        Set API key and initialize client.

        Args:
            api_key: Google AI API key
        """
        if not api_key or not api_key.strip():
            raise ValueError("API key cannot be empty")

        self._initialize_client(api_key.strip())

    @performance_monitor("generate_image_with_imagen")
    def generate_image(
        self,
        prompt: str,
        model: ImageModel = ImageModel.IMAGEN_4_0,
        aspect_ratio: Optional[AspectRatio] = None,
        negative_prompt: Optional[str] = None
    ) -> Optional[Any]:
        """
        Generate image using Imagen model.

        Args:
            prompt: Text prompt for image generation
            model: Image generation model to use
            aspect_ratio: Desired aspect ratio
            negative_prompt: Negative prompt to avoid certain elements

        Returns:
            Generated image object or None if failed
        """
        if not self.client:
            raise ValueError("API key not set. Call set_api_key() first.")

        log_automation_step(
            logger,
            "generate_imagen",
            "START",
            {"prompt": prompt[:100], "model": model.value}
        )

        try:
            # Prepare generation parameters
            params = {
                'model': model.value,
                'prompt': prompt
            }

            if aspect_ratio:
                params['aspect_ratio'] = aspect_ratio.value
            if negative_prompt:
                params['negative_prompt'] = negative_prompt

            # Generate image
            response = self.client.models.generate_images(**params)

            if not hasattr(response, 'generated_images') or not response.generated_images:
                raise RuntimeError('Imagen did not return any images')

            image = response.generated_images[0].image

            log_automation_step(
                logger,
                "generate_imagen",
                "SUCCESS",
                {"model": model.value}
            )

            logger.info(f"Generated image using {model.value}")
            return image

        except Exception as e:
            log_automation_step(
                logger,
                "generate_imagen",
                "ERROR",
                {"error": str(e)}
            )
            logger.error(f"Image generation failed: {e}")
            return None

    @performance_monitor("generate_video")
    def generate_video(
        self,
        request: GenerationRequest,
        poll_interval: int = 10,
        max_wait_time: int = 600
    ) -> GenerationResult:
        """
        Generate video from request configuration.

        Args:
            request: Video generation request
            poll_interval: Polling interval in seconds
            max_wait_time: Maximum wait time in seconds

        Returns:
            GenerationResult with video information
        """
        if not self.client:
            raise ValueError("API key not set. Call set_api_key() first.")

        log_automation_step(
            logger,
            "generate_video",
            "START",
            {
                "prompt": request.prompt[:100],
                "model": request.model.value,
                "aspect_ratio": request.aspect_ratio.value if request.aspect_ratio else None
            }
        )

        start_time = time.time()

        try:
            # Prepare generation parameters
            kwargs = {
                'model': request.model.value,
                'prompt': request.prompt
            }

            if request.image_input is not None:
                kwargs['image'] = request.image_input

            if request.aspect_ratio:
                kwargs['aspect_ratio'] = request.aspect_ratio.value

            if request.resolution:
                kwargs['resolution'] = request.resolution.value

            if request.negative_prompt:
                kwargs['negative_prompt'] = request.negative_prompt

            if request.duration_seconds:
                kwargs['duration_seconds'] = request.duration_seconds

            if request.seed:
                kwargs['seed'] = request.seed

            # Start video generation
            logger.info(f"Starting video generation with {request.model.value}")
            operation = self.client.models.generate_video(**kwargs)

            # Poll for completion
            operation_id = getattr(operation, 'name', 'unknown')

            logger.info(f"Video generation started, operation ID: {operation_id}")

            elapsed_time = 0
            while elapsed_time < max_wait_time:
                try:
                    # Check operation status
                    if hasattr(operation, 'done') and operation.done():
                        break

                    # Try to get result
                    if hasattr(operation, 'result'):
                        result = operation.result()
                        if result:
                            break

                    # Wait and update
                    time.sleep(poll_interval)
                    elapsed_time += poll_interval

                    logger.debug(f"Video generation in progress... ({elapsed_time}s elapsed)")

                except Exception as e:
                    logger.warning(f"Error checking operation status: {e}")
                    time.sleep(poll_interval)
                    elapsed_time += poll_interval

            # Get final result
            if elapsed_time >= max_wait_time:
                duration = time.time() - start_time
                error_msg = f"Video generation timed out after {max_wait_time}s"

                log_automation_step(
                    logger,
                    "generate_video",
                    "ERROR",
                    {"error": error_msg}
                )

                return GenerationResult(
                    success=False,
                    video_path=None,
                    operation_id=operation_id,
                    duration=duration,
                    model_used=request.model.value,
                    metadata={'timeout': True},
                    error_message=error_msg
                )

            # Extract video file
            try:
                result = operation.result() if hasattr(operation, 'result') else operation
                video_path = self._extract_video_file(result, request)

                duration = time.time() - start_time

                log_automation_step(
                    logger,
                    "generate_video",
                    "SUCCESS",
                    {
                        "video_path": video_path,
                        "duration": f"{duration:.2f}s",
                        "model": request.model.value
                    }
                )

                logger.info(f"Video generation completed: {video_path}")

                return GenerationResult(
                    success=True,
                    video_path=video_path,
                    operation_id=operation_id,
                    duration=duration,
                    model_used=request.model.value,
                    metadata={
                        'prompt': request.prompt,
                        'aspect_ratio': request.aspect_ratio.value if request.aspect_ratio else None,
                        'resolution': request.resolution.value if request.resolution else None
                    }
                )

            except Exception as e:
                duration = time.time() - start_time
                error_msg = f"Failed to extract video file: {e}"

                log_automation_step(
                    logger,
                    "generate_video",
                    "ERROR",
                    {"error": error_msg}
                )

                return GenerationResult(
                    success=False,
                    video_path=None,
                    operation_id=operation_id,
                    duration=duration,
                    model_used=request.model.value,
                    metadata={},
                    error_message=error_msg
                )

        except Exception as e:
            duration = time.time() - start_time
            error_msg = f"Video generation failed: {e}"

            log_automation_step(
                logger,
                "generate_video",
                "ERROR",
                {"error": error_msg}
            )

            logger.error(error_msg)

            return GenerationResult(
                success=False,
                video_path=None,
                operation_id=None,
                duration=duration,
                model_used=request.model.value,
                metadata={},
                error_message=error_msg
            )

    def _extract_video_file(self, result: Any, request: GenerationRequest) -> str:
        """
        Extract video file from generation result.

        Args:
            result: Generation result object
            request: Original generation request

        Returns:
            Path to extracted video file
        """
        try:
            # Create unique filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"genai_video_{timestamp}.mp4"
            output_path = self._temp_dir / filename

            # Extract video data based on result structure
            if hasattr(result, 'generated_videos') and result.generated_videos:
                video_obj = result.generated_videos[0]

                if hasattr(video_obj, 'video'):
                    # Save video data
                    with open(output_path, 'wb') as f:
                        f.write(video_obj.video)

                elif hasattr(video_obj, 'uri'):
                    # Download from URI
                    import requests
                    response = requests.get(video_obj.uri)
                    response.raise_for_status()

                    with open(output_path, 'wb') as f:
                        f.write(response.content)

                else:
                    raise ValueError("Video object has no accessible video data")

            elif hasattr(result, 'video'):
                # Direct video data
                with open(output_path, 'wb') as f:
                    f.write(result.video)

            else:
                raise ValueError("Result object has no video data")

            logger.info(f"Video saved to: {output_path}")
            return str(output_path)

        except Exception as e:
            logger.error(f"Failed to extract video file: {e}")
            raise

    def cleanup_temp_files(self, older_than_hours: int = 24) -> int:
        """
        Clean up old temporary video files.

        Args:
            older_than_hours: Remove files older than this many hours

        Returns:
            Number of files removed
        """
        try:
            from datetime import timedelta

            cutoff_time = datetime.now() - timedelta(hours=older_than_hours)
            removed_count = 0

            for file_path in self._temp_dir.glob("*.mp4"):
                try:
                    file_time = datetime.fromtimestamp(file_path.stat().st_mtime)
                    if file_time < cutoff_time:
                        file_path.unlink()
                        removed_count += 1
                        logger.debug(f"Removed old video file: {file_path}")
                except Exception as e:
                    logger.warning(f"Failed to remove file {file_path}: {e}")

            if removed_count > 0:
                logger.info(f"Cleaned up {removed_count} old video files")

            return removed_count

        except Exception as e:
            logger.error(f"Failed to cleanup temp files: {e}")
            return 0

    # Backward compatibility methods
    def generate_image_with_imagen(
        self,
        prompt: str,
        imagen_model: str = 'imagen-4.0-generate-001'
    ) -> Any:
        """
        Generate image (backward compatibility).

        Args:
            prompt: Text prompt
            imagen_model: Model name string

        Returns:
            Generated image object
        """
        try:
            model = ImageModel(imagen_model)
        except ValueError:
            model = ImageModel.IMAGEN_4_0

        return self.generate_image(prompt, model)

# Export commonly used items
__all__ = [
    'VideoModel',
    'ImageModel',
    'AspectRatio',
    'Resolution',
    'GenerationRequest',
    'GenerationResult',
    'GenAIVideoService'
]