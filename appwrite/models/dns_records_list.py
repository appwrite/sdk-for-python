from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .dns_record import DnsRecord


class DnsRecordsList(AppwriteModel):
    """
    DNS records list

    Attributes
    ----------
    total : float
        Total number of dnsRecords that matched your query.
    dnsrecords : List[DnsRecord]
        List of dnsRecords.
    """

    total: float = Field(..., alias='total')
    dnsrecords: List[DnsRecord] = Field(..., alias='dnsRecords')
