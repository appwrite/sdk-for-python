from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .language import Language


class LanguageList(AppwriteModel):
    """
    Languages List

    Attributes
    ----------
    total : float
        Total number of languages that matched your query.
    languages : List[Language]
        List of languages.
    """

    total: float = Field(..., alias='total')
    languages: List[Language] = Field(..., alias='languages')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
