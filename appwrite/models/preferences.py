from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr, TypeAdapter, model_serializer

from .base_model import AppwriteModel

T = TypeVar('T')

_PAYLOAD_ADAPTER = TypeAdapter(Dict[str, Any])


class Preferences(AppwriteModel, Generic[T]):
    """
    Preferences
    """

    pass

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'Preferences[T]':
        """Create Preferences instance with typed data."""
        user_data = dict(data)
        instance = cls.model_validate({})
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

    @model_serializer(mode='wrap')
    def _serialize_model(self, handler, info):
        result = handler(self)
        data = self._serialize_data(info, info.include, info.exclude)
        if isinstance(result, dict) and isinstance(data, dict):
            return {**result, **data}

        return data
