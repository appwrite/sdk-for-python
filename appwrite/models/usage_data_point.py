from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class UsageDataPoint(AppwriteModel):
    """
    usageDataPoint

    Attributes
    ----------
    time : str
        Bucket start timestamp (ISO 8601). When `interval` is omitted this is the request end time, marking the aggregate as-of moment.
    value : float
        Aggregated value for the bucket.
    path : Optional[str]
        API endpoint path when broken down by `path`.
    method : Optional[str]
        HTTP method when broken down by `method`.
    status : Optional[str]
        HTTP status code when broken down by `status`.
    service : Optional[str]
        API service segment when broken down by `service`.
    country : Optional[str]
        Country code when broken down by `country`.
    region : Optional[str]
        Appwrite region when broken down by `region`.
    hostname : Optional[str]
        Caller origin hostname when broken down by `hostname`.
    osname : Optional[str]
        Operating system name when broken down by `osName`.
    clienttype : Optional[str]
        Client type when broken down by `clientType`.
    clientname : Optional[str]
        Client name when broken down by `clientName`.
    devicename : Optional[str]
        Device classification when broken down by `deviceName`.
    teamid : Optional[str]
        Owning team ID when broken down by `teamId`.
    resourceid : Optional[str]
        External resource ID when broken down by `resourceId`.
    resource : Optional[str]
        Resource type when broken down by `resource` (gauges only).
    """
    time: str = Field(..., alias='time')
    value: float = Field(..., alias='value')
    path: Optional[str] = Field(default=None, alias='path')
    method: Optional[str] = Field(default=None, alias='method')
    status: Optional[str] = Field(default=None, alias='status')
    service: Optional[str] = Field(default=None, alias='service')
    country: Optional[str] = Field(default=None, alias='country')
    region: Optional[str] = Field(default=None, alias='region')
    hostname: Optional[str] = Field(default=None, alias='hostname')
    osname: Optional[str] = Field(default=None, alias='osName')
    clienttype: Optional[str] = Field(default=None, alias='clientType')
    clientname: Optional[str] = Field(default=None, alias='clientName')
    devicename: Optional[str] = Field(default=None, alias='deviceName')
    teamid: Optional[str] = Field(default=None, alias='teamId')
    resourceid: Optional[str] = Field(default=None, alias='resourceId')
    resource: Optional[str] = Field(default=None, alias='resource')
