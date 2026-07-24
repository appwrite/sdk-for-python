from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .app_key import AppKey

class AppKeyList(AppwriteModel):
    """
    App keys list

    Attributes
    ----------
    total : float
        Total number of keys that matched your query.
    keys : List[AppKey]
        List of keys.
    """
    total: float = Field(..., alias='total')
    keys: List[AppKey] = Field(..., alias='keys')
