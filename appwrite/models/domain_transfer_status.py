from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.domain_transfer_status_enum import DomainTransferStatusEnum


class DomainTransferStatus(AppwriteModel):
    """
    domainTransferStatus

    Attributes
    ----------
    status : DomainTransferStatusEnum
        Transfer status.
    reason : str
        Additional transfer status information.
    timestamp : str
        Transfer status timestamp in ISO 8601 format.
    """

    status: DomainTransferStatusEnum = Field(..., alias='status')
    reason: str = Field(..., alias='reason')
    timestamp: str = Field(..., alias='timestamp')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'status' not in data:
            data['status'] = 'pending_registry'
        if 'reason' not in data:
            data['reason'] = ''
        if 'timestamp' not in data:
            data['timestamp'] = ''
        return data
