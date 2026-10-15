from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.project_protocol_id import ProjectProtocolId


class ProjectProtocol(AppwriteModel):
    """
    ProjectProtocol

    Attributes
    ----------
    id : ProjectProtocolId
        Protocol ID.
    enabled : bool
        Protocol status.
    """

    id: ProjectProtocolId = Field(..., alias='$id')
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
