from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .dedicated_database_restoration import DedicatedDatabaseRestoration


class DedicatedDatabaseRestorationList(AppwriteModel):
    """
    Dedicated database restorations list

    Attributes
    ----------
    total : float
        Total number of restorations that matched your query.
    restorations : List[DedicatedDatabaseRestoration]
        List of restorations.
    """

    total: float = Field(..., alias='total')
    restorations: List[DedicatedDatabaseRestoration] = Field(..., alias='restorations')
