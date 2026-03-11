from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Log(AppwriteModel):
    """
    Log

    Attributes
    ----------
    event : str
        Event name.
    userid : str
        User ID.
    useremail : str
        User Email.
    username : str
        User Name.
    mode : str
        API mode when event triggered.
    ip : str
        IP session in use when the session was created.
    time : str
        Log creation date in ISO 8601 format.
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
    """
    event: str = Field(..., alias='event')
    userid: str = Field(..., alias='userId')
    useremail: str = Field(..., alias='userEmail')
    username: str = Field(..., alias='userName')
    mode: str = Field(..., alias='mode')
    ip: str = Field(..., alias='ip')
    time: str = Field(..., alias='time')
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
