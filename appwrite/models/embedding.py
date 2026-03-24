from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class Embedding(AppwriteModel):
    """
    Embedding

    Attributes
    ----------
    model : str
        Embedding model used to generate embeddings.
    dimension : float
        Number of dimensions for each embedding vector.
    embedding : List[Any]
        Embedding vector values. If an error occurs, this will be an empty array.
    error : str
        Error message if embedding generation fails. Empty string if no error.
    """
    model: str = Field(..., alias='model')
    dimension: float = Field(..., alias='dimension')
    embedding: List[Any] = Field(..., alias='embedding')
    error: str = Field(..., alias='error')
