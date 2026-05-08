from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
