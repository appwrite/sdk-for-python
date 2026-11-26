from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.video_rendition_status import VideoRenditionStatus
from ..enums.video_output import VideoOutput
from ..enums.video_codec_id import VideoCodecId


class VideoRendition(AppwriteModel):
    """
    Video rendition

    Attributes
    ----------
    id : str
        Rendition ID.
    createdat : str
        Rendition creation time in ISO 8601 format.
    updatedat : str
        Rendition update date in ISO 8601 format.
    videoid : str
        Video ID.
    profileid : str
        Video profile ID this rendition was encoded against.
    name : str
        Rendition name, derived from its dimensions and bitrate.
    startedat : str
        Transcoding start time in ISO 8601 format.
    endedat : str
        Transcoding end time in ISO 8601 format.
    width : float
        Rendition width in pixels.
    height : float
        Rendition height in pixels.
    videobitrate : float
        Video bitrate in bits per second.
    audiobitrate : float
        Audio bitrate in bits per second.
    targetduration : float
        Longest segment duration in seconds.
    status : VideoRenditionStatus
        Transcoding status: one of `pending`, `started`, `ended`, `ready`, `error` or `aborted`.
    error : str
        Why the rendition failed or was aborted. Empty unless `status` is `error` or `aborted`.
    progress : float
        Transcoding progress as a percentage, from 0 to 100.
    output : VideoOutput
        Streaming output format: `hls`, `dash`, or `cmaf`.
    codec : VideoCodecId
        Video encode codec snapshotted from the profile at create time: one of `h264`, `hevc`, or `vp9`.
    size : float
        Stored rendition size in bytes.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    videoid: str = Field(..., alias='videoId')
    profileid: str = Field(..., alias='profileId')
    name: str = Field(..., alias='name')
    startedat: str = Field(..., alias='startedAt')
    endedat: str = Field(..., alias='endedAt')
    width: float = Field(..., alias='width')
    height: float = Field(..., alias='height')
    videobitrate: float = Field(..., alias='videoBitRate')
    audiobitrate: float = Field(..., alias='audioBitRate')
    targetduration: float = Field(..., alias='targetDuration')
    status: VideoRenditionStatus = Field(..., alias='status')
    error: str = Field(..., alias='error')
    progress: float = Field(..., alias='progress')
    output: VideoOutput = Field(..., alias='output')
    codec: VideoCodecId = Field(..., alias='codec')
    size: float = Field(..., alias='size')

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
        if 'videoId' not in data and 'videoid' not in data:
            data['videoId'] = ''
        if 'profileId' not in data and 'profileid' not in data:
            data['profileId'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'startedAt' not in data and 'startedat' not in data:
            data['startedAt'] = ''
        if 'endedAt' not in data and 'endedat' not in data:
            data['endedAt'] = ''
        if 'width' not in data:
            data['width'] = 0
        if 'height' not in data:
            data['height'] = 0
        if 'videoBitRate' not in data and 'videobitrate' not in data:
            data['videoBitRate'] = 0
        if 'audioBitRate' not in data and 'audiobitrate' not in data:
            data['audioBitRate'] = 0
        if 'targetDuration' not in data and 'targetduration' not in data:
            data['targetDuration'] = 0
        if 'status' not in data:
            data['status'] = 'pending'
        if 'error' not in data:
            data['error'] = ''
        if 'progress' not in data:
            data['progress'] = 0
        if 'output' not in data:
            data['output'] = 'hls'
        if 'codec' not in data:
            data['codec'] = 'h264'
        if 'size' not in data:
            data['size'] = 0
        return data
