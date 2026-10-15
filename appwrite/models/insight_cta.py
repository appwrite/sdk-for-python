from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'label' not in data:
            data['label'] = ''
        if 'service' not in data:
            data['service'] = ''
        if 'method' not in data:
            data['method'] = ''
        if 'params' not in data:
            data['params'] = {}
        return data
