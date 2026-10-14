from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class Bucket(AppwriteModel):
    """
    Bucket

    Attributes
    ----------
    id : str
        Bucket ID.
    createdat : str
        Bucket creation time in ISO 8601 format.
    updatedat : str
        Bucket update date in ISO 8601 format.
    permissions : List[Any]
        Bucket permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    filesecurity : bool
        Whether file-level security is enabled. [Learn more about permissions](https://appwrite.io/docs/permissions).
    name : str
        Bucket name.
    enabled : bool
        Bucket enabled.
    maximumfilesize : float
        Maximum file size supported.
    allowedfileextensions : List[Any]
        Allowed file extensions.
    compression : str
        Compression algorithm chosen for compression. Will be one of none, [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd).
    encryption : bool
        Bucket is encrypted.
    antivirus : bool
        Virus scanning is enabled.
    transformations : bool
        Image transformations are enabled.
    totalsize : float
        Total size of this bucket in bytes.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    filesecurity: bool = Field(..., alias='fileSecurity')
    name: str = Field(..., alias='name')
    enabled: bool = Field(..., alias='enabled')
    maximumfilesize: float = Field(..., alias='maximumFileSize')
    allowedfileextensions: List[Any] = Field(..., alias='allowedFileExtensions')
    compression: str = Field(..., alias='compression')
    encryption: bool = Field(..., alias='encryption')
    antivirus: bool = Field(..., alias='antivirus')
    transformations: bool = Field(..., alias='transformations')
    totalsize: float = Field(..., alias='totalSize')

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
        if '$permissions' not in data and 'permissions' not in data:
            data['$permissions'] = []
        if 'fileSecurity' not in data and 'filesecurity' not in data:
            data['fileSecurity'] = False
        if 'name' not in data:
            data['name'] = ''
        if 'enabled' not in data:
            data['enabled'] = True
        if 'maximumFileSize' not in data and 'maximumfilesize' not in data:
            data['maximumFileSize'] = 0
        if 'allowedFileExtensions' not in data and 'allowedfileextensions' not in data:
            data['allowedFileExtensions'] = []
        if 'compression' not in data:
            data['compression'] = ''
        if 'encryption' not in data:
            data['encryption'] = True
        if 'antivirus' not in data:
            data['antivirus'] = True
        if 'transformations' not in data:
            data['transformations'] = True
        if 'totalSize' not in data and 'totalsize' not in data:
            data['totalSize'] = 0
        return data
