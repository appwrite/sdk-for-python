from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class AlgoSha(AppwriteModel):
    """
    AlgoSHA

    Attributes
    ----------
    type : str
        Algo type.
    """

    type: str = Field(..., alias='type')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'type' not in data:
            data['type'] = 'sha'
        return data
