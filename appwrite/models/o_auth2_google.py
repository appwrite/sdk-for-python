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
    nativeenabled : Optional[bool]
        Native Google sign-in is active and can be used to create sessions from an ID token. Independent of enabled, which only controls the browser-based flow.
    nativeclientids : Optional[List[Any]]
        Additional OAuth2 client IDs accepted as ID token audiences for native sign-in, next to the client ID.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    prompt: List[OAuth2GooglePrompt] = Field(..., alias='prompt')
    nativeenabled: Optional[bool] = Field(default=None, alias='nativeEnabled')
    nativeclientids: Optional[List[Any]] = Field(default=None, alias='nativeClientIds')
