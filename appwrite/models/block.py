from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Block(AppwriteModel):
    """
    Block

    Attributes
    ----------
    createdat : str
        Block creation date in ISO 8601 format.
    resourcetype : str
        Resource type that is blocked
    resourceid : str
        Resource identifier that is blocked
    reason : Optional[str]
        Reason for the block. Can be null if no reason was provided.
    expiredat : Optional[str]
        Block expiration date in ISO 8601 format. Can be null if the block does not expire.
    """
    createdat: str = Field(..., alias='$createdAt')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
    reason: Optional[str] = Field(default=None, alias='reason')
    expiredat: Optional[str] = Field(default=None, alias='expiredAt')
