from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .oauth2_project import Oauth2Project


class Oauth2ProjectList(AppwriteModel):
    """
    OAuth2 accessible projects list

    Attributes
    ----------
    total : float
        Total number of projects that matched your query.
    projects : List[Oauth2Project]
        List of projects.
    """

    total: float = Field(..., alias='total')
    projects: List[Oauth2Project] = Field(..., alias='projects')

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
