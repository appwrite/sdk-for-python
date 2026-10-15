from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
        if 'status' not in data:
            data['status'] = 'pending'
        if 'operations' not in data:
            data['operations'] = 0
        if 'expiresAt' not in data and 'expiresat' not in data:
            data['expiresAt'] = ''
        return data
