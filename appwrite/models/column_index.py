from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
        if 'type' not in data:
            data['type'] = ''
        if 'status' not in data:
            data['status'] = ''
        if 'error' not in data:
            data['error'] = ''
        if 'columns' not in data:
            data['columns'] = []
        if 'lengths' not in data:
            data['lengths'] = []
        return data
