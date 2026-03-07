from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class Row(AppwriteModel):
    """
    Row

    Attributes
    ----------
    id : str
        Row ID.
    sequence : float
        Row sequence ID.
    tableid : str
        Table ID.
    databaseid : str
        Database ID.
    createdat : str
        Row creation date in ISO 8601 format.
    updatedat : str
        Row update date in ISO 8601 format.
    permissions : List[Any]
        Row permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    """
    id: str = Field(..., alias='$id')
    sequence: float = Field(..., alias='$sequence')
    tableid: str = Field(..., alias='$tableId')
    databaseid: str = Field(..., alias='$databaseId')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
