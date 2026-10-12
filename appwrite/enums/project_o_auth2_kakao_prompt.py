from enum import Enum


class ProjectOAuth2KakaoPrompt(Enum):
    NONE = "none"
    LOGIN = "login"
    CREATE = "create"
    SELECT_ACCOUNT = "select_account"
