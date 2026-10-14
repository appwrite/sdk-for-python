from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'name' not in data:
            data['name'] = ''
        if 'unit' not in data:
            data['unit'] = ''
        if 'currency' not in data:
            data['currency'] = ''
        if 'price' not in data:
            data['price'] = 0
        if 'value' not in data:
            data['value'] = 0
        if 'invoiceDesc' not in data and 'invoicedesc' not in data:
            data['invoiceDesc'] = ''
        return data
