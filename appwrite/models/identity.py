from typing import Any, Dict, List, Optional, Union

from pydantic import Field

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
