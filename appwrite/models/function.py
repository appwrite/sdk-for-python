from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
from .variable import Variable

class Function(AppwriteModel):
    """
    Function

    Attributes
    ----------
    id : str
        Function ID.
    createdat : str
        Function creation date in ISO 8601 format.
    updatedat : str
        Function update date in ISO 8601 format.
    execute : List[Any]
        Execution permissions.
    name : str
        Function name.
    enabled : bool
        Function enabled.
    live : bool
        Is the function deployed with the latest configuration? This is set to false if you&#039;ve changed an environment variables, entrypoint, commands, or other settings that needs redeploy to be applied. When the value is false, redeploy the function to update it with the latest configuration.
    logging : bool
        When disabled, executions will exclude logs and errors, and will be slightly faster.
    runtime : str
        Function execution and build runtime.
    deploymentid : str
        Function&#039;s active deployment ID.
    deploymentcreatedat : str
        Active deployment creation date in ISO 8601 format.
    latestdeploymentid : str
        Function&#039;s latest deployment ID.
    latestdeploymentcreatedat : str
        Latest deployment creation date in ISO 8601 format.
    latestdeploymentstatus : str
        Status of latest deployment. Possible values are &quot;waiting&quot;, &quot;processing&quot;, &quot;building&quot;, &quot;ready&quot;, and &quot;failed&quot;.
    scopes : List[Any]
        Allowed permission scopes.
    vars : List[Variable]
        Function variables.
    events : List[Any]
        Function trigger events.
    schedule : str
        Function execution schedule in CRON format.
    timeout : float
        Function execution timeout in seconds.
    entrypoint : str
        The entrypoint file used to execute the deployment.
    commands : str
        The build command used to build the deployment.
    version : str
        Version of Open Runtimes used for the function.
    installationid : str
        Function VCS (Version Control System) installation id.
    providerrepositoryid : str
        VCS (Version Control System) Repository ID
    providerbranch : str
        VCS (Version Control System) branch name
    providerrootdirectory : str
        Path to function in VCS (Version Control System) repository
    providersilentmode : bool
        Is VCS (Version Control System) connection is in silent mode? When in silence mode, no comments will be posted on the repository pull or merge requests
    specification : str
        Machine specification for builds and executions.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    execute: List[Any] = Field(..., alias='execute')
    name: str = Field(..., alias='name')
    enabled: bool = Field(..., alias='enabled')
    live: bool = Field(..., alias='live')
    logging: bool = Field(..., alias='logging')
    runtime: str = Field(..., alias='runtime')
    deploymentid: str = Field(..., alias='deploymentId')
    deploymentcreatedat: str = Field(..., alias='deploymentCreatedAt')
    latestdeploymentid: str = Field(..., alias='latestDeploymentId')
    latestdeploymentcreatedat: str = Field(..., alias='latestDeploymentCreatedAt')
    latestdeploymentstatus: str = Field(..., alias='latestDeploymentStatus')
    scopes: List[Any] = Field(..., alias='scopes')
    vars: List[Variable] = Field(..., alias='vars')
    events: List[Any] = Field(..., alias='events')
    schedule: str = Field(..., alias='schedule')
    timeout: float = Field(..., alias='timeout')
    entrypoint: str = Field(..., alias='entrypoint')
    commands: str = Field(..., alias='commands')
    version: str = Field(..., alias='version')
    installationid: str = Field(..., alias='installationId')
    providerrepositoryid: str = Field(..., alias='providerRepositoryId')
    providerbranch: str = Field(..., alias='providerBranch')
    providerrootdirectory: str = Field(..., alias='providerRootDirectory')
    providersilentmode: bool = Field(..., alias='providerSilentMode')
    specification: str = Field(..., alias='specification')
