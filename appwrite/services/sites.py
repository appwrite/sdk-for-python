from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.site_list import SiteList;
from ..enums.framework import Framework;
from ..enums.build_runtime import BuildRuntime;
from ..enums.adapter import Adapter;
from ..models.site import Site;
from ..models.framework_list import FrameworkList;
from ..models.specification_list import SpecificationList;
from ..models.deployment_list import DeploymentList;
from ..input_file import InputFile
from ..models.deployment import Deployment;
from ..enums.template_reference_type import TemplateReferenceType;
from ..enums.vcs_reference_type import VCSReferenceType;
from ..enums.deployment_download_type import DeploymentDownloadType;
from ..models.execution_list import ExecutionList;
from ..models.execution import Execution;
from ..models.variable_list import VariableList;
from ..models.variable import Variable;

class Sites(Service):

    def __init__(self, client) -> None:
        super(Sites, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None    ) -> SiteList:
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
        SiteList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=SiteList)


    def create(
        self,
        site_id: str,
        name: str,
        framework: Framework,
        build_runtime: BuildRuntime,
        enabled: Optional[bool] = None,
        logging: Optional[bool] = None,
        timeout: Optional[float] = None,
        install_command: Optional[str] = None,
        build_command: Optional[str] = None,
        output_directory: Optional[str] = None,
        adapter: Optional[Adapter] = None,
        installation_id: Optional[str] = None,
        fallback_file: Optional[str] = None,
        provider_repository_id: Optional[str] = None,
        provider_branch: Optional[str] = None,
        provider_silent_mode: Optional[bool] = None,
        provider_root_directory: Optional[str] = None,
        specification: Optional[str] = None    ) -> Site:
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
        Site            API response as a typed Pydantic model
        
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


        api_params['siteId'] = self._normalize_value(site_id)
        api_params['name'] = self._normalize_value(name)
        api_params['framework'] = self._normalize_value(framework)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if logging is not None:
            api_params['logging'] = self._normalize_value(logging)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)
        if install_command is not None:
            api_params['installCommand'] = self._normalize_value(install_command)
        if build_command is not None:
            api_params['buildCommand'] = self._normalize_value(build_command)
        if output_directory is not None:
            api_params['outputDirectory'] = self._normalize_value(output_directory)
        api_params['buildRuntime'] = self._normalize_value(build_runtime)
        if adapter is not None:
            api_params['adapter'] = self._normalize_value(adapter)
        if installation_id is not None:
            api_params['installationId'] = self._normalize_value(installation_id)
        if fallback_file is not None:
            api_params['fallbackFile'] = self._normalize_value(fallback_file)
        if provider_repository_id is not None:
            api_params['providerRepositoryId'] = self._normalize_value(provider_repository_id)
        if provider_branch is not None:
            api_params['providerBranch'] = self._normalize_value(provider_branch)
        if provider_silent_mode is not None:
            api_params['providerSilentMode'] = self._normalize_value(provider_silent_mode)
        if provider_root_directory is not None:
            api_params['providerRootDirectory'] = self._normalize_value(provider_root_directory)
        if specification is not None:
            api_params['specification'] = self._normalize_value(specification)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Site)


    def list_frameworks(
        self    ) -> FrameworkList:
        """
        Get a list of all frameworks that are currently available on the server instance.

        Returns
        -------
        FrameworkList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/frameworks'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=FrameworkList)


    def list_specifications(
        self    ) -> SpecificationList:
        """
        List allowed site specifications for this instance.

        Returns
        -------
        SpecificationList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/specifications'
        api_params = {}

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=SpecificationList)


    def get(
        self,
        site_id: str    ) -> Site:
        """
        Get a site by its unique ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        
        Returns
        -------
        Site            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Site)


    def update(
        self,
        site_id: str,
        name: str,
        framework: Framework,
        enabled: Optional[bool] = None,
        logging: Optional[bool] = None,
        timeout: Optional[float] = None,
        install_command: Optional[str] = None,
        build_command: Optional[str] = None,
        output_directory: Optional[str] = None,
        build_runtime: Optional[BuildRuntime] = None,
        adapter: Optional[Adapter] = None,
        fallback_file: Optional[str] = None,
        installation_id: Optional[str] = None,
        provider_repository_id: Optional[str] = None,
        provider_branch: Optional[str] = None,
        provider_silent_mode: Optional[bool] = None,
        provider_root_directory: Optional[str] = None,
        specification: Optional[str] = None    ) -> Site:
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
        Site            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        api_params['name'] = self._normalize_value(name)
        api_params['framework'] = self._normalize_value(framework)
        if enabled is not None:
            api_params['enabled'] = self._normalize_value(enabled)
        if logging is not None:
            api_params['logging'] = self._normalize_value(logging)
        if timeout is not None:
            api_params['timeout'] = self._normalize_value(timeout)
        if install_command is not None:
            api_params['installCommand'] = self._normalize_value(install_command)
        if build_command is not None:
            api_params['buildCommand'] = self._normalize_value(build_command)
        if output_directory is not None:
            api_params['outputDirectory'] = self._normalize_value(output_directory)
        if build_runtime is not None:
            api_params['buildRuntime'] = self._normalize_value(build_runtime)
        if adapter is not None:
            api_params['adapter'] = self._normalize_value(adapter)
        if fallback_file is not None:
            api_params['fallbackFile'] = self._normalize_value(fallback_file)
        if installation_id is not None:
            api_params['installationId'] = self._normalize_value(installation_id)
        if provider_repository_id is not None:
            api_params['providerRepositoryId'] = self._normalize_value(provider_repository_id)
        if provider_branch is not None:
            api_params['providerBranch'] = self._normalize_value(provider_branch)
        if provider_silent_mode is not None:
            api_params['providerSilentMode'] = self._normalize_value(provider_silent_mode)
        if provider_root_directory is not None:
            api_params['providerRootDirectory'] = self._normalize_value(provider_root_directory)
        if specification is not None:
            api_params['specification'] = self._normalize_value(specification)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Site)


    def delete(
        self,
        site_id: str    ) -> Dict[str, Any]:
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def update_site_deployment(
        self,
        site_id: str,
        deployment_id: str    ) -> Site:
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
        Site            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        api_params['deploymentId'] = self._normalize_value(deployment_id)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Site)


    def list_deployments(
        self,
        site_id: str,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None    ) -> DeploymentList:
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
        DeploymentList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/deployments'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=DeploymentList)


    def create_deployment(
        self,
        site_id: str,
        code: InputFile,
        install_command: Optional[str] = None,
        build_command: Optional[str] = None,
        output_directory: Optional[str] = None,
        activate: Optional[bool] = None,
        on_progress = None    ) -> Deployment:
        """
        Create a new site code deployment. Use this endpoint to upload a new version of your site code. To activate your newly uploaded code, you'll need to update the site's deployment to use your new deployment ID.

        Parameters
        ----------
        site_id : str
            Site ID.
        code : InputFile
            Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.
        install_command : Optional[str]
            Install Commands.
        build_command : Optional[str]
            Build Commands.
        output_directory : Optional[str]
            Output Directory.
        activate : Optional[bool]
            Automatically activate the deployment when it is finished building.
                on_progress : callable, optional
            Optional callback for upload progress
        
        Returns
        -------
        Deployment            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        if install_command is not None:
            api_params['installCommand'] = self._normalize_value(install_command)
        if build_command is not None:
            api_params['buildCommand'] = self._normalize_value(build_command)
        if output_directory is not None:
            api_params['outputDirectory'] = self._normalize_value(output_directory)
        api_params['code'] = self._normalize_value(code)
        if activate is not None:
            api_params['activate'] = self._normalize_value(str(activate).lower() if type(activate) is bool else activate)

        param_name = 'code'


        upload_id = ''

        response = self.client.chunked_upload(api_path, {
            'content-type': 'multipart/form-data',
        }, api_params, param_name, on_progress, upload_id)

        return self._parse_response(response, model=Deployment)


    def create_duplicate_deployment(
        self,
        site_id: str,
        deployment_id: str    ) -> Deployment:
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
        Deployment            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        api_params['deploymentId'] = self._normalize_value(deployment_id)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def create_template_deployment(
        self,
        site_id: str,
        repository: str,
        owner: str,
        root_directory: str,
        type: TemplateReferenceType,
        reference: str,
        activate: Optional[bool] = None    ) -> Deployment:
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
        Deployment            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        api_params['repository'] = self._normalize_value(repository)
        api_params['owner'] = self._normalize_value(owner)
        api_params['rootDirectory'] = self._normalize_value(root_directory)
        api_params['type'] = self._normalize_value(type)
        api_params['reference'] = self._normalize_value(reference)
        if activate is not None:
            api_params['activate'] = self._normalize_value(activate)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def create_vcs_deployment(
        self,
        site_id: str,
        type: VCSReferenceType,
        reference: str,
        activate: Optional[bool] = None    ) -> Deployment:
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
        Deployment            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        api_params['type'] = self._normalize_value(type)
        api_params['reference'] = self._normalize_value(reference)
        if activate is not None:
            api_params['activate'] = self._normalize_value(activate)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def get_deployment(
        self,
        site_id: str,
        deployment_id: str    ) -> Deployment:
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
        Deployment            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{deploymentId}', str(self._normalize_value(deployment_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def delete_deployment(
        self,
        site_id: str,
        deployment_id: str    ) -> Dict[str, Any]:
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{deploymentId}', str(self._normalize_value(deployment_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def get_deployment_download(
        self,
        site_id: str,
        deployment_id: str,
        type: Optional[DeploymentDownloadType] = None    ) -> bytes:
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{deploymentId}', str(self._normalize_value(deployment_id)))

        if type is not None:
            api_params['type'] = self._normalize_value(type)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def update_deployment_status(
        self,
        site_id: str,
        deployment_id: str    ) -> Deployment:
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
        Deployment            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{deploymentId}', str(self._normalize_value(deployment_id)))


        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Deployment)


    def list_logs(
        self,
        site_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None    ) -> ExecutionList:
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
        ExecutionList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/logs'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=ExecutionList)


    def get_log(
        self,
        site_id: str,
        log_id: str    ) -> Execution:
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
        Execution            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{logId}', str(self._normalize_value(log_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Execution)


    def delete_log(
        self,
        site_id: str,
        log_id: str    ) -> Dict[str, Any]:
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{logId}', str(self._normalize_value(log_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_variables(
        self,
        site_id: str    ) -> VariableList:
        """
        Get a list of all variables of a specific site.

        Parameters
        ----------
        site_id : str
            Site unique ID.
        
        Returns
        -------
        VariableList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/sites/{siteId}/variables'
        api_params = {}
        if site_id is None:
            raise AppwriteException('Missing required parameter: "site_id"')

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=VariableList)


    def create_variable(
        self,
        site_id: str,
        key: str,
        value: str,
        secret: Optional[bool] = None    ) -> Variable:
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
        Variable            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['value'] = self._normalize_value(value)
        if secret is not None:
            api_params['secret'] = self._normalize_value(secret)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Variable)


    def get_variable(
        self,
        site_id: str,
        variable_id: str    ) -> Variable:
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
        Variable            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Variable)


    def update_variable(
        self,
        site_id: str,
        variable_id: str,
        key: str,
        value: Optional[str] = None,
        secret: Optional[bool] = None    ) -> Variable:
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
        Variable            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))

        api_params['key'] = self._normalize_value(key)
        api_params['value'] = self._normalize_value(value)
        api_params['secret'] = self._normalize_value(secret)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Variable)


    def delete_variable(
        self,
        site_id: str,
        variable_id: str    ) -> Dict[str, Any]:
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

        api_path = api_path.replace('{siteId}', str(self._normalize_value(site_id)))
        api_path = api_path.replace('{variableId}', str(self._normalize_value(variable_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response

