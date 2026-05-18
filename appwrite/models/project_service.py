from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.project_service_id import ProjectServiceId

class ProjectService(AppwriteModel):
    """
    ProjectService

    Attributes
    ----------
    id : ProjectServiceId
        Service ID.
    enabled : bool
        Service status.
    """
    id: ProjectServiceId = Field(..., alias='$id')
    enabled: bool = Field(..., alias='enabled')
