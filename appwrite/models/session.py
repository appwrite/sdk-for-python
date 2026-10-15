from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
        if 'expire' not in data:
            data['expire'] = ''
        if 'provider' not in data:
            data['provider'] = ''
        if 'providerUid' not in data and 'provideruid' not in data:
            data['providerUid'] = ''
        if 'providerAccessToken' not in data and 'provideraccesstoken' not in data:
            data['providerAccessToken'] = ''
        if 'providerAccessTokenExpiry' not in data and 'provideraccesstokenexpiry' not in data:
            data['providerAccessTokenExpiry'] = ''
        if 'providerRefreshToken' not in data and 'providerrefreshtoken' not in data:
            data['providerRefreshToken'] = ''
        if 'ip' not in data:
            data['ip'] = ''
        if 'osCode' not in data and 'oscode' not in data:
            data['osCode'] = ''
        if 'osName' not in data and 'osname' not in data:
            data['osName'] = ''
        if 'osVersion' not in data and 'osversion' not in data:
            data['osVersion'] = ''
        if 'clientType' not in data and 'clienttype' not in data:
            data['clientType'] = ''
        if 'clientCode' not in data and 'clientcode' not in data:
            data['clientCode'] = ''
        if 'clientName' not in data and 'clientname' not in data:
            data['clientName'] = ''
        if 'clientVersion' not in data and 'clientversion' not in data:
            data['clientVersion'] = ''
        if 'clientEngine' not in data and 'clientengine' not in data:
            data['clientEngine'] = ''
        if 'clientEngineVersion' not in data and 'clientengineversion' not in data:
            data['clientEngineVersion'] = ''
        if 'deviceName' not in data and 'devicename' not in data:
            data['deviceName'] = ''
        if 'deviceBrand' not in data and 'devicebrand' not in data:
            data['deviceBrand'] = ''
        if 'deviceModel' not in data and 'devicemodel' not in data:
            data['deviceModel'] = ''
        if 'countryCode' not in data and 'countrycode' not in data:
            data['countryCode'] = ''
        if 'countryName' not in data and 'countryname' not in data:
            data['countryName'] = ''
        if 'current' not in data:
            data['current'] = False
        if 'factors' not in data:
            data['factors'] = []
        if 'secret' not in data:
            data['secret'] = ''
        if 'mfaUpdatedAt' not in data and 'mfaupdatedat' not in data:
            data['mfaUpdatedAt'] = ''
        return data
