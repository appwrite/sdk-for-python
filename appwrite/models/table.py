from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .column_boolean import ColumnBoolean
from .column_integer import ColumnInteger
from .column_float import ColumnFloat
from .column_email import ColumnEmail
from .column_enum import ColumnEnum
from .column_url import ColumnUrl
from .column_ip import ColumnIp
from .column_datetime import ColumnDatetime
from .column_relationship import ColumnRelationship
from .column_point import ColumnPoint
from .column_line import ColumnLine
from .column_polygon import ColumnPolygon
from .column_varchar import ColumnVarchar
from .column_text import ColumnText
from .column_mediumtext import ColumnMediumtext
from .column_longtext import ColumnLongtext
from .column_string import ColumnString
from .column_index import ColumnIndex

class Table(AppwriteModel):
    """
    Table

    Attributes
    ----------
    id : str
        Table ID.
    createdat : str
        Table creation date in ISO 8601 format.
    updatedat : str
        Table update date in ISO 8601 format.
    permissions : List[Any]
        Table permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    databaseid : str
        Database ID.
    name : str
        Table name.
    enabled : bool
        Table enabled. Can be &#039;enabled&#039; or &#039;disabled&#039;. When disabled, the table is inaccessible to users, but remains accessible to Server SDKs using API keys.
    rowsecurity : bool
        Whether row-level permissions are enabled. [Learn more about permissions](https://appwrite.io/docs/permissions).
    columns : List[Union[ColumnBoolean, ColumnInteger, ColumnFloat, ColumnEmail, ColumnEnum, ColumnUrl, ColumnIp, ColumnDatetime, ColumnRelationship, ColumnPoint, ColumnLine, ColumnPolygon, ColumnVarchar, ColumnText, ColumnMediumtext, ColumnLongtext, ColumnString]]
        Table columns.
    indexes : List[ColumnIndex]
        Table indexes.
    bytesmax : float
        Maximum row size in bytes. Returns 0 when no limit applies.
    bytesused : float
        Currently used row size in bytes based on defined columns.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    databaseid: str = Field(..., alias='databaseId')
    name: str = Field(..., alias='name')
    enabled: bool = Field(..., alias='enabled')
    rowsecurity: bool = Field(..., alias='rowSecurity')
    columns: List[Union[ColumnBoolean, ColumnInteger, ColumnFloat, ColumnEmail, ColumnEnum, ColumnUrl, ColumnIp, ColumnDatetime, ColumnRelationship, ColumnPoint, ColumnLine, ColumnPolygon, ColumnVarchar, ColumnText, ColumnMediumtext, ColumnLongtext, ColumnString]] = Field(..., alias='columns')
    indexes: List[ColumnIndex] = Field(..., alias='indexes')
    bytesmax: float = Field(..., alias='bytesMax')
    bytesused: float = Field(..., alias='bytesUsed')
