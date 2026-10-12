from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class PolicyMfaFactors(AppwriteModel):
    """
    Policy MFA Factors

    Attributes
    ----------
    id : str
        Policy ID.
    totp : bool
        Whether TOTP can be used to complete an MFA challenge.
    email : bool
        Whether email can be used to complete an MFA challenge.
    phone : bool
        Whether phone (SMS) can be used to complete an MFA challenge.
    custom : bool
        Whether the custom factor can be used to complete an MFA challenge.
    """

    id: str = Field(..., alias='$id')
    totp: bool = Field(..., alias='totp')
    email: bool = Field(..., alias='email')
    phone: bool = Field(..., alias='phone')
    custom: bool = Field(..., alias='custom')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'totp' not in data:
            data['totp'] = True
        if 'email' not in data:
            data['email'] = True
        if 'phone' not in data:
            data['phone'] = True
        if 'custom' not in data:
            data['custom'] = False
        return data
