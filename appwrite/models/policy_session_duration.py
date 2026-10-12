from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class PolicySessionDuration(AppwriteModel):
    """
    Policy Session Duration

    Attributes
    ----------
    id : str
        Policy ID.
    duration : float
        Session duration in seconds.
    """

    id: str = Field(..., alias='$id')
    duration: float = Field(..., alias='duration')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'duration' not in data:
            data['duration'] = 31536000
        return data
