from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class PolicyPasskey(AppwriteModel):
    """
    Policy Passkey

    Attributes
    ----------
    id : str
        Policy ID.
    rpid : str
        Relying party ID passkeys are bound to. Empty until configured.
    origins : List[Any]
        Web origins passkeys work on, from the project&#039;s platforms on the relying party ID and a localhost web platform. Read-only.
    """

    id: str = Field(..., alias='$id')
    rpid: str = Field(..., alias='rpId')
    origins: List[Any] = Field(..., alias='origins')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'rpId' not in data and 'rpid' not in data:
            data['rpId'] = ''
        if 'origins' not in data:
            data['origins'] = []
        return data
