from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class BillingPlanAddonDetails(AppwriteModel):
    """
    Details

    Attributes
    ----------
    supported : bool
        Is the addon supported in the plan?
    planincluded : float
        Addon plan included value
    limit : float
        Addon limit
    type : str
        Addon type
    currency : str
        Price currency
    price : float
        Price
    value : float
        Resource value
    invoicedesc : str
        Description on invoice
    """
    supported: bool = Field(..., alias='supported')
    planincluded: float = Field(..., alias='planIncluded')
    limit: float = Field(..., alias='limit')
    type: str = Field(..., alias='type')
    currency: str = Field(..., alias='currency')
    price: float = Field(..., alias='price')
    value: float = Field(..., alias='value')
    invoicedesc: str = Field(..., alias='invoiceDesc')
