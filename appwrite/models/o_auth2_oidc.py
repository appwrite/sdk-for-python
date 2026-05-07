from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OAuth2Oidc(AppwriteModel):
    """
    OAuth2Oidc

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    clientid : str
        OpenID Connect OAuth2 client ID.
    clientsecret : str
        OpenID Connect OAuth2 client secret.
    wellknownurl : str
        OpenID Connect well-known configuration URL. When set, authorization, token, and user info endpoints can be discovered automatically.
    authorizationurl : str
        OpenID Connect authorization endpoint URL.
    tokenurl : str
        OpenID Connect token endpoint URL.
    userinfourl : str
        OpenID Connect user info endpoint URL.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    wellknownurl: str = Field(..., alias='wellKnownURL')
    authorizationurl: str = Field(..., alias='authorizationURL')
    tokenurl: str = Field(..., alias='tokenURL')
    userinfourl: str = Field(..., alias='userInfoURL')
