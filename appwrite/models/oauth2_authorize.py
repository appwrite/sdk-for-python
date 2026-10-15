from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Oauth2Authorize(AppwriteModel):
    """
    OAuth2 Authorize

    Attributes
    ----------
    grantid : str
        OAuth2 grant ID. Set when the user must give explicit consent; pass it to the approve or reject endpoint. Empty when a redirect URL is returned instead.
    redirecturl : str
        URL the end user should be redirected to when the flow can complete without consent. Empty when consent is still required.
    """

    grantid: str = Field(..., alias='grantId')
    redirecturl: str = Field(..., alias='redirectUrl')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'grantId' not in data and 'grantid' not in data:
            data['grantId'] = ''
        if 'redirectUrl' not in data and 'redirecturl' not in data:
            data['redirectUrl'] = ''
        return data
