from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.o_auth2_kakao_prompt import OAuth2KakaoPrompt


class OAuth2Kakao(AppwriteModel):
    """
    OAuth2Kakao

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    clientid : str
        Kakao OAuth2 REST API key.
    clientsecret : str
        Kakao OAuth2 client secret.
    prompt : List[OAuth2KakaoPrompt]
        Kakao OAuth2 prompt values.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    prompt: List[OAuth2KakaoPrompt] = Field(..., alias='prompt')
