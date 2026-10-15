from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class MfaType(AppwriteModel):
    """
    MFAType

    Attributes
    ----------
    secret : str
        Secret token used for TOTP factor.
    uri : str
        URI for authenticator apps.
    """

    secret: str = Field(..., alias='secret')
    uri: str = Field(..., alias='uri')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'secret' not in data:
            data['secret'] = ''
        if 'uri' not in data:
            data['uri'] = ''
        return data
