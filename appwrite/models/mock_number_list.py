from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .mock_number import MockNumber


class MockNumberList(AppwriteModel):
    """
    Mock Numbers List

    Attributes
    ----------
    total : float
        Total number of mockNumbers that matched your query.
    mocknumbers : List[MockNumber]
        List of mockNumbers.
    """

    total: float = Field(..., alias='total')
    mocknumbers: List[MockNumber] = Field(..., alias='mockNumbers')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
