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
    time : str
        Log creation date in ISO 8601 format.
    projectid : str
        Project ID.
    teamid : str
        Team ID.
    hostname : str
        Hostname.
    countrycode : str
        Country two-character ISO 3166-1 alpha code.
    countryname : str
        Country name.
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
    time: str = Field(..., alias='time')
    projectid: str = Field(..., alias='projectId')
    teamid: str = Field(..., alias='teamId')
    hostname: str = Field(..., alias='hostname')
    countrycode: str = Field(..., alias='countryCode')
    countryname: str = Field(..., alias='countryName')
