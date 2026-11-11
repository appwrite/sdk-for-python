from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Environment(AppwriteModel):
    """
    Environment

    Attributes
    ----------
    id : str
        Environment ID, as passed in the X-Appwrite-Environment header.
    createdat : str
        Environment creation date in ISO 8601 format.
    updatedat : str
        Environment update date in ISO 8601 format.
    projectid : str
        ID of the project the environment belongs to, as passed in the X-Appwrite-Project header.
    name : str
        Environment name.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    projectid: str = Field(..., alias='projectId')
    name: str = Field(..., alias='name')

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
        if 'projectId' not in data and 'projectid' not in data:
            data['projectId'] = ''
        if 'name' not in data:
            data['name'] = ''
        return data
