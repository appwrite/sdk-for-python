from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .video_caption import VideoCaption


class VideoCaptionList(AppwriteModel):
    """
    Video Captions List

    Attributes
    ----------
    total : float
        Total number of captions that matched your query.
    captions : List[VideoCaption]
        List of captions.
    """

    total: float = Field(..., alias='total')
    captions: List[VideoCaption] = Field(..., alias='captions')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'captions' not in data:
            data['captions'] = []
        return data
