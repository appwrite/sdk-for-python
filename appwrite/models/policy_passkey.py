from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
