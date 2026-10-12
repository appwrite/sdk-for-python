from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'userId' not in data and 'userid' not in data:
            data['userId'] = ''
        if 'source' not in data:
            data['source'] = ''
        return data
