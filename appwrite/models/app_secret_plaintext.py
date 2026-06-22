from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AppSecretPlaintext(AppwriteModel):
    """
    AppSecretPlaintext

    Attributes
    ----------
    id : str
        Secret ID.
    createdat : str
        Secret creation time in ISO 8601 format.
    updatedat : str
        Secret update time in ISO 8601 format.
    appid : str
        Application ID this secret belongs to.
    secret : str
        Application client secret. Returned in full only when the secret is created; subsequent reads return a masked value.
    hint : str
        Last few characters of the client secret, used to help identify it.
    createdbyid : str
        ID of the user who created the secret.
    createdbyname : str
        Name of the user who created the secret.
    lastaccessedat : Optional[str]
        Time the secret was last used for authentication in ISO 8601 format. Null if never used.
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
