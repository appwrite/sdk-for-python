from enum import Enum


class AlertComparator(Enum):
    GREATERTHAN = "greaterThan"
    GREATERTHANEQUAL = "greaterThanEqual"
    LESSTHAN = "lessThan"
    LESSTHANEQUAL = "lessThanEqual"
