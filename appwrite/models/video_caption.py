from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.video_caption_status import VideoCaptionStatus


class VideoCaption(AppwriteModel):
    """
    Video caption

    Attributes
    ----------
    id : str
        Caption ID.
    createdat : str
        Caption creation time in ISO 8601 format.
    updatedat : str
        Caption update date in ISO 8601 format.
    videoid : str
        Video ID.
    bucketid : str
        Storage bucket ID holding the caption file.
    fileid : str
        Caption file ID.
    name : str
        Caption display name.
    language : str
        Caption ISO 639-2 language code.
    default : bool
        Is this the default caption track?
    embedded : bool
        Was this track auto-extracted from the source container? Extracted tracks have no backing file; extraction runs once per video, so a deleted extracted track is not re-created.
    targetduration : float
        Longest segment duration in seconds.
    status : VideoCaptionStatus
        Packaging status: one of `pending`, `started`, `ready`, `error` or `aborted`.
    error : str
        Why the caption failed or was aborted. Empty unless `status` is `error` or `aborted`.
    size : float
        Stored caption size in bytes.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    videoid: str = Field(..., alias='videoId')
    bucketid: str = Field(..., alias='bucketId')
    fileid: str = Field(..., alias='fileId')
    name: str = Field(..., alias='name')
    language: str = Field(..., alias='language')
    default: bool = Field(..., alias='default')
    embedded: bool = Field(..., alias='embedded')
    targetduration: float = Field(..., alias='targetDuration')
    status: VideoCaptionStatus = Field(..., alias='status')
    error: str = Field(..., alias='error')
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
        if 'bucketId' not in data and 'bucketid' not in data:
            data['bucketId'] = ''
        if 'fileId' not in data and 'fileid' not in data:
            data['fileId'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'language' not in data:
            data['language'] = ''
        if 'default' not in data:
            data['default'] = False
        if 'embedded' not in data:
            data['embedded'] = False
        if 'targetDuration' not in data and 'targetduration' not in data:
            data['targetDuration'] = 0
        if 'status' not in data:
            data['status'] = 'pending'
        if 'error' not in data:
            data['error'] = ''
        if 'size' not in data:
            data['size'] = 0
        return data
