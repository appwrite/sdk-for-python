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
    mode : str
        Block mode. full blocks reads and writes; readOnly blocks writes only.
    reason : Optional[str]
        Reason for the block. Can be null if no reason was provided.
    expiredat : Optional[str]
        Block expiration date in ISO 8601 format. Can be null if the block does not expire.
    projectname : str
        Name of the project this block applies to.
    region : str
        Region of the project this block applies to.
    organizationname : str
        Name of the organization that owns the project.
    organizationid : str
        ID of the organization that owns the project.
    billingplan : str
        Billing plan of the organization that owns the project.
    """
    createdat: str = Field(..., alias='$createdAt')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
    mode: str = Field(..., alias='mode')
    reason: Optional[str] = Field(default=None, alias='reason')
    expiredat: Optional[str] = Field(default=None, alias='expiredAt')
    projectname: str = Field(..., alias='projectName')
    region: str = Field(..., alias='region')
    organizationname: str = Field(..., alias='organizationName')
    organizationid: str = Field(..., alias='organizationId')
    billingplan: str = Field(..., alias='billingPlan')
