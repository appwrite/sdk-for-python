from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class OAuth2Keycloak(AppwriteModel):
    """
    OAuth2Keycloak

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    clientid : str
        Keycloak OAuth2 client ID.
    clientsecret : str
        Keycloak OAuth2 client secret.
    endpoint : str
        Keycloak OAuth2 endpoint domain.
    realmname : str
        Keycloak OAuth2 realm name.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    endpoint: str = Field(..., alias='endpoint')
    realmname: str = Field(..., alias='realmName')

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
        if 'clientId' not in data and 'clientid' not in data:
            data['clientId'] = ''
        if 'clientSecret' not in data and 'clientsecret' not in data:
            data['clientSecret'] = ''
        if 'endpoint' not in data:
            data['endpoint'] = ''
        if 'realmName' not in data and 'realmname' not in data:
            data['realmName'] = ''
        return data
