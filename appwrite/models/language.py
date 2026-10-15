from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Language(AppwriteModel):
    """
    Language

    Attributes
    ----------
    name : str
        Language name.
    code : str
        Language two-character ISO 639-1 codes.
    nativename : str
        Language native name.
    """

    name: str = Field(..., alias='name')
    code: str = Field(..., alias='code')
    nativename: str = Field(..., alias='nativeName')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'name' not in data:
            data['name'] = ''
        if 'code' not in data:
            data['code'] = ''
        if 'nativeName' not in data and 'nativename' not in data:
            data['nativeName'] = ''
        return data
