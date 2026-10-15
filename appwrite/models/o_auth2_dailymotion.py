from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class OAuth2Dailymotion(AppwriteModel):
    """
    OAuth2Dailymotion

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    apikey : str
        Dailymotion OAuth2 API key.
    apisecret : str
        Dailymotion OAuth2 API secret.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    apikey: str = Field(..., alias='apiKey')
    apisecret: str = Field(..., alias='apiSecret')

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
        if 'apiKey' not in data and 'apikey' not in data:
            data['apiKey'] = ''
        if 'apiSecret' not in data and 'apisecret' not in data:
            data['apiSecret'] = ''
        return data
