from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
