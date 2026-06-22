from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..models.report_list import ReportList
from ..models.report import Report
from ..models.insight_list import InsightList
from ..models.insight import Insight

class Advisor(Service):

    def __init__(self, client) -> None:
        super(Advisor, self).__init__(client)

    def list_reports(
        self,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> ReportList:
        """
        Get a list of all the project's analyzer reports. You can use the query params to filter your results.
        

        Parameters
        ----------
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: appId, type, targetType, target, analyzedAt
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        ReportList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/reports'
        api_params = {}

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=ReportList)


    def get_report(
        self,
        report_id: str
    ) -> Report:
        """
        Get an analyzer report by its unique ID. The response includes the report's metadata and the nested insights it produced.
        

        Parameters
        ----------
        report_id : str
            Report ID.
        
        Returns
        -------
        Report
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/reports/{reportId}'
        api_params = {}
        if report_id is None:
            raise AppwriteException('Missing required parameter: "report_id"')

        api_path = api_path.replace('{reportId}', str(self._normalize_value(report_id)))


        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Report)


    def delete_report(
        self,
        report_id: str
    ) -> Dict[str, Any]:
        """
        Delete an analyzer report by its unique ID. Nested insights and CTA metadata are removed asynchronously by the deletes worker.
        

        Parameters
        ----------
        report_id : str
            Report ID.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/reports/{reportId}'
        api_params = {}
        if report_id is None:
            raise AppwriteException('Missing required parameter: "report_id"')

        api_path = api_path.replace('{reportId}', str(self._normalize_value(report_id)))


        response = self.client.call('delete', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
        }, api_params)

        return response


    def list_insights(
        self,
        report_id: str,
        queries: Optional[List[str]] = None,
        total: Optional[bool] = None
    ) -> InsightList:
        """
        List the insights produced under a single analyzer report. You can use the query params to filter your results further.
        

        Parameters
        ----------
        report_id : str
            Parent report ID.
        queries : Optional[List[str]]
            Array of query strings generated using the Query class provided by the SDK. [Learn more about queries](https://appwrite.io/docs/queries). Maximum of 100 queries are allowed, each 4096 characters long. You may filter on the following attributes: type, severity, status, resourceType, resourceId, parentResourceType, parentResourceId, analyzedAt, dismissedAt, dismissedBy
        total : Optional[bool]
            When set to false, the total count returned will be 0 and will not be calculated.
        
        Returns
        -------
        InsightList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/reports/{reportId}/insights'
        api_params = {}
        if report_id is None:
            raise AppwriteException('Missing required parameter: "report_id"')

        api_path = api_path.replace('{reportId}', str(self._normalize_value(report_id)))

        if queries is not None:
            api_params['queries'] = self._normalize_value(queries)
        if total is not None:
            api_params['total'] = self._normalize_value(total)

        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=InsightList)


    def get_insight(
        self,
        report_id: str,
        insight_id: str
    ) -> Insight:
        """
        Get an insight by its unique ID, scoped to its parent report.
        

        Parameters
        ----------
        report_id : str
            Parent report ID.
        insight_id : str
            Insight ID.
        
        Returns
        -------
        Insight
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/reports/{reportId}/insights/{insightId}'
        api_params = {}
        if report_id is None:
            raise AppwriteException('Missing required parameter: "report_id"')

        if insight_id is None:
            raise AppwriteException('Missing required parameter: "insight_id"')

        api_path = api_path.replace('{reportId}', str(self._normalize_value(report_id)))
        api_path = api_path.replace('{insightId}', str(self._normalize_value(insight_id)))


        response = self.client.call('get', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Insight)

