from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from ..enums.health_antivirus_status import HealthAntivirusStatus

class HealthAntivirus(AppwriteModel):
    """
    Health Antivirus

    Attributes
    ----------
    version : str
        Antivirus version.
    status : HealthAntivirusStatus
        Antivirus status. Possible values are: `disabled`, `offline`, `online`
    """
    version: str = Field(..., alias='version')
    status: HealthAntivirusStatus = Field(..., alias='status')
