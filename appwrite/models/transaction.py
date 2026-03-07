from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel

class Transaction(AppwriteModel):
    """
    Transaction

    Attributes
    ----------
    id : str
        Transaction ID.
    createdat : str
        Transaction creation time in ISO 8601 format.
    updatedat : str
        Transaction update date in ISO 8601 format.
    status : str
        Current status of the transaction. One of: pending, committing, committed, rolled_back, failed.
    operations : float
        Number of operations in the transaction.
    expiresat : str
        Expiration time in ISO 8601 format.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    status: str = Field(..., alias='status')
    operations: float = Field(..., alias='operations')
    expiresat: str = Field(..., alias='expiresAt')
