from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel


class DatabaseMigration(AppwriteModel):
    """
    Database Migration

    Attributes
    ----------
    id : str
        Database migration ID.
    createdat : str
        Migration creation time in ISO 8601 format.
    updatedat : str
        Migration update time in ISO 8601 format.
    projectid : str
        Project ID that owns the migrating database.
    databaseid : str
        Logical database ID being migrated.
    specification : str
        Dedicated compute specification provisioned for the migration target.
    phase : str
        Migration phase. Possible values: pending, provisioned, capturing, backfilling, catching_up, verifying, ready_to_cutover, cutover, soaking, done, failed, rolled_back.
    attempt : float
        Number of times a migration step has failed and been recorded.
    lasterror : str
        Reason the most recent migration step failed, empty while none has.
    lagdocuments : float
        Number of documents still pending replication to the target.
    changelogwatermark : float
        Highest source changelog sequence applied to the target so far.
    verifiedat : str
        Time the migrated data was verified against the source in ISO 8601 format.
    cutoverat : str
        Time routing was flipped to the target in ISO 8601 format.
    soakuntil : str
        Time the post-cutover soak window ends in ISO 8601 format.
    autocutover : bool
        Whether the migration cuts over automatically once ready. Set when the migration is created and never changed afterwards, so it always reports what was asked for.
    cutoverrequested : bool
        Whether a cutover has been requested and not yet attempted. Set by the cutover endpoint and cleared when the attempt is made, so a cutover that fails a check parks the migration again rather than retrying on its own.
    paused : bool
        Whether the migration is paused.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    projectid: str = Field(..., alias='projectId')
    databaseid: str = Field(..., alias='databaseId')
    specification: str = Field(..., alias='specification')
    phase: str = Field(..., alias='phase')
    attempt: float = Field(..., alias='attempt')
    lasterror: str = Field(..., alias='lastError')
    lagdocuments: float = Field(..., alias='lagDocuments')
    changelogwatermark: float = Field(..., alias='changelogWatermark')
    verifiedat: str = Field(..., alias='verifiedAt')
    cutoverat: str = Field(..., alias='cutoverAt')
    soakuntil: str = Field(..., alias='soakUntil')
    autocutover: bool = Field(..., alias='autoCutover')
    cutoverrequested: bool = Field(..., alias='cutoverRequested')
    paused: bool = Field(..., alias='paused')

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
        if 'projectId' not in data and 'projectid' not in data:
            data['projectId'] = ''
        if 'databaseId' not in data and 'databaseid' not in data:
            data['databaseId'] = ''
        if 'specification' not in data:
            data['specification'] = ''
        if 'phase' not in data:
            data['phase'] = 'pending'
        if 'attempt' not in data:
            data['attempt'] = 0
        if 'lastError' not in data and 'lasterror' not in data:
            data['lastError'] = ''
        if 'lagDocuments' not in data and 'lagdocuments' not in data:
            data['lagDocuments'] = 0
        if 'changelogWatermark' not in data and 'changelogwatermark' not in data:
            data['changelogWatermark'] = 0
        if 'verifiedAt' not in data and 'verifiedat' not in data:
            data['verifiedAt'] = ''
        if 'cutoverAt' not in data and 'cutoverat' not in data:
            data['cutoverAt'] = ''
        if 'soakUntil' not in data and 'soakuntil' not in data:
            data['soakUntil'] = ''
        if 'autoCutover' not in data and 'autocutover' not in data:
            data['autoCutover'] = True
        if 'cutoverRequested' not in data and 'cutoverrequested' not in data:
            data['cutoverRequested'] = False
        if 'paused' not in data:
            data['paused'] = False
        return data
