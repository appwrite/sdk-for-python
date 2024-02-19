from enum import Enum

class AuthenticationFactor(Enum):
    TOTP = "totp"
    PHONE = "phone"
    EMAIL = "email"
