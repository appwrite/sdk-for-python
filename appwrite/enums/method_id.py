from enum import Enum

class MethodId(Enum):
    EMAIL_PASSWORD = "email-password"
    MAGIC_URL = "magic-url"
    EMAIL_OTP = "email-otp"
    ANONYMOUS = "anonymous"
    INVITES = "invites"
    JWT = "jwt"
    PHONE = "phone"
