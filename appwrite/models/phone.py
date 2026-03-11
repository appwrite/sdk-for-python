from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
