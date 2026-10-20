from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class PolicyPasswordPersonalData(AppwriteModel):
    """
    Policy Password Personal Data

    Attributes
    ----------
    id : str
        Policy ID.
    enabled : bool
        Whether password personal data policy is enabled.
    denylist : List[Any]
        Custom terms blocked by case-insensitive substring matching when enabled.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    denylist: List[Any] = Field(..., alias='denyList')

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
        if 'denyList' not in data and 'denylist' not in data:
            data['denyList'] = []
        return data
