from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .attribute_boolean import AttributeBoolean
from .attribute_integer import AttributeInteger
from .attribute_float import AttributeFloat
from .attribute_email import AttributeEmail
from .attribute_enum import AttributeEnum
from .attribute_url import AttributeUrl
from .attribute_ip import AttributeIp
from .attribute_datetime import AttributeDatetime
from .attribute_relationship import AttributeRelationship
from .attribute_point import AttributePoint
from .attribute_line import AttributeLine
from .attribute_polygon import AttributePolygon
from .attribute_varchar import AttributeVarchar
from .attribute_text import AttributeText
from .attribute_mediumtext import AttributeMediumtext
from .attribute_longtext import AttributeLongtext
from .attribute_string import AttributeString

class AttributeList(AppwriteModel):
    """
    Attributes List

    Attributes
    ----------
    total : float
        Total number of attributes in the given collection.
    attributes : List[Union[AttributeBoolean, AttributeInteger, AttributeFloat, AttributeEmail, AttributeEnum, AttributeUrl, AttributeIp, AttributeDatetime, AttributeRelationship, AttributePoint, AttributeLine, AttributePolygon, AttributeVarchar, AttributeText, AttributeMediumtext, AttributeLongtext, AttributeString]]
        List of attributes.
    """
    total: float = Field(..., alias='total')
    attributes: List[Union[AttributeBoolean, AttributeInteger, AttributeFloat, AttributeEmail, AttributeEnum, AttributeUrl, AttributeIp, AttributeDatetime, AttributeRelationship, AttributePoint, AttributeLine, AttributePolygon, AttributeVarchar, AttributeText, AttributeMediumtext, AttributeLongtext, AttributeString]] = Field(..., alias='attributes')
