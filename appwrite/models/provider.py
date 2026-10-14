from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Provider(AppwriteModel):
    """
    Provider

    Attributes
    ----------
    id : str
        Provider ID.
    createdat : str
        Provider creation time in ISO 8601 format.
    updatedat : str
        Provider update date in ISO 8601 format.
    name : str
        The name for the provider instance.
    provider : str
        The name of the provider service.
    enabled : bool
        Is provider enabled?
    type : str
        Type of provider.
    credentials : Dict[str, Any]
        Provider credentials.
    options : Optional[Dict[str, Any]]
        Provider options.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    provider: str = Field(..., alias='provider')
    enabled: bool = Field(..., alias='enabled')
    type: str = Field(..., alias='type')
    credentials: Dict[str, Any] = Field(..., alias='credentials')
    options: Optional[Dict[str, Any]] = Field(default=None, alias='options')

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
        if 'provider' not in data:
            data['provider'] = ''
        if 'enabled' not in data:
            data['enabled'] = True
        if 'type' not in data:
            data['type'] = ''
        if 'credentials' not in data:
            data['credentials'] = []
        return data
