from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class OAuth2X(AppwriteModel):
    """
    OAuth2X

    Attributes
    ----------
    id : str
        OAuth2 provider ID.
    enabled : bool
        OAuth2 provider is active and can be used to create sessions.
    customerkey : str
        X OAuth2 customer key.
    secretkey : str
        X OAuth2 secret key.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    customerkey: str = Field(..., alias='customerKey')
    secretkey: str = Field(..., alias='secretKey')

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
        if 'secretKey' not in data and 'secretkey' not in data:
            data['secretKey'] = ''
        return data
