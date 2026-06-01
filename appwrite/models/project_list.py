from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .project import Project

class ProjectList(AppwriteModel):
    """
    Projects List

    Attributes
    ----------
    total : float
        Total number of projects that matched your query.
    projects : List[Project]
        List of projects.
    """
    total: float = Field(..., alias='total')
    projects: List[Project] = Field(..., alias='projects')
