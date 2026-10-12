from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.deployment_status import DeploymentStatus


class Deployment(AppwriteModel):
    """
    Deployment

    Attributes
    ----------
    id : str
        Deployment ID.
    createdat : str
        Deployment creation date in ISO 8601 format.
    updatedat : str
        Deployment update date in ISO 8601 format.
    type : str
        Type of deployment.
    resourceid : str
        Resource ID.
    resourcetype : str
        Resource type.
    entrypoint : str
        The entrypoint file to use to execute the deployment code.
    sourcesize : float
        The code size in bytes.
    buildsize : float
        The build output size in bytes.
    totalsize : float
        The total size in bytes (source and build output).
    buildid : str
        The current build ID.
    activate : bool
        Whether the deployment should be automatically activated.
    screenshotlight : str
        Screenshot with light theme preference file ID.
    screenshotdark : str
        Screenshot with dark theme preference file ID.
    status : DeploymentStatus
        The deployment status. Possible values are &quot;waiting&quot;, &quot;processing&quot;, &quot;building&quot;, &quot;ready&quot;, &quot;canceled&quot; and &quot;failed&quot;.
    buildlogs : str
        The build logs.
    buildduration : float
        The current build time in seconds.
    providerrepositoryname : str
        The name of the vcs provider repository
    providerrepositoryowner : str
        The name of the vcs provider repository owner
    providerrepositoryurl : str
        The url of the vcs provider repository
    providercommithash : str
        The commit hash of the vcs commit
    providercommitauthorurl : str
        The url of vcs commit author
    providercommitauthor : str
        The name of vcs commit author
    providercommitmessage : str
        The commit message
    providercommiturl : str
        The url of the vcs commit
    providerbranch : str
        The branch of the vcs repository
    providerbranchurl : str
        The branch of the vcs repository
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    type: str = Field(..., alias='type')
    resourceid: str = Field(..., alias='resourceId')
    resourcetype: str = Field(..., alias='resourceType')
    entrypoint: str = Field(..., alias='entrypoint')
    sourcesize: float = Field(..., alias='sourceSize')
    buildsize: float = Field(..., alias='buildSize')
    totalsize: float = Field(..., alias='totalSize')
    buildid: str = Field(..., alias='buildId')
    activate: bool = Field(..., alias='activate')
    screenshotlight: str = Field(..., alias='screenshotLight')
    screenshotdark: str = Field(..., alias='screenshotDark')
    status: DeploymentStatus = Field(..., alias='status')
    buildlogs: str = Field(..., alias='buildLogs')
    buildduration: float = Field(..., alias='buildDuration')
    providerrepositoryname: str = Field(..., alias='providerRepositoryName')
    providerrepositoryowner: str = Field(..., alias='providerRepositoryOwner')
    providerrepositoryurl: str = Field(..., alias='providerRepositoryUrl')
    providercommithash: str = Field(..., alias='providerCommitHash')
    providercommitauthorurl: str = Field(..., alias='providerCommitAuthorUrl')
    providercommitauthor: str = Field(..., alias='providerCommitAuthor')
    providercommitmessage: str = Field(..., alias='providerCommitMessage')
    providercommiturl: str = Field(..., alias='providerCommitUrl')
    providerbranch: str = Field(..., alias='providerBranch')
    providerbranchurl: str = Field(..., alias='providerBranchUrl')

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
        if 'type' not in data:
            data['type'] = ''
        if 'resourceId' not in data and 'resourceid' not in data:
            data['resourceId'] = ''
        if 'resourceType' not in data and 'resourcetype' not in data:
            data['resourceType'] = ''
        if 'entrypoint' not in data:
            data['entrypoint'] = ''
        if 'sourceSize' not in data and 'sourcesize' not in data:
            data['sourceSize'] = 0
        if 'buildSize' not in data and 'buildsize' not in data:
            data['buildSize'] = 0
        if 'totalSize' not in data and 'totalsize' not in data:
            data['totalSize'] = 0
        if 'buildId' not in data and 'buildid' not in data:
            data['buildId'] = ''
        if 'activate' not in data:
            data['activate'] = False
        if 'screenshotLight' not in data and 'screenshotlight' not in data:
            data['screenshotLight'] = ''
        if 'screenshotDark' not in data and 'screenshotdark' not in data:
            data['screenshotDark'] = ''
        if 'buildLogs' not in data and 'buildlogs' not in data:
            data['buildLogs'] = ''
        if 'buildDuration' not in data and 'buildduration' not in data:
            data['buildDuration'] = 0
        if 'providerRepositoryName' not in data and 'providerrepositoryname' not in data:
            data['providerRepositoryName'] = ''
        if 'providerRepositoryOwner' not in data and 'providerrepositoryowner' not in data:
            data['providerRepositoryOwner'] = ''
        if 'providerRepositoryUrl' not in data and 'providerrepositoryurl' not in data:
            data['providerRepositoryUrl'] = ''
        if 'providerCommitHash' not in data and 'providercommithash' not in data:
            data['providerCommitHash'] = ''
        if 'providerCommitAuthorUrl' not in data and 'providercommitauthorurl' not in data:
            data['providerCommitAuthorUrl'] = ''
        if 'providerCommitAuthor' not in data and 'providercommitauthor' not in data:
            data['providerCommitAuthor'] = ''
        if 'providerCommitMessage' not in data and 'providercommitmessage' not in data:
            data['providerCommitMessage'] = ''
        if 'providerCommitUrl' not in data and 'providercommiturl' not in data:
            data['providerCommitUrl'] = ''
        if 'providerBranch' not in data and 'providerbranch' not in data:
            data['providerBranch'] = ''
        if 'providerBranchUrl' not in data and 'providerbranchurl' not in data:
            data['providerBranchUrl'] = ''
        return data
