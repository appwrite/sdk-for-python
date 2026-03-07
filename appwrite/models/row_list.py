from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .row import Row

class RowList(AppwriteModel):
    """
    Rows List

    Attributes
    ----------
    total : float
        Total number of rows that matched your query.
    rows : List[Row]
        List of rows.
    """
    total: float = Field(..., alias='total')
    rows: List[Row] = Field(..., alias='rows')
