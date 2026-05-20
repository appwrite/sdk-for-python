from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .dev_key import DevKey
from .project_auth_method import ProjectAuthMethod
from .project_service import ProjectService
from .project_protocol import ProjectProtocol
from .billing_limits import BillingLimits
from .block import Block

class Project(AppwriteModel):
    """
    Project

    Attributes
    ----------
    id : str
        Project ID.
    createdat : str
        Project creation date in ISO 8601 format.
    updatedat : str
        Project update date in ISO 8601 format.
    name : str
        Project name.
    teamid : str
        Project team ID.
    devkeys : List[DevKey]
        Deprecated since 1.9.5: List of dev keys.
    smtpenabled : bool
        Status for custom SMTP
    smtpsendername : str
        SMTP sender name
    smtpsenderemail : str
        SMTP sender email
    smtpreplytoname : str
        SMTP reply to name
    smtpreplytoemail : str
        SMTP reply to email
    smtphost : str
        SMTP server host name
    smtpport : float
        SMTP server port
    smtpusername : str
        SMTP server username
    smtppassword : str
        SMTP server password. This property is write-only and always returned empty.
    smtpsecure : str
        SMTP server secure protocol
    pingcount : float
        Number of times the ping was received for this project.
    pingedat : str
        Last ping datetime in ISO 8601 format.
    labels : List[Any]
        Labels for the project.
    status : str
        Project status
    authmethods : List[ProjectAuthMethod]
        List of auth methods.
    services : List[ProjectService]
        List of services.
    protocols : List[ProjectProtocol]
        List of protocols.
    region : str
        Project region
    billinglimits : Optional[BillingLimits]
        Billing limits reached
    blocks : List[Block]
        Project blocks information
    consoleaccessedat : str
        Last time the project was accessed via console. Used with plan&#039;s projectInactivityDays to determine if project is paused.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    teamid: str = Field(..., alias='teamId')
    devkeys: List[DevKey] = Field(..., alias='devKeys')
    smtpenabled: bool = Field(..., alias='smtpEnabled')
    smtpsendername: str = Field(..., alias='smtpSenderName')
    smtpsenderemail: str = Field(..., alias='smtpSenderEmail')
    smtpreplytoname: str = Field(..., alias='smtpReplyToName')
    smtpreplytoemail: str = Field(..., alias='smtpReplyToEmail')
    smtphost: str = Field(..., alias='smtpHost')
    smtpport: float = Field(..., alias='smtpPort')
    smtpusername: str = Field(..., alias='smtpUsername')
    smtppassword: str = Field(..., alias='smtpPassword')
    smtpsecure: str = Field(..., alias='smtpSecure')
    pingcount: float = Field(..., alias='pingCount')
    pingedat: str = Field(..., alias='pingedAt')
    labels: List[Any] = Field(..., alias='labels')
    status: str = Field(..., alias='status')
    authmethods: List[ProjectAuthMethod] = Field(..., alias='authMethods')
    services: List[ProjectService] = Field(..., alias='services')
    protocols: List[ProjectProtocol] = Field(..., alias='protocols')
    region: str = Field(..., alias='region')
    billinglimits: Optional[BillingLimits] = Field(default=None, alias='billingLimits')
    blocks: List[Block] = Field(..., alias='blocks')
    consoleaccessedat: str = Field(..., alias='consoleAccessedAt')
