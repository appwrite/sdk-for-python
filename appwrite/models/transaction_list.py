from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .transaction import Transaction


class TransactionList(AppwriteModel):
    """
    Transaction List

    Attributes
    ----------
    total : float
        Total number of transactions that matched your query.
    transactions : List[Transaction]
        List of transactions.
    """

    total: float = Field(..., alias='total')
    transactions: List[Transaction] = Field(..., alias='transactions')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'transactions' not in data:
            data['transactions'] = []
        return data
