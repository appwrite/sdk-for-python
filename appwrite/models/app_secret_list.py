from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .app_secret import AppSecret

class AppSecretList(AppwriteModel):
    """
    App secrets list

    Attributes
    ----------
    total : float
        Total number of secrets that matched your query.
    secrets : List[AppSecret]
        List of secrets.
    """
    total: float = Field(..., alias='total')
    secrets: List[AppSecret] = Field(..., alias='secrets')
