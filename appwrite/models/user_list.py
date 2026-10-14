from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .user import User

T = TypeVar('T')


class UserList(AppwriteModel, Generic[T]):
    """
    Users List

    Attributes
    ----------
    total : float
        Total number of users that matched your query.
    users : List[User[T]]
        List of users.
    """

    total: float = Field(..., alias='total')
    users: List[User[T]] = Field(..., alias='users')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'users' not in data:
            data['users'] = []
        return data

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'UserList[T]':
        """Create UserList instance with typed data."""
        instance = cls.model_validate(data)
        if 'users' in data and data['users'] is not None:
            instance.users = [User.with_data(row, model_type) for row in data['users']]
        return instance
