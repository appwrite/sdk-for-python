from enum import Enum


class VideoCaptionStatus(Enum):
    PENDING = "pending"
    STARTED = "started"
    READY = "ready"
    ERROR = "error"
    ABORTED = "aborted"
