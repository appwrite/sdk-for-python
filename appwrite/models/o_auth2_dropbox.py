from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
