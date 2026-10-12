from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.domain_transfer_status_enum import DomainTransferStatusEnum
from .dns_record import DnsRecord


class Domain(AppwriteModel):
    """
    Domain

    Attributes
    ----------
    id : str
        Domain ID.
    createdat : str
        Domain creation time in ISO 8601 format.
    updatedat : str
        Domain update date in ISO 8601 format.
    domain : str
        Domain name.
    registrar : str
        Domain registrar (e.g. &quot;appwrite&quot; or &quot;third_party&quot;).
    nameservers : str
        Nameservers setting. &quot;Appwrite&quot; or empty string.
    expire : str
        Domain expiry date in ISO 8601 format.
    renewal : str
        Domain renewal date in ISO 8601 format.
    autorenewal : bool
        If set to true, the domain will automatically renew.
    renewalprice : float
        Renewal price (in cents).
    transferstatus : Optional[DomainTransferStatusEnum]
        Transfer status for domains being transferred in. Null when the domain is not being transferred.
    teamid : str
        Team ID.
    dnsrecords : List[DnsRecord]
        Dns records
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    domain: str = Field(..., alias='domain')
    registrar: str = Field(..., alias='registrar')
    nameservers: str = Field(..., alias='nameservers')
    expire: str = Field(..., alias='expire')
    renewal: str = Field(..., alias='renewal')
    autorenewal: bool = Field(..., alias='autoRenewal')
    renewalprice: float = Field(..., alias='renewalPrice')
    transferstatus: Optional[DomainTransferStatusEnum] = Field(default=None, alias='transferStatus')
    teamid: str = Field(..., alias='teamId')
    dnsrecords: List[DnsRecord] = Field(..., alias='dnsRecords')

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
        if 'domain' not in data:
            data['domain'] = ''
        if 'registrar' not in data:
            data['registrar'] = ''
        if 'nameservers' not in data:
            data['nameservers'] = ''
        if 'expire' not in data:
            data['expire'] = ''
        if 'renewal' not in data:
            data['renewal'] = ''
        if 'autoRenewal' not in data and 'autorenewal' not in data:
            data['autoRenewal'] = False
        if 'renewalPrice' not in data and 'renewalprice' not in data:
            data['renewalPrice'] = 0
        if 'teamId' not in data and 'teamid' not in data:
            data['teamId'] = ''
        return data
