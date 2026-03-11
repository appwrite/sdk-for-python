from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
