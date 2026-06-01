from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Presence(AppwriteModel):
    """
    Presence

    Attributes
    ----------
    id : str
        Presence ID.
    createdat : str
        Presence creation date in ISO 8601 format.
    updatedat : str
        Presence update date in ISO 8601 format.
    permissions : List[Any]
        Presence permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    userid : str
        User ID.
    status : Optional[str]
        Presence status.
    source : str
        Presence source.
    expiresat : Optional[str]
        Presence expiry date in ISO 8601 format.
    metadata : Optional[Dict[str, Any]]
        Presence metadata.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    userid: str = Field(..., alias='userId')
    status: Optional[str] = Field(default=None, alias='status')
    source: str = Field(..., alias='source')
    expiresat: Optional[str] = Field(default=None, alias='expiresAt')
    metadata: Optional[Dict[str, Any]] = Field(default=None, alias='metadata')
