from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    description : str
        Optional description for the webhook.
    url : str
        Webhook URL endpoint.
    events : List[Any]
        Webhook trigger events.
    tls : bool
        Indicates if SSL / TLS certificate verification is enabled.
    authusername : str
        HTTP basic authentication username.
    authpassword : str
        HTTP basic authentication password. Write-only: always returned empty.
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
    description: str = Field(..., alias='description')
    url: str = Field(..., alias='url')
    events: List[Any] = Field(..., alias='events')
    tls: bool = Field(..., alias='tls')
    authusername: str = Field(..., alias='authUsername')
    authpassword: str = Field(..., alias='authPassword')
    secret: str = Field(..., alias='secret')
    enabled: bool = Field(..., alias='enabled')
    logs: str = Field(..., alias='logs')
    attempts: float = Field(..., alias='attempts')

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
        if 'name' not in data:
            data['name'] = ''
        if 'description' not in data:
            data['description'] = ''
        if 'url' not in data:
            data['url'] = ''
        if 'events' not in data:
            data['events'] = []
        if 'tls' not in data:
            data['tls'] = True
        if 'authUsername' not in data and 'authusername' not in data:
            data['authUsername'] = ''
        if 'authPassword' not in data and 'authpassword' not in data:
            data['authPassword'] = ''
        if 'secret' not in data:
            data['secret'] = ''
        if 'enabled' not in data:
            data['enabled'] = True
        if 'logs' not in data:
            data['logs'] = ''
        if 'attempts' not in data:
            data['attempts'] = 0
        return data
