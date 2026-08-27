from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .additional_resource import AdditionalResource


class UsageBillingPlan(AppwriteModel):
    """
    usageBillingPlan

    Attributes
    ----------
    bandwidth : AdditionalResource
        Bandwidth additional resources
    executions : AdditionalResource
        Executions additional resources
    member : Optional[AdditionalResource]
        Member additional resources
    realtime : AdditionalResource
        Realtime additional resources
    realtimemessages : AdditionalResource
        Realtime messages additional resources
    realtimebandwidth : Optional[AdditionalResource]
        Realtime bandwidth additional resources
    storage : AdditionalResource
        Storage additional resources
    users : AdditionalResource
        User additional resources
    gbhours : AdditionalResource
        GBHour additional resources
    imagetransformations : AdditionalResource
        Image transformation additional resources
    credits : Optional[AdditionalResource]
        Credits additional resources
    """

    bandwidth: AdditionalResource = Field(..., alias='bandwidth')
    executions: AdditionalResource = Field(..., alias='executions')
    member: Optional[AdditionalResource] = Field(default=None, alias='member')
    realtime: AdditionalResource = Field(..., alias='realtime')
    realtimemessages: AdditionalResource = Field(..., alias='realtimeMessages')
    realtimebandwidth: Optional[AdditionalResource] = Field(default=None, alias='realtimeBandwidth')
    storage: AdditionalResource = Field(..., alias='storage')
    users: AdditionalResource = Field(..., alias='users')
    gbhours: AdditionalResource = Field(..., alias='GBHours')
    imagetransformations: AdditionalResource = Field(..., alias='imageTransformations')
    credits: Optional[AdditionalResource] = Field(default=None, alias='credits')
