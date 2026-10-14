from enum import Enum


class ProjectOAuth2OktaPrompt(Enum):
    NONE = "none"
    LOGIN = "login"
    CONSENT = "consent"
