from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    nativeenabled : bool
        Native Google sign-in is active and can be used to create sessions from an ID token. Independent of enabled, which only controls the browser-based flow.
    nativeclientids : List[Any]
        Additional OAuth2 client IDs accepted as ID token audiences for native sign-in, next to the client ID.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    prompt: List[OAuth2GooglePrompt] = Field(..., alias='prompt')
    nativeenabled: bool = Field(..., alias='nativeEnabled')
    nativeclientids: List[Any] = Field(..., alias='nativeClientIds')

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
        if 'clientId' not in data and 'clientid' not in data:
            data['clientId'] = ''
        if 'clientSecret' not in data and 'clientsecret' not in data:
            data['clientSecret'] = ''
        if 'prompt' not in data:
            data['prompt'] = ['consent']
        if 'nativeEnabled' not in data and 'nativeenabled' not in data:
            data['nativeEnabled'] = False
        if 'nativeClientIds' not in data and 'nativeclientids' not in data:
            data['nativeClientIds'] = []
        return data
