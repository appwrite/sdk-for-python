from ..service import Service
from typing import Any, Dict, List, Optional, Union, Type, TypeVar
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.team_list import TeamList;
from ..models.team import Team;
from ..models.membership_list import MembershipList;
from ..models.membership import Membership;
from ..models.preferences import Preferences;

T = TypeVar('T')

class Teams(Service):

    def __init__(self, client) -> None:
        super(Teams, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None,
        model_type: Type[T] = dict    ) -> TeamList[T]:
        """
        Get a list of all the teams in which the current user is a member. You can use the parameters to filter your results.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: name, total, billingPlan
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        TeamList[T]            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return TeamList.with_data(response, model_type)


    def create(
        self,
        team_id: str,
        name: str,
        roles: Optional[List[str]] = None,
        model_type: Type[T] = dict    ) -> Team[T]:
        """
        Create a new team. The user who creates the team will automatically be assigned as the owner of the team. Only the users with the owner role can invite new members, add new owners and delete or update the team.

        Parameters
        ----------
        team_id : str
            Team ID. Choose a custom ID or generate a random ID with `ID.unique()`. Valid chars are a-z, A-Z, 0-9, period, hyphen, and underscore. Can't start with a special char. Max length is 36 chars.
        name : str
            Team name. Max length: 128 chars.
        roles : Optional[List[str]]
            Array of strings. Use this param to set the roles in the team for the user who created it. The default role is **owner**. A role can be any string. Learn more about [roles and permissions](https://appwrite.io/docs/permissions). Maximum of 100 roles are allowed, each 32 characters long.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        Team[T]            API response as a typed Pydantic model
        
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


        api_params['teamId'] = self._normalize_value(team_id)
        api_params['name'] = self._normalize_value(name)
        if roles is not None:
            api_params['roles'] = self._normalize_value(roles)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Team.with_data(response, model_type)


    def get(
        self,
        team_id: str,
        model_type: Type[T] = dict    ) -> Team[T]:
        """
        Get a team by its ID. All team members have read access for this resource.

        Parameters
        ----------
        team_id : str
            Team ID.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        Team[T]            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams/{teamId}'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        api_path = api_path.replace('{teamId}', str(self._normalize_value(team_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return Team.with_data(response, model_type)


    def update_name(
        self,
        team_id: str,
        name: str,
        model_type: Type[T] = dict    ) -> Team[T]:
        """
        Update the team's name by its unique ID.

        Parameters
        ----------
        team_id : str
            Team ID.
        name : str
            New team name. Max length: 128 chars.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        Team[T]            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{teamId}', str(self._normalize_value(team_id)))

        api_params['name'] = self._normalize_value(name)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Team.with_data(response, model_type)


    def delete(
        self,
        team_id: str    ) -> Dict[str, Any]:
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

        api_path = api_path.replace('{teamId}', str(self._normalize_value(team_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_memberships(
        self,
        team_id: str,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None    ) -> MembershipList:
        """
        Use this endpoint to list a team's members using the team's ID. All team members have read access to this endpoint. Hide sensitive attributes from the response by toggling membership privacy in the Console.

        Parameters
        ----------
        team_id : str
            Team ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: userId, teamId, invited, joined, confirm, roles
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        MembershipList            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams/{teamId}/memberships'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        api_path = api_path.replace('{teamId}', str(self._normalize_value(team_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=MembershipList)


    def create_membership(
        self,
        team_id: str,
        roles: List[str],
        email: Optional[str] = None,
        user_id: Optional[str] = None,
        phone: Optional[str] = None,
        url: Optional[str] = None,
        name: Optional[str] = None    ) -> Membership:
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
            Array of strings. Use this param to set the user roles in the team. A role can be any string. Learn more about [roles and permissions](https://appwrite.io/docs/permissions). Maximum of 100 roles are allowed, each 81 characters long.
        email : Optional[str]
            Email of the new team member.
        user_id : Optional[str]
            ID of the user to be added to a team.
        phone : Optional[str]
            Phone number. Format this number with a leading '+' and a country code, e.g., +16175551212.
        url : Optional[str]
            URL to redirect the user back to your app from the invitation email. This parameter is not required when an API key is supplied. Only URLs from hostnames in your project platform list are allowed. This requirement helps to prevent an [open redirect](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html) attack against your project API.
        name : Optional[str]
            Name of the new team member. Max length: 128 chars.
        
        Returns
        -------
        Membership            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{teamId}', str(self._normalize_value(team_id)))

        if email is not None:
            api_params['email'] = self._normalize_value(email)
        if user_id is not None:
            api_params['userId'] = self._normalize_value(user_id)
        if phone is not None:
            api_params['phone'] = self._normalize_value(phone)
        api_params['roles'] = self._normalize_value(roles)
        if url is not None:
            api_params['url'] = self._normalize_value(url)
        if name is not None:
            api_params['name'] = self._normalize_value(name)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Membership)


    def get_membership(
        self,
        team_id: str,
        membership_id: str    ) -> Membership:
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
        Membership            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{teamId}', str(self._normalize_value(team_id)))
        api_path = api_path.replace('{membershipId}', str(self._normalize_value(membership_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Membership)


    def update_membership(
        self,
        team_id: str,
        membership_id: str,
        roles: List[str]    ) -> Membership:
        """
        Modify the roles of a team member. Only team members with the owner role have access to this endpoint. Learn more about [roles and permissions](https://appwrite.io/docs/permissions).
        

        Parameters
        ----------
        team_id : str
            Team ID.
        membership_id : str
            Membership ID.
        roles : List[str]
            An array of strings. Use this param to set the user's roles in the team. A role can be any string. Learn more about [roles and permissions](https://appwrite.io/docs/permissions). Maximum of 100 roles are allowed, each 81 characters long.
        
        Returns
        -------
        Membership            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{teamId}', str(self._normalize_value(team_id)))
        api_path = api_path.replace('{membershipId}', str(self._normalize_value(membership_id)))

        api_params['roles'] = self._normalize_value(roles)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Membership)


    def delete_membership(
        self,
        team_id: str,
        membership_id: str    ) -> Dict[str, Any]:
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

        api_path = api_path.replace('{teamId}', str(self._normalize_value(team_id)))
        api_path = api_path.replace('{membershipId}', str(self._normalize_value(membership_id)))


        response = self.client.call('delete', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return response


    def update_membership_status(
        self,
        team_id: str,
        membership_id: str,
        user_id: str,
        secret: str    ) -> Membership:
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
        Membership            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{teamId}', str(self._normalize_value(team_id)))
        api_path = api_path.replace('{membershipId}', str(self._normalize_value(membership_id)))

        api_params['userId'] = self._normalize_value(user_id)
        api_params['secret'] = self._normalize_value(secret)

        response = self.client.call('patch', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Membership)


    def get_prefs(
        self,
        team_id: str,
        model_type: Type[T] = dict    ) -> Preferences[T]:
        """
        Get the team's shared preferences by its unique ID. If a preference doesn't need to be shared by all team members, prefer storing them in [user preferences](https://appwrite.io/docs/references/cloud/client-web/account#getPrefs).

        Parameters
        ----------
        team_id : str
            Team ID.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        Preferences[T]            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/teams/{teamId}/prefs'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')

        api_path = api_path.replace('{teamId}', str(self._normalize_value(team_id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return Preferences.with_data(response, model_type)


    def update_prefs(
        self,
        team_id: str,
        prefs: Dict[str, Any],
        model_type: Type[T] = dict    ) -> Preferences[T]:
        """
        Update the team's preferences by its unique ID. The object you pass is stored as is and replaces any previous value. The maximum allowed prefs size is 64kB and throws an error if exceeded.

        Parameters
        ----------
        team_id : str
            Team ID.
        prefs : Dict[str, Any]
            Prefs key-value JSON object.
        
        model_type : Type[T], optional
            Pydantic model class for the user-defined data. Defaults to dict for backward compatibility.
        
        Returns
        -------
        Preferences[T]            API response as a typed Pydantic model
        
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

        api_path = api_path.replace('{teamId}', str(self._normalize_value(team_id)))

        api_params['prefs'] = self._normalize_value(prefs)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return Preferences.with_data(response, model_type)

