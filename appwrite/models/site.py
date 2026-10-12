from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from .variable import Variable


class Site(AppwriteModel):
    """
    Site

    Attributes
    ----------
    id : str
        Site ID.
    createdat : str
        Site creation date in ISO 8601 format.
    updatedat : str
        Site update date in ISO 8601 format.
    name : str
        Site name.
    enabled : bool
        Site enabled.
    live : bool
        Is the site deployed with the latest configuration? This is set to false if you&#039;ve changed an environment variables, entrypoint, commands, or other settings that needs redeploy to be applied. When the value is false, redeploy the site to update it with the latest configuration.
    logging : bool
        When disabled, request logs will exclude logs and errors, and site responses will be slightly faster.
    framework : str
        Site framework.
    deploymentretention : float
        How many days to keep the non-active deployments before they will be automatically deleted.
    deploymentid : str
        Site&#039;s active deployment ID.
    deploymentcreatedat : str
        Active deployment creation date in ISO 8601 format.
    deploymentscreenshotlight : str
        Screenshot of active deployment with light theme preference file ID.
    deploymentscreenshotdark : str
        Screenshot of active deployment with dark theme preference file ID.
    latestdeploymentid : str
        Site&#039;s latest deployment ID.
    latestdeploymentcreatedat : str
        Latest deployment creation date in ISO 8601 format.
    latestdeploymentstatus : str
        Status of latest deployment. Possible values are &quot;waiting&quot;, &quot;processing&quot;, &quot;building&quot;, &quot;ready&quot;, and &quot;failed&quot;.
    scopes : List[Any]
        Allowed permission scopes.
    vars : List[Variable]
        Site variables.
    timeout : float
        Site request timeout in seconds.
    installcommand : str
        The install command used to install the site dependencies.
    buildcommand : str
        The build command used to build the site.
    startcommand : str
        Custom command to use when starting site runtime.
    outputdirectory : str
        The directory where the site build output is located.
    installationid : str
        Site VCS (Version Control System) installation id.
    providerrepositoryid : str
        VCS (Version Control System) Repository ID
    providerbranch : str
        VCS (Version Control System) branch name
    providerrootdirectory : str
        Path to site in VCS (Version Control System) repository
    providersilentmode : bool
        Is VCS (Version Control System) connection is in silent mode? When in silence mode, no comments will be posted on the repository pull or merge requests
    providerbranches : List[Any]
        List of branch name patterns that trigger automatic deployments. Supports glob wildcards. Empty list deploys on all branches.
    providerpaths : List[Any]
        List of file path patterns that trigger automatic deployments. Supports glob wildcards. Empty list deploys on all file changes.
    buildspecification : str
        Machine specification for deployment builds.
    runtimespecification : str
        Machine specification for SSR executions.
    buildruntime : str
        Site build runtime.
    adapter : str
        Site framework adapter.
    fallbackfile : str
        Name of fallback file to use instead of 404 page. If null, Appwrite 404 page will be displayed.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    enabled: bool = Field(..., alias='enabled')
    live: bool = Field(..., alias='live')
    logging: bool = Field(..., alias='logging')
    framework: str = Field(..., alias='framework')
    deploymentretention: float = Field(..., alias='deploymentRetention')
    deploymentid: str = Field(..., alias='deploymentId')
    deploymentcreatedat: str = Field(..., alias='deploymentCreatedAt')
    deploymentscreenshotlight: str = Field(..., alias='deploymentScreenshotLight')
    deploymentscreenshotdark: str = Field(..., alias='deploymentScreenshotDark')
    latestdeploymentid: str = Field(..., alias='latestDeploymentId')
    latestdeploymentcreatedat: str = Field(..., alias='latestDeploymentCreatedAt')
    latestdeploymentstatus: str = Field(..., alias='latestDeploymentStatus')
    scopes: List[Any] = Field(..., alias='scopes')
    vars: List[Variable] = Field(..., alias='vars')
    timeout: float = Field(..., alias='timeout')
    installcommand: str = Field(..., alias='installCommand')
    buildcommand: str = Field(..., alias='buildCommand')
    startcommand: str = Field(..., alias='startCommand')
    outputdirectory: str = Field(..., alias='outputDirectory')
    installationid: str = Field(..., alias='installationId')
    providerrepositoryid: str = Field(..., alias='providerRepositoryId')
    providerbranch: str = Field(..., alias='providerBranch')
    providerrootdirectory: str = Field(..., alias='providerRootDirectory')
    providersilentmode: bool = Field(..., alias='providerSilentMode')
    providerbranches: List[Any] = Field(..., alias='providerBranches')
    providerpaths: List[Any] = Field(..., alias='providerPaths')
    buildspecification: str = Field(..., alias='buildSpecification')
    runtimespecification: str = Field(..., alias='runtimeSpecification')
    buildruntime: str = Field(..., alias='buildRuntime')
    adapter: str = Field(..., alias='adapter')
    fallbackfile: str = Field(..., alias='fallbackFile')

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
        if 'name' not in data:
            data['name'] = ''
        if 'enabled' not in data:
            data['enabled'] = True
        if 'live' not in data:
            data['live'] = True
        if 'logging' not in data:
            data['logging'] = True
        if 'framework' not in data:
            data['framework'] = ''
        if 'deploymentRetention' not in data and 'deploymentretention' not in data:
            data['deploymentRetention'] = 0
        if 'deploymentId' not in data and 'deploymentid' not in data:
            data['deploymentId'] = ''
        if 'deploymentCreatedAt' not in data and 'deploymentcreatedat' not in data:
            data['deploymentCreatedAt'] = ''
        if 'deploymentScreenshotLight' not in data and 'deploymentscreenshotlight' not in data:
            data['deploymentScreenshotLight'] = ''
        if 'deploymentScreenshotDark' not in data and 'deploymentscreenshotdark' not in data:
            data['deploymentScreenshotDark'] = ''
        if 'latestDeploymentId' not in data and 'latestdeploymentid' not in data:
            data['latestDeploymentId'] = ''
        if 'latestDeploymentCreatedAt' not in data and 'latestdeploymentcreatedat' not in data:
            data['latestDeploymentCreatedAt'] = ''
        if 'latestDeploymentStatus' not in data and 'latestdeploymentstatus' not in data:
            data['latestDeploymentStatus'] = ''
        if 'scopes' not in data:
            data['scopes'] = []
        if 'timeout' not in data:
            data['timeout'] = 15
        if 'installCommand' not in data and 'installcommand' not in data:
            data['installCommand'] = ''
        if 'buildCommand' not in data and 'buildcommand' not in data:
            data['buildCommand'] = ''
        if 'startCommand' not in data and 'startcommand' not in data:
            data['startCommand'] = ''
        if 'outputDirectory' not in data and 'outputdirectory' not in data:
            data['outputDirectory'] = ''
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
        if 'buildRuntime' not in data and 'buildruntime' not in data:
            data['buildRuntime'] = ''
        return data
