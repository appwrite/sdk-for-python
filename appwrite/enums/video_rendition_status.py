from enum import Enum


class VideoRenditionStatus(Enum):
    PENDING = "pending"
    STARTED = "started"
    ENDED = "ended"
    READY = "ready"
    ERROR = "error"
    ABORTED = "aborted"
