from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class BillingLimits(AppwriteModel):
    """
    BillingLimits

    Attributes
    ----------
    bandwidth : float
        Bandwidth limit
    storage : float
        Storage limit
    users : float
        Users limit
    executions : float
        Executions limit
    gbhours : float
        GBHours limit
    imagetransformations : float
        Image transformations limit
    authphone : float
        Auth phone limit
    budgetlimit : float
        Budget limit percentage
    """
    bandwidth: float = Field(..., alias='bandwidth')
    storage: float = Field(..., alias='storage')
    users: float = Field(..., alias='users')
    executions: float = Field(..., alias='executions')
    gbhours: float = Field(..., alias='GBHours')
    imagetransformations: float = Field(..., alias='imageTransformations')
    authphone: float = Field(..., alias='authPhone')
    budgetlimit: float = Field(..., alias='budgetLimit')
