from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    prompt : List[OAuth2OidcPrompt]
        OpenID Connect prompt values controlling the authentication and consent screens.
    wellknownurl : str
        OpenID Connect well-known configuration URL. When set, authorization, token, and user info endpoints can be discovered automatically.
    authorizationurl : str
        OpenID Connect authorization endpoint URL.
    tokenurl : str
        OpenID Connect token endpoint URL.
    userinfourl : str
        OpenID Connect user info endpoint URL.
    maxage : Optional[float]
        Maximum authentication age in seconds. When set, the user must have authenticated within this many seconds.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    prompt: List[OAuth2OidcPrompt] = Field(..., alias='prompt')
    wellknownurl: str = Field(..., alias='wellKnownURL')
    authorizationurl: str = Field(..., alias='authorizationURL')
    tokenurl: str = Field(..., alias='tokenURL')
    userinfourl: str = Field(..., alias='userInfoURL')
    maxage: Optional[float] = Field(default=None, alias='maxAge')

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
        if 'prompt' not in data:
            data['prompt'] = []
        if 'wellKnownURL' not in data and 'wellknownurl' not in data:
            data['wellKnownURL'] = ''
        if 'authorizationURL' not in data and 'authorizationurl' not in data:
            data['authorizationURL'] = ''
        if 'tokenURL' not in data and 'tokenurl' not in data:
            data['tokenURL'] = ''
        if 'userInfoURL' not in data and 'userinfourl' not in data:
            data['userInfoURL'] = ''
        return data
