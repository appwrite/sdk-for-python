from enum import Enum

class ProxyRuleStatus(Enum):
    UNVERIFIED = "unverified"
    VERIFYING = "verifying"
    VERIFIED = "verified"
