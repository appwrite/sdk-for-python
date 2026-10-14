from enum import Enum


class OAuth2Auth0Prompt(Enum):
    NONE = "none"
    LOGIN = "login"
    CONSENT = "consent"
