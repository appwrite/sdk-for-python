from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class PolicyAccountDevices(AppwriteModel):
    """
    Policy Account Devices

    Attributes
    ----------
    id : str
        Policy ID.
    enabled : bool
        Whether account devices are enabled. When disabled, new account devices can no longer be created.
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
            data['enabled'] = True
        return data
