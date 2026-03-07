from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .message import Message

class MessageList(AppwriteModel):
    """
    Message list

    Attributes
    ----------
    total : float
        Total number of messages that matched your query.
    messages : List[Message]
        List of messages.
    """
    total: float = Field(..., alias='total')
    messages: List[Message] = Field(..., alias='messages')
