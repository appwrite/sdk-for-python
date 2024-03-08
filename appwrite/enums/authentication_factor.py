from enum import Enum

class AuthenticationFactor(Enum):
    EMAIL = "email"
    PHONE = "phone"
    TOTP = "totp"
    RECOVERYCODE = "recoverycode"
