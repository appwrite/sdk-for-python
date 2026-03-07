from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class ColumnIndex(AppwriteModel):
    """
    Index

    Attributes
    ----------
    id : str
        Index ID.
    createdat : str
        Index creation date in ISO 8601 format.
    updatedat : str
        Index update date in ISO 8601 format.
    key : str
        Index Key.
    type : str
        Index type.
    status : str
        Index status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    error : str
        Error message. Displays error generated on failure of creating or deleting an index.
    columns : List[Any]
        Index columns.
    lengths : List[Any]
        Index columns length.
    orders : Optional[List[Any]]
        Index orders.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    key: str = Field(..., alias='key')
    type: str = Field(..., alias='type')
    status: str = Field(..., alias='status')
    error: str = Field(..., alias='error')
    columns: List[Any] = Field(..., alias='columns')
    lengths: List[Any] = Field(..., alias='lengths')
    orders: Optional[List[Any]] = Field(default=None, alias='orders')
