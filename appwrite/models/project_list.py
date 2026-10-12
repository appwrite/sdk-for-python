from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
