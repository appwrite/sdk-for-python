from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.video_output import VideoOutput


class VideoCodec(AppwriteModel):
    """
    Video codec

    Attributes
    ----------
    id : str
        Codec ID.
    name : str
        Codec display name.
    outputs : List[VideoOutput]
        Streaming output formats this codec may be packaged into.
    """

    id: str = Field(..., alias='$id')
    name: str = Field(..., alias='name')
    outputs: List[VideoOutput] = Field(..., alias='outputs')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'outputs' not in data:
            data['outputs'] = []
        return data
