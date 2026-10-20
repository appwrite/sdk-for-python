from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .attribute_boolean import AttributeBoolean
from .attribute_bigint import AttributeBigint
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
    description : str
        Optional description for the collection.
    enabled : bool
        Collection enabled. Can be &#039;enabled&#039; or &#039;disabled&#039;. When disabled, the collection is inaccessible to users, but remains accessible to Server SDKs using API keys.
    documentsecurity : bool
        Whether document-level permissions are enabled. [Learn more about permissions](https://appwrite.io/docs/permissions).
    attributes : List[Union[AttributeBoolean, AttributeBigint, AttributeInteger, AttributeFloat, AttributeEmail, AttributeEnum, AttributeUrl, AttributeIp, AttributeDatetime, AttributeRelationship, AttributePoint, AttributeLine, AttributePolygon, AttributeVarchar, AttributeText, AttributeMediumtext, AttributeLongtext, AttributeString]]
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
    description: str = Field(..., alias='description')
    enabled: bool = Field(..., alias='enabled')
    documentsecurity: bool = Field(..., alias='documentSecurity')
    attributes: List[
        Union[
            AttributeBoolean,
            AttributeBigint,
            AttributeInteger,
            AttributeFloat,
            AttributeEmail,
            AttributeEnum,
            AttributeUrl,
            AttributeIp,
            AttributeDatetime,
            AttributeRelationship,
            AttributePoint,
            AttributeLine,
            AttributePolygon,
            AttributeVarchar,
            AttributeText,
            AttributeMediumtext,
            AttributeLongtext,
            AttributeString,
        ]
    ] = Field(..., alias='attributes')
    indexes: List[Index] = Field(..., alias='indexes')
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
        if 'documentSecurity' not in data and 'documentsecurity' not in data:
            data['documentSecurity'] = False
        if 'attributes' not in data:
            data['attributes'] = []
        if 'indexes' not in data:
            data['indexes'] = []
        if 'bytesMax' not in data and 'bytesmax' not in data:
            data['bytesMax'] = 0
        if 'bytesUsed' not in data and 'bytesused' not in data:
            data['bytesUsed'] = 0
        return data
