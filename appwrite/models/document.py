from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class Document(AppwriteModel):
    """
    Document

    Attributes
    ----------
    id : str
        Document ID.
    sequence : float
        Document sequence ID.
    collectionid : str
        Collection ID.
    databaseid : str
        Database ID.
    createdat : str
        Document creation date in ISO 8601 format.
    updatedat : str
        Document update date in ISO 8601 format.
    permissions : List[Any]
        Document permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    """
    id: str = Field(..., alias='$id')
    sequence: float = Field(..., alias='$sequence')
    collectionid: str = Field(..., alias='$collectionId')
    databaseid: str = Field(..., alias='$databaseId')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
