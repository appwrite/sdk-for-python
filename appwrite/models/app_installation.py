from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class AppInstallation(AppwriteModel):
    """
    AppInstallation

    Attributes
    ----------
    id : str
        Installation ID.
    createdat : str
        Installation creation time in ISO 8601 format.
    updatedat : str
        Installation update time in ISO 8601 format.
    appid : str
        ID of the installed application.
    teamid : str
        ID of the team the application is installed on.
    scopes : List[Any]
        Scopes granted to the application. Snapshot of the application&#039;s installation scopes taken when the installation was created or last updated.
    authorizationdetails : List[Any]
        Authorization details granted to the application. Rich authorization request (RFC 9396) style entries; the Appwrite Console stores authorized project IDs here.
    createdbyid : str
        ID of the user who created the installation.
    createdbyname : str
        Name of the user who created the installation.
    lastaccessedat : Optional[str]
        Time an access token was last issued for the installation in ISO 8601 format. Null if never used.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    appid: str = Field(..., alias='appId')
    teamid: str = Field(..., alias='teamId')
    scopes: List[Any] = Field(..., alias='scopes')
    authorizationdetails: List[Any] = Field(..., alias='authorizationDetails')
    createdbyid: str = Field(..., alias='createdById')
    createdbyname: str = Field(..., alias='createdByName')
    lastaccessedat: Optional[str] = Field(default=None, alias='lastAccessedAt')

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
        if 'appId' not in data and 'appid' not in data:
            data['appId'] = ''
        if 'teamId' not in data and 'teamid' not in data:
            data['teamId'] = ''
        if 'scopes' not in data:
            data['scopes'] = []
        if 'authorizationDetails' not in data and 'authorizationdetails' not in data:
            data['authorizationDetails'] = []
        if 'createdById' not in data and 'createdbyid' not in data:
            data['createdById'] = ''
        if 'createdByName' not in data and 'createdbyname' not in data:
            data['createdByName'] = ''
        return data
