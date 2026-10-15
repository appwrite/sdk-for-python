from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class OAuth2Gitlab(AppwriteModel):
    """
    OAuth2Gitlab

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    applicationid : str
        GitLab OAuth2 application ID.
    secret : str
        GitLab OAuth2 secret.
    endpoint : str
        GitLab OAuth2 endpoint URL. Defaults to https://gitlab.com for self-hosted instances.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    applicationid: str = Field(..., alias='applicationId')
    secret: str = Field(..., alias='secret')
    endpoint: str = Field(..., alias='endpoint')

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
        if 'applicationId' not in data and 'applicationid' not in data:
            data['applicationId'] = ''
        if 'secret' not in data:
            data['secret'] = ''
        if 'endpoint' not in data:
            data['endpoint'] = ''
        return data
