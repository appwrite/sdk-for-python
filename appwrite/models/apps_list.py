from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .app import App

class AppsList(AppwriteModel):
    """
    Apps list

    Attributes
    ----------
    total : float
        Total number of apps that matched your query.
    apps : List[App]
        List of apps.
    """
    total: float = Field(..., alias='total')
    apps: List[App] = Field(..., alias='apps')
