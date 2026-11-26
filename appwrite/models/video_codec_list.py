from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .video_codec import VideoCodec


class VideoCodecList(AppwriteModel):
    """
    Video Codecs List

    Attributes
    ----------
    total : float
        Total number of codecs that matched your query.
    codecs : List[VideoCodec]
        List of codecs.
    """

    total: float = Field(..., alias='total')
    codecs: List[VideoCodec] = Field(..., alias='codecs')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'codecs' not in data:
            data['codecs'] = []
        return data
