from enum import Enum

class ProjectPolicy(Enum):
    PASSWORD_DICTIONARY = "password-dictionary"
    PASSWORD_HISTORY = "password-history"
    PASSWORD_PERSONAL_DATA = "password-personal-data"
    SESSION_ALERT = "session-alert"
    SESSION_DURATION = "session-duration"
    SESSION_INVALIDATION = "session-invalidation"
    SESSION_LIMIT = "session-limit"
    USER_LIMIT = "user-limit"
    MEMBERSHIP_PRIVACY = "membership-privacy"
