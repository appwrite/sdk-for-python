from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .video import Video


class VideoList(AppwriteModel):
    """
    Videos List

    Attributes
    ----------
    total : float
        Total number of videos that matched your query.
    videos : List[Video]
        List of videos.
    """

    total: float = Field(..., alias='total')
    videos: List[Video] = Field(..., alias='videos')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'videos' not in data:
            data['videos'] = []
        return data
