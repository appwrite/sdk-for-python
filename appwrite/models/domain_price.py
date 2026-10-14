from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel


class DomainPrice(AppwriteModel):
    """
    DomainPrice

    Attributes
    ----------
    domain : str
        Domain name.
    tld : str
        Top-level domain for the requested domain.
    available : bool
        Whether the domain is currently available for registration.
    price : Optional[float]
        Domain registration price. Null when the price could not be resolved, for example for an unsupported TLD.
    periodyears : float
        Price period in years.
    premium : bool
        Whether the domain is a premium domain.
    renewalprice : Optional[float]
        Domain renewal price for the same period. Null when the domain was not priced or the registrar has no renewal price for it.
    renewalperiodyears : float
        Renewal price period in years.
    """

    domain: str = Field(..., alias='domain')
    tld: str = Field(..., alias='tld')
    available: bool = Field(..., alias='available')
    price: Optional[float] = Field(default=None, alias='price')
    periodyears: float = Field(..., alias='periodYears')
    premium: bool = Field(..., alias='premium')
    renewalprice: Optional[float] = Field(default=None, alias='renewalPrice')
    renewalperiodyears: float = Field(..., alias='renewalPeriodYears')
