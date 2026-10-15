from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
        if 'passkeyId' not in data and 'passkeyid' not in data:
            data['passkeyId'] = ''
        if 'expire' not in data:
            data['expire'] = ''
        if 'publicKey' not in data and 'publickey' not in data:
            data['publicKey'] = {}
        return data
