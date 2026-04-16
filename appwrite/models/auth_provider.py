from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AuthProvider(AppwriteModel):
    """
    AuthProvider

    Attributes
    ----------
    key : str
        Auth Provider.
    name : str
        Auth Provider name.
    appid : str
        OAuth 2.0 application ID.
    secret : str
        OAuth 2.0 application secret. Might be JSON string if provider requires extra configuration.
    enabled : bool
        Auth Provider is active and can be used to create session.
    """
    key: str = Field(..., alias='key')
    name: str = Field(..., alias='name')
    appid: str = Field(..., alias='appId')
    secret: str = Field(..., alias='secret')
    enabled: bool = Field(..., alias='enabled')
