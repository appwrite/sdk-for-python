from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .passkey import Passkey


class PasskeyList(AppwriteModel):
    """
    Passkeys List

    Attributes
    ----------
    total : float
        Total number of passkeys that matched your query.
    passkeys : List[Passkey]
        List of passkeys.
    """

    total: float = Field(..., alias='total')
    passkeys: List[Passkey] = Field(..., alias='passkeys')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
