from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    expiredat : Optional[str]
        Block expiration date in ISO 8601 format. Can be null if the block does not expire.
    """

    createdat: str = Field(..., alias='$createdAt')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
    mode: str = Field(..., alias='mode')
    expiredat: Optional[str] = Field(default=None, alias='expiredAt')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if 'resourceType' not in data and 'resourcetype' not in data:
            data['resourceType'] = ''
        if 'resourceId' not in data and 'resourceid' not in data:
            data['resourceId'] = ''
        if 'mode' not in data:
            data['mode'] = 'full'
        return data
