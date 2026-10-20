from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    description : str
        Optional description for the variable.
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
    description: str = Field(..., alias='description')
    value: str = Field(..., alias='value')
    secret: bool = Field(..., alias='secret')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'key' not in data:
            data['key'] = ''
        if 'description' not in data:
            data['description'] = ''
        if 'value' not in data:
            data['value'] = ''
        if 'secret' not in data:
            data['secret'] = False
        if 'resourceType' not in data and 'resourcetype' not in data:
            data['resourceType'] = ''
        if 'resourceId' not in data and 'resourceid' not in data:
            data['resourceId'] = ''
        return data
