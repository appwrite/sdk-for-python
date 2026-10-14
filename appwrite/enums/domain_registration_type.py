from enum import Enum


class DomainRegistrationType(Enum):
    NEW = "new"
    TRANSFER = "transfer"
    RENEWAL = "renewal"
    TRADE = "trade"
