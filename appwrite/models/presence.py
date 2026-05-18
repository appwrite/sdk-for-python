from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

T = TypeVar('T')

class Presence(AppwriteModel, Generic[T]):
    """
    Presence

    Attributes
    ----------
    id : str
        Presence ID.
    createdat : str
        Presence creation date in ISO 8601 format.
    updatedat : str
        Presence update date in ISO 8601 format.
    permissions : List[Any]
        Presence permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    userid : str
        User ID.
    status : Optional[str]
        Presence status.
    source : str
        Presence source.
    expiresat : Optional[str]
        Presence expiry date in ISO 8601 format.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    userid: str = Field(..., alias='userId')
    status: Optional[str] = Field(default=None, alias='status')
    source: str = Field(..., alias='source')
    expiresat: Optional[str] = Field(default=None, alias='expiresAt')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'Presence[T]':
        """Create Presence instance with typed data."""
        internal_fields = {k: v for k, v in data.items() if k.startswith('$')}
        user_data = {k: v for k, v in data.items() if not k.startswith('$')}
        instance = cls.model_validate(internal_fields)
        instance._metadata = model_type(**user_data) if model_type is not dict else user_data
        return instance

    _metadata: Any = PrivateAttr(default_factory=dict)

    @property
    def metadata(self) -> T:
        return cast(T, self._metadata)

    @metadata.setter
    def metadata(self, value: T) -> None:
        object.__setattr__(self, '_metadata', value)

    def to_dict(self) -> Dict[str, Any]:
        result = super().to_dict()
        if hasattr(self, '_metadata'):
            if isinstance(self._metadata, dict):
                result['metadata'] = self._metadata
            elif hasattr(self._metadata, 'model_dump'):
                result['metadata'] = self._metadata.model_dump(mode='json')
            else:
                result['metadata'] = self._metadata
        return result
