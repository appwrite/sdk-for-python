from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .dedicated_database import DedicatedDatabase


class DedicatedDatabaseList(AppwriteModel):
    """
    Dedicated databases list

    Attributes
    ----------
    total : float
        Total number of databases that matched your query.
    databases : List[DedicatedDatabase]
        List of databases.
    """

    total: float = Field(..., alias='total')
    databases: List[DedicatedDatabase] = Field(..., alias='databases')
