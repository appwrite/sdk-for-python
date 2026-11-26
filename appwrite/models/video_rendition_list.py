from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .video_rendition import VideoRendition


class VideoRenditionList(AppwriteModel):
    """
    Video Renditions List

    Attributes
    ----------
    total : float
        Total number of renditions that matched your query.
    renditions : List[VideoRendition]
        List of renditions.
    """

    total: float = Field(..., alias='total')
    renditions: List[VideoRendition] = Field(..., alias='renditions')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'renditions' not in data:
            data['renditions'] = []
        return data
