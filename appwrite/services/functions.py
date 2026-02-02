from ..service import Service
from typing import List, Dict, Any, Optional
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..enums.runtime import Runtime;
from ..enums.scopes import Scopes;
from ..input_file import InputFile
from ..enums.template_reference_type import TemplateReferenceType;
from ..enums.vcs_reference_type import VCSReferenceType;
from ..enums.deployment_download_type import DeploymentDownloadType;
from ..enums.execution_method import ExecutionMethod;

class Functions(Service):

    def __init__(self, client) -> None:
        super(Functions, self).__init__(client)

    def list(self, queries: Optional[List[str]] = None, search: Optional[str] = None, total: Optional[bool] = None) -> Dict[str, Any]:
        """
        Get a list of all the project's functions. You can use the query params to filter your results.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, enabled, runtime, deploymentId, schedule, scheduleNext, schedulePrevious, timeout, entrypoint, commands, installationId
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

        api_path = '/functions'
        api_params = {}

        if queries is not None:
            api_params['queries'] = queries
        if search is not None:
            api_params['search'] = search
        if total is not None:
            api_params['total'] = total

        return self.client.call('get', api_path, {
        }, api_params)

    def create(self, function_id: str, name: str, runtime: Runtime, execute: Optional[List[str]] = None, events: Optional[List[str]] = None, schedule: Optional[str] = None, timeout: Optional[float] = None, enabled: Optional[bool] = None, logging: Optional[bool] = None, entrypoint: Optional[str] = None, commands: Optional[str] = None, scopes: Optional[List[Scopes]] = None, installation_id: Optional[str] = None, provider_repository_id: Optional[str] = None, provider_branch: Optional[str] = None, provider_silent_mode: Optional[bool] = None, provider_root_directory: Optional[str] = None, specification: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new function. You can pass a list of [permissions](https://appwrite.io/docs/permissions) to allow different project users or team with access to execute the function using the client API.

        Parameters
        ----------
        function_id : str
            Function ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Function name. Max length: 128 chars.
        runtime : Runtime
            Execution runtime.
        execute : Optional[List[str]]
            An array of role strings with execution permissions. By default no user is granted with any execute permissions. [learn more about roles](https://appwrite.io/docs/permissions#permission-roles). Maximum of 100 roles are allowed, each 64 characters long.
        events : Optional[List[str]]
            Events list. Maximum of 100 events are allowed.
        schedule : Optional[str]
            Schedule CRON syntax.
        timeout : Optional[float]
            Function maximum execution time in seconds.
        enabled : Optional[bool]
            Is function enabled? When set to 'disabled', users cannot access the function but Server SDKs with and API key can still access the function. No data is lost when this is toggled.
        logging : Optional[bool]
            When disabled, executions will exclude logs and errors, and will be slightly faster.
        entrypoint : Optional[str]
            Entrypoint File. This path is relative to the "providerRootDirectory".
        commands : Optional[str]
            Build Commands.
        scopes : Optional[List[Scopes]]
            List of scopes allowed for API key auto-generated for every execution. Maximum of 100 scopes are allowed.
        installation_id : Optional[str]
            Appwrite Installation ID for VCS (Version Control System) deployment.
        provider_repository_id : Optional[str]
            Repository ID of the repo linked to the function.
        provider_branch : Optional[str]
            Production branch for the repo linked to the function.
        provider_silent_mode : Optional[bool]
            Is the VCS (Version Control System) connection in silent mode for the repo linked to the function? In silent mode, comments will not be made on commits and pull requests.
        provider_root_directory : Optional[str]
            Path to function code in the linked repo.
        specification : Optional[str]
            Runtime specification for the function and builds.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/functions'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        if runtime is None:
            raise AppwriteException('Missing required parameter: "runtime"')


        api_params['functionId'] = function_id
        api_params['name'] = name
        api_params['runtime'] = runtime
        if execute is not None:
            api_params['execute'] = execute
        if events is not None:
            api_params['events'] = events
        if schedule is not None:
            api_params['schedule'] = schedule
        if timeout is not None:
            api_params['timeout'] = timeout
        if enabled is not None:
            api_params['enabled'] = enabled
        if logging is not None:
            api_params['logging'] = logging
        if entrypoint is not None:
            api_params['entrypoint'] = entrypoint
        if commands is not None:
            api_params['commands'] = commands
        if scopes is not None:
            api_params['scopes'] = scopes
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

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_runtimes(self) -> Dict[str, Any]:
        """
        Get a list of all runtimes that are currently active on your instance.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/functions/runtimes'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def list_specifications(self) -> Dict[str, Any]:
        """
        List allowed function specifications for this instance.

        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/functions/specifications'
        api_params = {}

        return self.client.call('get', api_path, {
        }, api_params)

    def get(self, function_id: str) -> Dict[str, Any]:
        """
        Get a function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/functions/{functionId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', function_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update(self, function_id: str, name: str, runtime: Optional[Runtime] = None, execute: Optional[List[str]] = None, events: Optional[List[str]] = None, schedule: Optional[str] = None, timeout: Optional[float] = None, enabled: Optional[bool] = None, logging: Optional[bool] = None, entrypoint: Optional[str] = None, commands: Optional[str] = None, scopes: Optional[List[Scopes]] = None, installation_id: Optional[str] = None, provider_repository_id: Optional[str] = None, provider_branch: Optional[str] = None, provider_silent_mode: Optional[bool] = None, provider_root_directory: Optional[str] = None, specification: Optional[str] = None) -> Dict[str, Any]:
        """
        Update function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function ID.
        name : str
            Function name. Max length: 128 chars.
        runtime : Optional[Runtime]
            Execution runtime.
        execute : Optional[List[str]]
            An array of role strings with execution permissions. By default no user is granted with any execute permissions. [learn more about roles](https://appwrite.io/docs/permissions#permission-roles). Maximum of 100 roles are allowed, each 64 characters long.
        events : Optional[List[str]]
            Events list. Maximum of 100 events are allowed.
        schedule : Optional[str]
            Schedule CRON syntax.
        timeout : Optional[float]
            Maximum execution time in seconds.
        enabled : Optional[bool]
            Is function enabled? When set to 'disabled', users cannot access the function but Server SDKs with and API key can still access the function. No data is lost when this is toggled.
        logging : Optional[bool]
            When disabled, executions will exclude logs and errors, and will be slightly faster.
        entrypoint : Optional[str]
            Entrypoint File. This path is relative to the "providerRootDirectory".
        commands : Optional[str]
            Build Commands.
        scopes : Optional[List[Scopes]]
            List of scopes allowed for API Key auto-generated for every execution. Maximum of 100 scopes are allowed.
        installation_id : Optional[str]
            Appwrite Installation ID for VCS (Version Controle System) deployment.
        provider_repository_id : Optional[str]
            Repository ID of the repo linked to the function
        provider_branch : Optional[str]
            Production branch for the repo linked to the function
        provider_silent_mode : Optional[bool]
            Is the VCS (Version Control System) connection in silent mode for the repo linked to the function? In silent mode, comments will not be made on commits and pull requests.
        provider_root_directory : Optional[str]
            Path to function code in the linked repo.
        specification : Optional[str]
            Runtime specification for the function and builds.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/functions/{functionId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{functionId}', function_id)

        api_params['name'] = name
        if runtime is not None:
            api_params['runtime'] = runtime
        if execute is not None:
            api_params['execute'] = execute
        if events is not None:
            api_params['events'] = events
        if schedule is not None:
            api_params['schedule'] = schedule
        if timeout is not None:
            api_params['timeout'] = timeout
        if enabled is not None:
            api_params['enabled'] = enabled
        if logging is not None:
            api_params['logging'] = logging
        if entrypoint is not None:
            api_params['entrypoint'] = entrypoint
        if commands is not None:
            api_params['commands'] = commands
        if scopes is not None:
            api_params['scopes'] = scopes
        if installation_id is not None:
            api_params['installationId'] = installation_id
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

    def delete(self, function_id: str) -> Dict[str, Any]:
        """
        Delete a function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/functions/{functionId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', function_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_function_deployment(self, function_id: str, deployment_id: str) -> Dict[str, Any]:
        """
        Update the function active deployment. Use this endpoint to switch the code deployment that should be used when visitor opens your function.

        Parameters
        ----------
        function_id : str
            Function ID.
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

        api_path = '/functions/{functionId}/deployment'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', function_id)

        api_params['deploymentId'] = deployment_id

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_deployments(self, function_id: str, queries: Optional[List[str]] = None, search: Optional[str] = None, total: Optional[bool] = None) -> Dict[str, Any]:
        """
        Get a list of all the function's code deployments. You can use the query params to filter your results.

        Parameters
        ----------
        function_id : str
            Function ID.
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

        api_path = '/functions/{functionId}/deployments'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', function_id)

        if queries is not None:
            api_params['queries'] = queries
        if search is not None:
            api_params['search'] = search
        if total is not None:
            api_params['total'] = total

        return self.client.call('get', api_path, {
        }, api_params)

    def create_deployment(self, function_id: str, code: InputFile, activate: bool, entrypoint: Optional[str] = None, commands: Optional[str] = None, on_progress = None) -> Dict[str, Any]:
        """
        Create a new function code deployment. Use this endpoint to upload a new version of your code function. To execute your newly uploaded code, you'll need to update the function's deployment to use your new deployment UID.
        
        This endpoint accepts a tar.gz file compressed with your code. Make sure to include any dependencies your code has within the compressed file. You can learn more about code packaging in the [Appwrite Cloud Functions tutorial](https://appwrite.io/docs/functions).
        
        Use the "command" param to set the entrypoint used to execute your code.

        Parameters
        ----------
        function_id : str
            Function ID.
        code : InputFile
            Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.
        activate : bool
            Automatically activate the deployment when it is finished building.
        entrypoint : Optional[str]
            Entrypoint File.
        commands : Optional[str]
            Build Commands.
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

        api_path = '/functions/{functionId}/deployments'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if code is None:
            raise AppwriteException('Missing required parameter: "code"')

        if activate is None:
            raise AppwriteException('Missing required parameter: "activate"')

        api_path = api_path.replace('{functionId}', function_id)

        if entrypoint is not None:
            api_params['entrypoint'] = entrypoint
        if commands is not None:
            api_params['commands'] = commands
        api_params['code'] = code
        api_params['activate'] = str(activate).lower() if type(activate) is bool else activate

        param_name = 'code'


        upload_id = ''

        return self.client.chunked_upload(api_path, {
            'content-type': 'multipart/form-data',
        }, api_params, param_name, on_progress, upload_id)

    def create_duplicate_deployment(self, function_id: str, deployment_id: str, build_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new build for an existing function deployment. This endpoint allows you to rebuild a deployment with the updated function configuration, including its entrypoint and build commands if they have been modified. The build process will be queued and executed asynchronously. The original deployment's code will be preserved and used for the new build.

        Parameters
        ----------
        function_id : str
            Function ID.
        deployment_id : str
            Deployment ID.
        build_id : Optional[str]
            Build unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/functions/{functionId}/deployments/duplicate'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', function_id)

        api_params['deploymentId'] = deployment_id
        if build_id is not None:
            api_params['buildId'] = build_id

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def create_template_deployment(self, function_id: str, repository: str, owner: str, root_directory: str, type: TemplateReferenceType, reference: str, activate: Optional[bool] = None) -> Dict[str, Any]:
        """
        Create a deployment based on a template.
        
        Use this endpoint with combination of [listTemplates](https://appwrite.io/docs/products/functions/templates) to find the template details.

        Parameters
        ----------
        function_id : str
            Function ID.
        repository : str
            Repository name of the template.
        owner : str
            The name of the owner of the template.
        root_directory : str
            Path to function code in the template repo.
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

        api_path = '/functions/{functionId}/deployments/template'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

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

        api_path = api_path.replace('{functionId}', function_id)

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

    def create_vcs_deployment(self, function_id: str, type: VCSReferenceType, reference: str, activate: Optional[bool] = None) -> Dict[str, Any]:
        """
        Create a deployment when a function is connected to VCS.
        
        This endpoint lets you create deployment from a branch, commit, or a tag.

        Parameters
        ----------
        function_id : str
            Function ID.
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

        api_path = '/functions/{functionId}/deployments/vcs'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if type is None:
            raise AppwriteException('Missing required parameter: "type"')

        if reference is None:
            raise AppwriteException('Missing required parameter: "reference"')

        api_path = api_path.replace('{functionId}', function_id)

        api_params['type'] = type
        api_params['reference'] = reference
        if activate is not None:
            api_params['activate'] = activate

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_deployment(self, function_id: str, deployment_id: str) -> Dict[str, Any]:
        """
        Get a function deployment by its unique ID.

        Parameters
        ----------
        function_id : str
            Function ID.
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

        api_path = '/functions/{functionId}/deployments/{deploymentId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def delete_deployment(self, function_id: str, deployment_id: str) -> Dict[str, Any]:
        """
        Delete a code deployment by its unique ID.

        Parameters
        ----------
        function_id : str
            Function ID.
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

        api_path = '/functions/{functionId}/deployments/{deploymentId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_deployment_download(self, function_id: str, deployment_id: str, type: Optional[DeploymentDownloadType] = None) -> bytes:
        """
        Get a function deployment content by its unique ID. The endpoint response return with a 'Content-Disposition: attachment' header that tells the browser to start downloading the file to user downloads directory.

        Parameters
        ----------
        function_id : str
            Function ID.
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

        api_path = '/functions/{functionId}/deployments/{deploymentId}/download'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)

        if type is not None:
            api_params['type'] = type

        return self.client.call('get', api_path, {
        }, api_params)

    def update_deployment_status(self, function_id: str, deployment_id: str) -> Dict[str, Any]:
        """
        Cancel an ongoing function deployment build. If the build is already in progress, it will be stopped and marked as canceled. If the build hasn't started yet, it will be marked as canceled without executing. You cannot cancel builds that have already completed (status 'ready') or failed. The response includes the final build status and details.

        Parameters
        ----------
        function_id : str
            Function ID.
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

        api_path = '/functions/{functionId}/deployments/{deploymentId}/status'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if deployment_id is None:
            raise AppwriteException('Missing required parameter: "deployment_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{deploymentId}', deployment_id)


        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_executions(self, function_id: str, queries: Optional[List[str]] = None, total: Optional[bool] = None) -> Dict[str, Any]:
        """
        Get a list of all the current user function execution logs. You can use the query params to filter your results.

        Parameters
        ----------
        function_id : str
            Function ID.
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

        api_path = '/functions/{functionId}/executions'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', function_id)

        if queries is not None:
            api_params['queries'] = queries
        if total is not None:
            api_params['total'] = total

        return self.client.call('get', api_path, {
        }, api_params)

    def create_execution(self, function_id: str, body: Optional[str] = None, xasync: Optional[bool] = None, path: Optional[str] = None, method: Optional[ExecutionMethod] = None, headers: Optional[dict] = None, scheduled_at: Optional[str] = None) -> Dict[str, Any]:
        """
        Trigger a function execution. The returned object will return you the current execution status. You can ping the `Get Execution` endpoint to get updates on the current execution status. Once this endpoint is called, your function execution process will start asynchronously.

        Parameters
        ----------
        function_id : str
            Function ID.
        body : Optional[str]
            HTTP body of execution. Default value is empty string.
        xasync : Optional[bool]
            Execute code in the background. Default value is false.
        path : Optional[str]
            HTTP path of execution. Path can include query params. Default value is /
        method : Optional[ExecutionMethod]
            HTTP method of execution. Default value is POST.
        headers : Optional[dict]
            HTTP headers of execution. Defaults to empty.
        scheduled_at : Optional[str]
            Scheduled execution time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. DateTime value must be in future with precision in minutes.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/functions/{functionId}/executions'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', function_id)

        if body is not None:
            api_params['body'] = body
        if xasync is not None:
            api_params['async'] = xasync
        if path is not None:
            api_params['path'] = path
        if method is not None:
            api_params['method'] = method
        if headers is not None:
            api_params['headers'] = headers
        api_params['scheduledAt'] = scheduled_at

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_execution(self, function_id: str, execution_id: str) -> Dict[str, Any]:
        """
        Get a function execution log by its unique ID.

        Parameters
        ----------
        function_id : str
            Function ID.
        execution_id : str
            Execution ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/functions/{functionId}/executions/{executionId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if execution_id is None:
            raise AppwriteException('Missing required parameter: "execution_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{executionId}', execution_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def delete_execution(self, function_id: str, execution_id: str) -> Dict[str, Any]:
        """
        Delete a function execution by its unique ID.

        Parameters
        ----------
        function_id : str
            Function ID.
        execution_id : str
            Execution ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/functions/{functionId}/executions/{executionId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if execution_id is None:
            raise AppwriteException('Missing required parameter: "execution_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{executionId}', execution_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_variables(self, function_id: str) -> Dict[str, Any]:
        """
        Get a list of all variables of a specific function.

        Parameters
        ----------
        function_id : str
            Function unique ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/functions/{functionId}/variables'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        api_path = api_path.replace('{functionId}', function_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def create_variable(self, function_id: str, key: str, value: str, secret: Optional[bool] = None) -> Dict[str, Any]:
        """
        Create a new function environment variable. These variables can be accessed in the function at runtime as environment variables.

        Parameters
        ----------
        function_id : str
            Function unique ID.
        key : str
            Variable key. Max length: 255 chars.
        value : str
            Variable value. Max length: 8192 chars.
        secret : Optional[bool]
            Secret variables can be updated or deleted, but only functions can read them during build and runtime.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/functions/{functionId}/variables'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        if value is None:
            raise AppwriteException('Missing required parameter: "value"')

        api_path = api_path.replace('{functionId}', function_id)

        api_params['key'] = key
        api_params['value'] = value
        if secret is not None:
            api_params['secret'] = secret

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_variable(self, function_id: str, variable_id: str) -> Dict[str, Any]:
        """
        Get a variable by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.
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

        api_path = '/functions/{functionId}/variables/{variableId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{variableId}', variable_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_variable(self, function_id: str, variable_id: str, key: str, value: Optional[str] = None, secret: Optional[bool] = None) -> Dict[str, Any]:
        """
        Update variable by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.
        variable_id : str
            Variable unique ID.
        key : str
            Variable key. Max length: 255 chars.
        value : Optional[str]
            Variable value. Max length: 8192 chars.
        secret : Optional[bool]
            Secret variables can be updated or deleted, but only functions can read them during build and runtime.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/functions/{functionId}/variables/{variableId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        if key is None:
            raise AppwriteException('Missing required parameter: "key"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{variableId}', variable_id)

        api_params['key'] = key
        api_params['value'] = value
        api_params['secret'] = secret

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_variable(self, function_id: str, variable_id: str) -> Dict[str, Any]:
        """
        Delete a variable by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.
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

        api_path = '/functions/{functionId}/variables/{variableId}'
        api_params = {}
        if function_id is None:
            raise AppwriteException('Missing required parameter: "function_id"')

        if variable_id is None:
            raise AppwriteException('Missing required parameter: "variable_id"')

        api_path = api_path.replace('{functionId}', function_id)
        api_path = api_path.replace('{variableId}', variable_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)
