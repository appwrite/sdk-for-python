from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OAuth2Facebook(AppwriteModel):
    """
    OAuth2Facebook

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    appid : str
        Facebook OAuth2 app ID.
    appsecret : str
        Facebook OAuth2 app secret.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    appid: str = Field(..., alias='appId')
    appsecret: str = Field(..., alias='appSecret')
