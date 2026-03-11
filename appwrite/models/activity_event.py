from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ActivityEvent(AppwriteModel):
    """
    ActivityEvent

    Attributes
    ----------
    id : str
        Event ID.
    usertype : str
        User type.
    userid : str
        User ID.
    useremail : str
        User Email.
    username : str
        User Name.
    resourceparent : str
        Resource parent.
    resourcetype : str
        Resource type.
    resourceid : str
        Resource ID.
    resource : str
        Resource.
    event : str
        Event name.
    useragent : str
        User agent.
    ip : str
        IP address.
    mode : str
        API mode when event triggered.
    country : str
        Location.
    time : str
        Log creation date in ISO 8601 format.
    projectid : str
        Project ID.
    teamid : str
        Team ID.
    hostname : str
        Hostname.
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
    id: str = Field(..., alias='$id')
    usertype: str = Field(..., alias='userType')
    userid: str = Field(..., alias='userId')
    useremail: str = Field(..., alias='userEmail')
    username: str = Field(..., alias='userName')
    resourceparent: str = Field(..., alias='resourceParent')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
    resource: str = Field(..., alias='resource')
    event: str = Field(..., alias='event')
    useragent: str = Field(..., alias='userAgent')
    ip: str = Field(..., alias='ip')
    mode: str = Field(..., alias='mode')
    country: str = Field(..., alias='country')
    time: str = Field(..., alias='time')
    projectid: str = Field(..., alias='projectId')
    teamid: str = Field(..., alias='teamId')
    hostname: str = Field(..., alias='hostname')
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
