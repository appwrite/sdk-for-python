from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.o_auth2_github_prompt import OAuth2GithubPrompt


class OAuth2Github(AppwriteModel):
    """
    OAuth2GitHub

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    clientid : str
        GitHub OAuth2 client ID. For GitHub Apps, use the &quot;App ID&quot; when both an App ID and client ID are available.
    clientsecret : str
        GitHub OAuth2 client secret.
    prompt : Optional[List[OAuth2GithubPrompt]]
        GitHub OAuth2 prompt values.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    prompt: Optional[List[OAuth2GithubPrompt]] = Field(default=None, alias='prompt')
