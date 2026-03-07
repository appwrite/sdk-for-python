from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from ..enums.column_status import ColumnStatus

class ColumnRelationship(AppwriteModel):
    """
    ColumnRelationship

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
    relatedtable : str
        The ID of the related table.
    relationtype : str
        The type of the relationship.
    twoway : bool
        Is the relationship two-way?
    twowaykey : str
        The key of the two-way relationship.
    ondelete : str
        How deleting the parent document will propagate to child documents.
    side : str
        Whether this is the parent or child side of the relationship
    """
    key: str = Field(..., alias='key')
    type: str = Field(..., alias='type')
    status: ColumnStatus = Field(..., alias='status')
    error: str = Field(..., alias='error')
    required: bool = Field(..., alias='required')
    array: Optional[bool] = Field(default=None, alias='array')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    relatedtable: str = Field(..., alias='relatedTable')
    relationtype: str = Field(..., alias='relationType')
    twoway: bool = Field(..., alias='twoWay')
    twowaykey: str = Field(..., alias='twoWayKey')
    ondelete: str = Field(..., alias='onDelete')
    side: str = Field(..., alias='side')
