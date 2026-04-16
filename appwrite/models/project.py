from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .mock_number import MockNumber
from .auth_provider import AuthProvider
from .platform_web import PlatformWeb
from .platform_apple import PlatformApple
from .platform_android import PlatformAndroid
from .platform_windows import PlatformWindows
from .platform_linux import PlatformLinux
from .webhook import Webhook
from .key import Key
from .dev_key import DevKey
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
    description : str
        Project description.
    teamid : str
        Project team ID.
    logo : str
        Project logo file ID.
    url : str
        Project website URL.
    legalname : str
        Company legal name.
    legalcountry : str
        Country code in [ISO 3166-1](http://en.wikipedia.org/wiki/ISO_3166-1) two-character format.
    legalstate : str
        State name.
    legalcity : str
        City name.
    legaladdress : str
        Company Address.
    legaltaxid : str
        Company Tax ID.
    authduration : float
        Session duration in seconds.
    authlimit : float
        Max users allowed. 0 is unlimited.
    authsessionslimit : float
        Max sessions allowed per user. 100 maximum.
    authpasswordhistory : float
        Max allowed passwords in the history list per user. Max passwords limit allowed in history is 20. Use 0 for disabling password history.
    authpassworddictionary : bool
        Whether or not to check user&#039;s password against most commonly used passwords.
    authpersonaldatacheck : bool
        Whether or not to check the user password for similarity with their personal data.
    authdisposableemails : bool
        Whether or not to disallow disposable email addresses during signup and email updates.
    authcanonicalemails : bool
        Whether or not to require canonical email addresses during signup and email updates.
    authfreeemails : bool
        Whether or not to disallow free email addresses during signup and email updates.
    authmocknumbers : List[MockNumber]
        An array of mock numbers and their corresponding verification codes (OTPs).
    authsessionalerts : bool
        Whether or not to send session alert emails to users.
    authmembershipsusername : bool
        Whether or not to show user names in the teams membership response.
    authmembershipsuseremail : bool
        Whether or not to show user emails in the teams membership response.
    authmembershipsmfa : bool
        Whether or not to show user MFA status in the teams membership response.
    authinvalidatesessions : bool
        Whether or not all existing sessions should be invalidated on password change
    oauthproviders : List[AuthProvider]
        List of Auth Providers.
    platforms : List[Union[PlatformWeb, PlatformApple, PlatformAndroid, PlatformWindows, PlatformLinux]]
        List of Platforms.
    webhooks : List[Webhook]
        List of Webhooks.
    keys : List[Key]
        List of API Keys.
    devkeys : List[DevKey]
        List of dev keys.
    smtpenabled : bool
        Status for custom SMTP
    smtpsendername : str
        SMTP sender name
    smtpsenderemail : str
        SMTP sender email
    smtpreplyto : str
        SMTP reply to email
    smtphost : str
        SMTP server host name
    smtpport : float
        SMTP server port
    smtpusername : str
        SMTP server username
    smtppassword : str
        SMTP server password
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
    authemailpassword : bool
        Email/Password auth method status
    authusersauthmagicurl : bool
        Magic URL auth method status
    authemailotp : bool
        Email (OTP) auth method status
    authanonymous : bool
        Anonymous auth method status
    authinvites : bool
        Invites auth method status
    authjwt : bool
        JWT auth method status
    authphone : bool
        Phone auth method status
    servicestatusforaccount : bool
        Account service status
    servicestatusforavatars : bool
        Avatars service status
    servicestatusfordatabases : bool
        Databases (legacy) service status
    servicestatusfortablesdb : bool
        TablesDB service status
    servicestatusforlocale : bool
        Locale service status
    servicestatusforhealth : bool
        Health service status
    servicestatusforproject : bool
        Project service status
    servicestatusforstorage : bool
        Storage service status
    servicestatusforteams : bool
        Teams service status
    servicestatusforusers : bool
        Users service status
    servicestatusforvcs : bool
        VCS service status
    servicestatusforsites : bool
        Sites service status
    servicestatusforfunctions : bool
        Functions service status
    servicestatusforproxy : bool
        Proxy service status
    servicestatusforgraphql : bool
        GraphQL service status
    servicestatusformigrations : bool
        Migrations service status
    servicestatusformessaging : bool
        Messaging service status
    protocolstatusforrest : bool
        REST protocol status
    protocolstatusforgraphql : bool
        GraphQL protocol status
    protocolstatusforwebsocket : bool
        Websocket protocol status
    region : str
        Project region
    billinglimits : BillingLimits
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
    description: str = Field(..., alias='description')
    teamid: str = Field(..., alias='teamId')
    logo: str = Field(..., alias='logo')
    url: str = Field(..., alias='url')
    legalname: str = Field(..., alias='legalName')
    legalcountry: str = Field(..., alias='legalCountry')
    legalstate: str = Field(..., alias='legalState')
    legalcity: str = Field(..., alias='legalCity')
    legaladdress: str = Field(..., alias='legalAddress')
    legaltaxid: str = Field(..., alias='legalTaxId')
    authduration: float = Field(..., alias='authDuration')
    authlimit: float = Field(..., alias='authLimit')
    authsessionslimit: float = Field(..., alias='authSessionsLimit')
    authpasswordhistory: float = Field(..., alias='authPasswordHistory')
    authpassworddictionary: bool = Field(..., alias='authPasswordDictionary')
    authpersonaldatacheck: bool = Field(..., alias='authPersonalDataCheck')
    authdisposableemails: bool = Field(..., alias='authDisposableEmails')
    authcanonicalemails: bool = Field(..., alias='authCanonicalEmails')
    authfreeemails: bool = Field(..., alias='authFreeEmails')
    authmocknumbers: List[MockNumber] = Field(..., alias='authMockNumbers')
    authsessionalerts: bool = Field(..., alias='authSessionAlerts')
    authmembershipsusername: bool = Field(..., alias='authMembershipsUserName')
    authmembershipsuseremail: bool = Field(..., alias='authMembershipsUserEmail')
    authmembershipsmfa: bool = Field(..., alias='authMembershipsMfa')
    authinvalidatesessions: bool = Field(..., alias='authInvalidateSessions')
    oauthproviders: List[AuthProvider] = Field(..., alias='oAuthProviders')
    platforms: List[Union[PlatformWeb, PlatformApple, PlatformAndroid, PlatformWindows, PlatformLinux]] = Field(..., alias='platforms')
    webhooks: List[Webhook] = Field(..., alias='webhooks')
    keys: List[Key] = Field(..., alias='keys')
    devkeys: List[DevKey] = Field(..., alias='devKeys')
    smtpenabled: bool = Field(..., alias='smtpEnabled')
    smtpsendername: str = Field(..., alias='smtpSenderName')
    smtpsenderemail: str = Field(..., alias='smtpSenderEmail')
    smtpreplyto: str = Field(..., alias='smtpReplyTo')
    smtphost: str = Field(..., alias='smtpHost')
    smtpport: float = Field(..., alias='smtpPort')
    smtpusername: str = Field(..., alias='smtpUsername')
    smtppassword: str = Field(..., alias='smtpPassword')
    smtpsecure: str = Field(..., alias='smtpSecure')
    pingcount: float = Field(..., alias='pingCount')
    pingedat: str = Field(..., alias='pingedAt')
    labels: List[Any] = Field(..., alias='labels')
    status: str = Field(..., alias='status')
    authemailpassword: bool = Field(..., alias='authEmailPassword')
    authusersauthmagicurl: bool = Field(..., alias='authUsersAuthMagicURL')
    authemailotp: bool = Field(..., alias='authEmailOtp')
    authanonymous: bool = Field(..., alias='authAnonymous')
    authinvites: bool = Field(..., alias='authInvites')
    authjwt: bool = Field(..., alias='authJWT')
    authphone: bool = Field(..., alias='authPhone')
    servicestatusforaccount: bool = Field(..., alias='serviceStatusForAccount')
    servicestatusforavatars: bool = Field(..., alias='serviceStatusForAvatars')
    servicestatusfordatabases: bool = Field(..., alias='serviceStatusForDatabases')
    servicestatusfortablesdb: bool = Field(..., alias='serviceStatusForTablesdb')
    servicestatusforlocale: bool = Field(..., alias='serviceStatusForLocale')
    servicestatusforhealth: bool = Field(..., alias='serviceStatusForHealth')
    servicestatusforproject: bool = Field(..., alias='serviceStatusForProject')
    servicestatusforstorage: bool = Field(..., alias='serviceStatusForStorage')
    servicestatusforteams: bool = Field(..., alias='serviceStatusForTeams')
    servicestatusforusers: bool = Field(..., alias='serviceStatusForUsers')
    servicestatusforvcs: bool = Field(..., alias='serviceStatusForVcs')
    servicestatusforsites: bool = Field(..., alias='serviceStatusForSites')
    servicestatusforfunctions: bool = Field(..., alias='serviceStatusForFunctions')
    servicestatusforproxy: bool = Field(..., alias='serviceStatusForProxy')
    servicestatusforgraphql: bool = Field(..., alias='serviceStatusForGraphql')
    servicestatusformigrations: bool = Field(..., alias='serviceStatusForMigrations')
    servicestatusformessaging: bool = Field(..., alias='serviceStatusForMessaging')
    protocolstatusforrest: bool = Field(..., alias='protocolStatusForRest')
    protocolstatusforgraphql: bool = Field(..., alias='protocolStatusForGraphql')
    protocolstatusforwebsocket: bool = Field(..., alias='protocolStatusForWebsocket')
    region: str = Field(..., alias='region')
    billinglimits: BillingLimits = Field(..., alias='billingLimits')
    blocks: List[Block] = Field(..., alias='blocks')
    consoleaccessedat: str = Field(..., alias='consoleAccessedAt')
