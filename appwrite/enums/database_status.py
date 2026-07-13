from enum import Enum

class DatabaseStatus(Enum):
    PROVISIONING = "provisioning"
    READY = "ready"
    FAILED = "failed"
