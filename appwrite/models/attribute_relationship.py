from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.attribute_status import AttributeStatus

class AttributeRelationship(AppwriteModel):
    """
    AttributeRelationship

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
    relatedcollection : str
        The ID of the related collection.
    relationtype : str
        The type of the relationship.
    twoway : bool
        Is the relationship two-way?
    twowaykey : str
        The key of the two-way relationship.
    ondelete : str
        How deleting the parent document will propagate to child documents.
    side : str
        Whether this is the parent or child side of the relationship
    """
    key: str = Field(..., alias='key')
    type: str = Field(..., alias='type')
    status: AttributeStatus = Field(..., alias='status')
    error: str = Field(..., alias='error')
    required: bool = Field(..., alias='required')
    array: Optional[bool] = Field(default=None, alias='array')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    relatedcollection: str = Field(..., alias='relatedCollection')
    relationtype: str = Field(..., alias='relationType')
    twoway: bool = Field(..., alias='twoWay')
    twowaykey: str = Field(..., alias='twoWayKey')
    ondelete: str = Field(..., alias='onDelete')
    side: str = Field(..., alias='side')
