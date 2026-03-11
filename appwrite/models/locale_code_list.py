from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .locale_code import LocaleCode

class LocaleCodeList(AppwriteModel):
    """
    Locale codes list

    Attributes
    ----------
    total : float
        Total number of localeCodes that matched your query.
    localecodes : List[LocaleCode]
        List of localeCodes.
    """
    total: float = Field(..., alias='total')
    localecodes: List[LocaleCode] = Field(..., alias='localeCodes')
