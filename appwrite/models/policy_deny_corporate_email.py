from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class PolicyDenyCorporateEmail(AppwriteModel):
    """
    Policy Deny Corporate Email

    Attributes
    ----------
    id : str
        Policy ID.
    enabled : bool
        Whether the deny non-corporate email policy is enabled.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')

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
        return data
