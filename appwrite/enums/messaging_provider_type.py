from enum import Enum

class MessagingProviderType(Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"
