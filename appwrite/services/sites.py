from ..service import Service
from typing import List, Dict, Any, Optional
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..enums.framework import Framework;
from ..enums.build_runtime import BuildRuntime;
from ..enums.adapter import Adapter;
from ..input_file import InputFile
from ..enums.template_reference_type import TemplateReferenceType;
from ..enums.vcs_reference_type import VCSReferenceType;
from ..enums.deployment_download_type import DeploymentDownloadType;

class Sites(Service):

    def __init__(self, client) -> None:
        super(Sites, self).__init__(client)

    def list(self, queries: Optional[List[str]] = None, search: Optional[str] = None, total: Optional[bool] = None) -> Dict[str, Any]:
        """
        Get a list of all the project's sites. You can use the query params to filter your results.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, enabled, framework, deploymentId, buildCommand, installCommand, outputDirectory, installationId
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites'
        api_params = {}

        if queries is not None:
            api_params['queries'] = queries
        if search is not None:
            api_params['search'] = search
        if total is not None:
            api_params['total'] = total

        return self.client.call('get', api_path, {
        }, api_params)

    def create(self, site_id: str, name: str, framework: Framework, build_runtime: BuildRuntime, enabled: Optional[bool] = None, logging: Optional[bool] = None, timeout: Optional[float] = None, install_command: Optional[str] = None, build_command: Optional[str] = None, output_directory: Optional[str] = None, adapter: Optional[Adapter] = None, installation_id: Optional[str] = None, fallback_file: Optional[str] = None, provider_repository_id: Optional[str] = None, provider_branch: Optional[str] = None, provider_silent_mode: Optional[bool] = None, provider_root_directory: Optional[str] = None, specification: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new site.

        Parameters
        ----------
        site_id : str
            Site ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Site name. Max length: 128 chars.
        framework : Framework
            Sites framework.
        build_runtime : BuildRuntime
            Runtime to use during build step.
        enabled : Optional[bool]
            Is site enabled? When set to 'disabled', users cannot access the site but Server SDKs with and API key can still access the site. No data is lost when this is toggled.
        logging : Optional[bool]
            When disabled, request logs will exclude logs and errors, and site responses will be slightly faster.
        timeout : Optional[float]
            Maximum request time in seconds.
        install_command : Optional[str]
            Install Command.
        build_command : Optional[str]
            Build Command.
        output_directory : Optional[str]
            Output Directory for site.
        adapter : Optional[Adapter]
            Framework adapter defining rendering strategy. Allowed values are: static, ssr
        installation_id : Optional[str]
            Appwrite Installation ID for VCS (Version Control System) deployment.
        fallback_file : Optional[str]
            Fallback file for single page application sites.
        provider_repository_id : Optional[str]
            Repository ID of the repo linked to the site.
        provider_branch : Optional[str]
            Production branch for the repo linked to the site.
        provider_silent_mode : Optional[bool]
            Is the VCS (Version Control System) connection in silent mode for the repo linked to the site? In silent mode, comments will not be made on commits and pull requests.
        provider_root_directory : Optional[str]
            Path to site code in the linked repo.
        specification : Optional[str]
            Framework specification for the site and builds.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if framework is None:
            raise AppwriteException('Missing required parameter: "framework"')

        if build_runtime is None:
            raise AppwriteException('Missing required parameter: "build_runtime"')


        api_params['siteId'] = site_id
        api_params['name'] = name
        api_params['framework'] = framework
        if enabled is not None:
            api_params['enabled'] = enabled
        if logging is not None:
            api_params['logging'] = logging
        if timeout is not None:
            api_params['timeout'] = timeout
        if install_command is not None:
            api_params['installCommand'] = install_command
        if build_command is not None:
            api_params['buildCommand'] = build_command
        if output_directory is not None:
            api_params['outputDirectory'] = output_directory
        api_params['buildRuntime'] = build_runtime
        if adapter is not None:
            api_params['adapter'] = adapter
        if installation_id is not None:
            api_params['installationId'] = installation_id
        if fallback_file is not None:
            api_params['fallbackFile'] = fallback_file
        if provider_repository_id is not None:
            api_params['providerRepositoryId'] = provider_repository_id
        if provider_branch is not None:
            api_params['providerBranch'] = provider_branch
        if provider_silent_mode is not None:
            api_params['providerSilentMode'] = provider_silent_mode
        if provider_root_directory is not None:
            api_params['providerRootDirectory'] = provider_root_directory
        if specification is not None:
            api_params['specification'] = specification

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_frameworks(self) -> Dict[str, Any]:
        """
        Get a list of all frameworks that are currently available on the server instance.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/frameworks'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def list_specifications(self) -> Dict[str, Any]:
        """
        List allowed site specifications for this instance.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/specifications'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def get(self, site_id: str) -> Dict[str, Any]:
        """
        Get a site by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', site_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update(self, site_id: str, name: str, framework: Framework, enabled: Optional[bool] = None, logging: Optional[bool] = None, timeout: Optional[float] = None, install_command: Optional[str] = None, build_command: Optional[str] = None, output_directory: Optional[str] = None, build_runtime: Optional[BuildRuntime] = None, adapter: Optional[Adapter] = None, fallback_file: Optional[str] = None, installation_id: Optional[str] = None, provider_repository_id: Optional[str] = None, provider_branch: Optional[str] = None, provider_silent_mode: Optional[bool] = None, provider_root_directory: Optional[str] = None, specification: Optional[str] = None) -> Dict[str, Any]:
        """
        Update site by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        name : str
            Site name. Max length: 128 chars.
        framework : Framework
            Sites framework.
        enabled : Optional[bool]
            Is site enabled? When set to 'disabled', users cannot access the site but Server SDKs with and API key can still access the site. No data is lost when this is toggled.
        logging : Optional[bool]
            When disabled, request logs will exclude logs and errors, and site responses will be slightly faster.
        timeout : Optional[float]
            Maximum request time in seconds.
        install_command : Optional[str]
            Install Command.
        build_command : Optional[str]
            Build Command.
        output_directory : Optional[str]
            Output Directory for site.
        build_runtime : Optional[BuildRuntime]
            Runtime to use during build step.
        adapter : Optional[Adapter]
            Framework adapter defining rendering strategy. Allowed values are: static, ssr
        fallback_file : Optional[str]
            Fallback file for single page application sites.
        installation_id : Optional[str]
            Appwrite Installation ID for VCS (Version Control System) deployment.
        provider_repository_id : Optional[str]
            Repository ID of the repo linked to the site.
        provider_branch : Optional[str]
            Production branch for the repo linked to the site.
        provider_silent_mode : Optional[bool]
            Is the VCS (Version Control System) connection in silent mode for the repo linked to the site? In silent mode, comments will not be made on commits and pull requests.
        provider_root_directory : Optional[str]
            Path to site code in the linked repo.
        specification : Optional[str]
            Framework specification for the site and builds.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if framework is None:
            raise AppwriteException('Missing required parameter: "framework"')

        api_path = api_path.replace('{siteId}', site_id)

        api_params['name'] = name
        api_params['framework'] = framework
        if enabled is not None:
            api_params['enabled'] = enabled
        if logging is not None:
            api_params['logging'] = logging
        if timeout is not None:
            api_params['timeout'] = timeout
        if install_command is not None:
            api_params['installCommand'] = install_command
        if build_command is not None:
            api_params['buildCommand'] = build_command
        if output_directory is not None:
            api_params['outputDirectory'] = output_directory
        if build_runtime is not None:
            api_params['buildRuntime'] = build_runtime
        if adapter is not None:
            api_params['adapter'] = adapter
        if fallback_file is not None:
            api_params['fallbackFile'] = fallback_file
        if installation_id is not None:
            api_params['installationId'] = installation_id
        if provider_repository_id is not None:
            api_params['providerRepositoryId'] = provider_repository_id
        if provider_branch is not None:
            api_params['providerBranch'] = provider_branch
        if provider_silent_mode is not None:
            api_params['providerSilentMode'] = provider_silent_mode
        if provider_root_directory is not None:
            api_params['providerRootDirectory'] = provider_root_directory
        if specification is not None:
            api_params['specification'] = specification

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete(self, site_id: str) -> Dict[str, Any]:
        """
        Delete a site by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', site_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_site_deployment(self, site_id: str, deployment_id: str) -> Dict[str, Any]:
        """
        Update the site active deployment. Use this endpoint to switch the code deployment that should be used when visitor opens your site.

        Parameters
        ----------
        site_id : str
            Site ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/deployment'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{siteId}', site_id)

        api_params['deploymentId'] = deployment_id

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_deployments(self, site_id: str, queries: Optional[List[str]] = None, search: Optional[str] = None, total: Optional[bool] = None) -> Dict[str, Any]:
        """
        Get a list of all the site's code deployments. You can use the query params to filter your results.

        Parameters
        ----------
        site_id : str
            Site ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: buildSize, sourceSize, totalSize, buildDuration, status, activate, type
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/deployments'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', site_id)

        if queries is not None:
            api_params['queries'] = queries
        if search is not None:
            api_params['search'] = search
        if total is not None:
            api_params['total'] = total

        return self.client.call('get', api_path, {
        }, api_params)

    def create_deployment(self, site_id: str, code: InputFile, activate: bool, install_command: Optional[str] = None, build_command: Optional[str] = None, output_directory: Optional[str] = None, on_progress = None) -> Dict[str, Any]:
        """
        Create a new site code deployment. Use this endpoint to upload a new version of your site code. To activate your newly uploaded code, you'll need to update the site's deployment to use your new deployment ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        code : InputFile
            Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.
        activate : bool
            Automatically activate the deployment when it is finished building.
        install_command : Optional[str]
            Install Commands.
        build_command : Optional[str]
            Build Commands.
        output_directory : Optional[str]
            Output Directory.
                on_progress : callable, optional
            Optional callback for upload progress
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/deployments'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        if activate is None:
            raise AppwriteException('Missing required parameter: "activate"')

        api_path = api_path.replace('{siteId}', site_id)

        if install_command is not None:
            api_params['installCommand'] = install_command
        if build_command is not None:
            api_params['buildCommand'] = build_command
        if output_directory is not None:
            api_params['outputDirectory'] = output_directory
        api_params['code'] = code
        api_params['activate'] = str(activate).lower() if type(activate) is bool else activate

        param_name = 'code'


        upload_id = ''

        return self.client.chunked_upload(api_path, {
            'content-type': 'multipart/form-data',
        }, api_params, param_name, on_progress, upload_id)

    def create_duplicate_deployment(self, site_id: str, deployment_id: str) -> Dict[str, Any]:
        """
        Create a new build for an existing site deployment. This endpoint allows you to rebuild a deployment with the updated site configuration, including its commands and output directory if they have been modified. The build process will be queued and executed asynchronously. The original deployment's code will be preserved and used for the new build.

        Parameters
        ----------
        site_id : str
            Site ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/deployments/duplicate'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{siteId}', site_id)

        api_params['deploymentId'] = deployment_id

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_template_deployment(self, site_id: str, repository: str, owner: str, root_directory: str, type: TemplateReferenceType, reference: str, activate: Optional[bool] = None) -> Dict[str, Any]:
        """
        Create a deployment based on a template.
        
        Use this endpoint with combination of [listTemplates](https://appwrite.io/docs/products/sites/templates) to find the template details.

        Parameters
        ----------
        site_id : str
            Site ID.
        repository : str
            Repository name of the template.
        owner : str
            The name of the owner of the template.
        root_directory : str
            Path to site code in the template repo.
        type : TemplateReferenceType
            Type for the reference provided. Can be commit, branch, or tag
        reference : str
            Reference value, can be a commit hash, branch name, or release tag
        activate : Optional[bool]
            Automatically activate the deployment when it is finished building.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/deployments/template'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if repository is None:
            raise AppwriteException('Missing required parameter: "repository"')

        if owner is None:
            raise AppwriteException('Missing required parameter: "owner"')

        if root_directory is None:
            raise AppwriteException('Missing required parameter: "root_directory"')

        if type is None:
            raise AppwriteException('Missing required parameter: "type"')

        if reference is None:
            raise AppwriteException('Missing required parameter: "reference"')

        api_path = api_path.replace('{siteId}', site_id)

        api_params['repository'] = repository
        api_params['owner'] = owner
        api_params['rootDirectory'] = root_directory
        api_params['type'] = type
        api_params['reference'] = reference
        if activate is not None:
            api_params['activate'] = activate

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_vcs_deployment(self, site_id: str, type: VCSReferenceType, reference: str, activate: Optional[bool] = None) -> Dict[str, Any]:
        """
        Create a deployment when a site is connected to VCS.
        
        This endpoint lets you create deployment from a branch, commit, or a tag.

        Parameters
        ----------
        site_id : str
            Site ID.
        type : VCSReferenceType
            Type of reference passed. Allowed values are: branch, commit
        reference : str
            VCS reference to create deployment from. Depending on type this can be: branch name, commit hash
        activate : Optional[bool]
            Automatically activate the deployment when it is finished building.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/deployments/vcs'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if type is None:
            raise AppwriteException('Missing required parameter: "type"')

        if reference is None:
            raise AppwriteException('Missing required parameter: "reference"')

        api_path = api_path.replace('{siteId}', site_id)

        api_params['type'] = type
        api_params['reference'] = reference
        if activate is not None:
            api_params['activate'] = activate

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_deployment(self, site_id: str, deployment_id: str) -> Dict[str, Any]:
        """
        Get a site deployment by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/deployments/{deploymentId}'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{siteId}', site_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def delete_deployment(self, site_id: str, deployment_id: str) -> Dict[str, Any]:
        """
        Delete a site deployment by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/deployments/{deploymentId}'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{siteId}', site_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_deployment_download(self, site_id: str, deployment_id: str, type: Optional[DeploymentDownloadType] = None) -> bytes:
        """
        Get a site deployment content by its unique ID. The endpoint response return with a 'Content-Disposition: attachment' header that tells the browser to start downloading the file to user downloads directory.

        Parameters
        ----------
        site_id : str
            Site ID.
        deployment_id : str
            Deployment ID.
        type : Optional[DeploymentDownloadType]
            Deployment file to download. Can be: "source", "output".
        
        Returns
        -------
        bytes
            Response as bytes
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/deployments/{deploymentId}/download'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{siteId}', site_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)

        if type is not None:
            api_params['type'] = type

        return self.client.call('get', api_path, {
        }, api_params)

    def update_deployment_status(self, site_id: str, deployment_id: str) -> Dict[str, Any]:
        """
        Cancel an ongoing site deployment build. If the build is already in progress, it will be stopped and marked as canceled. If the build hasn't started yet, it will be marked as canceled without executing. You cannot cancel builds that have already completed (status 'ready') or failed. The response includes the final build status and details.

        Parameters
        ----------
        site_id : str
            Site ID.
        deployment_id : str
            Deployment ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/deployments/{deploymentId}/status'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{siteId}', site_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)


        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_logs(self, site_id: str, queries: Optional[List[str]] = None, total: Optional[bool] = None) -> Dict[str, Any]:
        """
        Get a list of all site logs. You can use the query params to filter your results.

        Parameters
        ----------
        site_id : str
            Site ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: trigger, status, responseStatusCode, duration, requestMethod, requestPath, deploymentId
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/logs'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', site_id)

        if queries is not None:
            api_params['queries'] = queries
        if total is not None:
            api_params['total'] = total

        return self.client.call('get', api_path, {
        }, api_params)

    def get_log(self, site_id: str, log_id: str) -> Dict[str, Any]:
        """
        Get a site request log by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        log_id : str
            Log ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/logs/{logId}'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if log_id is None:
            raise AppwriteException('Missing required parameter: "log_id"')

        api_path = api_path.replace('{siteId}', site_id)
        api_path = api_path.replace('{logId}', log_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def delete_log(self, site_id: str, log_id: str) -> Dict[str, Any]:
        """
        Delete a site log by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        log_id : str
            Log ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/logs/{logId}'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if log_id is None:
            raise AppwriteException('Missing required parameter: "log_id"')

        api_path = api_path.replace('{siteId}', site_id)
        api_path = api_path.replace('{logId}', log_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_variables(self, site_id: str) -> Dict[str, Any]:
        """
        Get a list of all variables of a specific site.

        Parameters
        ----------
        site_id : str
            Site unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/variables'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', site_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def create_variable(self, site_id: str, key: str, value: str, secret: Optional[bool] = None) -> Dict[str, Any]:
        """
        Create a new site variable. These variables can be accessed during build and runtime (server-side rendering) as environment variables.

        Parameters
        ----------
        site_id : str
            Site unique ID.
        key : str
            Variable key. Max length: 255 chars.
        value : str
            Variable value. Max length: 8192 chars.
        secret : Optional[bool]
            Secret variables can be updated or deleted, but only sites can read them during build and runtime.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/variables'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if value is None:
            raise AppwriteException('Missing required parameter: "value"')

        api_path = api_path.replace('{siteId}', site_id)

        api_params['key'] = key
        api_params['value'] = value
        if secret is not None:
            api_params['secret'] = secret

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_variable(self, site_id: str, variable_id: str) -> Dict[str, Any]:
        """
        Get a variable by its unique ID.

        Parameters
        ----------
        site_id : str
            Site unique ID.
        variable_id : str
            Variable unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/variables/{variableId}'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{siteId}', site_id)
        api_path = api_path.replace('{variableId}', variable_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_variable(self, site_id: str, variable_id: str, key: str, value: Optional[str] = None, secret: Optional[bool] = None) -> Dict[str, Any]:
        """
        Update variable by its unique ID.

        Parameters
        ----------
        site_id : str
            Site unique ID.
        variable_id : str
            Variable unique ID.
        key : str
            Variable key. Max length: 255 chars.
        value : Optional[str]
            Variable value. Max length: 8192 chars.
        secret : Optional[bool]
            Secret variables can be updated or deleted, but only sites can read them during build and runtime.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/variables/{variableId}'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{siteId}', site_id)
        api_path = api_path.replace('{variableId}', variable_id)

        api_params['key'] = key
        api_params['value'] = value
        api_params['secret'] = secret

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_variable(self, site_id: str, variable_id: str) -> Dict[str, Any]:
        """
        Delete a variable by its unique ID.

        Parameters
        ----------
        site_id : str
            Site unique ID.
        variable_id : str
            Variable unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/variables/{variableId}'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{siteId}', site_id)
        api_path = api_path.replace('{variableId}', variable_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)
