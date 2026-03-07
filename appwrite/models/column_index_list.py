from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .column_index import ColumnIndex

class ColumnIndexList(AppwriteModel):
    """
    Column Indexes List

    Attributes
    ----------
    total : float
        Total number of indexes that matched your query.
    indexes : List[ColumnIndex]
        List of indexes.
    """
    total: float = Field(..., alias='total')
    indexes: List[ColumnIndex] = Field(..., alias='indexes')
