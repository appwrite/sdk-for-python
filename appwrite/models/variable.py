from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class Variable(AppwriteModel):
    """
    Variable

    Attributes
    ----------
    id : str
        Variable ID.
    createdat : str
        Variable creation date in ISO 8601 format.
    updatedat : str
        Variable creation date in ISO 8601 format.
    key : str
        Variable key.
    value : str
        Variable value.
    secret : bool
        Variable secret flag. Secret variables can only be updated or deleted, but never read.
    resourcetype : str
        Service to which the variable belongs. Possible values are &quot;project&quot;, &quot;function&quot;
    resourceid : str
        ID of resource to which the variable belongs. If resourceType is &quot;project&quot;, it is empty. If resourceType is &quot;function&quot;, it is ID of the function.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    key: str = Field(..., alias='key')
    value: str = Field(..., alias='value')
    secret: bool = Field(..., alias='secret')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
