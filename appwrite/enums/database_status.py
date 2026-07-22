from enum import Enum

class DatabaseStatus(Enum):
    PROVISIONING = "provisioning"
    READY = "ready"
    INACTIVE = "inactive"
    PAUSED = "paused"
    FAILED = "failed"
    DELETING = "deleting"
    DELETED = "deleted"
    RESTORING = "restoring"
    SCALING = "scaling"
    UPGRADING = "upgrading"
    MIGRATING = "migrating"
    PAUSING = "pausing"
    RESUMING = "resuming"
    FAILING_OVER = "failing-over"
