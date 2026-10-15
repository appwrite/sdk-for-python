from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'messages' not in data:
            data['messages'] = []
        return data
