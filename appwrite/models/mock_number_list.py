from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
