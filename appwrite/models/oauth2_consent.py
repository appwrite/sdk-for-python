from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Oauth2Consent(AppwriteModel):
    """
    OAuth2 Consent

    Attributes
    ----------
    id : str
        Consent ID.
    createdat : str
        Consent creation time in ISO 8601 format.
    updatedat : str
        Consent update date in ISO 8601 format.
    userid : str
        ID of the user the consent belongs to.
    appid : str
        ID of the registered app the consent was given to. Empty for URL-form (CIMD) clients.
    cimdurl : str
        Client ID metadata document URL of the client the consent was given to. Empty for registered apps.
    scopes : List[Any]
        OAuth2 scopes the user consented to.
    resources : List[Any]
        RFC 8707 resource indicators the user consented to.
    authorizationdetails : str
        Authorization details the user consented to, as a JSON string. Each entry has a `type` plus project-defined fields.
    expire : str
        Consent expiration time in ISO 8601 format. Empty when the consent has no token-bound expiry yet.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    userid: str = Field(..., alias='userId')
    appid: str = Field(..., alias='appId')
    cimdurl: str = Field(..., alias='cimdUrl')
    scopes: List[Any] = Field(..., alias='scopes')
    resources: List[Any] = Field(..., alias='resources')
    authorizationdetails: str = Field(..., alias='authorizationDetails')
    expire: str = Field(..., alias='expire')
