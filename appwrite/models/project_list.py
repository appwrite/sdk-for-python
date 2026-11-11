from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .project import Project

T = TypeVar('T')


class ProjectList(AppwriteModel, Generic[T]):
    """
    Projects List

    Attributes
    ----------
    total : float
        Total number of projects that matched your query.
    projects : List[Project[T]]
        List of projects.
    """

    total: float = Field(..., alias='total')
    projects: List[Project[T]] = Field(..., alias='projects')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'projects' not in data:
            data['projects'] = []
        return data

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'ProjectList[T]':
        """Create ProjectList instance with typed data."""
        instance = cls.model_validate(data)
        if 'projects' in data and data['projects'] is not None:
            instance.projects = [Project.with_data(row, model_type) for row in data['projects']]
        return instance
