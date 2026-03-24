from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .vectorsdb_collection import VectorsdbCollection

class VectorsdbCollectionList(AppwriteModel):
    """
    VectorsDB Collections List

    Attributes
    ----------
    total : float
        Total number of collections that matched your query.
    collections : List[VectorsdbCollection]
        List of collections.
    """
    total: float = Field(..., alias='total')
    collections: List[VectorsdbCollection] = Field(..., alias='collections')
