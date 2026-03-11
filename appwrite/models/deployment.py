from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
