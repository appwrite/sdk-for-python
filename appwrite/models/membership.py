from typing import Any, Dict, List, Optional, Union

from pydantic import Field

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
    roles : List[Any]
        User list of roles
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    userid: str = Field(..., alias='userId')
    username: str = Field(..., alias='userName')
    useremail: str = Field(..., alias='userEmail')
    teamid: str = Field(..., alias='teamId')
    teamname: str = Field(..., alias='teamName')
    invited: str = Field(..., alias='invited')
    joined: str = Field(..., alias='joined')
    confirm: bool = Field(..., alias='confirm')
    mfa: bool = Field(..., alias='mfa')
    roles: List[Any] = Field(..., alias='roles')
