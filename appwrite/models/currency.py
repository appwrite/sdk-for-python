from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Currency(AppwriteModel):
    """
    Currency

    Attributes
    ----------
    symbol : str
        Currency symbol.
    name : str
        Currency name.
    symbolnative : str
        Currency native symbol.
    decimaldigits : float
        Number of decimal digits.
    rounding : float
        Currency digit rounding.
    code : str
        Currency code in [ISO 4217-1](http://en.wikipedia.org/wiki/ISO_4217) three-character format.
    nameplural : str
        Currency plural name
    """

    symbol: str = Field(..., alias='symbol')
    name: str = Field(..., alias='name')
    symbolnative: str = Field(..., alias='symbolNative')
    decimaldigits: float = Field(..., alias='decimalDigits')
    rounding: float = Field(..., alias='rounding')
    code: str = Field(..., alias='code')
    nameplural: str = Field(..., alias='namePlural')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'symbol' not in data:
            data['symbol'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'symbolNative' not in data and 'symbolnative' not in data:
            data['symbolNative'] = ''
        if 'decimalDigits' not in data and 'decimaldigits' not in data:
            data['decimalDigits'] = 0
        if 'rounding' not in data:
            data['rounding'] = 0
        if 'code' not in data:
            data['code'] = ''
        if 'namePlural' not in data and 'nameplural' not in data:
            data['namePlural'] = ''
        return data
