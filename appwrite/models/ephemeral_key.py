from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class EphemeralKey(AppwriteModel):
    """
    Ephemeral Key

    Attributes
    ----------
    id : str
        Key ID.
    createdat : str
        Key creation date in ISO 8601 format.
    updatedat : str
        Key update date in ISO 8601 format.
    name : str
        Key name.
    description : str
        Optional description for the key.
    expire : str
        Key expiration date in ISO 8601 format.
    scopes : List[Any]
        Allowed permission scopes.
    secret : str
        Secret key.
    accessedat : str
        Most recent access date in ISO 8601 format. This attribute is only updated again after 24 hours.
    sdks : List[Any]
        List of SDK user agents that used this key.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    description: str = Field(..., alias='description')
    expire: str = Field(..., alias='expire')
    scopes: List[Any] = Field(..., alias='scopes')
    secret: str = Field(..., alias='secret')
    accessedat: str = Field(..., alias='accessedAt')
    sdks: List[Any] = Field(..., alias='sdks')

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
        if 'name' not in data:
            data['name'] = ''
        if 'description' not in data:
            data['description'] = ''
        if 'expire' not in data:
            data['expire'] = ''
        if 'scopes' not in data:
            data['scopes'] = []
        if 'secret' not in data:
            data['secret'] = ''
        if 'accessedAt' not in data and 'accessedat' not in data:
            data['accessedAt'] = ''
        if 'sdks' not in data:
            data['sdks'] = []
        return data
