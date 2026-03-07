from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .document import Document

class DocumentList(AppwriteModel):
    """
    Documents List

    Attributes
    ----------
    total : float
        Total number of documents that matched your query.
    documents : List[Document]
        List of documents.
    """
    total: float = Field(..., alias='total')
    documents: List[Document] = Field(..., alias='documents')
