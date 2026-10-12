from enum import Enum


class ProjectOAuth2MicrosoftPrompt(Enum):
    NONE = "none"
    LOGIN = "login"
    CONSENT = "consent"
    SELECT_ACCOUNT = "select_account"
