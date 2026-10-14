from enum import Enum


class OAuth2OktaPrompt(Enum):
    NONE = "none"
    LOGIN = "login"
    CONSENT = "consent"
