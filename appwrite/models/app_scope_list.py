from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .app_scope import AppScope

class AppScopeList(AppwriteModel):
    """
    App scopes list

    Attributes
    ----------
    total : float
        Total number of scopes that matched your query.
    scopes : List[AppScope]
        List of scopes.
    """
    total: float = Field(..., alias='total')
    scopes: List[AppScope] = Field(..., alias='scopes')
