from ..service import Service
from typing import List, Dict, Any
from ..exception import AppwriteException

class Teams(Service):

    def __init__(self, client) -> None:
        super(Teams, self).__init__(client)

    def list(self, queries: List[str] = None, search: str = None) -> Dict[str, Any]:
        """
        Get a list of all the teams in which the current user is a member. You can use the parameters to filter your results.

        Parameters
        ----------
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, total, billingPlan
        search : str
            Search term to filter your list results. Max length: 256 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams'
        api_params = {}

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
        }, api_params)

    def create(self, team_id: str, name: str, roles: List[str] = None) -> Dict[str, Any]:
        """
        Create a new team. The user who creates the team will automatically be assigned as the owner of the team. Only the users with the owner role can invite new members, add new owners and delete or update the team.

        Parameters
        ----------
        team_id : str
            Team ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Team name. Max length: 128 chars.
        roles : List[str]
            Array of strings. Use this param to set the roles in the team for the user who created it. The default role is **owner**. A role can be any string. Learn more about [roles and permissions](https://appwrite.io/docs/permissions). Maximum of 100 roles are allowed, each 32 characters long.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')


        api_params['teamId'] = team_id
        api_params['name'] = name
        api_params['roles'] = roles

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get(self, team_id: str) -> Dict[str, Any]:
        """
        Get a team by its ID. All team members have read access for this resource.

        Parameters
        ----------
        team_id : str
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

        api_path = '/teams/{teamId}'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        api_path = api_path.replace('{teamId}', team_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_name(self, team_id: str, name: str) -> Dict[str, Any]:
        """
        Update the team's name by its unique ID.

        Parameters
        ----------
        team_id : str
            Team ID.
        name : str
            New team name. Max length: 128 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams/{teamId}'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_path = api_path.replace('{teamId}', team_id)

        api_params['name'] = name

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete(self, team_id: str) -> Dict[str, Any]:
        """
        Delete a team using its ID. Only team members with the owner role can delete the team.

        Parameters
        ----------
        team_id : str
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

        api_path = '/teams/{teamId}'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        api_path = api_path.replace('{teamId}', team_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def list_memberships(self, team_id: str, queries: List[str] = None, search: str = None) -> Dict[str, Any]:
        """
        Use this endpoint to list a team's members using the team's ID. All team members have read access to this endpoint. Hide sensitive attributes from the response by toggling membership privacy in the Console.

        Parameters
        ----------
        team_id : str
            Team ID.
        queries : List[str]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, teamId, invited, joined, confirm, roles
        search : str
            Search term to filter your list results. Max length: 256 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams/{teamId}/memberships'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        api_path = api_path.replace('{teamId}', team_id)

        api_params['queries'] = queries
        api_params['search'] = search

        return self.client.call('get', api_path, {
        }, api_params)

    def create_membership(self, team_id: str, roles: List[str], email: str = None, user_id: str = None, phone: str = None, url: str = None, name: str = None) -> Dict[str, Any]:
        """
        Invite a new member to join your team. Provide an ID for existing users, or invite unregistered users using an email or phone number. If initiated from a Client SDK, Appwrite will send an email or sms with a link to join the team to the invited user, and an account will be created for them if one doesn't exist. If initiated from a Server SDK, the new member will be added automatically to the team.
        
        You only need to provide one of a user ID, email, or phone number. Appwrite will prioritize accepting the user ID > email > phone number if you provide more than one of these parameters.
        
        Use the `url` parameter to redirect the user from the invitation email to your app. After the user is redirected, use the [Update Team Membership Status](https://appwrite.io/docs/references/cloud/client-web/teams#updateMembershipStatus) endpoint to allow the user to accept the invitation to the team. 
        
        Please note that to avoid a [Redirect Attack](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) Appwrite will accept the only redirect URLs under the domains you have added as a platform on the Appwrite Console.
        

        Parameters
        ----------
        team_id : str
            Team ID.
        roles : List[str]
            Array of strings. Use this param to set the user roles in the team. A role can be any string. Learn more about [roles and permissions](https://appwrite.io/docs/permissions). Maximum of 100 roles are allowed, each 32 characters long.
        email : str
            Email of the new team member.
        user_id : str
            ID of the user to be added to a team.
        phone : str
            Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        url : str
            URL to redirect the user back to your app from the invitation email. This parameter is not required when an API key is supplied. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
        name : str
            Name of the new team member. Max length: 128 chars.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams/{teamId}/memberships'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if roles is None:
            raise AppwriteException('Missing required parameter: "roles"')

        api_path = api_path.replace('{teamId}', team_id)

        api_params['email'] = email
        api_params['userId'] = user_id
        api_params['phone'] = phone
        api_params['roles'] = roles
        api_params['url'] = url
        api_params['name'] = name

        return self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_membership(self, team_id: str, membership_id: str) -> Dict[str, Any]:
        """
        Get a team member by the membership unique id. All team members have read access for this resource. Hide sensitive attributes from the response by toggling membership privacy in the Console.

        Parameters
        ----------
        team_id : str
            Team ID.
        membership_id : str
            Membership ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams/{teamId}/memberships/{membershipId}'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        api_path = api_path.replace('{teamId}', team_id)
        api_path = api_path.replace('{membershipId}', membership_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_membership(self, team_id: str, membership_id: str, roles: List[str]) -> Dict[str, Any]:
        """
        Modify the roles of a team member. Only team members with the owner role have access to this endpoint. Learn more about [roles and permissions](https://appwrite.io/docs/permissions).
        

        Parameters
        ----------
        team_id : str
            Team ID.
        membership_id : str
            Membership ID.
        roles : List[str]
            An array of strings. Use this param to set the user's roles in the team. A role can be any string. Learn more about [roles and permissions](https://appwrite.io/docs/permissions). Maximum of 100 roles are allowed, each 32 characters long.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams/{teamId}/memberships/{membershipId}'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        if roles is None:
            raise AppwriteException('Missing required parameter: "roles"')

        api_path = api_path.replace('{teamId}', team_id)
        api_path = api_path.replace('{membershipId}', membership_id)

        api_params['roles'] = roles

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def delete_membership(self, team_id: str, membership_id: str) -> Dict[str, Any]:
        """
        This endpoint allows a user to leave a team or for a team owner to delete the membership of any other team member. You can also use this endpoint to delete a user membership even if it is not accepted.

        Parameters
        ----------
        team_id : str
            Team ID.
        membership_id : str
            Membership ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams/{teamId}/memberships/{membershipId}'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        api_path = api_path.replace('{teamId}', team_id)
        api_path = api_path.replace('{membershipId}', membership_id)


        return self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def update_membership_status(self, team_id: str, membership_id: str, user_id: str, secret: str) -> Dict[str, Any]:
        """
        Use this endpoint to allow a user to accept an invitation to join a team after being redirected back to your app from the invitation email received by the user.
        
        If the request is successful, a session for the user is automatically created.
        

        Parameters
        ----------
        team_id : str
            Team ID.
        membership_id : str
            Membership ID.
        user_id : str
            User ID.
        secret : str
            Secret key.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams/{teamId}/memberships/{membershipId}/status'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if membership_id is None:
            raise AppwriteException('Missing required parameter: "membership_id"')

        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')

        api_path = api_path.replace('{teamId}', team_id)
        api_path = api_path.replace('{membershipId}', membership_id)

        api_params['userId'] = user_id
        api_params['secret'] = secret

        return self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

    def get_prefs(self, team_id: str) -> Dict[str, Any]:
        """
        Get the team's shared preferences by its unique ID. If a preference doesn't need to be shared by all team members, prefer storing them in [user preferences](https://appwrite.io/docs/references/cloud/client-web/account#getPrefs).

        Parameters
        ----------
        team_id : str
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

        api_path = '/teams/{teamId}/prefs'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        api_path = api_path.replace('{teamId}', team_id)


        return self.client.call('get', api_path, {
        }, api_params)

    def update_prefs(self, team_id: str, prefs: dict) -> Dict[str, Any]:
        """
        Update the team's preferences by its unique ID. The object you pass is stored as is and replaces any previous value. The maximum allowed prefs size is 64kB and throws an error if exceeded.

        Parameters
        ----------
        team_id : str
            Team ID.
        prefs : dict
            Prefs key-value JSON object.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams/{teamId}/prefs'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        if prefs is None:
            raise AppwriteException('Missing required parameter: "prefs"')

        api_path = api_path.replace('{teamId}', team_id)

        api_params['prefs'] = prefs

        return self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)
