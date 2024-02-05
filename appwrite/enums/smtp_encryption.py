from enum import Enum

class SMTPEncryption(Enum):
    NONE = "none"
    SSL = "ssl"
    TLS = "tls"
