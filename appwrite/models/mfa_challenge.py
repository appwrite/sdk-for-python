from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class MfaChallenge(AppwriteModel):
    """
    MFA Challenge

    Attributes
    ----------
    id : str
        Token ID.
    createdat : str
        Token creation date in ISO 8601 format.
    userid : str
        User ID.
    expire : str
        Token expiration date in ISO 8601 format.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    userid: str = Field(..., alias='userId')
    expire: str = Field(..., alias='expire')
