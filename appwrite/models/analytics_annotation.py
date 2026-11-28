from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class AnalyticsAnnotation(AppwriteModel):
    """
    AnalyticsAnnotation

    Attributes
    ----------
    id : str
        Annotation ID.
    createdat : str
        Annotation creation date in ISO 8601 format.
    updatedat : str
        Annotation update date in ISO 8601 format.
    propertyid : str
        ID of the analytics property the annotation belongs to.
    date : str
        Point in time the annotation marks, in ISO 8601 format.
    content : str
        Annotation text.
    userid : str
        ID of the user who created the annotation. Empty when it was created with an API key.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    propertyid: str = Field(..., alias='propertyId')
    date: str = Field(..., alias='date')
    content: str = Field(..., alias='content')
    userid: str = Field(..., alias='userId')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if 'propertyId' not in data and 'propertyid' not in data:
            data['propertyId'] = ''
        if 'date' not in data:
            data['date'] = ''
        if 'content' not in data:
            data['content'] = ''
        if 'userId' not in data and 'userid' not in data:
            data['userId'] = ''
        return data
