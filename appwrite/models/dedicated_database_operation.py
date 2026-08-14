from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel

class DedicatedDatabaseOperation(AppwriteModel):
    """
    Operation

    Attributes
    ----------
    id : str
        Operation ID.
    createdat : str
        Operation creation time in ISO 8601 format.
    databaseid : str
        Database ID the operation ran against.
    type : str
        Operation type, such as provision, update, restore, pausing, resuming, failover, backup-create or cross-region-enable.
    status : str
        Operation status. Possible values: running (in progress), completed (finished successfully), failed (ended in an error).
    attempts : float
        Number of times this operation has been attempted.
    requestedat : Optional[str]
        Time the operation was requested, in ISO 8601 format.
    startedat : Optional[str]
        Time the operation started, in ISO 8601 format.
    completedat : Optional[str]
        Time the operation reached a terminal state, in ISO 8601 format.
    errorcode : str
        Machine-readable failure code. `Interrupted` marks an attempt that ended before its outcome could be confirmed.
    errormessage : str
        Failure message if the operation failed.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    databaseid: str = Field(..., alias='databaseId')
    type: str = Field(..., alias='type')
    status: str = Field(..., alias='status')
    attempts: float = Field(..., alias='attempts')
    requestedat: Optional[str] = Field(default=None, alias='requestedAt')
    startedat: Optional[str] = Field(default=None, alias='startedAt')
    completedat: Optional[str] = Field(default=None, alias='completedAt')
    errorcode: str = Field(..., alias='errorCode')
    errormessage: str = Field(..., alias='errorMessage')
