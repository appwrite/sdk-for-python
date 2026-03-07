from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from ..enums.attribute_status import AttributeStatus

class AttributeIp(AppwriteModel):
    """
    AttributeIP

    Attributes
    ----------
    key : str
        Attribute Key.
    type : str
        Attribute type.
    status : AttributeStatus
        Attribute status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    error : str
        Error message. Displays error generated on failure of creating or deleting an attribute.
    required : bool
        Is attribute required?
    array : Optional[bool]
        Is attribute an array?
    createdat : str
        Attribute creation date in ISO 8601 format.
    updatedat : str
        Attribute update date in ISO 8601 format.
    format : str
        String format.
    default : Optional[str]
        Default value for attribute when not provided. Cannot be set when attribute is required.
    """
    key: str = Field(..., alias='key')
    type: str = Field(..., alias='type')
    status: AttributeStatus = Field(..., alias='status')
    error: str = Field(..., alias='error')
    required: bool = Field(..., alias='required')
    array: Optional[bool] = Field(default=None, alias='array')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    format: str = Field(..., alias='format')
    default: Optional[str] = Field(default=None, alias='default')
