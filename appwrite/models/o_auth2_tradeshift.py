from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class OAuth2Tradeshift(AppwriteModel):
    """
    OAuth2Tradeshift

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    oauth2clientid : str
        Tradeshift OAuth2 client ID.
    oauth2clientsecret : str
        Tradeshift OAuth2 client secret.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    oauth2clientid: str = Field(..., alias='oauth2ClientId')
    oauth2clientsecret: str = Field(..., alias='oauth2ClientSecret')
