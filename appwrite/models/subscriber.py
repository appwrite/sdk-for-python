from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
        if 'targetId' not in data and 'targetid' not in data:
            data['targetId'] = ''
        if 'userId' not in data and 'userid' not in data:
            data['userId'] = ''
        if 'userName' not in data and 'username' not in data:
            data['userName'] = ''
        if 'topicId' not in data and 'topicid' not in data:
            data['topicId'] = ''
        if 'providerType' not in data and 'providertype' not in data:
            data['providerType'] = ''
        return data
