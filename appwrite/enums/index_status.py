from enum import Enum

class IndexStatus(Enum):
    AVAILABLE = "available"
    PROCESSING = "processing"
    DELETING = "deleting"
    STUCK = "stuck"
    FAILED = "failed"
