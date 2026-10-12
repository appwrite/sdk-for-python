from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Passkey(AppwriteModel):
    """
    Passkey

    Attributes
    ----------
    id : str
        Passkey ID.
    createdat : str
        Passkey creation date in ISO 8601 format.
    updatedat : str
        Passkey update date in ISO 8601 format.
    name : str
        Passkey name.
    accessedat : str
        Most recent sign-in with this passkey in ISO 8601 format. Empty until the passkey is used to sign in.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
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
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'accessedAt' not in data and 'accessedat' not in data:
            data['accessedAt'] = ''
        return data
