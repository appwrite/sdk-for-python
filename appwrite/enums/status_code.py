from enum import Enum

class StatusCode(Enum):
    MOVED_PERMANENTLY_301 = "301"
    FOUND_302 = "302"
    TEMPORARY_REDIRECT_307 = "307"
    PERMANENT_REDIRECT_308 = "308"
