from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.o_auth2_auth0_prompt import OAuth2Auth0Prompt


class OAuth2Auth0(AppwriteModel):
    """
    OAuth2Auth0

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    clientid : str
        Auth0 OAuth2 client ID.
    clientsecret : str
        Auth0 OAuth2 client secret.
    prompt : Optional[List[OAuth2Auth0Prompt]]
        Auth0 OAuth2 prompt values.
    endpoint : str
        Auth0 OAuth2 endpoint domain.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    prompt: Optional[List[OAuth2Auth0Prompt]] = Field(default=None, alias='prompt')
    endpoint: str = Field(..., alias='endpoint')
