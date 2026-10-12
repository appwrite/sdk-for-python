from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Topic(AppwriteModel):
    """
    Topic

    Attributes
    ----------
    id : str
        Topic ID.
    createdat : str
        Topic creation time in ISO 8601 format.
    updatedat : str
        Topic update date in ISO 8601 format.
    name : str
        The name of the topic.
    emailtotal : float
        Total count of email subscribers subscribed to the topic.
    smstotal : float
        Total count of SMS subscribers subscribed to the topic.
    pushtotal : float
        Total count of push subscribers subscribed to the topic.
    subscribe : List[Any]
        Subscribe permissions.
    qos : Optional[float]
        MQTT QoS for delivery on this topic. Null lets the subscriber choose their level.
    expiry : Optional[float]
        Message retention in seconds for offline delivery.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    emailtotal: float = Field(..., alias='emailTotal')
    smstotal: float = Field(..., alias='smsTotal')
    pushtotal: float = Field(..., alias='pushTotal')
    subscribe: List[Any] = Field(..., alias='subscribe')
    qos: Optional[float] = Field(default=None, alias='qos')
    expiry: Optional[float] = Field(default=None, alias='expiry')

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
        if 'emailTotal' not in data and 'emailtotal' not in data:
            data['emailTotal'] = 0
        if 'smsTotal' not in data and 'smstotal' not in data:
            data['smsTotal'] = 0
        if 'pushTotal' not in data and 'pushtotal' not in data:
            data['pushTotal'] = 0
        if 'subscribe' not in data:
            data['subscribe'] = ['users']
        return data
