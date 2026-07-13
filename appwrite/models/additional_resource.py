from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class AdditionalResource(AppwriteModel):
    """
    AdditionalResource

    Attributes
    ----------
    name : str
        Resource name
    unit : str
        Resource unit
    currency : str
        Price currency
    price : float
        Price
    value : float
        Resource value
    invoicedesc : str
        Description on invoice
    """
    name: str = Field(..., alias='name')
    unit: str = Field(..., alias='unit')
    currency: str = Field(..., alias='currency')
    price: float = Field(..., alias='price')
    value: float = Field(..., alias='value')
    invoicedesc: str = Field(..., alias='invoiceDesc')
