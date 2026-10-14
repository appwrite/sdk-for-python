from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .oauth2_consent_token import Oauth2ConsentToken


class Oauth2ConsentTokenList(AppwriteModel):
    """
    OAuth2 consent tokens list

    Attributes
    ----------
    total : float
        Total number of tokens that matched your query.
    tokens : List[Oauth2ConsentToken]
        List of tokens.
    """

    total: float = Field(..., alias='total')
    tokens: List[Oauth2ConsentToken] = Field(..., alias='tokens')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'tokens' not in data:
            data['tokens'] = []
        return data
