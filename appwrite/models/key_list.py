from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .key import Key


class KeyList(AppwriteModel):
    """
    API Keys List

    Attributes
    ----------
    total : float
        Total number of keys that matched your query.
    keys : List[Key]
        List of keys.
    """

    total: float = Field(..., alias='total')
    keys: List[Key] = Field(..., alias='keys')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
