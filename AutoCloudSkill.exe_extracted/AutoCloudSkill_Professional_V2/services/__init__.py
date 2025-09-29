"""
Services module __init__.py for AutoCloudSkill Professional.

Provides convenient imports for all service components.
"""

from .captcha_service import (
    CaptchaType,
    SolverEngine,
    CaptchaSolution,
    AudioCaptchaSolver,
    CaptchaSolverService
)

from .firefox_relay_service import (
    RelayStatus,
    EmailMask,
    EmailMessage,
    FirefoxRelayService
)

from .gmail_service import (
    EmailMessage as GmailMessage,
    GmailService,
    SCOPES as GMAIL_SCOPES
)

from .randomuser_service import (
    Gender,
    UserData,
    RandomUserService
)

from .genai_video_service import (
    VideoModel,
    ImageModel,
    AspectRatio,
    Resolution,
    GenerationRequest,
    GenerationResult,
    GenAIVideoService
)

from .video_postprocess_service import (
    VideoCodec,
    AudioCodec,
    Quality,
    ProcessingOptions,
    ProcessingResult,
    VideoPostprocessService
)

__all__ = [
    # Captcha Service
    'CaptchaType',
    'SolverEngine',
    'CaptchaSolution',
    'AudioCaptchaSolver',
    'CaptchaSolverService',

    # Firefox Relay Service
    'RelayStatus',
    'EmailMask',
    'EmailMessage',
    'FirefoxRelayService',

    # Gmail Service
    'GmailMessage',
    'GmailService',
    'GMAIL_SCOPES',

    # RandomUser Service
    'Gender',
    'UserData',
    'RandomUserService',

    # GenAI Video Service
    'VideoModel',
    'ImageModel',
    'AspectRatio',
    'Resolution',
    'GenerationRequest',
    'GenerationResult',
    'GenAIVideoService',

    # Video Postprocess Service
    'VideoCodec',
    'AudioCodec',
    'Quality',
    'ProcessingOptions',
    'ProcessingResult',
    'VideoPostprocessService'
]