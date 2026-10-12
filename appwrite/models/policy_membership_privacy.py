from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class PolicyMembershipPrivacy(AppwriteModel):
    """
    Policy Membership Privacy

    Attributes
    ----------
    id : str
        Policy ID.
    userid : bool
        Whether user ID is visible in memberships.
    useremail : bool
        Whether user email is visible in memberships.
    userphone : bool
        Whether user phone is visible in memberships.
    username : bool
        Whether user name is visible in memberships.
    usermfa : bool
        Whether user MFA status is visible in memberships.
    useraccessedat : bool
        Whether user last access time is visible in memberships.
    """

    id: str = Field(..., alias='$id')
    userid: bool = Field(..., alias='userId')
    useremail: bool = Field(..., alias='userEmail')
    userphone: bool = Field(..., alias='userPhone')
    username: bool = Field(..., alias='userName')
    usermfa: bool = Field(..., alias='userMFA')
    useraccessedat: bool = Field(..., alias='userAccessedAt')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'userId' not in data and 'userid' not in data:
            data['userId'] = False
        if 'userEmail' not in data and 'useremail' not in data:
            data['userEmail'] = False
        if 'userPhone' not in data and 'userphone' not in data:
            data['userPhone'] = False
        if 'userName' not in data and 'username' not in data:
            data['userName'] = False
        if 'userMFA' not in data and 'usermfa' not in data:
            data['userMFA'] = False
        if 'userAccessedAt' not in data and 'useraccessedat' not in data:
            data['userAccessedAt'] = False
        return data
