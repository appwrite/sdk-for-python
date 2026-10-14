from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class DedicatedDatabaseBackupStorage(AppwriteModel):
    """
    BackupStorageConfig

    Attributes
    ----------
    provider : str
        Storage provider. Possible values: s3 (Amazon S3 or S3-compatible), gcs (Google Cloud Storage), azure (Azure Blob Storage).
    bucket : str
        Storage bucket or container name.
    region : str
        Storage region.
    prefix : str
        Object key prefix for backups.
    endpoint : str
        Custom endpoint for S3-compatible storage.
    """

    provider: str = Field(..., alias='provider')
    bucket: str = Field(..., alias='bucket')
    region: str = Field(..., alias='region')
    prefix: str = Field(..., alias='prefix')
    endpoint: str = Field(..., alias='endpoint')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if 'provider' not in data:
            data['provider'] = ''
        if 'bucket' not in data:
            data['bucket'] = ''
        if 'region' not in data:
            data['region'] = ''
        if 'prefix' not in data:
            data['prefix'] = 'backups/'
        if 'endpoint' not in data:
            data['endpoint'] = ''
        return data
