from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .locale_code import LocaleCode


class LocaleCodeList(AppwriteModel):
    """
    Locale codes list

    Attributes
    ----------
    total : float
        Total number of localeCodes that matched your query.
    localecodes : List[LocaleCode]
        List of localeCodes.
    """

    total: float = Field(..., alias='total')
    localecodes: List[LocaleCode] = Field(..., alias='localeCodes')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
