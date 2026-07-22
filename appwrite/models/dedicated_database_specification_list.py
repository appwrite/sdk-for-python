from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .dedicated_database_specification import DedicatedDatabaseSpecification
from .dedicated_database_specification_pricing import DedicatedDatabaseSpecificationPricing

class DedicatedDatabaseSpecificationList(AppwriteModel):
    """
    SpecificationList

    Attributes
    ----------
    specifications : List[DedicatedDatabaseSpecification]
        List of dedicated database specifications.
    total : float
        Total number of specifications.
    pricing : DedicatedDatabaseSpecificationPricing
        Overage and add-on pricing shared across all specifications.
    """
    specifications: List[DedicatedDatabaseSpecification] = Field(..., alias='specifications')
    total: float = Field(..., alias='total')
    pricing: DedicatedDatabaseSpecificationPricing = Field(..., alias='pricing')
