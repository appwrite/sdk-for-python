from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .table import Table

class TableList(AppwriteModel):
    """
    Tables List

    Attributes
    ----------
    total : float
        Total number of tables that matched your query.
    tables : List[Table]
        List of tables.
    """
    total: float = Field(..., alias='total')
    tables: List[Table] = Field(..., alias='tables')
