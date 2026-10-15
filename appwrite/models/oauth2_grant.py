from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    resources : List[Any]
        Requested RFC 8707 resource indicators the user is being asked to consent to.
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
    resources: List[Any] = Field(..., alias='resources')
    authorizationdetails: str = Field(..., alias='authorizationDetails')
    prompt: str = Field(..., alias='prompt')
    redirecturi: str = Field(..., alias='redirectUri')
    authtime: float = Field(..., alias='authTime')
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
        if 'scopes' not in data:
            data['scopes'] = []
        if 'resources' not in data:
            data['resources'] = []
        if 'authorizationDetails' not in data and 'authorizationdetails' not in data:
            data['authorizationDetails'] = '[]'
        if 'prompt' not in data:
            data['prompt'] = ''
        if 'redirectUri' not in data and 'redirecturi' not in data:
            data['redirectUri'] = ''
        if 'authTime' not in data and 'authtime' not in data:
            data['authTime'] = 0
        if 'expire' not in data:
            data['expire'] = ''
        return data
