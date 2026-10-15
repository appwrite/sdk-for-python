from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .app_key import AppKey


class AppKeyList(AppwriteModel):
    """
    App keys list

    Attributes
    ----------
    total : float
        Total number of keys that matched your query.
    keys : List[AppKey]
        List of keys.
    """

    total: float = Field(..., alias='total')
    keys: List[AppKey] = Field(..., alias='keys')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'keys' not in data:
            data['keys'] = []
        return data
