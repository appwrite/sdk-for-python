from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
    prompt : Optional[List[OAuth2SalesforcePrompt]]
        Salesforce OAuth2 prompt values.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    customerkey: str = Field(..., alias='customerKey')
    customersecret: str = Field(..., alias='customerSecret')
    prompt: Optional[List[OAuth2SalesforcePrompt]] = Field(default=None, alias='prompt')
