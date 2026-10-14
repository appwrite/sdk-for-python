from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class LocaleCode(AppwriteModel):
    """
    LocaleCode

    Attributes
    ----------
    code : str
        Locale codes in [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)
    name : str
        Locale name
    """

    code: str = Field(..., alias='code')
    name: str = Field(..., alias='name')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'code' not in data:
            data['code'] = ''
        if 'name' not in data:
            data['name'] = ''
        return data
