from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
    secrets: List[AppSecret] = Field(..., alias='secrets')
