from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'actorType' not in data and 'actortype' not in data:
            data['actorType'] = ''
        if 'actorId' not in data and 'actorid' not in data:
            data['actorId'] = ''
        if 'actorEmail' not in data and 'actoremail' not in data:
            data['actorEmail'] = ''
        if 'actorName' not in data and 'actorname' not in data:
            data['actorName'] = ''
        if 'resourceParent' not in data and 'resourceparent' not in data:
            data['resourceParent'] = ''
        if 'resourceType' not in data and 'resourcetype' not in data:
            data['resourceType'] = ''
        if 'resourceId' not in data and 'resourceid' not in data:
            data['resourceId'] = ''
        if 'resource' not in data:
            data['resource'] = ''
        if 'event' not in data:
            data['event'] = ''
        if 'userAgent' not in data and 'useragent' not in data:
            data['userAgent'] = ''
        if 'ip' not in data:
            data['ip'] = ''
        if 'mode' not in data:
            data['mode'] = ''
        if 'country' not in data:
            data['country'] = ''
        if 'continentCode' not in data and 'continentcode' not in data:
            data['continentCode'] = ''
        if 'city' not in data:
            data['city'] = ''
        if 'subdivisions' not in data:
            data['subdivisions'] = ''
        if 'isp' not in data:
            data['isp'] = ''
        if 'autonomousSystemNumber' not in data and 'autonomoussystemnumber' not in data:
            data['autonomousSystemNumber'] = ''
        if 'autonomousSystemOrganization' not in data and 'autonomoussystemorganization' not in data:
            data['autonomousSystemOrganization'] = ''
        if 'connectionType' not in data and 'connectiontype' not in data:
            data['connectionType'] = ''
        if 'connectionUsageType' not in data and 'connectionusagetype' not in data:
            data['connectionUsageType'] = ''
        if 'connectionOrganization' not in data and 'connectionorganization' not in data:
            data['connectionOrganization'] = ''
        if 'time' not in data:
            data['time'] = ''
        if 'projectId' not in data and 'projectid' not in data:
            data['projectId'] = ''
        if 'teamId' not in data and 'teamid' not in data:
            data['teamId'] = ''
        if 'hostname' not in data:
            data['hostname'] = ''
        if 'sdk' not in data:
            data['sdk'] = ''
        if 'sdkVersion' not in data and 'sdkversion' not in data:
            data['sdkVersion'] = ''
        return data
