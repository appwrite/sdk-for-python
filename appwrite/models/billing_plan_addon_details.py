from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    currency : Optional[str]
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
    currency: Optional[str] = Field(default=None, alias='currency')
    price: float = Field(..., alias='price')
    value: float = Field(..., alias='value')
    invoicedesc: str = Field(..., alias='invoiceDesc')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'supported' not in data:
            data['supported'] = False
        if 'planIncluded' not in data and 'planincluded' not in data:
            data['planIncluded'] = 0
        if 'limit' not in data:
            data['limit'] = 0
        if 'type' not in data:
            data['type'] = 'numeric'
        if 'price' not in data:
            data['price'] = 0
        if 'value' not in data:
            data['value'] = 0
        if 'invoiceDesc' not in data and 'invoicedesc' not in data:
            data['invoiceDesc'] = ''
        return data
