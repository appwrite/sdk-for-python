from enum import Enum

class ProjectOAuth2GooglePrompt(Enum):
    NONE = "none"
    CONSENT = "consent"
    SELECT_ACCOUNT = "select_account"
