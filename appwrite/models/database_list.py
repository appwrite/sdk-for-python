from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .database import Database

class DatabaseList(AppwriteModel):
    """
    Databases List

    Attributes
    ----------
    total : float
        Total number of databases that matched your query.
    databases : List[Database]
        List of databases.
    """
    total: float = Field(..., alias='total')
    databases: List[Database] = Field(..., alias='databases')
