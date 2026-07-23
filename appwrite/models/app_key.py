from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AppKey(AppwriteModel):
    """
    AppKey

    Attributes
    ----------
    id : str
        App key ID.
    createdat : str
        App key creation time in ISO 8601 format.
    updatedat : str
        App key update time in ISO 8601 format.
    appid : str
        Application ID this app key belongs to.
    secret : str
        App key secret.
    hint : str
        Last few characters of the app key secret, used to help identify it.
    createdbyid : str
        ID of the user who created the app key.
    createdbyname : str
        Name of the user who created the app key.
    lastaccessedat : Optional[str]
        Time the app key was last used for authentication in ISO 8601 format. Null if never used.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    appid: str = Field(..., alias='appId')
    secret: str = Field(..., alias='secret')
    hint: str = Field(..., alias='hint')
    createdbyid: str = Field(..., alias='createdById')
    createdbyname: str = Field(..., alias='createdByName')
    lastaccessedat: Optional[str] = Field(default=None, alias='lastAccessedAt')
