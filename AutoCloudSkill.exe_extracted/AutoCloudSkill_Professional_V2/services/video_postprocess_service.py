"""
Professional video post-processing service for AutoCloudSkill.

This module provides comprehensive video processing capabilities:
- Audio removal and manipulation
- Video format conversion
- Quality adjustment and compression
- Professional ffmpeg integration
- Batch processing support

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import os
import subprocess
import tempfile
import logging
from pathlib import Path
from typing import Optional, Dict, Any, List, Union, Tuple
from dataclasses import dataclass
from enum import Enum
import shutil

from utils.logger import setup_application_logging, log_automation_step, performance_monitor
from config.settings import settings

logger = setup_application_logging('VideoPostprocessService')

class VideoCodec(Enum):
    """Video codec options."""
    H264 = "libx264"
    H265 = "libx265"
    VP9 = "libvpx-vp9"
    AV1 = "libaom-av1"
    COPY = "copy"

class AudioCodec(Enum):
    """Audio codec options."""
    AAC = "aac"
    MP3 = "libmp3lame"
    OPUS = "libopus"
    COPY = "copy"
    REMOVE = "remove"

class Quality(Enum):
    """Video quality presets."""
    VERY_FAST = "veryfast"
    FAST = "fast"
    MEDIUM = "medium"
    SLOW = "slow"
    VERY_SLOW = "veryslow"

@dataclass
class ProcessingOptions:
    """Video processing configuration."""
    video_codec: VideoCodec = VideoCodec.H264
    audio_codec: AudioCodec = AudioCodec.AAC
    quality_preset: Quality = Quality.FAST
    crf: int = 23  # Constant Rate Factor (0-51, lower = better quality)
    bitrate: Optional[str] = None  # e.g., "2M", "1000k"
    resolution: Optional[Tuple[int, int]] = None  # (width, height)
    framerate: Optional[int] = None
    remove_audio: bool = False
    trim_start: Optional[float] = None  # seconds
    trim_end: Optional[float] = None  # seconds

@dataclass
class ProcessingResult:
    """Video processing result."""
    success: bool
    output_path: Optional[str]
    original_size: int
    processed_size: int
    duration: float
    compression_ratio: float
    metadata: Dict[str, Any]
    error_message: Optional[str] = None

class VideoPostprocessService:
    """Professional video post-processing service."""

    def __init__(self, ffmpeg_path: Optional[str] = None):
        """
        Initialize video post-processing service.

        Args:
            ffmpeg_path: Custom path to ffmpeg executable
        """
        self.ffmpeg_path = ffmpeg_path or self._find_ffmpeg()
        self._temp_dir = Path(tempfile.gettempdir()) / 'autocloudskill_video'
        self._temp_dir.mkdir(exist_ok=True)

        logger.info(f"Video postprocess service initialized with ffmpeg: {self.ffmpeg_path}")

    def _find_ffmpeg(self) -> str:
        """
        Find ffmpeg executable.

        Returns:
            Path to ffmpeg executable

        Raises:
            RuntimeError: If ffmpeg is not found
        """
        try:
            # Try imageio-ffmpeg first
            import imageio_ffmpeg as iio_ffmpeg
            ffmpeg_path = iio_ffmpeg.get_ffmpeg_exe()
            if os.path.exists(ffmpeg_path):
                return ffmpeg_path
        except ImportError:
            pass

        # Try system PATH
        ffmpeg_candidates = ['ffmpeg', 'ffmpeg.exe']
        for candidate in ffmpeg_candidates:
            if shutil.which(candidate):
                return candidate

        # Check common installation paths
        common_paths = [
            r'C:\ffmpeg\bin\ffmpeg.exe',
            r'C:\Program Files\ffmpeg\bin\ffmpeg.exe',
            '/usr/bin/ffmpeg',
            '/usr/local/bin/ffmpeg'
        ]

        for path in common_paths:
            if os.path.exists(path):
                return path

        raise RuntimeError(
            "ffmpeg not found. Please install ffmpeg or imageio-ffmpeg package."
        )

    def _run_ffmpeg(
        self,
        command: List[str],
        input_path: Optional[str] = None
    ) -> subprocess.CompletedProcess:
        """
        Run ffmpeg command with proper error handling.

        Args:
            command: ffmpeg command arguments
            input_path: Input file path for validation

        Returns:
            Completed process object

        Raises:
            RuntimeError: If ffmpeg command fails
        """
        # Validate input file
        if input_path and not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")

        # Prepare command
        full_command = [self.ffmpeg_path] + command

        # Set creation flags for Windows to hide console
        creation_flags = 0
        if os.name == 'nt':
            creation_flags = subprocess.CREATE_NO_WINDOW

        try:
            logger.debug(f"Running ffmpeg command: {' '.join(command)}")

            result = subprocess.run(
                full_command,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=creation_flags,
                text=True
            )

            return result

        except subprocess.CalledProcessError as e:
            error_msg = f"ffmpeg failed: {e.stderr}"
            logger.error(error_msg)
            raise RuntimeError(error_msg) from e

    @performance_monitor("remove_audio")
    def remove_audio(
        self,
        input_path: str,
        output_path: Optional[str] = None,
        inplace: bool = False
    ) -> str:
        """
        Remove audio from video file.

        Args:
            input_path: Input video file path
            output_path: Output file path (optional)
            inplace: Replace original file

        Returns:
            Output file path

        Raises:
            FileNotFoundError: If input file doesn't exist
            RuntimeError: If processing fails
        """
        log_automation_step(
            logger,
            "remove_audio",
            "START",
            {"input_path": input_path, "inplace": inplace}
        )

        input_file = Path(input_path)
        if not input_file.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")

        # Determine output path
        if inplace:
            temp_output = self._temp_dir / f"{input_file.stem}_noaudio{input_file.suffix}"
            final_output = input_path
        else:
            if output_path:
                final_output = output_path
            else:
                final_output = str(input_file.parent / f"{input_file.stem}_noaudio{input_file.suffix}")
            temp_output = final_output

        try:
            # Build ffmpeg command
            command = [
                '-y',  # Overwrite output files
                '-i', str(input_file),  # Input file
                '-c:v', 'copy',  # Copy video stream without re-encoding
                '-an',  # Remove audio streams
                str(temp_output)
            ]

            # Run ffmpeg
            self._run_ffmpeg(command, str(input_file))

            # Move file if inplace
            if inplace:
                shutil.move(str(temp_output), final_output)

            log_automation_step(
                logger,
                "remove_audio",
                "SUCCESS",
                {"output_path": final_output}
            )

            logger.info(f"Audio removed: {final_output}")
            return final_output

        except Exception as e:
            # Cleanup temporary file
            if temp_output.exists():
                try:
                    temp_output.unlink()
                except Exception:
                    pass

            log_automation_step(
                logger,
                "remove_audio",
                "ERROR",
                {"error": str(e)}
            )

            raise

    @performance_monitor("process_video")
    def process_video(
        self,
        input_path: str,
        output_path: Optional[str] = None,
        options: Optional[ProcessingOptions] = None
    ) -> ProcessingResult:
        """
        Process video with comprehensive options.

        Args:
            input_path: Input video file path
            output_path: Output file path (optional)
            options: Processing options

        Returns:
            ProcessingResult with operation details
        """
        if options is None:
            options = ProcessingOptions()

        input_file = Path(input_path)
        if not input_file.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")

        # Determine output path
        if not output_path:
            suffix = "_processed"
            output_path = str(input_file.parent / f"{input_file.stem}{suffix}{input_file.suffix}")

        log_automation_step(
            logger,
            "process_video",
            "START",
            {
                "input_path": input_path,
                "output_path": output_path,
                "remove_audio": options.remove_audio
            }
        )

        import time
        start_time = time.time()
        original_size = input_file.stat().st_size

        try:
            # Build ffmpeg command
            command = ['-y', '-i', str(input_file)]

            # Video codec and quality settings
            if options.video_codec != VideoCodec.COPY:
                command.extend(['-c:v', options.video_codec.value])

                if options.video_codec in [VideoCodec.H264, VideoCodec.H265]:
                    command.extend(['-preset', options.quality_preset.value])
                    command.extend(['-crf', str(options.crf)])

                if options.bitrate:
                    command.extend(['-b:v', options.bitrate])

            else:
                command.extend(['-c:v', 'copy'])

            # Audio settings
            if options.remove_audio or options.audio_codec == AudioCodec.REMOVE:
                command.append('-an')
            elif options.audio_codec != AudioCodec.COPY:
                command.extend(['-c:a', options.audio_codec.value])
            else:
                command.extend(['-c:a', 'copy'])

            # Resolution
            if options.resolution:
                width, height = options.resolution
                command.extend(['-vf', f'scale={width}:{height}'])

            # Frame rate
            if options.framerate:
                command.extend(['-r', str(options.framerate)])

            # Trimming
            if options.trim_start is not None:
                command.extend(['-ss', str(options.trim_start)])

            if options.trim_end is not None:
                duration = options.trim_end - (options.trim_start or 0)
                command.extend(['-t', str(duration)])

            # Output file
            command.append(output_path)

            # Run ffmpeg
            self._run_ffmpeg(command, input_path)

            # Calculate results
            duration = time.time() - start_time
            processed_size = Path(output_path).stat().st_size
            compression_ratio = original_size / processed_size if processed_size > 0 else 1.0

            result = ProcessingResult(
                success=True,
                output_path=output_path,
                original_size=original_size,
                processed_size=processed_size,
                duration=duration,
                compression_ratio=compression_ratio,
                metadata={
                    'video_codec': options.video_codec.value,
                    'audio_codec': options.audio_codec.value if not options.remove_audio else 'removed',
                    'quality_preset': options.quality_preset.value,
                    'crf': options.crf
                }
            )

            log_automation_step(
                logger,
                "process_video",
                "SUCCESS",
                {
                    "output_path": output_path,
                    "compression_ratio": f"{compression_ratio:.2f}",
                    "duration": f"{duration:.2f}s"
                }
            )

            logger.info(f"Video processed: {output_path} (compression: {compression_ratio:.2f}x)")
            return result

        except Exception as e:
            duration = time.time() - start_time
            error_msg = str(e)

            result = ProcessingResult(
                success=False,
                output_path=None,
                original_size=original_size,
                processed_size=0,
                duration=duration,
                compression_ratio=1.0,
                metadata={},
                error_message=error_msg
            )

            log_automation_step(
                logger,
                "process_video",
                "ERROR",
                {"error": error_msg}
            )

            logger.error(f"Video processing failed: {error_msg}")
            return result

    def get_video_info(self, input_path: str) -> Dict[str, Any]:
        """
        Get video file information.

        Args:
            input_path: Video file path

        Returns:
            Dictionary with video metadata
        """
        try:
            command = [
                '-i', input_path,
                '-f', 'null',
                '-'
            ]

            result = self._run_ffmpeg(command, input_path)

            # Parse ffmpeg output for metadata
            # This is a simplified implementation
            metadata = {
                'file_path': input_path,
                'file_size': os.path.getsize(input_path),
                'format': 'unknown',
                'duration': 'unknown',
                'video_codec': 'unknown',
                'audio_codec': 'unknown',
                'resolution': 'unknown'
            }

            # Extract basic info from stderr (ffmpeg outputs info to stderr)
            output = result.stderr
            if 'Duration:' in output:
                duration_line = [line for line in output.split('\n') if 'Duration:' in line]
                if duration_line:
                    metadata['duration'] = duration_line[0].split('Duration:')[1].split(',')[0].strip()

            return metadata

        except Exception as e:
            logger.error(f"Failed to get video info: {e}")
            return {'error': str(e)}

    def batch_process(
        self,
        input_files: List[str],
        output_dir: Optional[str] = None,
        options: Optional[ProcessingOptions] = None
    ) -> List[ProcessingResult]:
        """
        Process multiple video files.

        Args:
            input_files: List of input file paths
            output_dir: Output directory (optional)
            options: Processing options

        Returns:
            List of ProcessingResult objects
        """
        results = []

        for i, input_file in enumerate(input_files):
            try:
                logger.info(f"Processing file {i + 1}/{len(input_files)}: {input_file}")

                # Determine output path
                if output_dir:
                    input_path = Path(input_file)
                    output_path = str(Path(output_dir) / f"{input_path.stem}_processed{input_path.suffix}")
                else:
                    output_path = None

                result = self.process_video(input_file, output_path, options)
                results.append(result)

            except Exception as e:
                logger.error(f"Failed to process {input_file}: {e}")
                results.append(ProcessingResult(
                    success=False,
                    output_path=None,
                    original_size=0,
                    processed_size=0,
                    duration=0.0,
                    compression_ratio=1.0,
                    metadata={},
                    error_message=str(e)
                ))

        successful = sum(1 for r in results if r.success)
        logger.info(f"Batch processing completed: {successful}/{len(input_files)} successful")

        return results

    def cleanup_temp_files(self) -> int:
        """
        Clean up temporary files.

        Returns:
            Number of files removed
        """
        try:
            removed_count = 0
            for file_path in self._temp_dir.glob("*"):
                try:
                    if file_path.is_file():
                        file_path.unlink()
                        removed_count += 1
                except Exception as e:
                    logger.warning(f"Failed to remove temp file {file_path}: {e}")

            if removed_count > 0:
                logger.info(f"Cleaned up {removed_count} temporary files")

            return removed_count

        except Exception as e:
            logger.error(f"Failed to cleanup temp files: {e}")
            return 0

    # Backward compatibility methods
    def remove_audio_inplace(self, input_path: str) -> str:
        """
        Remove audio in-place (backward compatibility).

        Args:
            input_path: Input video file path

        Returns:
            Output file path (same as input)
        """
        return self.remove_audio(input_path, inplace=True)

# Export commonly used items
__all__ = [
    'VideoCodec',
    'AudioCodec',
    'Quality',
    'ProcessingOptions',
    'ProcessingResult',
    'VideoPostprocessService'
]