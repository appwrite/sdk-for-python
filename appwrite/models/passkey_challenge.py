from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class PasskeyChallenge(AppwriteModel):
    """
    Passkey Challenge

    Attributes
    ----------
    id : str
        Challenge ID. When signing in, pass it back with the credential to receive a token.
    createdat : str
        Challenge creation date in ISO 8601 format.
    passkeyid : str
        ID of the passkey being registered. Empty for sign-in challenges.
    expire : str
        Challenge expiration date in ISO 8601 format.
    publickey : Dict[str, Any]
        WebAuthn options in JSON form. Pass them to `PublicKeyCredential.parseCreationOptionsFromJSON()` when registering, or `PublicKeyCredential.parseRequestOptionsFromJSON()` when signing in.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    passkeyid: str = Field(..., alias='passkeyId')
    expire: str = Field(..., alias='expire')
    publickey: Dict[str, Any] = Field(..., alias='publicKey')
