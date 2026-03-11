from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ResourceToken(AppwriteModel):
    """
    ResourceToken

    Attributes
    ----------
    id : str
        Token ID.
    createdat : str
        Token creation date in ISO 8601 format.
    resourceid : str
        Resource ID.
    resourcetype : str
        Resource type.
    expire : str
        Token expiration date in ISO 8601 format.
    secret : str
        JWT encoded string.
    accessedat : str
        Most recent access date in ISO 8601 format. This attribute is only updated again after 24 hours.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    resourceid: str = Field(..., alias='resourceId')
    resourcetype: str = Field(..., alias='resourceType')
    expire: str = Field(..., alias='expire')
    secret: str = Field(..., alias='secret')
    accessedat: str = Field(..., alias='accessedAt')
