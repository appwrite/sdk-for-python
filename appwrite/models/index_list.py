from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .index import Index

class IndexList(AppwriteModel):
    """
    Indexes List

    Attributes
    ----------
    total : float
        Total number of indexes that matched your query.
    indexes : List[Index]
        List of indexes.
    """
    total: float = Field(..., alias='total')
    indexes: List[Index] = Field(..., alias='indexes')
