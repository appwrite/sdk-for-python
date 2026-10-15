from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .app_secret import AppSecret


class App(AppwriteModel):
    """
    App

    Attributes
    ----------
    id : str
        App ID.
    createdat : str
        App creation time in ISO 8601 format.
    updatedat : str
        App update date in ISO 8601 format.
    name : str
        Application name.
    description : str
        Application description shown to users during OAuth2 consent.
    clienturi : str
        Application homepage URL shown to users during OAuth2 consent.
    logouri : str
        Application logo URL shown to users during OAuth2 consent.
    privacypolicyurl : str
        Application privacy policy URL shown to users during OAuth2 consent.
    termsurl : str
        Application terms of service URL shown to users during OAuth2 consent.
    contacts : List[Any]
        Application support or security contact emails.
    tagline : str
        Application tagline shown to users during OAuth2 consent.
    tags : List[Any]
        Application tags shown to users during OAuth2 consent.
    labels : List[Any]
        Application labels. Read-only for clients; only a server SDK using a project API key can update them.
    images : List[Any]
        Application image URLs shown to users during OAuth2 consent.
    supporturl : str
        Application support URL shown to users during OAuth2 consent.
    datadeletionurl : str
        Application data deletion URL shown to users during OAuth2 consent.
    redirecturis : List[Any]
        List of authorized redirect URIs. These URIs can be used to redirect users after they authenticate.
    postlogoutredirecturis : List[Any]
        List of authorized post-logout redirect URIs for OpenID Connect RP-Initiated Logout. The logout endpoint only redirects users to URIs in this list after ending their session.
    enabled : bool
        Whether the app is enabled or not.
    type : str
        OAuth2 client type. `public` for SPAs, mobile, and native apps that cannot keep a client secret (PKCE required); `confidential` for server-side clients that authenticate with a client secret.
    deviceflow : bool
        Whether this client may use the OAuth2 Device Authorization Grant (RFC 8628).
    teamid : str
        ID of team that owns the application, if owned by team. Otherwise, user ID will be used.
    userid : str
        ID of user who owns the application, if owned by user. Otherwise, team ID will be used.
    installationscopes : List[Any]
        Scopes the application requests when installed on a team. Organization-level and project-level scopes only.
    installationredirecturl : str
        URL users are redirected to after creating or updating an installation of this application. Empty for no redirect.
    secrets : List[AppSecret]
        List of application secrets.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    description: str = Field(..., alias='description')
    clienturi: str = Field(..., alias='clientUri')
    logouri: str = Field(..., alias='logoUri')
    privacypolicyurl: str = Field(..., alias='privacyPolicyUrl')
    termsurl: str = Field(..., alias='termsUrl')
    contacts: List[Any] = Field(..., alias='contacts')
    tagline: str = Field(..., alias='tagline')
    tags: List[Any] = Field(..., alias='tags')
    labels: List[Any] = Field(..., alias='labels')
    images: List[Any] = Field(..., alias='images')
    supporturl: str = Field(..., alias='supportUrl')
    datadeletionurl: str = Field(..., alias='dataDeletionUrl')
    redirecturis: List[Any] = Field(..., alias='redirectUris')
    postlogoutredirecturis: List[Any] = Field(..., alias='postLogoutRedirectUris')
    enabled: bool = Field(..., alias='enabled')
    type: str = Field(..., alias='type')
    deviceflow: bool = Field(..., alias='deviceFlow')
    teamid: str = Field(..., alias='teamId')
    userid: str = Field(..., alias='userId')
    installationscopes: List[Any] = Field(..., alias='installationScopes')
    installationredirecturl: str = Field(..., alias='installationRedirectUrl')
    secrets: List[AppSecret] = Field(..., alias='secrets')

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
        if 'description' not in data:
            data['description'] = ''
        if 'clientUri' not in data and 'clienturi' not in data:
            data['clientUri'] = ''
        if 'logoUri' not in data and 'logouri' not in data:
            data['logoUri'] = ''
        if 'privacyPolicyUrl' not in data and 'privacypolicyurl' not in data:
            data['privacyPolicyUrl'] = ''
        if 'termsUrl' not in data and 'termsurl' not in data:
            data['termsUrl'] = ''
        if 'contacts' not in data:
            data['contacts'] = []
        if 'tagline' not in data:
            data['tagline'] = ''
        if 'tags' not in data:
            data['tags'] = []
        if 'labels' not in data:
            data['labels'] = []
        if 'images' not in data:
            data['images'] = []
        if 'supportUrl' not in data and 'supporturl' not in data:
            data['supportUrl'] = ''
        if 'dataDeletionUrl' not in data and 'datadeletionurl' not in data:
            data['dataDeletionUrl'] = ''
        if 'redirectUris' not in data and 'redirecturis' not in data:
            data['redirectUris'] = []
        if 'postLogoutRedirectUris' not in data and 'postlogoutredirecturis' not in data:
            data['postLogoutRedirectUris'] = []
        if 'enabled' not in data:
            data['enabled'] = True
        if 'type' not in data:
            data['type'] = 'confidential'
        if 'deviceFlow' not in data and 'deviceflow' not in data:
            data['deviceFlow'] = False
        if 'teamId' not in data and 'teamid' not in data:
            data['teamId'] = ''
        if 'userId' not in data and 'userid' not in data:
            data['userId'] = ''
        if 'installationScopes' not in data and 'installationscopes' not in data:
            data['installationScopes'] = []
        if 'installationRedirectUrl' not in data and 'installationredirecturl' not in data:
            data['installationRedirectUrl'] = ''
        if 'secrets' not in data:
            data['secrets'] = []
        return data
