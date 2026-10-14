from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'key' not in data:
            data['key'] = ''
        if 'type' not in data:
            data['type'] = ''
        if 'error' not in data:
            data['error'] = ''
        if 'required' not in data:
            data['required'] = False
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'relationType' not in data and 'relationtype' not in data:
            data['relationType'] = ''
        if 'twoWay' not in data and 'twoway' not in data:
            data['twoWay'] = False
        if 'twoWayKey' not in data and 'twowaykey' not in data:
            data['twoWayKey'] = ''
        if 'onDelete' not in data and 'ondelete' not in data:
            data['onDelete'] = 'restrict'
        if 'side' not in data:
            data['side'] = ''
        return data
