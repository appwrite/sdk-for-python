from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Country(AppwriteModel):
    """
    Country

    Attributes
    ----------
    name : str
        Country name.
    code : str
        Country two-character ISO 3166-1 alpha code.
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
