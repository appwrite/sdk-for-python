from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class File(AppwriteModel):
    """
    File

    Attributes
    ----------
    id : str
        File ID.
    bucketid : str
        Bucket ID.
    createdat : str
        File creation date in ISO 8601 format.
    updatedat : str
        File update date in ISO 8601 format.
    permissions : List[Any]
        File permissions. [Learn more about permissions](https://appwrite.io/docs/permissions).
    name : str
        File name.
    folder : str
        Virtual folder containing the file, with a trailing slash. Empty for the bucket root.
    key : str
        Full virtual path of the file: the folder followed by the file name.
    signature : str
        File MD5 signature.
    mimetype : str
        File mime type.
    sizeoriginal : float
        File original size in bytes.
    sizeactual : float
        File actual stored size in bytes after compression and/or encryption.
    chunkstotal : float
        Total number of chunks available
    chunksuploaded : float
        Total number of chunks uploaded
    encryption : bool
        Whether file contents are encrypted at rest.
    compression : str
        Compression algorithm used for the file. Will be one of none, [gzip](https://en.wikipedia.org/wiki/Gzip), or [zstd](https://en.wikipedia.org/wiki/Zstd).
    """

    id: str = Field(..., alias='$id')
    bucketid: str = Field(..., alias='bucketId')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    name: str = Field(..., alias='name')
    folder: str = Field(..., alias='folder')
    key: str = Field(..., alias='key')
    signature: str = Field(..., alias='signature')
    mimetype: str = Field(..., alias='mimeType')
    sizeoriginal: float = Field(..., alias='sizeOriginal')
    sizeactual: float = Field(..., alias='sizeActual')
    chunkstotal: float = Field(..., alias='chunksTotal')
    chunksuploaded: float = Field(..., alias='chunksUploaded')
    encryption: bool = Field(..., alias='encryption')
    compression: str = Field(..., alias='compression')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'bucketId' not in data and 'bucketid' not in data:
            data['bucketId'] = ''
        if '$createdAt' not in data and 'createdat' not in data:
            data['$createdAt'] = ''
        if '$updatedAt' not in data and 'updatedat' not in data:
            data['$updatedAt'] = ''
        if '$permissions' not in data and 'permissions' not in data:
            data['$permissions'] = []
        if 'name' not in data:
            data['name'] = ''
        if 'folder' not in data:
            data['folder'] = ''
        if 'key' not in data:
            data['key'] = ''
        if 'signature' not in data:
            data['signature'] = ''
        if 'mimeType' not in data and 'mimetype' not in data:
            data['mimeType'] = ''
        if 'sizeOriginal' not in data and 'sizeoriginal' not in data:
            data['sizeOriginal'] = 0
        if 'sizeActual' not in data and 'sizeactual' not in data:
            data['sizeActual'] = 0
        if 'chunksTotal' not in data and 'chunkstotal' not in data:
            data['chunksTotal'] = 0
        if 'chunksUploaded' not in data and 'chunksuploaded' not in data:
            data['chunksUploaded'] = 0
        if 'encryption' not in data:
            data['encryption'] = False
        if 'compression' not in data:
            data['compression'] = 'none'
        return data
