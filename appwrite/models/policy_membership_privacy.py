from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
