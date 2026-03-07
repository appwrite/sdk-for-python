from typing import Any, Dict, List, Optional, Union

from pydantic import Field

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
    signature : str
        File MD5 signature.
    mimetype : str
        File mime type.
    sizeoriginal : float
        File original size in bytes.
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
    signature: str = Field(..., alias='signature')
    mimetype: str = Field(..., alias='mimeType')
    sizeoriginal: float = Field(..., alias='sizeOriginal')
    chunkstotal: float = Field(..., alias='chunksTotal')
    chunksuploaded: float = Field(..., alias='chunksUploaded')
    encryption: bool = Field(..., alias='encryption')
    compression: str = Field(..., alias='compression')
