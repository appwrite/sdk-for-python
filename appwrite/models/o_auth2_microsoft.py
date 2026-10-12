from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.o_auth2_microsoft_prompt import OAuth2MicrosoftPrompt


class OAuth2Microsoft(AppwriteModel):
    """
    OAuth2Microsoft

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    applicationid : str
        Microsoft OAuth2 application ID.
    applicationsecret : str
        Microsoft OAuth2 application secret.
    prompt : List[OAuth2MicrosoftPrompt]
        Microsoft OAuth2 prompt values.
    tenant : str
        Microsoft Entra ID tenant identifier. Use &#039;common&#039;, &#039;organizations&#039;, &#039;consumers&#039; or a specific tenant ID.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    applicationid: str = Field(..., alias='applicationId')
    applicationsecret: str = Field(..., alias='applicationSecret')
    prompt: List[OAuth2MicrosoftPrompt] = Field(..., alias='prompt')
    tenant: str = Field(..., alias='tenant')

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
        if 'applicationSecret' not in data and 'applicationsecret' not in data:
            data['applicationSecret'] = ''
        if 'prompt' not in data:
            data['prompt'] = []
        if 'tenant' not in data:
            data['tenant'] = ''
        return data
