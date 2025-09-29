"""
Video Postprocess Service untuk processing video hasil generate
"""
import os
import logging
from pathlib import Path
from typing import List, Optional

logger = logging.getLogger(__name__)

class VideoPostprocessService:
    """Service untuk post-processing video hasil generate"""

    def __init__(self):
        self.logger = logger

    def remove_audio_inplace(self, video_path: str) -> bool:
        """
        Hapus audio dari video file secara in-place
        
        Args:
            video_path: Path ke video file
            
        Returns:
            True jika berhasil, False jika error
        """
        try:
            if not os.path.exists(video_path):
                self.logger.error(f'Video file not found: {video_path}')
                return False
            
            # Create temporary file
            temp_path = f"{video_path}.temp"
            
            # Use ffmpeg to remove audio
            import subprocess
            
            cmd = [
                'ffmpeg', '-i', video_path, 
                '-c:v', 'copy',  # Copy video stream without re-encoding
                '-an',           # Remove audio
                '-y',            # Overwrite output file
                temp_path
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Replace original with processed version
                os.replace(temp_path, video_path)
                self.logger.info(f'Successfully removed audio from: {video_path}')
                return True
            else:
                self.logger.error(f'FFmpeg error: {result.stderr}')
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                return False
                
        except Exception as e:
            self.logger.error(f'Error removing audio from video: {e}')
            return False

    def compress_video(self, video_path: str, output_path: str, quality: str = 'medium') -> bool:
        """
        Compress video untuk mengurangi ukuran file
        
        Args:
            video_path: Path ke video input
            output_path: Path ke video output
            quality: Quality level (low, medium, high)
            
        Returns:
            True jika berhasil, False jika error
        """
        try:
            if not os.path.exists(video_path):
                self.logger.error(f'Video file not found: {video_path}')
                return False
            
            # Quality settings
            quality_settings = {
                'low': ['-crf', '28', '-preset', 'fast'],
                'medium': ['-crf', '23', '-preset', 'medium'],
                'high': ['-crf', '18', '-preset', 'slow']
            }
            
            settings = quality_settings.get(quality, quality_settings['medium'])
            
            import subprocess
            
            cmd = [
                'ffmpeg', '-i', video_path,
                '-c:v', 'libx264',
                *settings,
                '-c:a', 'aac',
                '-y',
                output_path
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                self.logger.info(f'Successfully compressed video: {output_path}')
                return True
            else:
                self.logger.error(f'FFmpeg compression error: {result.stderr}')
                return False
                
        except Exception as e:
            self.logger.error(f'Error compressing video: {e}')
            return False

    def extract_frames(self, video_path: str, output_dir: str, fps: float = 1.0) -> List[str]:
        """
        Extract frames dari video sebagai gambar
        
        Args:
            video_path: Path ke video file
            output_dir: Directory untuk menyimpan frames
            fps: Frames per second untuk extract
            
        Returns:
            List path ke frame files yang berhasil diextract
        """
        try:
            if not os.path.exists(video_path):
                self.logger.error(f'Video file not found: {video_path}')
                return []
            
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)
            
            import subprocess
            
            # Extract frames
            cmd = [
                'ffmpeg', '-i', video_path,
                '-vf', f'fps={fps}',
                '-y',
                str(output_path / 'frame_%04d.png')
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Get list of extracted frames
                frames = list(output_path.glob('frame_*.png'))
                frames.sort()
                
                self.logger.info(f'Successfully extracted {len(frames)} frames from: {video_path}')
                return [str(f) for f in frames]
            else:
                self.logger.error(f'FFmpeg frame extraction error: {result.stderr}')
                return []
                
        except Exception as e:
            self.logger.error(f'Error extracting frames: {e}')
            return []

    def get_video_info(self, video_path: str) -> Optional[Dict]:
        """
        Get informasi video (duration, resolution, bitrate, etc.)
        
        Args:
            video_path: Path ke video file
            
        Returns:
            Dict dengan informasi video atau None jika error
        """
        try:
            if not os.path.exists(video_path):
                self.logger.error(f'Video file not found: {video_path}')
                return None
            
            import subprocess
            
            cmd = [
                'ffprobe', '-v', 'quiet',
                '-print_format', 'json',
                '-show_format',
                '-show_streams',
                video_path
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                import json
                info = json.loads(result.stdout)
                
                # Extract useful information
                video_info = {
                    'duration': float(info['format']['duration']),
                    'size': int(info['format']['size']),
                    'bitrate': int(info['format']['bit_rate']),
                    'format_name': info['format']['format_name']
                }
                
                # Get video stream info
                for stream in info['streams']:
                    if stream['codec_type'] == 'video':
                        video_info.update({
                            'width': stream['width'],
                            'height': stream['height'],
                            'codec': stream['codec_name'],
                            'fps': eval(stream['r_frame_rate'])
                        })
                        break
                
                return video_info
            else:
                self.logger.error(f'FFprobe error: {result.stderr}')
                return None
                
        except Exception as e:
            self.logger.error(f'Error getting video info: {e}')
            return None