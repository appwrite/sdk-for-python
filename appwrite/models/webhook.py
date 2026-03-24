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
    security : bool
        Indicated if SSL / TLS Certificate verification is enabled.
    httpuser : str
        HTTP basic authentication username.
    httppass : str
        HTTP basic authentication password.
    signaturekey : str
        Signature key which can be used to validated incoming
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
    security: bool = Field(..., alias='security')
    httpuser: str = Field(..., alias='httpUser')
    httppass: str = Field(..., alias='httpPass')
    signaturekey: str = Field(..., alias='signatureKey')
    enabled: bool = Field(..., alias='enabled')
    logs: str = Field(..., alias='logs')
    attempts: float = Field(..., alias='attempts')
