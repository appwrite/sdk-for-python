from enum import Enum


class WafRuleAction(Enum):
    BYPASS = "bypass"
    DENY = "deny"
    CHALLENGE = "challenge"
    RATELIMIT = "rateLimit"
    REDIRECT = "redirect"
