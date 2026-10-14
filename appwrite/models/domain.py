from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
