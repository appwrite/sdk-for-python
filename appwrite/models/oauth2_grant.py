from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Oauth2Grant(AppwriteModel):
    """
    OAuth2 Grant

    Attributes
    ----------
    id : str
        Grant ID.
    createdat : str
        Grant creation time in ISO 8601 format.
    updatedat : str
        Grant update date in ISO 8601 format.
    userid : str
        ID of the user the grant belongs to.
    appid : str
        ID of the OAuth2 client (app) the grant was requested for.
    scopes : List[Any]
        Requested OAuth2 scopes the user is being asked to consent to.
    authorizationdetails : str
        Requested authorization_details the user is being asked to consent to, as a JSON string. Each entry has a `type` plus project-defined fields.
    prompt : str
        OIDC prompt directive the consent screen should honor. Space-separated list of: login, consent, select_account.
    redirecturi : str
        Redirect URI the user will be sent to after the flow completes.
    authtime : float
        Unix timestamp of when the user last authenticated.
    expire : str
        Grant expiration time in ISO 8601 format.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    userid: str = Field(..., alias='userId')
    appid: str = Field(..., alias='appId')
    scopes: List[Any] = Field(..., alias='scopes')
    authorizationdetails: str = Field(..., alias='authorizationDetails')
    prompt: str = Field(..., alias='prompt')
    redirecturi: str = Field(..., alias='redirectUri')
    authtime: float = Field(..., alias='authTime')
    expire: str = Field(..., alias='expire')
