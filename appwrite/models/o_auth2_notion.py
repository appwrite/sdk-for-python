from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class OAuth2Notion(AppwriteModel):
    """
    OAuth2Notion

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    oauthclientid : str
        Notion OAuth2 client ID.
    oauthclientsecret : str
        Notion OAuth2 client secret.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    oauthclientid: str = Field(..., alias='oauthClientId')
    oauthclientsecret: str = Field(..., alias='oauthClientSecret')

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
        if 'oauthClientId' not in data and 'oauthclientid' not in data:
            data['oauthClientId'] = ''
        if 'oauthClientSecret' not in data and 'oauthclientsecret' not in data:
            data['oauthClientSecret'] = ''
        return data
