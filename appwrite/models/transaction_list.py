from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
