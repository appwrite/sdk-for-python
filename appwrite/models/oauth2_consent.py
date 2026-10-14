from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'userId' not in data and 'userid' not in data:
            data['userId'] = ''
        if 'appId' not in data and 'appid' not in data:
            data['appId'] = ''
        if 'cimdUrl' not in data and 'cimdurl' not in data:
            data['cimdUrl'] = ''
        if 'scopes' not in data:
            data['scopes'] = []
        if 'resources' not in data:
            data['resources'] = []
        if 'authorizationDetails' not in data and 'authorizationdetails' not in data:
            data['authorizationDetails'] = '[]'
        if 'expire' not in data:
            data['expire'] = ''
        return data
