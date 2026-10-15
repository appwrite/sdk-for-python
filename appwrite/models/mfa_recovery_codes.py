from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class MfaRecoveryCodes(AppwriteModel):
    """
    MFA Recovery Codes

    Attributes
    ----------
    recoverycodes : List[Any]
        Recovery codes.
    """

    recoverycodes: List[Any] = Field(..., alias='recoveryCodes')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'recoveryCodes' not in data and 'recoverycodes' not in data:
            data['recoveryCodes'] = []
        return data
