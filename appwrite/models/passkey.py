from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class Passkey(AppwriteModel):
    """
    Passkey

    Attributes
    ----------
    id : str
        Passkey ID.
    createdat : str
        Passkey creation date in ISO 8601 format.
    updatedat : str
        Passkey update date in ISO 8601 format.
    name : str
        Passkey name.
    accessedat : str
        Most recent sign-in with this passkey in ISO 8601 format. Empty until the passkey is used to sign in.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    accessedat: str = Field(..., alias='accessedAt')
