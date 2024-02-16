from enum import Enum

class Factor(Enum):
    TOTP = "totp"
    PHONE = "phone"
    EMAIL = "email"
