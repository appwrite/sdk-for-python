from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class InsightCTA(AppwriteModel):
    """
    InsightCTA

    Attributes
    ----------
    label : str
        Human-readable label for the CTA, used in UI.
    service : str
        Public API service (SDK namespace) the client should invoke. Must match the engine that owns the resource — for index suggestions: databases (legacy), tablesDB, documentsDB, or vectorsDB.
    method : str
        Public API method on the chosen service the client should invoke when this CTA is triggered.
    params : Dict[str, Any]
        Parameter map the client should pass to the service method when this CTA is triggered. Keys match the target API&#039;s parameter names (e.g. databaseId/tableId/columns for tablesDB, databaseId/collectionId/attributes for the legacy Databases API).
    """
    label: str = Field(..., alias='label')
    service: str = Field(..., alias='service')
    method: str = Field(..., alias='method')
    params: Dict[str, Any] = Field(..., alias='params')
