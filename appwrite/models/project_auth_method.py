from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.project_auth_method_id import ProjectAuthMethodId


class ProjectAuthMethod(AppwriteModel):
    """
    ProjectAuthMethod

    Attributes
    ----------
    id : ProjectAuthMethodId
        Auth method ID.
    enabled : bool
        Auth method status.
    """

    id: ProjectAuthMethodId = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'enabled' not in data:
            data['enabled'] = True
        return data
