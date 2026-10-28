from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class DnsRecord(AppwriteModel):
    """
    DNSRecord

    Attributes
    ----------
    id : str
        DNS Record ID.
    createdat : str
        DNS Record creation time in ISO 8601 format.
    updatedat : str
        DNS Record update date in ISO 8601 format.
    type : str
        DNS record type (e.g. A, CNAME, MX).
    name : str
        Record name relative to the domain, or `@` for the domain itself.
    value : str
        Value of the record (IP address, domain, etc.).
    ttl : float
        Time to live (in seconds).
    priority : float
        Record priority (commonly used for MX).
    lock : bool
        Whether this record is locked (read-only).
    weight : float
        Record weight (used for SRV records).
    port : float
        Target port (used for SRV records).
    comment : str
        Comment for the DNS record.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    type: str = Field(..., alias='type')
    name: str = Field(..., alias='name')
    value: str = Field(..., alias='value')
    ttl: float = Field(..., alias='ttl')
    priority: float = Field(..., alias='priority')
    lock: bool = Field(..., alias='lock')
    weight: float = Field(..., alias='weight')
    port: float = Field(..., alias='port')
    comment: str = Field(..., alias='comment')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'type' not in data:
            data['type'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'value' not in data:
            data['value'] = ''
        if 'ttl' not in data:
            data['ttl'] = 3600
        if 'priority' not in data:
            data['priority'] = 0
        if 'lock' not in data:
            data['lock'] = False
        if 'weight' not in data:
            data['weight'] = 0
        if 'port' not in data:
            data['port'] = 0
        if 'comment' not in data:
            data['comment'] = ''
        return data
