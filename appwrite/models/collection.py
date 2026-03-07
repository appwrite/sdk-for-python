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
from .index import Index

class Collection(AppwriteModel):
    """
    Collection

    Attributes
    ----------
    id : str
        Collection ID.
    createdat : str
        Collection creation date in ISO 8601 format.
    updatedat : str
        Collection update date in ISO 8601 format.
    permissions : List[Any]
        Collection permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    databaseid : str
        Database ID.
    name : str
        Collection name.
    enabled : bool
        Collection enabled. Can be &#039;enabled&#039; or &#039;disabled&#039;. When disabled, the collection is inaccessible to users, but remains accessible to Server SDKs using API keys.
    documentsecurity : bool
        Whether document-level permissions are enabled. [Learn more about permissions](https://appwrite.io/docs/permissions).
    attributes : List[Union[AttributeBoolean, AttributeInteger, AttributeFloat, AttributeEmail, AttributeEnum, AttributeUrl, AttributeIp, AttributeDatetime, AttributeRelationship, AttributePoint, AttributeLine, AttributePolygon, AttributeVarchar, AttributeText, AttributeMediumtext, AttributeLongtext, AttributeString]]
        Collection attributes.
    indexes : List[Index]
        Collection indexes.
    bytesmax : float
        Maximum document size in bytes. Returns 0 when no limit applies.
    bytesused : float
        Currently used document size in bytes based on defined attributes.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    databaseid: str = Field(..., alias='databaseId')
    name: str = Field(..., alias='name')
    enabled: bool = Field(..., alias='enabled')
    documentsecurity: bool = Field(..., alias='documentSecurity')
    attributes: List[Union[AttributeBoolean, AttributeInteger, AttributeFloat, AttributeEmail, AttributeEnum, AttributeUrl, AttributeIp, AttributeDatetime, AttributeRelationship, AttributePoint, AttributeLine, AttributePolygon, AttributeVarchar, AttributeText, AttributeMediumtext, AttributeLongtext, AttributeString]] = Field(..., alias='attributes')
    indexes: List[Index] = Field(..., alias='indexes')
    bytesmax: float = Field(..., alias='bytesMax')
    bytesused: float = Field(..., alias='bytesUsed')
