from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .app_installation import AppInstallation


class AppInstallationList(AppwriteModel):
    """
    App installations list

    Attributes
    ----------
    total : float
        Total number of installations that matched your query.
    installations : List[AppInstallation]
        List of installations.
    """

    total: float = Field(..., alias='total')
    installations: List[AppInstallation] = Field(..., alias='installations')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        return data
