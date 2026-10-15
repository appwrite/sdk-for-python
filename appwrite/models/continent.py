from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Continent(AppwriteModel):
    """
    Continent

    Attributes
    ----------
    name : str
        Continent name.
    code : str
        Continent two letter code.
    """

    name: str = Field(..., alias='name')
    code: str = Field(..., alias='code')

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
        return data
