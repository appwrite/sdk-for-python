from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .membership import Membership

class MembershipList(AppwriteModel):
    """
    Memberships List

    Attributes
    ----------
    total : float
        Total number of memberships that matched your query.
    memberships : List[Membership]
        List of memberships.
    """
    total: float = Field(..., alias='total')
    memberships: List[Membership] = Field(..., alias='memberships')
