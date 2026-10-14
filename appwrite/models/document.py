from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr, TypeAdapter, model_validator, model_serializer

from .base_model import AppwriteModel

T = TypeVar('T')

_PAYLOAD_ADAPTER = TypeAdapter(Dict[str, Any])


class Document(AppwriteModel, Generic[T]):
    """
    Document

    Attributes
    ----------
    id : str
        Document ID.
    sequence : str
        Document sequence ID.
    collectionid : str
        Collection ID.
    databaseid : str
        Database ID.
    createdat : str
        Document creation date in ISO 8601 format.
    updatedat : str
        Document update date in ISO 8601 format.
    permissions : List[Any]
        Document permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    """

    id: str = Field(..., alias='$id')
    sequence: str = Field(..., alias='$sequence')
    collectionid: str = Field(..., alias='$collectionId')
    databaseid: str = Field(..., alias='$databaseId')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$sequence' not in data and 'sequence' not in data:
            data['$sequence'] = ''
        if '$collectionId' not in data and 'collectionid' not in data:
            data['$collectionId'] = ''
        if '$databaseId' not in data and 'databaseid' not in data:
            data['$databaseId'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if '$permissions' not in data and 'permissions' not in data:
            data['$permissions'] = []
        return data

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'Document[T]':
        """Create Document instance with typed data."""
        internal_aliases = {
            '$id',
            '$sequence',
            '$collectionId',
            '$databaseId',
            '$createdAt',
            '$updatedAt',
            '$permissions',
        }
        internal_fields = {k: v for k, v in data.items() if k in internal_aliases}
        user_data = {k: v for k, v in data.items() if k not in internal_aliases and k != 'data'}
        nested = data.get('data')
        if isinstance(nested, dict):
            user_data = {**nested, **user_data}
        instance = cls.model_validate(internal_fields)
        instance._data = model_type(**user_data) if model_type is not dict else user_data
        return instance

    _data: Any = PrivateAttr(default_factory=dict)

    @property
    def data(self) -> T:
        return cast(T, self._data)

    @data.setter
    def data(self, value: T) -> None:
        object.__setattr__(self, '_data', value)

    def _serialize_data(self, info, include=None, exclude=None):
        if hasattr(self._data, 'model_dump'):
            return self._data.model_dump(
                mode=info.mode,
                by_alias=info.by_alias,
                exclude_unset=info.exclude_unset,
                exclude_defaults=info.exclude_defaults,
                exclude_none=info.exclude_none,
                include=include,
                exclude=exclude,
            )

        if isinstance(self._data, dict) and (include is not None or exclude is not None):
            return _PAYLOAD_ADAPTER.dump_python(
                self._data,
                mode=info.mode,
                by_alias=info.by_alias,
                exclude_unset=info.exclude_unset,
                exclude_defaults=info.exclude_defaults,
                exclude_none=info.exclude_none,
                include=include,
                exclude=exclude,
            )

        return self._data

    @staticmethod
    def _select_data(selector):
        """
        Resolves a pydantic include/exclude selector against the 'data' key, which is
        serialized here rather than declared as a field. Returns whether the key was
        named, and any nested selector to apply within it.
        """
        if selector is None:
            return False, None

        if isinstance(selector, dict):
            if 'data' not in selector:
                return False, None

            nested = selector['data']

            return True, nested if isinstance(nested, (dict, set, frozenset, list, tuple)) else None

        return 'data' in selector, None

    @model_serializer(mode='wrap')
    def _serialize_model(self, handler, info):
        result = handler(self)
        included, include_fields = self._select_data(info.include)
        excluded, exclude_fields = self._select_data(info.exclude)

        if info.include is not None and not included:
            return result

        if excluded and exclude_fields is None:
            return result

        result['data'] = self._serialize_data(info, include_fields, exclude_fields)
        return result
