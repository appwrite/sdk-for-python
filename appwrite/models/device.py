from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .session import Session


class Device(AppwriteModel):
    """
    Device

    Attributes
    ----------
    id : str
        Device ID.
    createdat : str
        Device creation date in ISO 8601 format.
    updatedat : str
        Device update date in ISO 8601 format.
    expire : str
        Device expiration date in ISO 8601 format.
    activesessionid : str
        ID of the session that is currently active on the device. Empty when no session is active, for example right after the active session was deleted.
    sessions : List[Session]
        List of sessions the device holds. Switch between them to change the active account.
    secret : str
        Secret used to authenticate the device. Carried by the device cookie; only included in the response if the request was made with an API key.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    expire: str = Field(..., alias='expire')
    activesessionid: str = Field(..., alias='activeSessionId')
    sessions: List[Session] = Field(..., alias='sessions')
    secret: str = Field(..., alias='secret', json_schema_extra={'format': 'password'})

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
        if 'expire' not in data:
            data['expire'] = ''
        if 'activeSessionId' not in data and 'activesessionid' not in data:
            data['activeSessionId'] = ''
        if 'sessions' not in data:
            data['sessions'] = []
        if 'secret' not in data:
            data['secret'] = ''
        return data
