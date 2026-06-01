from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class BillingLimits(AppwriteModel):
    """
    Limits

    Attributes
    ----------
    bandwidth : Optional[float]
        Bandwidth limit
    storage : Optional[float]
        Storage limit
    users : Optional[float]
        Users limit
    executions : Optional[float]
        Executions limit
    gbhours : Optional[float]
        GBHours limit
    imagetransformations : Optional[float]
        Image transformations limit
    authphone : Optional[float]
        Auth phone limit
    budgetlimit : Optional[float]
        Budget limit percentage
    """
    bandwidth: Optional[float] = Field(default=None, alias='bandwidth')
    storage: Optional[float] = Field(default=None, alias='storage')
    users: Optional[float] = Field(default=None, alias='users')
    executions: Optional[float] = Field(default=None, alias='executions')
    gbhours: Optional[float] = Field(default=None, alias='GBHours')
    imagetransformations: Optional[float] = Field(default=None, alias='imageTransformations')
    authphone: Optional[float] = Field(default=None, alias='authPhone')
    budgetlimit: Optional[float] = Field(default=None, alias='budgetLimit')
