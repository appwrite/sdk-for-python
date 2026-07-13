from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .dev_key import DevKey
from .project_auth_method import ProjectAuthMethod
from .project_service import ProjectService
from .project_protocol import ProjectProtocol
from .block import Block
from .billing_limits import BillingLimits

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
    region : str
        Project region
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
    onboarding : Dict[str, Any]
        Stage progress (completed or skipped) with timestamps and actor types, keyed by stage id.
    authmethods : List[ProjectAuthMethod]
        List of auth methods.
    services : List[ProjectService]
        List of services.
    protocols : List[ProjectProtocol]
        List of protocols.
    blocks : List[Block]
        Project blocks information
    consoleaccessedat : str
        Last time the project was accessed via console. Used with plan&#039;s projectInactivityDays to determine if project is paused.
    billinglimits : Optional[BillingLimits]
        Billing limits reached
    oauth2serverenabled : Optional[bool]
        OAuth2 server status
    oauth2serverauthorizationurl : Optional[str]
        OAuth2 server authorization URL
    oauth2serverscopes : Optional[List[Any]]
        OAuth2 server allowed scopes
    oauth2serverdefaultscopes : Optional[List[Any]]
        OAuth2 server scopes used when an authorization request omits the scope parameter
    oauth2serverauthorizationdetailstypes : Optional[List[Any]]
        OAuth2 server accepted RFC 9396 authorization_details types
    oauth2serveraccesstokenduration : Optional[float]
        OAuth2 server access token duration in seconds for confidential clients
    oauth2serverrefreshtokenduration : Optional[float]
        OAuth2 server refresh token duration in seconds for confidential clients
    oauth2serverpublicaccesstokenduration : Optional[float]
        OAuth2 server access token duration in seconds for public clients (SPAs, mobile, native)
    oauth2serverpublicrefreshtokenduration : Optional[float]
        OAuth2 server refresh token duration in seconds for public clients (SPAs, mobile, native)
    oauth2serverconfidentialpkce : Optional[bool]
        When enabled, PKCE is required for confidential clients (server-side flows using client_secret). PKCE is always required for public clients regardless of this setting.
    oauth2serververificationurl : Optional[str]
        URL to your application page where users enter the device flow user code. Empty when the Device Authorization Grant is not configured.
    oauth2serverusercodelength : Optional[float]
        Number of characters in the device flow user code, excluding the formatting separator.
    oauth2serverusercodeformat : Optional[str]
        Character set for device flow user codes: `numeric`, `alphabetic`, or `alphanumeric`.
    oauth2serverdevicecodeduration : Optional[float]
        Lifetime in seconds of device flow device codes and user codes.
    oauth2serverdiscoveryurl : Optional[str]
        OAuth2 server discovery URL
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    teamid: str = Field(..., alias='teamId')
    region: str = Field(..., alias='region')
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
    onboarding: Dict[str, Any] = Field(..., alias='onboarding')
    authmethods: List[ProjectAuthMethod] = Field(..., alias='authMethods')
    services: List[ProjectService] = Field(..., alias='services')
    protocols: List[ProjectProtocol] = Field(..., alias='protocols')
    blocks: List[Block] = Field(..., alias='blocks')
    consoleaccessedat: str = Field(..., alias='consoleAccessedAt')
    billinglimits: Optional[BillingLimits] = Field(default=None, alias='billingLimits')
    oauth2serverenabled: Optional[bool] = Field(default=None, alias='oAuth2ServerEnabled')
    oauth2serverauthorizationurl: Optional[str] = Field(default=None, alias='oAuth2ServerAuthorizationUrl')
    oauth2serverscopes: Optional[List[Any]] = Field(default=None, alias='oAuth2ServerScopes')
    oauth2serverdefaultscopes: Optional[List[Any]] = Field(default=None, alias='oAuth2ServerDefaultScopes')
    oauth2serverauthorizationdetailstypes: Optional[List[Any]] = Field(default=None, alias='oAuth2ServerAuthorizationDetailsTypes')
    oauth2serveraccesstokenduration: Optional[float] = Field(default=None, alias='oAuth2ServerAccessTokenDuration')
    oauth2serverrefreshtokenduration: Optional[float] = Field(default=None, alias='oAuth2ServerRefreshTokenDuration')
    oauth2serverpublicaccesstokenduration: Optional[float] = Field(default=None, alias='oAuth2ServerPublicAccessTokenDuration')
    oauth2serverpublicrefreshtokenduration: Optional[float] = Field(default=None, alias='oAuth2ServerPublicRefreshTokenDuration')
    oauth2serverconfidentialpkce: Optional[bool] = Field(default=None, alias='oAuth2ServerConfidentialPkce')
    oauth2serververificationurl: Optional[str] = Field(default=None, alias='oAuth2ServerVerificationUrl')
    oauth2serverusercodelength: Optional[float] = Field(default=None, alias='oAuth2ServerUserCodeLength')
    oauth2serverusercodeformat: Optional[str] = Field(default=None, alias='oAuth2ServerUserCodeFormat')
    oauth2serverdevicecodeduration: Optional[float] = Field(default=None, alias='oAuth2ServerDeviceCodeDuration')
    oauth2serverdiscoveryurl: Optional[str] = Field(default=None, alias='oAuth2ServerDiscoveryUrl')
