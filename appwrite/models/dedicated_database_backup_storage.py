from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
