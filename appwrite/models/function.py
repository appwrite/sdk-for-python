from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    description : str
        Optional description for the function.
    enabled : bool
        Function enabled.
    live : bool
        Is the function deployed with the latest configuration? This is set to false if you&#039;ve changed an environment variables, entrypoint, commands, or other settings that needs redeploy to be applied. When the value is false, redeploy the function to update it with the latest configuration.
    logging : bool
        When disabled, executions will exclude logs and errors, and will be slightly faster.
    runtime : str
        Function execution and build runtime.
    deploymentretention : float
        How many days to keep the non-active deployments before they will be automatically deleted.
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
    interval : Optional[float]
        Minutes between scheduled executions. 0 when the function has no interval.
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
    providerbranches : List[Any]
        List of branch name patterns that trigger automatic deployments. Supports glob wildcards. Empty list deploys on all branches.
    providerpaths : List[Any]
        List of file path patterns that trigger automatic deployments. Supports glob wildcards. Empty list deploys on all file changes.
    buildspecification : str
        Machine specification for deployment builds.
    runtimespecification : str
        Machine specification for executions.
    emailenabled : bool
        Whether inbound email (SMTP) may trigger this function. Opt-in; default is false. When disabled, recipients for this function are rejected.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    execute: List[Any] = Field(..., alias='execute')
    name: str = Field(..., alias='name')
    description: str = Field(..., alias='description')
    enabled: bool = Field(..., alias='enabled')
    live: bool = Field(..., alias='live')
    logging: bool = Field(..., alias='logging')
    runtime: str = Field(..., alias='runtime')
    deploymentretention: float = Field(..., alias='deploymentRetention')
    deploymentid: str = Field(..., alias='deploymentId')
    deploymentcreatedat: str = Field(..., alias='deploymentCreatedAt')
    latestdeploymentid: str = Field(..., alias='latestDeploymentId')
    latestdeploymentcreatedat: str = Field(..., alias='latestDeploymentCreatedAt')
    latestdeploymentstatus: str = Field(..., alias='latestDeploymentStatus')
    scopes: List[Any] = Field(..., alias='scopes')
    vars: List[Variable] = Field(..., alias='vars')
    events: List[Any] = Field(..., alias='events')
    schedule: str = Field(..., alias='schedule')
    interval: Optional[float] = Field(default=None, alias='interval')
    timeout: float = Field(..., alias='timeout')
    entrypoint: str = Field(..., alias='entrypoint')
    commands: str = Field(..., alias='commands')
    version: str = Field(..., alias='version')
    installationid: str = Field(..., alias='installationId')
    providerrepositoryid: str = Field(..., alias='providerRepositoryId')
    providerbranch: str = Field(..., alias='providerBranch')
    providerrootdirectory: str = Field(..., alias='providerRootDirectory')
    providersilentmode: bool = Field(..., alias='providerSilentMode')
    providerbranches: List[Any] = Field(..., alias='providerBranches')
    providerpaths: List[Any] = Field(..., alias='providerPaths')
    buildspecification: str = Field(..., alias='buildSpecification')
    runtimespecification: str = Field(..., alias='runtimeSpecification')
    emailenabled: bool = Field(..., alias='emailEnabled')

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
        if 'execute' not in data:
            data['execute'] = []
        if 'name' not in data:
            data['name'] = ''
        if 'description' not in data:
            data['description'] = ''
        if 'enabled' not in data:
            data['enabled'] = True
        if 'live' not in data:
            data['live'] = True
        if 'logging' not in data:
            data['logging'] = True
        if 'runtime' not in data:
            data['runtime'] = ''
        if 'deploymentRetention' not in data and 'deploymentretention' not in data:
            data['deploymentRetention'] = 0
        if 'deploymentId' not in data and 'deploymentid' not in data:
            data['deploymentId'] = ''
        if 'deploymentCreatedAt' not in data and 'deploymentcreatedat' not in data:
            data['deploymentCreatedAt'] = ''
        if 'latestDeploymentId' not in data and 'latestdeploymentid' not in data:
            data['latestDeploymentId'] = ''
        if 'latestDeploymentCreatedAt' not in data and 'latestdeploymentcreatedat' not in data:
            data['latestDeploymentCreatedAt'] = ''
        if 'latestDeploymentStatus' not in data and 'latestdeploymentstatus' not in data:
            data['latestDeploymentStatus'] = ''
        if 'scopes' not in data:
            data['scopes'] = []
        if 'vars' not in data:
            data['vars'] = []
        if 'events' not in data:
            data['events'] = []
        if 'schedule' not in data:
            data['schedule'] = ''
        if 'timeout' not in data:
            data['timeout'] = 15
        if 'entrypoint' not in data:
            data['entrypoint'] = ''
        if 'commands' not in data:
            data['commands'] = ''
        if 'version' not in data:
            data['version'] = 'v5'
        if 'installationId' not in data and 'installationid' not in data:
            data['installationId'] = ''
        if 'providerRepositoryId' not in data and 'providerrepositoryid' not in data:
            data['providerRepositoryId'] = ''
        if 'providerBranch' not in data and 'providerbranch' not in data:
            data['providerBranch'] = ''
        if 'providerRootDirectory' not in data and 'providerrootdirectory' not in data:
            data['providerRootDirectory'] = ''
        if 'providerSilentMode' not in data and 'providersilentmode' not in data:
            data['providerSilentMode'] = False
        if 'providerBranches' not in data and 'providerbranches' not in data:
            data['providerBranches'] = []
        if 'providerPaths' not in data and 'providerpaths' not in data:
            data['providerPaths'] = []
        if 'buildSpecification' not in data and 'buildspecification' not in data:
            data['buildSpecification'] = 's-1vcpu-512mb'
        if 'runtimeSpecification' not in data and 'runtimespecification' not in data:
            data['runtimeSpecification'] = 's-1vcpu-512mb'
        if 'emailEnabled' not in data and 'emailenabled' not in data:
            data['emailEnabled'] = False
        return data
