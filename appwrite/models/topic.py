from typing import Any, Dict, List, Optional, Union

from pydantic import Field

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
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    emailtotal: float = Field(..., alias='emailTotal')
    smstotal: float = Field(..., alias='smsTotal')
    pushtotal: float = Field(..., alias='pushTotal')
    subscribe: List[Any] = Field(..., alias='subscribe')
