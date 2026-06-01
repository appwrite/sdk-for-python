from enum import Enum

class StatusCode(Enum):
    MOVEDPERMANENTLY = "301"
    FOUND = "302"
    TEMPORARYREDIRECT = "307"
    PERMANENTREDIRECT = "308"
