from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Session(AppwriteModel):
    """
    Session

    Attributes
    ----------
    id : str
        Session ID.
    createdat : str
        Session creation date in ISO 8601 format.
    updatedat : str
        Session update date in ISO 8601 format.
    userid : str
        User ID.
    expire : str
        Session expiration date in ISO 8601 format.
    provider : str
        Session Provider.
    provideruid : str
        Session Provider User ID.
    provideraccesstoken : str
        Session Provider Access Token.
    provideraccesstokenexpiry : str
        The date of when the access token expires in ISO 8601 format.
    providerrefreshtoken : str
        Session Provider Refresh Token.
    ip : str
        IP in use when the session was created.
    oscode : str
        Operating system code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/os.json).
    osname : str
        Operating system name.
    osversion : str
        Operating system version.
    clienttype : str
        Client type.
    clientcode : str
        Client code name. View list of [available options](https://github.com/appwrite/appwrite/blob/master/docs/lists/clients.json).
    clientname : str
        Client name.
    clientversion : str
        Client version.
    clientengine : str
        Client engine name.
    clientengineversion : str
        Client engine name.
    devicename : str
        Device name.
    devicebrand : str
        Device brand name.
    devicemodel : str
        Device model name.
    countrycode : str
        Country two-character ISO 3166-1 alpha code.
    countryname : str
        Country name.
    current : bool
        Returns true if this the current user session.
    factors : List[Any]
        Returns a list of active session factors.
    secret : str
        Secret used to authenticate the user. Only included if the request was made with an API key
    mfaupdatedat : str
        Most recent date in ISO 8601 format when the session successfully passed MFA challenge.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    userid: str = Field(..., alias='userId')
    expire: str = Field(..., alias='expire')
    provider: str = Field(..., alias='provider')
    provideruid: str = Field(..., alias='providerUid')
    provideraccesstoken: str = Field(..., alias='providerAccessToken')
    provideraccesstokenexpiry: str = Field(..., alias='providerAccessTokenExpiry')
    providerrefreshtoken: str = Field(..., alias='providerRefreshToken')
    ip: str = Field(..., alias='ip')
    oscode: str = Field(..., alias='osCode')
    osname: str = Field(..., alias='osName')
    osversion: str = Field(..., alias='osVersion')
    clienttype: str = Field(..., alias='clientType')
    clientcode: str = Field(..., alias='clientCode')
    clientname: str = Field(..., alias='clientName')
    clientversion: str = Field(..., alias='clientVersion')
    clientengine: str = Field(..., alias='clientEngine')
    clientengineversion: str = Field(..., alias='clientEngineVersion')
    devicename: str = Field(..., alias='deviceName')
    devicebrand: str = Field(..., alias='deviceBrand')
    devicemodel: str = Field(..., alias='deviceModel')
    countrycode: str = Field(..., alias='countryCode')
    countryname: str = Field(..., alias='countryName')
    current: bool = Field(..., alias='current')
    factors: List[Any] = Field(..., alias='factors')
    secret: str = Field(..., alias='secret')
    mfaupdatedat: str = Field(..., alias='mfaUpdatedAt')
