from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    description : str
        Optional description for the index.
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
    description: str = Field(..., alias='description')
    type: str = Field(..., alias='type')
    status: IndexStatus = Field(..., alias='status')
    error: str = Field(..., alias='error')
    attributes: List[Any] = Field(..., alias='attributes')
    lengths: List[Any] = Field(..., alias='lengths')
    orders: Optional[List[Any]] = Field(default=None, alias='orders')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'key' not in data:
            data['key'] = ''
        if 'description' not in data:
            data['description'] = ''
        if 'type' not in data:
            data['type'] = ''
        if 'error' not in data:
            data['error'] = ''
        if 'attributes' not in data:
            data['attributes'] = []
        if 'lengths' not in data:
            data['lengths'] = []
        return data
