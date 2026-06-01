from enum import Enum

class ProjectPolicyId(Enum):
    PASSWORD_DICTIONARY = "password-dictionary"
    PASSWORD_HISTORY = "password-history"
    PASSWORD_PERSONAL_DATA = "password-personal-data"
    SESSION_ALERT = "session-alert"
    SESSION_DURATION = "session-duration"
    SESSION_INVALIDATION = "session-invalidation"
    SESSION_LIMIT = "session-limit"
    USER_LIMIT = "user-limit"
    MEMBERSHIP_PRIVACY = "membership-privacy"
    DENY_ALIASED_EMAIL = "deny-aliased-email"
    DENY_DISPOSABLE_EMAIL = "deny-disposable-email"
    DENY_FREE_EMAIL = "deny-free-email"
