from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .identity import Identity


class IdentityList(AppwriteModel):
    """
    Identities List

    Attributes
    ----------
    total : float
        Total number of identities that matched your query.
    identities : List[Identity]
        List of identities.
    """

    total: float = Field(..., alias='total')
    identities: List[Identity] = Field(..., alias='identities')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
