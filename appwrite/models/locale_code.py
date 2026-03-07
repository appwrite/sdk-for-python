from typing import Any, Dict, List, Optional, Union

from pydantic import Field

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
