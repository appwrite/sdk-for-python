from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class PolicyPasswordPwned(AppwriteModel):
    """
    Policy Password Pwned

    Attributes
    ----------
    id : str
        Policy ID.
    enabled : bool
        Whether passwords are checked against known data breaches and the result recorded on the user.
    sessions : bool
        Whether a sign-in with a breached password is refused until the password is reset.
    users : bool
        Whether a breached password is rejected when a user signs up or sets a new password.
    """

    id: str = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
    sessions: bool = Field(..., alias='sessions')
    users: bool = Field(..., alias='users')
