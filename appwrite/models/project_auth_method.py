from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
