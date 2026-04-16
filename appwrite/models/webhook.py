from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Webhook(AppwriteModel):
    """
    Webhook

    Attributes
    ----------
    id : str
        Webhook ID.
    createdat : str
        Webhook creation date in ISO 8601 format.
    updatedat : str
        Webhook update date in ISO 8601 format.
    name : str
        Webhook name.
    url : str
        Webhook URL endpoint.
    events : List[Any]
        Webhook trigger events.
    tls : bool
        Indicates if SSL / TLS certificate verification is enabled.
    authusername : str
        HTTP basic authentication username.
    authpassword : str
        HTTP basic authentication password.
    secret : str
        Signature key which can be used to validate incoming webhook payloads. Only returned on creation and secret rotation.
    enabled : bool
        Indicates if this webhook is enabled.
    logs : str
        Webhook error logs from the most recent failure.
    attempts : float
        Number of consecutive failed webhook attempts.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    url: str = Field(..., alias='url')
    events: List[Any] = Field(..., alias='events')
    tls: bool = Field(..., alias='tls')
    authusername: str = Field(..., alias='authUsername')
    authpassword: str = Field(..., alias='authPassword')
    secret: str = Field(..., alias='secret')
    enabled: bool = Field(..., alias='enabled')
    logs: str = Field(..., alias='logs')
    attempts: float = Field(..., alias='attempts')
