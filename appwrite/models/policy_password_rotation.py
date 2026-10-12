from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class PolicyPasswordRotation(AppwriteModel):
    """
    Policy Password Rotation

    Attributes
    ----------
    id : str
        Policy ID.
    enabled : bool
        Whether expired passwords require a reset before email/password sign-in.
    maxage : float
        Maximum password age in seconds.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    maxage: float = Field(..., alias='maxAge')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'enabled' not in data:
            data['enabled'] = False
        if 'maxAge' not in data and 'maxage' not in data:
            data['maxAge'] = 31536000
        return data
