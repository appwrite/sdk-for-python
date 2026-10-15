from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.o_auth2_salesforce_prompt import OAuth2SalesforcePrompt


class OAuth2Salesforce(AppwriteModel):
    """
    OAuth2Salesforce

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    customerkey : str
        Salesforce OAuth2 consumer key.
    customersecret : str
        Salesforce OAuth2 consumer secret.
    prompt : List[OAuth2SalesforcePrompt]
        Salesforce OAuth2 prompt values.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    customerkey: str = Field(..., alias='customerKey')
    customersecret: str = Field(..., alias='customerSecret')
    prompt: List[OAuth2SalesforcePrompt] = Field(..., alias='prompt')

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
        if 'customerKey' not in data and 'customerkey' not in data:
            data['customerKey'] = ''
        if 'customerSecret' not in data and 'customersecret' not in data:
            data['customerSecret'] = ''
        if 'prompt' not in data:
            data['prompt'] = []
        return data
