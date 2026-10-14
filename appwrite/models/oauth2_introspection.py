from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class Oauth2Introspection(AppwriteModel):
    """
    OAuth2 Introspection

    Attributes
    ----------
    active : bool
        Whether the token is currently active. An inactive token carries no other claims (RFC 7662).
    token_use : Optional[str]
        Kind of token that was introspected. Can be one of: `access_token` or `refresh_token`.
    token_type : Optional[str]
        OAuth2 token type.
    scope : Optional[str]
        Space-separated scopes granted to the token.
    client_id : Optional[str]
        OAuth2 client ID the token was issued to.
    sub : Optional[str]
        ID of the user who authorized the token.
    aud : Optional[List[Any]]
        Audiences the token is intended for. The first entry is the project API base URL; any further entries are the resource indicators requested at authorization time (RFC 8707).
    iss : Optional[str]
        Issuer URL of the token.
    exp : Optional[float]
        Expiration time as a Unix timestamp in seconds.
    iat : Optional[float]
        Issued-at time as a Unix timestamp in seconds.
    jti : Optional[str]
        Unique identifier of the token.
    authorization_details : Optional[List[Any]]
        Granted RFC 9396 authorization details, restricted to what the user can currently access.
    """

    active: bool = Field(..., alias='active')
    token_use: Optional[str] = Field(default=None, alias='token_use')
    token_type: Optional[str] = Field(default=None, alias='token_type')
    scope: Optional[str] = Field(default=None, alias='scope')
    client_id: Optional[str] = Field(default=None, alias='client_id')
    sub: Optional[str] = Field(default=None, alias='sub')
    aud: Optional[List[Any]] = Field(default=None, alias='aud')
    iss: Optional[str] = Field(default=None, alias='iss')
    exp: Optional[float] = Field(default=None, alias='exp')
    iat: Optional[float] = Field(default=None, alias='iat')
    jti: Optional[str] = Field(default=None, alias='jti')
    authorization_details: Optional[List[Any]] = Field(default=None, alias='authorization_details')
