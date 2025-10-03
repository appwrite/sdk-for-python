from enum import Enum

class ExecutionTrigger(Enum):
    HTTP = "http"
    SCHEDULE = "schedule"
    EVENT = "event"
