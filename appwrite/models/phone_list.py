from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .phone import Phone


class PhoneList(AppwriteModel):
    """
    Phones List

    Attributes
    ----------
    total : float
        Total number of phones that matched your query.
    phones : List[Phone]
        List of phones.
    """

    total: float = Field(..., alias='total')
    phones: List[Phone] = Field(..., alias='phones')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'phones' not in data:
            data['phones'] = []
        return data
