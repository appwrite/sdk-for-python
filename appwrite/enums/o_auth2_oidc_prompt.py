from enum import Enum

class OAuth2OidcPrompt(Enum):
    NONE = "none"
    LOGIN = "login"
    CONSENT = "consent"
    SELECT_ACCOUNT = "select_account"
