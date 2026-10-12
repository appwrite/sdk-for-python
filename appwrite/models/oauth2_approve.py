from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Oauth2Approve(AppwriteModel):
    """
    OAuth2 Approve

    Attributes
    ----------
    redirecturl : str
        URL the end user should be redirected to after the grant is approved, carrying the authorization `code` and/or `id_token` along with the original `state`.
    """

    redirecturl: str = Field(..., alias='redirectUrl')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'redirectUrl' not in data and 'redirecturl' not in data:
            data['redirectUrl'] = ''
        return data
