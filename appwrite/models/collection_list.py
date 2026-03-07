from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .collection import Collection

class CollectionList(AppwriteModel):
    """
    Collections List

    Attributes
    ----------
    total : float
        Total number of collections that matched your query.
    collections : List[Collection]
        List of collections.
    """
    total: float = Field(..., alias='total')
    collections: List[Collection] = Field(..., alias='collections')
