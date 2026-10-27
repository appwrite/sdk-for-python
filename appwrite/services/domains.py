from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.domains_list import DomainsList
from ..models.domain import Domain
from ..enums.domain_registration_type import DomainRegistrationType
from ..models.domain_price import DomainPrice
from ..models.domain_prices_list import DomainPricesList
from ..models.dns_records_list import DnsRecordsList
from ..models.dns_record import DnsRecord
from ..models.domain_transfer_status import DomainTransferStatus


class Domains(Service):

    def __init__(self, client) -> None:
        super(Domains, self).__init__(client)

    def list(
        self,
        queries: Optional[List[str]] = None,
        search: Optional[str] = None,
        total: Optional[bool] = None,
    ) -> DomainsList:
        """
        List all domains registered for this project. This endpoint supports pagination.

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/databases#querying-documents). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on attributes such as domain name, teamInternalId, expiration, etc.
        search : Optional[str]
            Search term to filter your list results. Max length: 256 chars.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        DomainsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains'
        api_params = {}
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if search is not None:
            api_params['search'] = self._normalize_value(search)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DomainsList)

    def create(
        self,
        team_id: str,
        domain: str,
    ) -> Domain:
        """
        Create a new domain. Before creating a domain, you need to ensure that your DNS provider is properly configured. After creating the domain, you can use the verification endpoint to check if the domain is ready to be used.

        Parameters
        ----------
        team_id : str
            Team unique ID.
        domain : str
            Domain name (e.g. "example.com").
        Returns
        -------
        Domain
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains'
        api_params = {}
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')
        if domain is None:
            raise AppwriteException('Missing required parameter: "domain"')
        api_params['teamId'] = self._normalize_value(team_id)
        api_params['domain'] = self._normalize_value(domain)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Domain)

    @deprecated("This API has been deprecated since 2.0.0. Please use `domains.list_prices` instead.")
    def get_price(
        self,
        domain: str,
        period_years: Optional[float] = None,
        registration_type: Optional[DomainRegistrationType] = None,
    ) -> DomainPrice:
        """
        Get the registration price for a domain name.

        .. deprecated::2.0.0
            This API has been deprecated since 2.0.0. Please use `domains.list_prices` instead.
        Parameters
        ----------
        domain : str
            Domain name to get price for.
        period_years : Optional[float]
            Number of years to calculate the domain price for. Must be at least 1.
        registration_type : Optional[DomainRegistrationType]
            Type of registration pricing to fetch. Allowed values: new, transfer, renewal, trade.
        Returns
        -------
        DomainPrice
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/price'
        api_params = {}
        if domain is None:
            raise AppwriteException('Missing required parameter: "domain"')
        api_params['domain'] = self._normalize_value(domain)
        if period_years is not None:
            api_params['periodYears'] = self._normalize_value(period_years)
        if registration_type is not None:
            api_params['registrationType'] = self._normalize_value(registration_type)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DomainPrice)

    def list_prices(
        self,
        domains: List[str],
        period_years: Optional[float] = None,
        registration_type: Optional[DomainRegistrationType] = None,
    ) -> DomainPricesList:
        """
        Check availability and get the requested registration price for one or more domain names. Availability is resolved for all domains in a single registrar lookup. Unavailable domains have a null price for new registrations, but can still be priced for renewal, transfer, or trade. Every priced domain also carries its renewal price for the same period, so a separate renewal lookup is not needed. A domain whose price could not be resolved, for example because its TLD is not supported, is returned with a null price.

        Parameters
        ----------
        domains : List[str]
            Domain names to check availability and price for. Maximum of 50 domains per request.
        period_years : Optional[float]
            Number of years to calculate the domain price for. Must be at least 1.
        registration_type : Optional[DomainRegistrationType]
            Type of registration pricing to fetch. Allowed values: new, transfer, renewal, trade.
        Returns
        -------
        DomainPricesList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/prices'
        api_params = {}
        if domains is None:
            raise AppwriteException('Missing required parameter: "domains"')
        api_params['domains'] = self._normalize_value(domains)
        if period_years is not None:
            api_params['periodYears'] = self._normalize_value(period_years)
        if registration_type is not None:
            api_params['registrationType'] = self._normalize_value(registration_type)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DomainPricesList)

    def get(
        self,
        domain_id: str,
    ) -> Domain:
        """
        Get a domain by its unique ID.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        Domain
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Domain)

    def delete(
        self,
        domain_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a domain by its unique ID. This endpoint can be used to delete a domain from your project.
        Once deleted, the domain will no longer be available for use and all associated resources will be removed.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def update_nameservers(
        self,
        domain_id: str,
        nameservers: Optional[List[str]] = None,
    ) -> Domain:
        """
        Update the registrar nameservers for the given domain. When nameservers are not provided,
        the domain will be updated to use Appwrite nameservers.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        nameservers : Optional[List[str]]
            Nameservers to set for the domain. Defaults to Appwrite nameservers when omitted.
        Returns
        -------
        Domain
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/nameservers'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        if nameservers is not None:
            api_params['nameservers'] = self._normalize_value(nameservers)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Domain)

    def verify_nameservers(
        self,
        domain_id: str,
    ) -> Domain:
        """
        Verify which NS records are used and update the domain accordingly. This will check the domain's
        nameservers and update the domain's status based on whether the nameservers match the expected
        Appwrite nameservers.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        Domain
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/nameservers/verification'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Domain)

    def get_preset_google_workspace(
        self,
        domain_id: str,
    ) -> DnsRecordsList:
        """
        List Google Workspace DNS records.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        DnsRecordsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/presets/google-workspace'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecordsList)

    def create_preset_google_workspace(
        self,
        domain_id: str,
    ) -> DnsRecordsList:
        """
        Add Google Workspace DNS records to the domain. This will create the required MX records
        for Google Workspace email hosting.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        DnsRecordsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/presets/google-workspace'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecordsList)

    def get_preset_i_cloud(
        self,
        domain_id: str,
    ) -> DnsRecordsList:
        """
        List iCloud DNS records.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        DnsRecordsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/presets/icloud'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecordsList)

    def create_preset_i_cloud(
        self,
        domain_id: str,
    ) -> DnsRecordsList:
        """
        Add iCloud DNS records to the domain. This will create the required MX and SPF records
        for using iCloud email services with your domain.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        DnsRecordsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/presets/icloud'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecordsList)

    def get_preset_mailgun(
        self,
        domain_id: str,
    ) -> DnsRecordsList:
        """
        List Mailgun DNS records.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        DnsRecordsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/presets/mailgun'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecordsList)

    def create_preset_mailgun(
        self,
        domain_id: str,
    ) -> DnsRecordsList:
        """
        Add Mailgun DNS records to the domain. This endpoint will create the required DNS records
        for Mailgun in the specified domain.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        DnsRecordsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/presets/mailgun'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecordsList)

    def get_preset_outlook(
        self,
        domain_id: str,
    ) -> DnsRecordsList:
        """
        List Outlook DNS records.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        DnsRecordsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/presets/outlook'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecordsList)

    def create_preset_outlook(
        self,
        domain_id: str,
    ) -> DnsRecordsList:
        """
        Add Outlook DNS records to the domain. This will create the required MX records
        for setting up Outlook email hosting for your domain.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        DnsRecordsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/presets/outlook'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecordsList)

    def get_preset_proton_mail(
        self,
        domain_id: str,
    ) -> DnsRecordsList:
        """
        List ProtonMail DNS records.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        DnsRecordsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/presets/proton-mail'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecordsList)

    def create_preset_proton_mail(
        self,
        domain_id: str,
    ) -> DnsRecordsList:
        """
        Add ProtonMail DNS records to the domain. This will create the required MX records
        for using ProtonMail with your custom domain.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        DnsRecordsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/presets/proton-mail'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecordsList)

    def get_preset_zoho(
        self,
        domain_id: str,
    ) -> DnsRecordsList:
        """
        List Zoho DNS records.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        DnsRecordsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/presets/zoho'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecordsList)

    def create_preset_zoho(
        self,
        domain_id: str,
    ) -> DnsRecordsList:
        """
        Add Zoho Mail DNS records to the domain. This will create the required MX records
        for setting up Zoho Mail on your domain.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        DnsRecordsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/presets/zoho'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecordsList)

    def list_records(
        self,
        domain_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None,
    ) -> DnsRecordsList:
        """
        List DNS records for a given domain. You can use this endpoint to list all the DNS records
        associated with your domain.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. You may filter on attributes such as type, name, value, etc. Maximum of 100 queries are allowed, each 4096 characters long.
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        Returns
        -------
        DnsRecordsList
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecordsList)

    def create_record_a(
        self,
        domain_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Create a new A record for the given domain. A records are used to point a domain name
        to an IPv4 address. The record value should be a valid IPv4 address.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            IPv4 address for this A record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment explaining what this record is for.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/a'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def update_record_a(
        self,
        domain_id: str,
        record_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Update an existing A record for the given domain. This endpoint allows you to modify
        the properties of an A record including its name (subdomain), IPv4 address, TTL,
        and optional comment.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        record_id : str
            DNS record unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            IPv4 address for this A record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment explaining what this record is for.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/a/{recordId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if record_id is None or record_id == '':
            raise AppwriteException('Missing required parameter: "record_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_path = api_path.replace('{recordId}', self._encode_path(record_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def create_record_aaaa(
        self,
        domain_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Create a new AAAA record for the given domain. This endpoint allows you to add a new IPv6 DNS record
        to your domain. The record will be used to point a hostname to an IPv6 address.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            IPv6 address for this AAAA record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment explaining what this record is for.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/aaaa'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def update_record_aaaa(
        self,
        domain_id: str,
        record_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Update an existing AAAA record for the given domain. This endpoint allows you to modify
        the properties of an existing AAAA record, including its name (subdomain), IPv6 address,
        TTL, and optional comment.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        record_id : str
            DNS record unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            IPv6 address for this AAAA record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/aaaa/{recordId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if record_id is None or record_id == '':
            raise AppwriteException('Missing required parameter: "record_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_path = api_path.replace('{recordId}', self._encode_path(record_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def create_record_alias(
        self,
        domain_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Create a new ALIAS record for the given domain. This record type can be used to point your domain
        to another domain name that will serve as an alias. This is particularly useful when you want to
        map your domain to a target domain that may change its IP address.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            Target domain for this ALIAS record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/alias'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def update_record_alias(
        self,
        domain_id: str,
        record_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Update an existing ALIAS record for the specified domain. This endpoint allows you to modify
        the properties of an existing ALIAS record including its name, target domain, TTL, and comment.

        The ALIAS record type is similar to a CNAME record but can be used at the zone apex (root domain).
        It provides a way to map one domain name to another.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        record_id : str
            DNS record unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            Target domain for this ALIAS record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/alias/{recordId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if record_id is None or record_id == '':
            raise AppwriteException('Missing required parameter: "record_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_path = api_path.replace('{recordId}', self._encode_path(record_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def create_record_caa(
        self,
        domain_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Create a new CAA record for the given domain. CAA records are used to specify which
        Certificate Authorities (CAs) are allowed to issue SSL/TLS certificates for your domain.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            CAA value (e.g. issuer domain).
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/caa'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def update_record_caa(
        self,
        domain_id: str,
        record_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Update an existing CAA record for the given domain. A CAA (Certification Authority Authorization)
        record is used to specify which certificate authorities (CAs) are authorized to issue certificates
        for a domain.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        record_id : str
            DNS record unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            CAA value (e.g. issuer domain).
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/caa/{recordId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if record_id is None or record_id == '':
            raise AppwriteException('Missing required parameter: "record_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_path = api_path.replace('{recordId}', self._encode_path(record_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def create_record_cname(
        self,
        domain_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Create a new CNAME record for the given domain.

        A CNAME record maps a subdomain to another domain name, allowing you to create aliases
        for your domain. For example, you can create a CNAME record to point 'blog.example.com'
        to 'example.wordpress.com'.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            Canonical target for this CNAME record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/cname'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def update_record_cname(
        self,
        domain_id: str,
        record_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Update an existing CNAME record for the given domain.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        record_id : str
            DNS record unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            Canonical target for this CNAME record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/cname/{recordId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if record_id is None or record_id == '':
            raise AppwriteException('Missing required parameter: "record_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_path = api_path.replace('{recordId}', self._encode_path(record_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def create_record_https(
        self,
        domain_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Create a new HTTPS record for the given domain. This record is used to configure HTTPS
        settings for your domain, enabling secure communication over SSL/TLS.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            Target for the HTTPS record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/https'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def update_record_https(
        self,
        domain_id: str,
        record_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Update an existing HTTPS record for the given domain. This endpoint allows you to modify
        the properties of an HTTPS record associated with your domain, including the name (subdomain),
        target value, TTL, and optional comment.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        record_id : str
            DNS record unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            Target for the HTTPS record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/https/{recordId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if record_id is None or record_id == '':
            raise AppwriteException('Missing required parameter: "record_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_path = api_path.replace('{recordId}', self._encode_path(record_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def create_record_mx(
        self,
        domain_id: str,
        name: str,
        value: str,
        ttl: float,
        priority: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Create a new MX record for the given domain. MX records are used to define the mail servers responsible
        for accepting email messages for the domain. Multiple MX records can be created with different priorities.
        The priority parameter determines the order in which mail servers are used, with lower values indicating
        higher priority.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            Mail server domain for this MX record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        priority : float
            MX priority. Lower values are tried first.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/mx'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        if priority is None:
            raise AppwriteException('Missing required parameter: "priority"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        api_params['priority'] = self._normalize_value(priority)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def update_record_mx(
        self,
        domain_id: str,
        record_id: str,
        name: str,
        value: str,
        ttl: float,
        priority: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Update an existing MX record for the given domain.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        record_id : str
            DNS record unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            Mail server domain for this MX record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        priority : float
            MX priority. Lower values are tried first.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/mx/{recordId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if record_id is None or record_id == '':
            raise AppwriteException('Missing required parameter: "record_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        if priority is None:
            raise AppwriteException('Missing required parameter: "priority"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_path = api_path.replace('{recordId}', self._encode_path(record_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        api_params['priority'] = self._normalize_value(priority)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def create_record_ns(
        self,
        domain_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Create a new NS record for the given domain. NS records specify the nameservers that are used
        to resolve the domain name to IP addresses. Each domain can have multiple NS records.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            Nameserver target for this NS record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/ns'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def update_record_ns(
        self,
        domain_id: str,
        record_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Update an existing NS record for the given domain. This endpoint allows you to modify
        the properties of an NS (nameserver) record associated with your domain. You can update
        the record name (subdomain), target nameserver value, TTL, and add or modify comments
        for better record management.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        record_id : str
            DNS record unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            Nameserver target for this NS record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/ns/{recordId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if record_id is None or record_id == '':
            raise AppwriteException('Missing required parameter: "record_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_path = api_path.replace('{recordId}', self._encode_path(record_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def create_record_srv(
        self,
        domain_id: str,
        name: str,
        value: str,
        ttl: float,
        priority: float,
        weight: float,
        port: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Create a new SRV record for the given domain. SRV records are used to define the location
        of servers for specific services. For example, they can be used to specify which server
        handles a specific service like SIP or XMPP for the domain.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        name : str
            Record name relative to the domain: the service and protocol, such as `_sip._tcp`. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            Target hostname for this SRV record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        priority : float
            Record priority. Lower values are tried first.
        weight : float
            Record weight, used to share load between targets of equal priority.
        port : float
            Port number for the service.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/srv'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        if priority is None:
            raise AppwriteException('Missing required parameter: "priority"')
        if weight is None:
            raise AppwriteException('Missing required parameter: "weight"')
        if port is None:
            raise AppwriteException('Missing required parameter: "port"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        api_params['priority'] = self._normalize_value(priority)
        api_params['weight'] = self._normalize_value(weight)
        api_params['port'] = self._normalize_value(port)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def update_record_srv(
        self,
        domain_id: str,
        record_id: str,
        name: str,
        value: str,
        ttl: float,
        priority: float,
        weight: float,
        port: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Update an existing SRV record for the given domain.

        Required parameters:
        - domainId: Domain unique ID
        - recordId: DNS record unique ID
        - name: Record name (service name)
        - value: Target hostname for this SRV record
        - ttl: Time to live, in seconds
        - priority: Record priority
        - weight: Record weight
        - port: Port number for the service

        Optional parameters:
        - comment: A comment for this record

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        record_id : str
            DNS record unique ID.
        name : str
            Record name relative to the domain: the service and protocol, such as `_sip._tcp`. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            Target hostname for this SRV record.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        priority : float
            Record priority. Lower values are tried first.
        weight : float
            Record weight, used to share load between targets of equal priority.
        port : float
            Port number for the service.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/srv/{recordId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if record_id is None or record_id == '':
            raise AppwriteException('Missing required parameter: "record_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        if priority is None:
            raise AppwriteException('Missing required parameter: "priority"')
        if weight is None:
            raise AppwriteException('Missing required parameter: "weight"')
        if port is None:
            raise AppwriteException('Missing required parameter: "port"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_path = api_path.replace('{recordId}', self._encode_path(record_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        api_params['priority'] = self._normalize_value(priority)
        api_params['weight'] = self._normalize_value(weight)
        api_params['port'] = self._normalize_value(port)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def create_record_txt(
        self,
        domain_id: str,
        name: str,
        ttl: float,
        value: Optional[str] = None,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Create a new TXT record for the given domain. TXT records can be used
        to provide additional information about your domain, such as domain
        verification records, SPF records, or DKIM records.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        value : Optional[str]
            TXT record value.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/txt'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_params['name'] = self._normalize_value(name)
        if value is not None:
            api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'post',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def update_record_txt(
        self,
        domain_id: str,
        record_id: str,
        name: str,
        value: str,
        ttl: float,
        comment: Optional[str] = None,
    ) -> DnsRecord:
        """
        Update an existing TXT record for the given domain.

        Update the TXT record details for a specific domain by providing the domain ID,
        record ID, and the new record configuration including name, value, TTL, and an optional comment.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        record_id : str
            DNS record unique ID.
        name : str
            Record name relative to the domain, such as `www`, or `@` for the domain itself. A full name ending in the domain is also accepted and stored relative to it.
        value : str
            TXT record value.
        ttl : float
            Time to live, in seconds. Must be between 1 and 2147483647.
        comment : Optional[str]
            A comment for this record.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/txt/{recordId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if record_id is None or record_id == '':
            raise AppwriteException('Missing required parameter: "record_id"')
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')
        if value is None:
            raise AppwriteException('Missing required parameter: "value"')
        if ttl is None:
            raise AppwriteException('Missing required parameter: "ttl"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_path = api_path.replace('{recordId}', self._encode_path(record_id))
        api_params['name'] = self._normalize_value(name)
        api_params['value'] = self._normalize_value(value)
        api_params['ttl'] = self._normalize_value(ttl)
        if comment is not None:
            api_params['comment'] = self._normalize_value(comment)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def get_record(
        self,
        domain_id: str,
        record_id: str,
    ) -> DnsRecord:
        """
        Get a single DNS record for a given domain by record ID.

        This endpoint allows you to retrieve a specific DNS record associated with a domain
        using its unique identifier. The record contains information about the DNS configuration
        such as type, value, and TTL settings.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        record_id : str
            DNS record unique ID.
        Returns
        -------
        DnsRecord
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/{recordId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if record_id is None or record_id == '':
            raise AppwriteException('Missing required parameter: "record_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_path = api_path.replace('{recordId}', self._encode_path(record_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DnsRecord)

    def delete_record(
        self,
        domain_id: str,
        record_id: str,
    ) -> Dict[str, Any]:
        """
        Delete a DNS record for the given domain. This endpoint allows you to delete an existing DNS record
        from a specific domain.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        record_id : str
            DNS record unique ID.
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/records/{recordId}'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if record_id is None or record_id == '':
            raise AppwriteException('Missing required parameter: "record_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_path = api_path.replace('{recordId}', self._encode_path(record_id))

        response = self.client.call(
            'delete',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return response

    def update_team(
        self,
        domain_id: str,
        team_id: str,
    ) -> Domain:
        """
        Update the team ID for a specific domain. The caller must administer the current
        team and be an owner of the destination team.

        Updating the team ID will transfer ownership and access control of the domain
        and all its DNS records to the new team.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        team_id : str
            New team unique ID.
        Returns
        -------
        Domain
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/team'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if team_id is None:
            raise AppwriteException('Missing required parameter: "team_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_params['teamId'] = self._normalize_value(team_id)

        response = self.client.call(
            'patch',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Domain)

    def get_transfer_status(
        self,
        domain_id: str,
    ) -> DomainTransferStatus:
        """
        Retrieve the current transfer status for a domain. Returns the status, an optional reason, and a timestamp of the last status change.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        DomainTransferStatus
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/transfers/status'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=DomainTransferStatus)

    def get_zone(
        self,
        domain_id: str,
    ) -> str:
        """
        Retrieve the DNS zone file for the given domain. This endpoint will return the DNS
        zone file in a standardized format that can be used to configure DNS servers.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        Returns
        -------
        str
            Response body as text

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/zone'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))

        response = self.client.call(
            'get',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'accept': 'text/plain',
            },
            api_params,
            response_type='text',
        )

        return response

    def update_zone(
        self,
        domain_id: str,
        content: str,
    ) -> Domain:
        """
        Update the DNS zone for the given domain using the provided zone file content.
        All parsed records the domain does not already have are imported and then the main domain document is returned.

        Parameters
        ----------
        domain_id : str
            Domain unique ID.
        content : str
            DNS zone file content as a string.
        Returns
        -------
        Domain
            API response as a typed Pydantic model

        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/domains/{domainId}/zone'
        api_params = {}
        if domain_id is None or domain_id == '':
            raise AppwriteException('Missing required parameter: "domain_id"')
        if content is None:
            raise AppwriteException('Missing required parameter: "content"')
        api_path = api_path.replace('{domainId}', self._encode_path(domain_id))
        api_params['content'] = self._normalize_value(content)

        response = self.client.call(
            'put',
            api_path,
            {
                'X-Appwrite-Project': self.client.get_config('project'),
                'content-type': 'application/json',
                'accept': 'application/json',
            },
            api_params,
        )

        return self._parse_response(response, model=Domain)
