from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .bucket import Bucket


class BucketList(AppwriteModel):
    """
    Buckets List

    Attributes
    ----------
    total : float
        Total number of buckets that matched your query.
    buckets : List[Bucket]
        List of buckets.
    """

    total: float = Field(..., alias='total')
    buckets: List[Bucket] = Field(..., alias='buckets')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
