from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .preferences import Preferences
from .project_auth_method import ProjectAuthMethod
from .project_service import ProjectService
from .project_protocol import ProjectProtocol
from .block import Block
from .billing_limits import BillingLimits

T = TypeVar('T')


class Project(AppwriteModel, Generic[T]):
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
    ldapenabled : bool
        Status for LDAP sign-in
    ldaphosts : List[Any]
        LDAP directory hosts, tried in order.
    ldapport : float
        LDAP directory port.
    ldapencryption : str
        LDAP transport encryption: none, ldaps or starttls.
    ldapverification : bool
        Whether the LDAP directory certificate is verified.
    ldapcertificate : str
        Certificate in PEM format of the authority that signed the LDAP directory certificate, or the directory certificate itself when it is self-signed. Empty for the system trust store.
    ldaptimeout : float
        Seconds to wait for the LDAP directory to connect and answer.
    ldapbasedn : str
        LDAP subtree the user search starts from.
    ldapbinddn : str
        LDAP service account used to search for users, empty for anonymous search.
    ldapbindpassword : str
        LDAP service account password. This property is write-only and always returned empty.
    ldapuserfilter : str
        LDAP filter that finds the user signing in, with {username} where the username they enter goes.
    ldaprequiredgroupdn : str
        LDAP group a user must belong to in order to sign in, empty to allow every user.
    ldapidattribute : str
        LDAP attribute holding the identifier that stays the same when an entry is renamed or moved.
    ldapemailattribute : str
        LDAP attribute holding the email address.
    ldapnameattribute : str
        LDAP attribute holding the display name.
    ldapphoneattribute : str
        LDAP attribute holding the phone number, empty when unmapped.
    pingcount : float
        Number of times the ping was received for this project.
    pingedat : str
        Last ping datetime in ISO 8601 format.
    labels : List[Any]
        Labels for the project.
    prefs : Optional[Preferences[T]]
        Project preferences as a key-value object
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
    wafenabled : Optional[bool]
        Whether WAF enforcement is enabled for the project.
    parentid : Optional[str]
        ID of the project this environment belongs to. Null when the project is not an environment.
    environmentid : Optional[str]
        ID of the environment, as passed in the X-Appwrite-Environment header, when the project is accessed as one. Null when the project is not an environment.
    billinglimits : Optional[BillingLimits]
        Billing limits reached
    firstaccessedat : Optional[str]
        First time the project received a non-console API request. Empty until the project is used.
    mcpaccessedat : Optional[str]
        Last time the project was accessed through the MCP server. Empty if it was never accessed via MCP.
    oauth2serverenabled : Optional[bool]
        OAuth2 server status
    oauth2serverauthorizationurl : Optional[str]
        OAuth2 server authorization URL
    oauth2serverscopes : Optional[List[Any]]
        OAuth2 server allowed scopes
    oauth2serverdefaultscopes : Optional[List[Any]]
        OAuth2 server scopes used when an authorization request omits the scope parameter
    oauth2serverinstallationscopes : Optional[List[Any]]
        Scopes an application may request when installed on a team
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
    oauth2serverinstallationaccesstokenduration : Optional[float]
        OAuth2 server access token duration in seconds for app installation access tokens
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
    smtpenabled: bool = Field(..., alias='smtpEnabled')
    smtpsendername: str = Field(..., alias='smtpSenderName')
    smtpsenderemail: str = Field(..., alias='smtpSenderEmail')
    smtpreplytoname: str = Field(..., alias='smtpReplyToName')
    smtpreplytoemail: str = Field(..., alias='smtpReplyToEmail')
    smtphost: str = Field(..., alias='smtpHost')
    smtpport: float = Field(..., alias='smtpPort')
    smtpusername: str = Field(..., alias='smtpUsername')
    smtppassword: str = Field(..., alias='smtpPassword', json_schema_extra={'format': 'password'})
    smtpsecure: str = Field(..., alias='smtpSecure')
    ldapenabled: bool = Field(..., alias='ldapEnabled')
    ldaphosts: List[Any] = Field(..., alias='ldapHosts')
    ldapport: float = Field(..., alias='ldapPort')
    ldapencryption: str = Field(..., alias='ldapEncryption')
    ldapverification: bool = Field(..., alias='ldapVerification')
    ldapcertificate: str = Field(..., alias='ldapCertificate')
    ldaptimeout: float = Field(..., alias='ldapTimeout')
    ldapbasedn: str = Field(..., alias='ldapBaseDn')
    ldapbinddn: str = Field(..., alias='ldapBindDn')
    ldapbindpassword: str = Field(..., alias='ldapBindPassword', json_schema_extra={'format': 'password'})
    ldapuserfilter: str = Field(..., alias='ldapUserFilter')
    ldaprequiredgroupdn: str = Field(..., alias='ldapRequiredGroupDn')
    ldapidattribute: str = Field(..., alias='ldapIdAttribute')
    ldapemailattribute: str = Field(..., alias='ldapEmailAttribute')
    ldapnameattribute: str = Field(..., alias='ldapNameAttribute')
    ldapphoneattribute: str = Field(..., alias='ldapPhoneAttribute')
    pingcount: float = Field(..., alias='pingCount')
    pingedat: str = Field(..., alias='pingedAt')
    labels: List[Any] = Field(..., alias='labels')
    prefs: Optional[Preferences[T]] = Field(default=None, alias='prefs')
    status: str = Field(..., alias='status')
    onboarding: Dict[str, Any] = Field(..., alias='onboarding')
    authmethods: List[ProjectAuthMethod] = Field(..., alias='authMethods')
    services: List[ProjectService] = Field(..., alias='services')
    protocols: List[ProjectProtocol] = Field(..., alias='protocols')
    blocks: List[Block] = Field(..., alias='blocks')
    consoleaccessedat: str = Field(..., alias='consoleAccessedAt')
    wafenabled: Optional[bool] = Field(default=None, alias='wafEnabled')
    parentid: Optional[str] = Field(default=None, alias='parentId')
    environmentid: Optional[str] = Field(default=None, alias='environmentId')
    billinglimits: Optional[BillingLimits] = Field(default=None, alias='billingLimits')
    firstaccessedat: Optional[str] = Field(default=None, alias='firstAccessedAt')
    mcpaccessedat: Optional[str] = Field(default=None, alias='mcpAccessedAt')
    oauth2serverenabled: Optional[bool] = Field(default=None, alias='oAuth2ServerEnabled')
    oauth2serverauthorizationurl: Optional[str] = Field(default=None, alias='oAuth2ServerAuthorizationUrl')
    oauth2serverscopes: Optional[List[Any]] = Field(default=None, alias='oAuth2ServerScopes')
    oauth2serverdefaultscopes: Optional[List[Any]] = Field(default=None, alias='oAuth2ServerDefaultScopes')
    oauth2serverinstallationscopes: Optional[List[Any]] = Field(default=None, alias='oAuth2ServerInstallationScopes')
    oauth2serverauthorizationdetailstypes: Optional[List[Any]] = Field(
        default=None,
        alias='oAuth2ServerAuthorizationDetailsTypes',
    )
    oauth2serveraccesstokenduration: Optional[float] = Field(default=None, alias='oAuth2ServerAccessTokenDuration')
    oauth2serverrefreshtokenduration: Optional[float] = Field(default=None, alias='oAuth2ServerRefreshTokenDuration')
    oauth2serverpublicaccesstokenduration: Optional[float] = Field(
        default=None,
        alias='oAuth2ServerPublicAccessTokenDuration',
    )
    oauth2serverpublicrefreshtokenduration: Optional[float] = Field(
        default=None,
        alias='oAuth2ServerPublicRefreshTokenDuration',
    )
    oauth2serverinstallationaccesstokenduration: Optional[float] = Field(
        default=None,
        alias='oAuth2ServerInstallationAccessTokenDuration',
    )
    oauth2serverconfidentialpkce: Optional[bool] = Field(default=None, alias='oAuth2ServerConfidentialPkce')
    oauth2serververificationurl: Optional[str] = Field(default=None, alias='oAuth2ServerVerificationUrl')
    oauth2serverusercodelength: Optional[float] = Field(default=None, alias='oAuth2ServerUserCodeLength')
    oauth2serverusercodeformat: Optional[str] = Field(default=None, alias='oAuth2ServerUserCodeFormat')
    oauth2serverdevicecodeduration: Optional[float] = Field(default=None, alias='oAuth2ServerDeviceCodeDuration')
    oauth2serverdiscoveryurl: Optional[str] = Field(default=None, alias='oAuth2ServerDiscoveryUrl')

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
        if 'name' not in data:
            data['name'] = ''
        if 'teamId' not in data and 'teamid' not in data:
            data['teamId'] = ''
        if 'region' not in data:
            data['region'] = 'fra'
        if 'smtpEnabled' not in data and 'smtpenabled' not in data:
            data['smtpEnabled'] = False
        if 'smtpSenderName' not in data and 'smtpsendername' not in data:
            data['smtpSenderName'] = ''
        if 'smtpSenderEmail' not in data and 'smtpsenderemail' not in data:
            data['smtpSenderEmail'] = ''
        if 'smtpReplyToName' not in data and 'smtpreplytoname' not in data:
            data['smtpReplyToName'] = ''
        if 'smtpReplyToEmail' not in data and 'smtpreplytoemail' not in data:
            data['smtpReplyToEmail'] = ''
        if 'smtpHost' not in data and 'smtphost' not in data:
            data['smtpHost'] = ''
        if 'smtpPort' not in data and 'smtpport' not in data:
            data['smtpPort'] = 0
        if 'smtpUsername' not in data and 'smtpusername' not in data:
            data['smtpUsername'] = ''
        if 'smtpPassword' not in data and 'smtppassword' not in data:
            data['smtpPassword'] = ''
        if 'smtpSecure' not in data and 'smtpsecure' not in data:
            data['smtpSecure'] = ''
        if 'ldapEnabled' not in data and 'ldapenabled' not in data:
            data['ldapEnabled'] = False
        if 'ldapHosts' not in data and 'ldaphosts' not in data:
            data['ldapHosts'] = []
        if 'ldapPort' not in data and 'ldapport' not in data:
            data['ldapPort'] = 636
        if 'ldapEncryption' not in data and 'ldapencryption' not in data:
            data['ldapEncryption'] = 'ldaps'
        if 'ldapVerification' not in data and 'ldapverification' not in data:
            data['ldapVerification'] = True
        if 'ldapCertificate' not in data and 'ldapcertificate' not in data:
            data['ldapCertificate'] = ''
        if 'ldapTimeout' not in data and 'ldaptimeout' not in data:
            data['ldapTimeout'] = 10
        if 'ldapBaseDn' not in data and 'ldapbasedn' not in data:
            data['ldapBaseDn'] = ''
        if 'ldapBindDn' not in data and 'ldapbinddn' not in data:
            data['ldapBindDn'] = ''
        if 'ldapBindPassword' not in data and 'ldapbindpassword' not in data:
            data['ldapBindPassword'] = ''
        if 'ldapUserFilter' not in data and 'ldapuserfilter' not in data:
            data['ldapUserFilter'] = '(uid={username})'
        if 'ldapRequiredGroupDn' not in data and 'ldaprequiredgroupdn' not in data:
            data['ldapRequiredGroupDn'] = ''
        if 'ldapIdAttribute' not in data and 'ldapidattribute' not in data:
            data['ldapIdAttribute'] = 'entryUUID'
        if 'ldapEmailAttribute' not in data and 'ldapemailattribute' not in data:
            data['ldapEmailAttribute'] = 'mail'
        if 'ldapNameAttribute' not in data and 'ldapnameattribute' not in data:
            data['ldapNameAttribute'] = 'cn'
        if 'ldapPhoneAttribute' not in data and 'ldapphoneattribute' not in data:
            data['ldapPhoneAttribute'] = ''
        if 'pingCount' not in data and 'pingcount' not in data:
            data['pingCount'] = 0
        if 'pingedAt' not in data and 'pingedat' not in data:
            data['pingedAt'] = ''
        if 'labels' not in data:
            data['labels'] = []
        if 'status' not in data:
            data['status'] = 'active'
        if 'onboarding' not in data:
            data['onboarding'] = {}
        if 'authMethods' not in data and 'authmethods' not in data:
            data['authMethods'] = []
        if 'services' not in data:
            data['services'] = []
        if 'protocols' not in data:
            data['protocols'] = []
        if 'blocks' not in data:
            data['blocks'] = []
        if 'consoleAccessedAt' not in data and 'consoleaccessedat' not in data:
            data['consoleAccessedAt'] = ''
        return data

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'Project[T]':
        """Create Project instance with typed data."""
        instance = cls.model_validate(data)
        if 'prefs' in data and data['prefs'] is not None:
            instance.prefs = Preferences.with_data(data['prefs'], model_type)
        return instance
