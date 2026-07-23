from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .app_installation import AppInstallation

class AppInstallationList(AppwriteModel):
    """
    App installations list

    Attributes
    ----------
    total : float
        Total number of installations that matched your query.
    installations : List[AppInstallation]
        List of installations.
    """
    total: float = Field(..., alias='total')
    installations: List[AppInstallation] = Field(..., alias='installations')
