from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
