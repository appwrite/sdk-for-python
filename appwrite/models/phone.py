from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Phone(AppwriteModel):
    """
    Phone

    Attributes
    ----------
    code : str
        Phone code.
    countrycode : str
        Country two-character ISO 3166-1 alpha code.
    countryname : str
        Country name.
    """

    code: str = Field(..., alias='code')
    countrycode: str = Field(..., alias='countryCode')
    countryname: str = Field(..., alias='countryName')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'code' not in data:
            data['code'] = ''
        if 'countryCode' not in data and 'countrycode' not in data:
            data['countryCode'] = ''
        if 'countryName' not in data and 'countryname' not in data:
            data['countryName'] = ''
        return data
