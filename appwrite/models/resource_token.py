from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
        if 'resourceId' not in data and 'resourceid' not in data:
            data['resourceId'] = ''
        if 'resourceType' not in data and 'resourcetype' not in data:
            data['resourceType'] = ''
        if 'expire' not in data:
            data['expire'] = ''
        if 'secret' not in data:
            data['secret'] = ''
        if 'accessedAt' not in data and 'accessedat' not in data:
            data['accessedAt'] = ''
        return data
