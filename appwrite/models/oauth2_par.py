from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Oauth2PAR(AppwriteModel):
    """
    OAuth2 PAR

    Attributes
    ----------
    request_uri : str
        Authorization request handle to pass to the authorize endpoint.
    expires_in : float
        Lifetime of the authorization request handle in seconds.
    """

    request_uri: str = Field(..., alias='request_uri')
    expires_in: float = Field(..., alias='expires_in')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'request_uri' not in data:
            data['request_uri'] = ''
        if 'expires_in' not in data:
            data['expires_in'] = 0
        return data
