from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .target import Target

class Subscriber(AppwriteModel):
    """
    Subscriber

    Attributes
    ----------
    id : str
        Subscriber ID.
    createdat : str
        Subscriber creation time in ISO 8601 format.
    updatedat : str
        Subscriber update date in ISO 8601 format.
    targetid : str
        Target ID.
    target : Target
        Target.
    userid : str
        Topic ID.
    username : str
        User Name.
    topicid : str
        Topic ID.
    providertype : str
        The target provider type. Can be one of the following: `email`, `sms` or `push`.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    targetid: str = Field(..., alias='targetId')
    target: Target = Field(..., alias='target')
    userid: str = Field(..., alias='userId')
    username: str = Field(..., alias='userName')
    topicid: str = Field(..., alias='topicId')
    providertype: str = Field(..., alias='providerType')
