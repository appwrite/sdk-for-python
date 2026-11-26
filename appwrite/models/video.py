from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.video_timeline_status import VideoTimelineStatus


class Video(AppwriteModel):
    """
    Video

    Attributes
    ----------
    id : str
        Video ID.
    createdat : str
        Video creation time in ISO 8601 format.
    updatedat : str
        Video update date in ISO 8601 format.
    permissions : List[Any]
        Video permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    bucketid : str
        Storage bucket ID holding the source file.
    fileid : str
        Source file ID.
    name : str
        Video name.
    size : float
        Source file size in bytes.
    format : str
        Container format.
    duration : float
        Video duration in milliseconds.
    width : float
        Video width in pixels.
    height : float
        Video height in pixels.
    aspectratio : str
        Video aspect ratio.
    videocodec : str
        Video codec.
    videoformat : str
        Video format.
    videoformatprofile : str
        Video format profile.
    videobitrate : float
        Video bitrate in bits per second.
    videoframerate : float
        Video frame rate in frames per second.
    videoframeratemode : str
        Video frame rate mode.
    audiocodec : str
        Audio codec.
    audioformat : str
        Audio format.
    audiobitrate : float
        Audio bitrate in bits per second.
    audiosamplerate : float
        Audio sample rate in hertz.
    timelinestatus : VideoTimelineStatus
        Thumbnail timeline job status: one of `pending`, `started`, `ready`, `skipped` (source has no video track) or `error`.
    timelineerror : str
        Why the timeline job failed. Empty unless `timelineStatus` is `error`.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    bucketid: str = Field(..., alias='bucketId')
    fileid: str = Field(..., alias='fileId')
    name: str = Field(..., alias='name')
    size: float = Field(..., alias='size')
    format: str = Field(..., alias='format')
    duration: float = Field(..., alias='duration')
    width: float = Field(..., alias='width')
    height: float = Field(..., alias='height')
    aspectratio: str = Field(..., alias='aspectRatio')
    videocodec: str = Field(..., alias='videoCodec')
    videoformat: str = Field(..., alias='videoFormat')
    videoformatprofile: str = Field(..., alias='videoFormatProfile')
    videobitrate: float = Field(..., alias='videoBitRate')
    videoframerate: float = Field(..., alias='videoFrameRate')
    videoframeratemode: str = Field(..., alias='videoFrameRateMode')
    audiocodec: str = Field(..., alias='audioCodec')
    audioformat: str = Field(..., alias='audioFormat')
    audiobitrate: float = Field(..., alias='audioBitRate')
    audiosamplerate: float = Field(..., alias='audioSampleRate')
    timelinestatus: VideoTimelineStatus = Field(..., alias='timelineStatus')
    timelineerror: str = Field(..., alias='timelineError')

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
        if '$permissions' not in data and 'permissions' not in data:
            data['$permissions'] = []
        if 'bucketId' not in data and 'bucketid' not in data:
            data['bucketId'] = ''
        if 'fileId' not in data and 'fileid' not in data:
            data['fileId'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'size' not in data:
            data['size'] = 0
        if 'format' not in data:
            data['format'] = ''
        if 'duration' not in data:
            data['duration'] = 0
        if 'width' not in data:
            data['width'] = 0
        if 'height' not in data:
            data['height'] = 0
        if 'aspectRatio' not in data and 'aspectratio' not in data:
            data['aspectRatio'] = ''
        if 'videoCodec' not in data and 'videocodec' not in data:
            data['videoCodec'] = ''
        if 'videoFormat' not in data and 'videoformat' not in data:
            data['videoFormat'] = ''
        if 'videoFormatProfile' not in data and 'videoformatprofile' not in data:
            data['videoFormatProfile'] = ''
        if 'videoBitRate' not in data and 'videobitrate' not in data:
            data['videoBitRate'] = 0
        if 'videoFrameRate' not in data and 'videoframerate' not in data:
            data['videoFrameRate'] = 0
        if 'videoFrameRateMode' not in data and 'videoframeratemode' not in data:
            data['videoFrameRateMode'] = ''
        if 'audioCodec' not in data and 'audiocodec' not in data:
            data['audioCodec'] = ''
        if 'audioFormat' not in data and 'audioformat' not in data:
            data['audioFormat'] = ''
        if 'audioBitRate' not in data and 'audiobitrate' not in data:
            data['audioBitRate'] = 0
        if 'audioSampleRate' not in data and 'audiosamplerate' not in data:
            data['audioSampleRate'] = 0
        if 'timelineStatus' not in data and 'timelinestatus' not in data:
            data['timelineStatus'] = 'pending'
        if 'timelineError' not in data and 'timelineerror' not in data:
            data['timelineError'] = ''
        return data
