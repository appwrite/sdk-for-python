from enum import Enum

class DeploymentStatus(Enum):
    WAITING = "waiting"
    PROCESSING = "processing"
    BUILDING = "building"
    READY = "ready"
    FAILED = "failed"
