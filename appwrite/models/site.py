from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

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
    buildspecification: str = Field(..., alias='buildSpecification')
    runtimespecification: str = Field(..., alias='runtimeSpecification')
    buildruntime: str = Field(..., alias='buildRuntime')
    adapter: str = Field(..., alias='adapter')
    fallbackfile: str = Field(..., alias='fallbackFile')
