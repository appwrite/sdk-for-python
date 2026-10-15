from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Token(AppwriteModel):
    """
    Token

    Attributes
    ----------
    id : str
        Token ID.
    createdat : str
        Token creation date in ISO 8601 format.
    userid : str
        User ID.
    secret : str
        Token secret key. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    expire : str
        Token expiration date in ISO 8601 format.
    phrase : str
        Security phrase of a token. Empty if security phrase was not requested when creating a token. It includes randomly generated phrase which is also sent in the external resource such as email.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    userid: str = Field(..., alias='userId')
    secret: str = Field(..., alias='secret')
    expire: str = Field(..., alias='expire')
    phrase: str = Field(..., alias='phrase')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if 'userId' not in data and 'userid' not in data:
            data['userId'] = ''
        if 'secret' not in data:
            data['secret'] = ''
        if 'expire' not in data:
            data['expire'] = ''
        if 'phrase' not in data:
            data['phrase'] = ''
        return data
