from ..service import Service
from typing import List, Dict, Any, Optional
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated

class Organizations(Service):

    def __init__(self, client) -> None:
        super(Organizations, self).__init__(client)

    def delete(self, organization_id: str) -> Dict[str, Any]:
        """
        Delete an organization.

        Parameters
        ----------
        organization_id : str
            Team ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organizations/{organizationId}'
        api_params = {}
        if organization_id is None:
            raise AppwriteException('Missing required parameter: "organization_id"')

        api_path = api_path.replace('{organizationId}', organization_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def estimation_delete_organization(self, organization_id: str) -> Dict[str, Any]:
        """
        Get estimation for deleting an organization.

        Parameters
        ----------
        organization_id : str
            Team ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/organizations/{organizationId}/estimations/delete-organization'
        api_params = {}
        if organization_id is None:
            raise AppwriteException('Missing required parameter: "organization_id"')

        api_path = api_path.replace('{organizationId}', organization_id)


        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)
