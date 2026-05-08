from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
