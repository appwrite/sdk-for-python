from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
