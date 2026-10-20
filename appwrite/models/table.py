from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .column_boolean import ColumnBoolean
from .column_bigint import ColumnBigint
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
    description : str
        Optional description for the table.
    enabled : bool
        Table enabled. Can be &#039;enabled&#039; or &#039;disabled&#039;. When disabled, the table is inaccessible to users, but remains accessible to Server SDKs using API keys.
    rowsecurity : bool
        Whether row-level permissions are enabled. [Learn more about permissions](https://appwrite.io/docs/permissions).
    columns : List[Union[ColumnBoolean, ColumnBigint, ColumnInteger, ColumnFloat, ColumnEmail, ColumnEnum, ColumnUrl, ColumnIp, ColumnDatetime, ColumnRelationship, ColumnPoint, ColumnLine, ColumnPolygon, ColumnVarchar, ColumnText, ColumnMediumtext, ColumnLongtext, ColumnString]]
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
    description: str = Field(..., alias='description')
    enabled: bool = Field(..., alias='enabled')
    rowsecurity: bool = Field(..., alias='rowSecurity')
    columns: List[
        Union[
            ColumnBoolean,
            ColumnBigint,
            ColumnInteger,
            ColumnFloat,
            ColumnEmail,
            ColumnEnum,
            ColumnUrl,
            ColumnIp,
            ColumnDatetime,
            ColumnRelationship,
            ColumnPoint,
            ColumnLine,
            ColumnPolygon,
            ColumnVarchar,
            ColumnText,
            ColumnMediumtext,
            ColumnLongtext,
            ColumnString,
        ]
    ] = Field(..., alias='columns')
    indexes: List[ColumnIndex] = Field(..., alias='indexes')
    bytesmax: float = Field(..., alias='bytesMax')
    bytesused: float = Field(..., alias='bytesUsed')

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
        if '$permissions' not in data and 'permissions' not in data:
            data['$permissions'] = []
        if 'databaseId' not in data and 'databaseid' not in data:
            data['databaseId'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'description' not in data:
            data['description'] = ''
        if 'enabled' not in data:
            data['enabled'] = True
        if 'rowSecurity' not in data and 'rowsecurity' not in data:
            data['rowSecurity'] = False
        if 'columns' not in data:
            data['columns'] = []
        if 'indexes' not in data:
            data['indexes'] = []
        if 'bytesMax' not in data and 'bytesmax' not in data:
            data['bytesMax'] = 0
        if 'bytesUsed' not in data and 'bytesused' not in data:
            data['bytesUsed'] = 0
        return data
