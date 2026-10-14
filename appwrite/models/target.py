from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Target(AppwriteModel):
    """
    Target

    Attributes
    ----------
    id : str
        Target ID.
    createdat : str
        Target creation time in ISO 8601 format.
    updatedat : str
        Target update date in ISO 8601 format.
    name : str
        Target Name.
    userid : str
        User ID.
    providerid : Optional[str]
        Provider ID.
    providertype : str
        The target provider type. Can be one of the following: `email`, `sms` or `push`.
    identifier : str
        The target identifier.
    expired : bool
        Is the target expired.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    userid: str = Field(..., alias='userId')
    providerid: Optional[str] = Field(default=None, alias='providerId')
    providertype: str = Field(..., alias='providerType')
    identifier: str = Field(..., alias='identifier')
    expired: bool = Field(..., alias='expired')

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
        if 'userId' not in data and 'userid' not in data:
            data['userId'] = ''
        if 'providerType' not in data and 'providertype' not in data:
            data['providerType'] = ''
        if 'identifier' not in data:
            data['identifier'] = ''
        if 'expired' not in data:
            data['expired'] = False
        return data
