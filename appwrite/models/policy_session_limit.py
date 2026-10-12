from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class PolicySessionLimit(AppwriteModel):
    """
    Policy Session Limit

    Attributes
    ----------
    id : str
        Policy ID.
    total : float
        Maximum number of sessions allowed per user. A value of 0 means the policy is disabled.
    """

    id: str = Field(..., alias='$id')
    total: float = Field(..., alias='total')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'total' not in data:
            data['total'] = 0
        return data
