from enum import Enum

class AttributeStatus(Enum):
    AVAILABLE = "available"
    PROCESSING = "processing"
    DELETING = "deleting"
    STUCK = "stuck"
    FAILED = "failed"
