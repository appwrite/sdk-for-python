from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OAuth2Okta(AppwriteModel):
    """
    OAuth2Okta

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    clientid : str
        Okta OAuth2 client ID.
    clientsecret : str
        Okta OAuth2 client secret.
    domain : str
        Okta OAuth2 domain.
    authorizationserverid : str
        Okta OAuth2 authorization server ID.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    domain: str = Field(..., alias='domain')
    authorizationserverid: str = Field(..., alias='authorizationServerId')
