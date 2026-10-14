from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    prompt : List[OAuth2GithubPrompt]
        GitHub OAuth2 prompt values.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    clientid: str = Field(..., alias='clientId')
    clientsecret: str = Field(..., alias='clientSecret')
    prompt: List[OAuth2GithubPrompt] = Field(..., alias='prompt')

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
            data['prompt'] = []
        return data
