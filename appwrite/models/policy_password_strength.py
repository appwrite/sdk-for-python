from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class PolicyPasswordStrength(AppwriteModel):
    """
    Policy Password Strength

    Attributes
    ----------
    id : str
        Policy ID.
    min : float
        Minimum password length required for user passwords.
    uppercase : bool
        Whether passwords must include at least one uppercase letter.
    lowercase : bool
        Whether passwords must include at least one lowercase letter.
    number : bool
        Whether passwords must include at least one number.
    symbols : bool
        Whether passwords must include at least one symbol.
    """

    id: str = Field(..., alias='$id')
    min: float = Field(..., alias='min')
    uppercase: bool = Field(..., alias='uppercase')
    lowercase: bool = Field(..., alias='lowercase')
    number: bool = Field(..., alias='number')
    symbols: bool = Field(..., alias='symbols')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'min' not in data:
            data['min'] = 8
        if 'uppercase' not in data:
            data['uppercase'] = False
        if 'lowercase' not in data:
            data['lowercase'] = False
        if 'number' not in data:
            data['number'] = False
        if 'symbols' not in data:
            data['symbols'] = False
        return data
