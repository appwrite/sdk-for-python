from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .video_profile import VideoProfile


class VideoProfileList(AppwriteModel):
    """
    Video Profiles List

    Attributes
    ----------
    total : float
        Total number of profiles that matched your query.
    profiles : List[VideoProfile]
        List of profiles.
    """

    total: float = Field(..., alias='total')
    profiles: List[VideoProfile] = Field(..., alias='profiles')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'profiles' not in data:
            data['profiles'] = []
        return data
