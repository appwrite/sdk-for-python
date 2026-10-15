from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Identity(AppwriteModel):
    """
    Identity

    Attributes
    ----------
    id : str
        Identity ID.
    createdat : str
        Identity creation date in ISO 8601 format.
    updatedat : str
        Identity update date in ISO 8601 format.
    userid : str
        User ID.
    provider : str
        Identity Provider.
    provideruid : str
        ID of the User in the Identity Provider.
    provideremail : str
        Email of the User in the Identity Provider.
    provideraccesstoken : str
        Identity Provider Access Token.
    provideraccesstokenexpiry : str
        The date of when the access token expires in ISO 8601 format.
    providerrefreshtoken : str
        Identity Provider Refresh Token.
    provideridtoken : str
        Identity Provider ID token (JWT) from the most recent native sign-in. Empty for identities created through the browser OAuth2 flow.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    userid: str = Field(..., alias='userId')
    provider: str = Field(..., alias='provider')
    provideruid: str = Field(..., alias='providerUid')
    provideremail: str = Field(..., alias='providerEmail')
    provideraccesstoken: str = Field(..., alias='providerAccessToken')
    provideraccesstokenexpiry: str = Field(..., alias='providerAccessTokenExpiry')
    providerrefreshtoken: str = Field(..., alias='providerRefreshToken')
    provideridtoken: str = Field(..., alias='providerIdToken')

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
        if 'provider' not in data:
            data['provider'] = ''
        if 'providerUid' not in data and 'provideruid' not in data:
            data['providerUid'] = ''
        if 'providerEmail' not in data and 'provideremail' not in data:
            data['providerEmail'] = ''
        if 'providerAccessToken' not in data and 'provideraccesstoken' not in data:
            data['providerAccessToken'] = ''
        if 'providerAccessTokenExpiry' not in data and 'provideraccesstokenexpiry' not in data:
            data['providerAccessTokenExpiry'] = ''
        if 'providerRefreshToken' not in data and 'providerrefreshtoken' not in data:
            data['providerRefreshToken'] = ''
        if 'providerIdToken' not in data and 'provideridtoken' not in data:
            data['providerIdToken'] = ''
        return data
