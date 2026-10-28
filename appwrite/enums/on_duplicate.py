from enum import Enum


class OnDuplicate(Enum):
    FAIL = "fail"
    SKIP = "skip"
    OVERWRITE = "overwrite"
