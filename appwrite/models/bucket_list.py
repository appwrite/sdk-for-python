from typing import Any, Dict, List, Optional, Union

from pydantic import Field

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
