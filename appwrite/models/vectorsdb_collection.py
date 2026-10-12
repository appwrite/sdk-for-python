from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .attribute_object import AttributeObject
from .attribute_vector import AttributeVector
from .index import Index


class VectorsdbCollection(AppwriteModel):
    """
    VectorsDB Collection

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
    attributes : List[Union[AttributeObject, AttributeVector]]
        Collection attributes.
    indexes : List[Index]
        Collection indexes.
    bytesmax : float
        Maximum document size in bytes. Returns 0 when no limit applies.
    bytesused : float
        Currently used document size in bytes based on defined attributes.
    dimension : float
        Embedding dimension.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    databaseid: str = Field(..., alias='databaseId')
    name: str = Field(..., alias='name')
    enabled: bool = Field(..., alias='enabled')
    documentsecurity: bool = Field(..., alias='documentSecurity')
    attributes: List[
        Union[
            AttributeObject,
            AttributeVector,
        ]
    ] = Field(..., alias='attributes')
    indexes: List[Index] = Field(..., alias='indexes')
    bytesmax: float = Field(..., alias='bytesMax')
    bytesused: float = Field(..., alias='bytesUsed')
    dimension: float = Field(..., alias='dimension')

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
        if 'databaseId' not in data and 'databaseid' not in data:
            data['databaseId'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'enabled' not in data:
            data['enabled'] = True
        if 'documentSecurity' not in data and 'documentsecurity' not in data:
            data['documentSecurity'] = False
        if 'bytesMax' not in data and 'bytesmax' not in data:
            data['bytesMax'] = 0
        if 'bytesUsed' not in data and 'bytesused' not in data:
            data['bytesUsed'] = 0
        if 'dimension' not in data:
            data['dimension'] = 0
        return data
