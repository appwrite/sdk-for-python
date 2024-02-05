from enum import Enum

class MessageType(Enum):
    DRAFT = "draft"
    CANCELLED = "cancelled"
    PROCESSING = "processing"
