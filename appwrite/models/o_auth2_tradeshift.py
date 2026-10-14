from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class OAuth2Tradeshift(AppwriteModel):
    """
    OAuth2Tradeshift

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    oauth2clientid : str
        Tradeshift OAuth2 client ID.
    oauth2clientsecret : str
        Tradeshift OAuth2 client secret.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    oauth2clientid: str = Field(..., alias='oauth2ClientId')
    oauth2clientsecret: str = Field(..., alias='oauth2ClientSecret')

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
        if 'oauth2ClientId' not in data and 'oauth2clientid' not in data:
            data['oauth2ClientId'] = ''
        if 'oauth2ClientSecret' not in data and 'oauth2clientsecret' not in data:
            data['oauth2ClientSecret'] = ''
        return data
