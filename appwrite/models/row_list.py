from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .row import Row

T = TypeVar('T')

class RowList(AppwriteModel, Generic[T]):
    """
    Rows List

    Attributes
    ----------
    total : float
        Total number of rows that matched your query.
    rows : List[Row[T]]
        List of rows.
    """
    total: float = Field(..., alias='total')
    rows: List[Row[T]] = Field(..., alias='rows')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'RowList[T]':
        """Create RowList instance with typed data."""
        instance = cls.model_validate(data)
        if 'rows' in data and data['rows'] is not None:
            instance.rows = [
                Row.with_data(row, model_type) 
                for row in data['rows']
            ]
        return instance
