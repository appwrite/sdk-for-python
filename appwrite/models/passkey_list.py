from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .passkey import Passkey


class PasskeyList(AppwriteModel):
    """
    Passkeys List

    Attributes
    ----------
    total : float
        Total number of passkeys that matched your query.
    passkeys : List[Passkey]
        List of passkeys.
    """

    total: float = Field(..., alias='total')
    passkeys: List[Passkey] = Field(..., alias='passkeys')
