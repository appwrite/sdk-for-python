from enum import Enum


class OAuth2MicrosoftPrompt(Enum):
    NONE = "none"
    LOGIN = "login"
    CONSENT = "consent"
    SELECT_ACCOUNT = "select_account"
