from enum import Enum


class ProjectOAuth2Auth0Prompt(Enum):
    NONE = "none"
    LOGIN = "login"
    CONSENT = "consent"
