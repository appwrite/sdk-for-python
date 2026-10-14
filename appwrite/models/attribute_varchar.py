from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.attribute_status import AttributeStatus


class AttributeVarchar(AppwriteModel):
    """
    AttributeVarchar

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
    size : float
        Attribute size.
    default : Optional[str]
        Default value for attribute when not provided. Cannot be set when attribute is required.
    encrypt : Optional[bool]
        Defines whether this attribute is encrypted or not.
    """

    key: str = Field(..., alias='key')
    type: str = Field(..., alias='type')
    status: AttributeStatus = Field(..., alias='status')
    error: str = Field(..., alias='error')
    required: bool = Field(..., alias='required')
    array: Optional[bool] = Field(default=None, alias='array')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    size: float = Field(..., alias='size')
    default: Optional[str] = Field(default=None, alias='default')
    encrypt: Optional[bool] = Field(default=None, alias='encrypt')

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
        if 'size' not in data:
            data['size'] = 0
        return data
