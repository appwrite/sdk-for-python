from enum import Enum


class VideoTimelineStatus(Enum):
    PENDING = "pending"
    STARTED = "started"
    READY = "ready"
    SKIPPED = "skipped"
    ERROR = "error"
