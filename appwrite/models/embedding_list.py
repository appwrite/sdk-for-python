from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .embedding import Embedding

class EmbeddingList(AppwriteModel):
    """
    Embedding list

    Attributes
    ----------
    total : float
        Total number of embeddings that matched your query.
    embeddings : List[Embedding]
        List of embeddings.
    """
    total: float = Field(..., alias='total')
    embeddings: List[Embedding] = Field(..., alias='embeddings')
