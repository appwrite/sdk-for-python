from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class AlgoScryptModified(AppwriteModel):
    """
    AlgoScryptModified

    Attributes
    ----------
    type : str
        Algo type.
    salt : str
        Salt used to compute hash.
    saltseparator : str
        Separator used to compute hash.
    signerkey : str
        Key used to compute hash.
    """

    type: str = Field(..., alias='type')
    salt: str = Field(..., alias='salt')
    saltseparator: str = Field(..., alias='saltSeparator')
    signerkey: str = Field(..., alias='signerKey')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'type' not in data:
            data['type'] = 'scryptMod'
        if 'salt' not in data:
            data['salt'] = ''
        if 'saltSeparator' not in data and 'saltseparator' not in data:
            data['saltSeparator'] = ''
        if 'signerKey' not in data and 'signerkey' not in data:
            data['signerKey'] = ''
        return data
