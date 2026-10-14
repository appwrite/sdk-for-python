from enum import Enum


class OAuth2KakaoPrompt(Enum):
    NONE = "none"
    LOGIN = "login"
    CREATE = "create"
    SELECT_ACCOUNT = "select_account"
