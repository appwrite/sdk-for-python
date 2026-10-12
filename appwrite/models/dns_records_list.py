from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
