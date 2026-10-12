from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'DocumentList[T]':
        """Create DocumentList instance with typed data."""
        instance = cls.model_validate(data)
        if 'documents' in data and data['documents'] is not None:
            instance.documents = [Document.with_data(row, model_type) for row in data['documents']]
        return instance
