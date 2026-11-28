from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .analytics_annotation import AnalyticsAnnotation


class AnalyticsAnnotationList(AppwriteModel):
    """
    Analytics annotations list

    Attributes
    ----------
    total : float
        Total number of annotations that matched your query.
    annotations : List[AnalyticsAnnotation]
        List of annotations.
    """

    total: float = Field(..., alias='total')
    annotations: List[AnalyticsAnnotation] = Field(..., alias='annotations')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'total' not in data:
            data['total'] = 0
        if 'annotations' not in data:
            data['annotations'] = []
        return data
