from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DevKey(AppwriteModel):
    """
    DevKey

    Attributes
    ----------
    id : str
        Key ID.
    createdat : str
        Key creation date in ISO 8601 format.
    updatedat : str
        Key update date in ISO 8601 format.
    name : str
        Key name.
    expire : str
        Key expiration date in ISO 8601 format.
    secret : str
        Secret key.
    accessedat : str
        Most recent access date in ISO 8601 format. This attribute is only updated again after 24 hours.
    sdks : List[Any]
        List of SDK user agents that used this key.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    expire: str = Field(..., alias='expire')
    secret: str = Field(..., alias='secret')
    accessedat: str = Field(..., alias='accessedAt')
    sdks: List[Any] = Field(..., alias='sdks')
