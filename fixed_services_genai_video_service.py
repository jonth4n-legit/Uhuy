"""
GenAI Video Service: wrapper modular untuk Google Gen AI (Gemini API) video generation.
Menggunakan package `google-genai`.

Referensi:
- https://ai.google.dev/gemini-api/docs/video
- https://googleapis.github.io/python-genai/
"""
from __future__ import annotations
import time
from typing import Optional, Dict, Any
from google import genai
from google.genai import types

class GenAIVideoService:
    """Service pembungkus untuk operasi video/image melalui Google Gen AI SDK.

    Catatan API Key:
    - API key dioper dari GUI dan dibangun ke Client langsung via parameter `api_key`.
    """

    def __init__(self, api_key: Optional[str] = None):
        if api_key and api_key.strip():
            self.client = genai.Client(api_key=api_key.strip())
        else:
            self.client = genai.Client()

    def generate_image_with_imagen(self, prompt: str, imagen_model: str = 'imagen-4.0-generate-001') -> Any:
        """Generate image menggunakan Imagen 4 (Ultra) untuk keperluan image-to-video.

        Returns: objek image dari SDK (mis. imagen.generated_images[0].image)
        """
        resp = self.client.models.generate_images(model=imagen_model, prompt=prompt)
        if not getattr(resp, 'generated_images', None):
            raise RuntimeError('Imagen tidak mengembalikan gambar.')
        return resp.generated_images[0].image

    def generate_video(self, *, prompt: str, model: str = 'veo-3.0-generate-001', 
                      aspect_ratio: Optional[str] = None, negative_prompt: Optional[str] = None, 
                      image: Optional[Any] = None, resolution: Optional[str] = None, 
                      poll_interval: int = 10) -> Dict[str, Any]:
        """Generate video dan tunggu sampai selesai (poll operation).

        Returns: dict dengan informasi file/video dan path sementara SDK.
        """
        kwargs = {'model': model, 'prompt': prompt}
        
        if image is not None:
            kwargs['image'] = image
        
        cfg_kwargs = {}
        if negative_prompt:
            cfg_kwargs['negative_prompt'] = negative_prompt
        if aspect_ratio:
            cfg_kwargs['aspect_ratio'] = aspect_ratio
        if resolution:
            cfg_kwargs['resolution'] = resolution
        
        if cfg_kwargs:
            kwargs['config'] = types.GenerateVideosConfig(**cfg_kwargs)
        
        operation = self.client.models.generate_videos(**kwargs)
        
        while not getattr(operation, 'done', False):
            time.sleep(max(1, int(poll_interval)))
            operation = self.client.operations.get(operation)
        
        if not getattr(operation, 'response', None) or not getattr(operation.response, 'generated_videos', None):
            raise RuntimeError('Operasi selesai tetapi tidak ada video yang dihasilkan.')
        
        return {
            'operation': operation,
            'generated_video': operation.response.generated_videos[0],
            'generated_videos': operation.response.generated_videos
        }

    def download_video(self, generated_video: Any, output_path: str) -> str:
        """Download video hasil generate ke `output_path`.
        Returns: output_path
        """
        self.client.files.download(file=generated_video.video)
        generated_video.video.save(output_path)
        return output_path

    def download_videos(self, generated_videos: Any, output_paths: list[str]) -> list[str]:
        """Download banyak video ke path yang disediakan satu-per-satu.
        Panjang output_paths harus sama atau lebih besar dari jumlah generated_videos; jika lebih kecil,
        hanya sebanyak output_paths yang akan diunduh.
        Returns: daftar path yang berhasil diunduh.
        """
        saved = []
        for idx, gv in enumerate(generated_videos):
            if idx >= len(output_paths):
                break
            self.client.files.download(file=gv.video)
            gv.video.save(output_paths[idx])
            saved.append(output_paths[idx])
        return saved