from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .key import Key

class KeyList(AppwriteModel):
    """
    API Keys List

    Attributes
    ----------
    total : float
        Total number of keys that matched your query.
    keys : List[Key]
        List of keys.
    """
    total: float = Field(..., alias='total')
    keys: List[Key] = Field(..., alias='keys')
