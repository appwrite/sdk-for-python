from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Oauth2ConsentToken(AppwriteModel):
    """
    OAuth2 Consent Token

    Attributes
    ----------
    id : str
        Token family ID.
    createdat : str
        Token creation time in ISO 8601 format.
    updatedat : str
        Token update date in ISO 8601 format. Refreshing the token family updates this.
    consentid : str
        ID of the consent the token family was issued under.
    userid : str
        ID of the user the token family belongs to.
    appid : str
        ID of the registered app the token family was issued to. Empty for URL-form (CIMD) clients.
    cimdurl : str
        Client ID metadata document URL of the client the token family was issued to. Empty for registered apps.
    scopes : List[Any]
        OAuth2 scopes granted on the token family.
    resources : List[Any]
        RFC 8707 resource indicators granted on the token family.
    authorizationdetails : str
        Authorization details granted on the token family, as a JSON string. Each entry has a `type` plus project-defined fields.
    expire : str
        Expiration time of the current access token of this family in ISO 8601 format.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    consentid: str = Field(..., alias='consentId')
    userid: str = Field(..., alias='userId')
    appid: str = Field(..., alias='appId')
    cimdurl: str = Field(..., alias='cimdUrl')
    scopes: List[Any] = Field(..., alias='scopes')
    resources: List[Any] = Field(..., alias='resources')
    authorizationdetails: str = Field(..., alias='authorizationDetails')
    expire: str = Field(..., alias='expire')
