from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .document import Document

T = TypeVar('T')

class DocumentList(AppwriteModel, Generic[T]):
    """
    Documents List

    Attributes
    ----------
    total : float
        Total number of documents that matched your query.
    documents : List[Document[T]]
        List of documents.
    """
    total: float = Field(..., alias='total')
    documents: List[Document[T]] = Field(..., alias='documents')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'DocumentList[T]':
        """Create DocumentList instance with typed data."""
        instance = cls.model_validate(data)
        if 'documents' in data and data['documents'] is not None:
            instance.documents = [
                Document.with_data(row, model_type) 
                for row in data['documents']
            ]
        return instance
