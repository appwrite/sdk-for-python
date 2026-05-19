from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.o_auth2_google_prompt import OAuth2GooglePrompt

class OAuth2Google(AppwriteModel):
    """
    OAuth2Google

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    clientid : str
        Google OAuth2 client ID.
    clientsecret : str
        Google OAuth2 client secret.
    prompt : List[OAuth2GooglePrompt]
        Google OAuth2 prompt values.
    """
    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    prompt: List[OAuth2GooglePrompt] = Field(..., alias='prompt')
