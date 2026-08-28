from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .dedicated_database_branch import DedicatedDatabaseBranch


class DedicatedDatabaseBranchList(AppwriteModel):
    """
    BranchList

    Attributes
    ----------
    total : float
        Total number of branches.
    branches : List[DedicatedDatabaseBranch]
        List of branches.
    """

    total: float = Field(..., alias='total')
    branches: List[DedicatedDatabaseBranch] = Field(..., alias='branches')
