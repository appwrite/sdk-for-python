from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class OAuth2Dropbox(AppwriteModel):
    """
    OAuth2Dropbox

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    appkey : str
        Dropbox OAuth2 app key.
    appsecret : str
        Dropbox OAuth2 app secret.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    appkey: str = Field(..., alias='appKey')
    appsecret: str = Field(..., alias='appSecret')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'enabled' not in data:
            data['enabled'] = False
        if 'appKey' not in data and 'appkey' not in data:
            data['appKey'] = ''
        if 'appSecret' not in data and 'appsecret' not in data:
            data['appSecret'] = ''
        return data
