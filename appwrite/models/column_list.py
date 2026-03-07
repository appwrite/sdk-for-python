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

class ColumnList(AppwriteModel):
    """
    Columns List

    Attributes
    ----------
    total : float
        Total number of columns in the given table.
    columns : List[Union[ColumnBoolean, ColumnInteger, ColumnFloat, ColumnEmail, ColumnEnum, ColumnUrl, ColumnIp, ColumnDatetime, ColumnRelationship, ColumnPoint, ColumnLine, ColumnPolygon, ColumnVarchar, ColumnText, ColumnMediumtext, ColumnLongtext, ColumnString]]
        List of columns.
    """
    total: float = Field(..., alias='total')
    columns: List[Union[ColumnBoolean, ColumnInteger, ColumnFloat, ColumnEmail, ColumnEnum, ColumnUrl, ColumnIp, ColumnDatetime, ColumnRelationship, ColumnPoint, ColumnLine, ColumnPolygon, ColumnVarchar, ColumnText, ColumnMediumtext, ColumnLongtext, ColumnString]] = Field(..., alias='columns')
