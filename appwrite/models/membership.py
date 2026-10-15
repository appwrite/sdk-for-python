from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Membership(AppwriteModel):
    """
    Membership

    Attributes
    ----------
    id : str
        Membership ID.
    createdat : str
        Membership creation date in ISO 8601 format.
    updatedat : str
        Membership update date in ISO 8601 format.
    userid : str
        User ID.
    username : str
        User name. Hide this attribute by toggling membership privacy in the Console.
    useremail : str
        User email address. Hide this attribute by toggling membership privacy in the Console.
    userphone : str
        User phone number. Hide this attribute by toggling membership privacy in the Console.
    teamid : str
        Team ID.
    teamname : str
        Team name.
    invited : str
        Date, the user has been invited to join the team in ISO 8601 format.
    joined : str
        Date, the user has accepted the invitation to join the team in ISO 8601 format.
    confirm : bool
        User confirmation status, true if the user has joined the team or false otherwise.
    mfa : bool
        Multi factor authentication status, true if the user has MFA enabled or false otherwise. Hide this attribute by toggling membership privacy in the Console.
    useraccessedat : str
        Most recent access date in ISO 8601 format. Show this attribute by toggling membership privacy in the Console.
    roles : List[Any]
        User list of roles
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    userid: str = Field(..., alias='userId')
    username: str = Field(..., alias='userName')
    useremail: str = Field(..., alias='userEmail')
    userphone: str = Field(..., alias='userPhone')
    teamid: str = Field(..., alias='teamId')
    teamname: str = Field(..., alias='teamName')
    invited: str = Field(..., alias='invited')
    joined: str = Field(..., alias='joined')
    confirm: bool = Field(..., alias='confirm')
    mfa: bool = Field(..., alias='mfa')
    useraccessedat: str = Field(..., alias='userAccessedAt')
    roles: List[Any] = Field(..., alias='roles')

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
        if 'userId' not in data and 'userid' not in data:
            data['userId'] = ''
        if 'userName' not in data and 'username' not in data:
            data['userName'] = ''
        if 'userEmail' not in data and 'useremail' not in data:
            data['userEmail'] = ''
        if 'userPhone' not in data and 'userphone' not in data:
            data['userPhone'] = ''
        if 'teamId' not in data and 'teamid' not in data:
            data['teamId'] = ''
        if 'teamName' not in data and 'teamname' not in data:
            data['teamName'] = ''
        if 'invited' not in data:
            data['invited'] = ''
        if 'joined' not in data:
            data['joined'] = ''
        if 'confirm' not in data:
            data['confirm'] = False
        if 'mfa' not in data:
            data['mfa'] = False
        if 'userAccessedAt' not in data and 'useraccessedat' not in data:
            data['userAccessedAt'] = ''
        if 'roles' not in data:
            data['roles'] = []
        return data
