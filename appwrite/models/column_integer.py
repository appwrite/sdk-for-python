from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.column_status import ColumnStatus

class ColumnInteger(AppwriteModel):
    """
    ColumnInteger

    Attributes
    ----------
    key : str
        Column Key.
    type : str
        Column type.
    status : ColumnStatus
        Column status. Possible values: `available`, `processing`, `deleting`, `stuck`, or `failed`
    error : str
        Error message. Displays error generated on failure of creating or deleting an column.
    required : bool
        Is column required?
    array : Optional[bool]
        Is column an array?
    createdat : str
        Column creation date in ISO 8601 format.
    updatedat : str
        Column update date in ISO 8601 format.
    min : Optional[float]
        Minimum value to enforce for new documents.
    max : Optional[float]
        Maximum value to enforce for new documents.
    default : Optional[float]
        Default value for column when not provided. Cannot be set when column is required.
    """
    key: str = Field(..., alias='key')
    type: str = Field(..., alias='type')
    status: ColumnStatus = Field(..., alias='status')
    error: str = Field(..., alias='error')
    required: bool = Field(..., alias='required')
    array: Optional[bool] = Field(default=None, alias='array')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    min: Optional[float] = Field(default=None, alias='min')
    max: Optional[float] = Field(default=None, alias='max')
    default: Optional[float] = Field(default=None, alias='default')
