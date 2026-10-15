from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class OAuth2Bitbucket(AppwriteModel):
    """
    OAuth2Bitbucket

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    key : str
        Bitbucket OAuth2 key.
    secret : str
        Bitbucket OAuth2 secret.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    key: str = Field(..., alias='key')
    secret: str = Field(..., alias='secret')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'enabled' not in data:
            data['enabled'] = False
        if 'key' not in data:
            data['key'] = ''
        if 'secret' not in data:
            data['secret'] = ''
        return data
