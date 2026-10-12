from enum import Enum


class DomainTransferStatusEnum(Enum):
    TRANSFERRABLE = "transferrable"
    NOT_TRANSFERRABLE = "not_transferrable"
    PENDING_OWNER = "pending_owner"
    PENDING_ADMIN = "pending_admin"
    PENDING_REGISTRY = "pending_registry"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    SERVICE_UNAVAILABLE = "service_unavailable"
