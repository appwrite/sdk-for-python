from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
        Record name or subdomain.
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
