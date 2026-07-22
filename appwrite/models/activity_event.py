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
    actortype : str
        Actor type.
    actorid : str
        Actor ID.
    actoremail : str
        Actor Email.
    actorname : str
        Actor Name.
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
    continentcode : str
        Continent code.
    city : str
        City name.
    subdivisions : str
        Region/state chain.
    isp : str
        Internet service provider.
    autonomoussystemnumber : str
        Autonomous System Number (ASN).
    autonomoussystemorganization : str
        Organization that owns the ASN.
    connectiontype : str
        Connection type (e.g. cable, cellular, corporate).
    connectionusagetype : str
        User type (e.g. residential, business, hosting).
    connectionorganization : str
        Registered organization of the IP.
    time : str
        Log creation date in ISO 8601 format.
    projectid : str
        Project ID.
    teamid : str
        Team ID.
    hostname : str
        Hostname.
    sdk : str
        Name of the SDK that triggered the event.
    sdkversion : str
        Version of the SDK that triggered the event.
    """
    id: str = Field(..., alias='$id')
    actortype: str = Field(..., alias='actorType')
    actorid: str = Field(..., alias='actorId')
    actoremail: str = Field(..., alias='actorEmail')
    actorname: str = Field(..., alias='actorName')
    resourceparent: str = Field(..., alias='resourceParent')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
    resource: str = Field(..., alias='resource')
    event: str = Field(..., alias='event')
    useragent: str = Field(..., alias='userAgent')
    ip: str = Field(..., alias='ip')
    mode: str = Field(..., alias='mode')
    country: str = Field(..., alias='country')
    continentcode: str = Field(..., alias='continentCode')
    city: str = Field(..., alias='city')
    subdivisions: str = Field(..., alias='subdivisions')
    isp: str = Field(..., alias='isp')
    autonomoussystemnumber: str = Field(..., alias='autonomousSystemNumber')
    autonomoussystemorganization: str = Field(..., alias='autonomousSystemOrganization')
    connectiontype: str = Field(..., alias='connectionType')
    connectionusagetype: str = Field(..., alias='connectionUsageType')
    connectionorganization: str = Field(..., alias='connectionOrganization')
    time: str = Field(..., alias='time')
    projectid: str = Field(..., alias='projectId')
    teamid: str = Field(..., alias='teamId')
    hostname: str = Field(..., alias='hostname')
    sdk: str = Field(..., alias='sdk')
    sdkversion: str = Field(..., alias='sdkVersion')
