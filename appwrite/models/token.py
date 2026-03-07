from typing import Any, Dict, List, Optional, Union

from pydantic import Field

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
