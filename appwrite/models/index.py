from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from ..enums.index_status import IndexStatus

class Index(AppwriteModel):
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
        Index key.
    type : str
        Index type.
    status : IndexStatus
        Index status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    error : str
        Error message. Displays error generated on failure of creating or deleting an index.
    attributes : List[Any]
        Index attributes.
    lengths : List[Any]
        Index attributes length.
    orders : Optional[List[Any]]
        Index orders.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    key: str = Field(..., alias='key')
    type: str = Field(..., alias='type')
    status: IndexStatus = Field(..., alias='status')
    error: str = Field(..., alias='error')
    attributes: List[Any] = Field(..., alias='attributes')
    lengths: List[Any] = Field(..., alias='lengths')
    orders: Optional[List[Any]] = Field(default=None, alias='orders')
