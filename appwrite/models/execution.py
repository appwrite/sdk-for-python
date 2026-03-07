from typing import Any, Dict, List, Optional, Union

from pydantic import Field

from .base_model import AppwriteModel
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
    functionid : str
        Function ID.
    deploymentid : str
        Function&#039;s deployment ID used to create the execution.
    trigger : ExecutionTrigger
        The trigger that caused the function to execute. Possible values can be: `http`, `schedule`, or `event`.
    status : ExecutionStatus
        The status of the function execution. Possible values can be: `waiting`, `processing`, `completed`, `failed`, or `scheduled`.
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
        Function logs. Includes the last 4,000 characters. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    errors : str
        Function errors. Includes the last 4,000 characters. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    duration : float
        Resource(function/site) execution duration in seconds.
    scheduledat : Optional[str]
        The scheduled time for execution. If left empty, execution will be queued immediately.
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    permissions: List[Any] = Field(..., alias='$permissions')
    functionid: str = Field(..., alias='functionId')
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
