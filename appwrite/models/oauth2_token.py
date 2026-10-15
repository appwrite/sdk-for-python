from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Oauth2Token(AppwriteModel):
    """
    OAuth2 Token

    Attributes
    ----------
    access_token : str
        OAuth2 access token.
    token_type : str
        OAuth2 token type.
    expires_in : float
        Access token lifetime in seconds.
    refresh_token : str
        OAuth2 refresh token.
    scope : str
        Space-separated scopes granted to the access token.
    authorization_details : Optional[str]
        Granted RFC 9396 authorization details as a JSON string.
    id_token : Optional[str]
        OpenID Connect ID token. Returned when the `openid` scope is granted.
    """

    access_token: str = Field(..., alias='access_token')
    token_type: str = Field(..., alias='token_type')
    expires_in: float = Field(..., alias='expires_in')
    refresh_token: str = Field(..., alias='refresh_token')
    scope: str = Field(..., alias='scope')
    authorization_details: Optional[str] = Field(default=None, alias='authorization_details')
    id_token: Optional[str] = Field(default=None, alias='id_token')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'access_token' not in data:
            data['access_token'] = ''
        if 'token_type' not in data:
            data['token_type'] = 'Bearer'
        if 'expires_in' not in data:
            data['expires_in'] = 0
        if 'refresh_token' not in data:
            data['refresh_token'] = ''
        if 'scope' not in data:
            data['scope'] = ''
        return data
