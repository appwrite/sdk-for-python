from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .o_auth2_github import OAuth2Github
from .o_auth2_discord import OAuth2Discord
from .o_auth2_figma import OAuth2Figma
from .o_auth2_dropbox import OAuth2Dropbox
from .o_auth2_dailymotion import OAuth2Dailymotion
from .o_auth2_bitbucket import OAuth2Bitbucket
from .o_auth2_bitly import OAuth2Bitly
from .o_auth2_box import OAuth2Box
from .o_auth2_autodesk import OAuth2Autodesk
from .o_auth2_google import OAuth2Google
from .o_auth2_zoom import OAuth2Zoom
from .o_auth2_zoho import OAuth2Zoho
from .o_auth2_yandex import OAuth2Yandex
from .o_auth2_x import OAuth2X
from .o_auth2_word_press import OAuth2WordPress
from .o_auth2_twitch import OAuth2Twitch
from .o_auth2_stripe import OAuth2Stripe
from .o_auth2_spotify import OAuth2Spotify
from .o_auth2_slack import OAuth2Slack
from .o_auth2_podio import OAuth2Podio
from .o_auth2_notion import OAuth2Notion
from .o_auth2_salesforce import OAuth2Salesforce
from .o_auth2_yahoo import OAuth2Yahoo
from .o_auth2_linkedin import OAuth2Linkedin
from .o_auth2_disqus import OAuth2Disqus
from .o_auth2_amazon import OAuth2Amazon
from .o_auth2_etsy import OAuth2Etsy
from .o_auth2_facebook import OAuth2Facebook
from .o_auth2_tradeshift import OAuth2Tradeshift
from .o_auth2_paypal import OAuth2Paypal
from .o_auth2_gitlab import OAuth2Gitlab
from .o_auth2_authentik import OAuth2Authentik
from .o_auth2_auth0 import OAuth2Auth0
from .o_auth2_fusion_auth import OAuth2FusionAuth
from .o_auth2_keycloak import OAuth2Keycloak
from .o_auth2_oidc import OAuth2Oidc
from .o_auth2_apple import OAuth2Apple
from .o_auth2_okta import OAuth2Okta
from .o_auth2_kick import OAuth2Kick
from .o_auth2_microsoft import OAuth2Microsoft

class OAuth2ProviderList(AppwriteModel):
    """
    OAuth2 Providers List

    Attributes
    ----------
    total : float
        Total number of OAuth2 providers in the given project.
    providers : List[Union[OAuth2Github, OAuth2Discord, OAuth2Figma, OAuth2Dropbox, OAuth2Dailymotion, OAuth2Bitbucket, OAuth2Bitly, OAuth2Box, OAuth2Autodesk, OAuth2Google, OAuth2Zoom, OAuth2Zoho, OAuth2Yandex, OAuth2X, OAuth2WordPress, OAuth2Twitch, OAuth2Stripe, OAuth2Spotify, OAuth2Slack, OAuth2Podio, OAuth2Notion, OAuth2Salesforce, OAuth2Yahoo, OAuth2Linkedin, OAuth2Disqus, OAuth2Amazon, OAuth2Etsy, OAuth2Facebook, OAuth2Tradeshift, OAuth2Paypal, OAuth2Gitlab, OAuth2Authentik, OAuth2Auth0, OAuth2FusionAuth, OAuth2Keycloak, OAuth2Oidc, OAuth2Apple, OAuth2Okta, OAuth2Kick, OAuth2Microsoft]]
        List of OAuth2 providers.
    """
    total: float = Field(..., alias='total')
    providers: List[Union[OAuth2Github, OAuth2Discord, OAuth2Figma, OAuth2Dropbox, OAuth2Dailymotion, OAuth2Bitbucket, OAuth2Bitly, OAuth2Box, OAuth2Autodesk, OAuth2Google, OAuth2Zoom, OAuth2Zoho, OAuth2Yandex, OAuth2X, OAuth2WordPress, OAuth2Twitch, OAuth2Stripe, OAuth2Spotify, OAuth2Slack, OAuth2Podio, OAuth2Notion, OAuth2Salesforce, OAuth2Yahoo, OAuth2Linkedin, OAuth2Disqus, OAuth2Amazon, OAuth2Etsy, OAuth2Facebook, OAuth2Tradeshift, OAuth2Paypal, OAuth2Gitlab, OAuth2Authentik, OAuth2Auth0, OAuth2FusionAuth, OAuth2Keycloak, OAuth2Oidc, OAuth2Apple, OAuth2Okta, OAuth2Kick, OAuth2Microsoft]] = Field(..., alias='providers')
