from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

from .base_model import AppwriteModel
from ..enums.execution_resource_type import ExecutionResourceType
from ..enums.execution_trigger import ExecutionTrigger
from ..enums.execution_status import ExecutionStatus
from .headers import Headers


class Execution(AppwriteModel):
    """
    Execution

    Attributes
    ----------
    id : str
        Execution ID.
    createdat : str
        Execution creation date in ISO 8601 format.
    updatedat : str
        Execution update date in ISO 8601 format.
    permissions : List[Any]
        Execution roles.
    resourceid : str
        Function or site ID.
    resourcetype : ExecutionResourceType
        Execution resource type.
    deploymentid : str
        Deployment ID used to create the execution.
    trigger : ExecutionTrigger
        The trigger that caused the resource to execute. Possible values can be: `http`, `schedule`, or `event`.
    status : ExecutionStatus
        The status of the resource execution. Possible values can be: `waiting`, `processing`, `completed`, `failed`, or `scheduled`.
    requestmethod : str
        HTTP request method type.
    requestpath : str
        HTTP request path and query.
    requestheaders : List[Headers]
        HTTP request headers as a key-value object. This will return only whitelisted headers. All headers are returned if execution is created as synchronous.
    responsestatuscode : float
        HTTP response status code.
    responsebody : str
        HTTP response body. This will return empty unless execution is created as synchronous.
    responseheaders : List[Headers]
        HTTP response headers as a key-value object. This will return only whitelisted headers. All headers are returned if execution is created as synchronous.
    logs : str
        Resource logs. Includes the last 4,000 characters. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    errors : str
        Resource errors. Includes the last 4,000 characters. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    duration : float
        Total time the resource(function/site) took to respond, in seconds.
    scheduledat : Optional[str]
        The scheduled time for execution. If left empty, execution will be queued immediately.
    """

    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    resourceid: str = Field(..., alias='resourceId')
    resourcetype: ExecutionResourceType = Field(..., alias='resourceType')
    deploymentid: str = Field(..., alias='deploymentId')
    trigger: ExecutionTrigger = Field(..., alias='trigger')
    status: ExecutionStatus = Field(..., alias='status')
    requestmethod: str = Field(..., alias='requestMethod')
    requestpath: str = Field(..., alias='requestPath')
    requestheaders: List[Headers] = Field(..., alias='requestHeaders')
    responsestatuscode: float = Field(..., alias='responseStatusCode')
    responsebody: str = Field(..., alias='responseBody')
    responseheaders: List[Headers] = Field(..., alias='responseHeaders')
    logs: str = Field(..., alias='logs')
    errors: str = Field(..., alias='errors')
    duration: float = Field(..., alias='duration')
    scheduledat: Optional[str] = Field(default=None, alias='scheduledAt')

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
        if 'resourceId' not in data and 'resourceid' not in data:
            data['resourceId'] = ''
        if 'resourceType' not in data and 'resourcetype' not in data:
            data['resourceType'] = 'functions'
        if 'deploymentId' not in data and 'deploymentid' not in data:
            data['deploymentId'] = ''
        if 'requestMethod' not in data and 'requestmethod' not in data:
            data['requestMethod'] = ''
        if 'requestPath' not in data and 'requestpath' not in data:
            data['requestPath'] = ''
        if 'responseStatusCode' not in data and 'responsestatuscode' not in data:
            data['responseStatusCode'] = 0
        if 'responseBody' not in data and 'responsebody' not in data:
            data['responseBody'] = ''
        if 'logs' not in data:
            data['logs'] = ''
        if 'errors' not in data:
            data['errors'] = ''
        if 'duration' not in data:
            data['duration'] = 0
        return data
