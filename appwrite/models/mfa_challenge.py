from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class MfaChallenge(AppwriteModel):
    """
    MFA Challenge

    Attributes
    ----------
    id : str
        Token ID.
    createdat : str
        Token creation date in ISO 8601 format.
    userid : str
        User ID.
    expire : str
        Token expiration date in ISO 8601 format.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    userid: str = Field(..., alias='userId')
    expire: str = Field(..., alias='expire')

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
        if 'userId' not in data and 'userid' not in data:
            data['userId'] = ''
        if 'expire' not in data:
            data['expire'] = ''
        return data
