from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
