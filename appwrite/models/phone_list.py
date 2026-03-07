from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .phone import Phone

class PhoneList(AppwriteModel):
    """
    Phones List

    Attributes
    ----------
    total : float
        Total number of phones that matched your query.
    phones : List[Phone]
        List of phones.
    """
    total: float = Field(..., alias='total')
    phones: List[Phone] = Field(..., alias='phones')
