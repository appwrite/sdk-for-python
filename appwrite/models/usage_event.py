from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class UsageEvent(AppwriteModel):
    """
    usageEvent

    Attributes
    ----------
    metric : str
        The metric key.
    value : float
        The metric value.
    time : str
        The event timestamp.
    path : str
        The API endpoint path.
    method : str
        The HTTP method.
    status : str
        HTTP status code. Stored as string to preserve unset state (empty string = not available).
    resourcetype : str
        The resource type.
    resourceid : str
        The resource ID.
    countrycode : str
        Country code in [ISO 3166-1](http://en.wikipedia.org/wiki/ISO_3166-1) two-character format.
    useragent : str
        The user agent string.
    """
    metric: str = Field(..., alias='metric')
    value: float = Field(..., alias='value')
    time: str = Field(..., alias='time')
    path: str = Field(..., alias='path')
    method: str = Field(..., alias='method')
    status: str = Field(..., alias='status')
    resourcetype: str = Field(..., alias='resourceType')
    resourceid: str = Field(..., alias='resourceId')
    countrycode: str = Field(..., alias='countryCode')
    useragent: str = Field(..., alias='userAgent')
