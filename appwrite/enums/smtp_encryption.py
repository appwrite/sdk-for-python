from enum import Enum

class SmtpEncryption(Enum):
    NONE = "none"
    SSL = "ssl"
    TLS = "tls"
