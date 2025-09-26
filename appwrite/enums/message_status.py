from enum import Enum

class MessageStatus(Enum):
    DRAFT = "draft"
    PROCESSING = "processing"
    SCHEDULED = "scheduled"
    SENT = "sent"
    FAILED = "failed"
