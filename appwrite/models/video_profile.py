from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.video_codec_id import VideoCodecId


class VideoProfile(AppwriteModel):
    """
    Video profile

    Attributes
    ----------
    id : str
        Video profile ID.
    createdat : str
        Video profile creation time in ISO 8601 format.
    updatedat : str
        Video profile update date in ISO 8601 format.
    name : str
        Video profile name.
    codec : VideoCodecId
        Video encode codec: one of `h264`, `hevc`, or `vp9`.
    videobitrate : float
        Target video bitrate in bits per second.
    audiobitrate : float
        Target audio bitrate in bits per second.
    width : float
        Target video width in pixels.
    height : float
        Target video height in pixels.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    codec: VideoCodecId = Field(..., alias='codec')
    videobitrate: float = Field(..., alias='videoBitRate')
    audiobitrate: float = Field(..., alias='audioBitRate')
    width: float = Field(..., alias='width')
    height: float = Field(..., alias='height')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'codec' not in data:
            data['codec'] = 'h264'
        if 'videoBitRate' not in data and 'videobitrate' not in data:
            data['videoBitRate'] = 0
        if 'audioBitRate' not in data and 'audiobitrate' not in data:
            data['audioBitRate'] = 0
        if 'width' not in data:
            data['width'] = 0
        if 'height' not in data:
            data['height'] = 0
        return data
