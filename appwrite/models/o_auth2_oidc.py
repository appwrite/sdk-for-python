from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.o_auth2_oidc_prompt import OAuth2OidcPrompt

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
    prompt : List[OAuth2OidcPrompt]
        OpenID Connect prompt values controlling the authentication and consent screens.
    maxage : Optional[float]
        Maximum authentication age in seconds. When set, the user must have authenticated within this many seconds.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    wellknownurl: str = Field(..., alias='wellKnownURL')
    authorizationurl: str = Field(..., alias='authorizationURL')
    tokenurl: str = Field(..., alias='tokenURL')
    userinfourl: str = Field(..., alias='userInfoURL')
    prompt: List[OAuth2OidcPrompt] = Field(..., alias='prompt')
    maxage: Optional[float] = Field(default=None, alias='maxAge')
