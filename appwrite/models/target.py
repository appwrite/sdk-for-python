from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Target(AppwriteModel):
    """
    Target

    Attributes
    ----------
    id : str
        Target ID.
    createdat : str
        Target creation time in ISO 8601 format.
    updatedat : str
        Target update date in ISO 8601 format.
    name : str
        Target Name.
    userid : str
        User ID.
    providerid : Optional[str]
        Provider ID.
    providertype : str
        The target provider type. Can be one of the following: `email`, `sms` or `push`.
    identifier : str
        The target identifier.
    expired : bool
        Is the target expired.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    userid: str = Field(..., alias='userId')
    providerid: Optional[str] = Field(default=None, alias='providerId')
    providertype: str = Field(..., alias='providerType')
    identifier: str = Field(..., alias='identifier')
    expired: bool = Field(..., alias='expired')
