from enum import Enum

class OAuth2GooglePrompt(Enum):
    NONE = "none"
    CONSENT = "consent"
    SELECT_ACCOUNT = "select_account"
