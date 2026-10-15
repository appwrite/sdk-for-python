from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.message_status import MessageStatus


class Message(AppwriteModel):
    """
    Message

    Attributes
    ----------
    id : str
        Message ID.
    createdat : str
        Message creation time in ISO 8601 format.
    updatedat : str
        Message update date in ISO 8601 format.
    providertype : str
        Message provider type.
    topics : List[Any]
        Topic IDs set as recipients.
    users : List[Any]
        User IDs set as recipients.
    targets : List[Any]
        Target IDs set as recipients.
    scheduledat : Optional[str]
        The scheduled time for message.
    deliveredat : Optional[str]
        The time when the message was delivered.
    deliveryerrors : Optional[List[Any]]
        Delivery errors if any.
    deliveredtotal : float
        Number of recipients the message was delivered to.
    data : Dict[str, Any]
        Data of the message.
    status : MessageStatus
        Status of delivery.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    providertype: str = Field(..., alias='providerType')
    topics: List[Any] = Field(..., alias='topics')
    users: List[Any] = Field(..., alias='users')
    targets: List[Any] = Field(..., alias='targets')
    scheduledat: Optional[str] = Field(default=None, alias='scheduledAt')
    deliveredat: Optional[str] = Field(default=None, alias='deliveredAt')
    deliveryerrors: Optional[List[Any]] = Field(default=None, alias='deliveryErrors')
    deliveredtotal: float = Field(..., alias='deliveredTotal')
    data: Dict[str, Any] = Field(..., alias='data')
    status: MessageStatus = Field(..., alias='status')

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
        if 'providerType' not in data and 'providertype' not in data:
            data['providerType'] = ''
        if 'topics' not in data:
            data['topics'] = []
        if 'users' not in data:
            data['users'] = []
        if 'targets' not in data:
            data['targets'] = []
        if 'deliveredTotal' not in data and 'deliveredtotal' not in data:
            data['deliveredTotal'] = 0
        if 'data' not in data:
            data['data'] = {}
        if 'status' not in data:
            data['status'] = 'draft'
        return data
