from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .user import User

class UserList(AppwriteModel):
    """
    Users List

    Attributes
    ----------
    total : float
        Total number of users that matched your query.
    users : List[User]
        List of users.
    """
    total: float = Field(..., alias='total')
    users: List[User] = Field(..., alias='users')
