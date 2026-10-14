from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .additional_resource import AdditionalResource


class UsageBillingPlan(AppwriteModel):
    """
    usageBillingPlan

    Attributes
    ----------
    bandwidth : Optional[AdditionalResource]
        Bandwidth additional resources
    executions : Optional[AdditionalResource]
        Executions additional resources
    member : Optional[AdditionalResource]
        Member additional resources
    realtime : Optional[AdditionalResource]
        Realtime additional resources
    realtimemessages : Optional[AdditionalResource]
        Realtime messages additional resources
    realtimebandwidth : Optional[AdditionalResource]
        Realtime bandwidth additional resources
    storage : Optional[AdditionalResource]
        Storage additional resources
    users : Optional[AdditionalResource]
        User additional resources
    gbhours : Optional[AdditionalResource]
        GBHour additional resources
    imagetransformations : Optional[AdditionalResource]
        Image transformation additional resources
    credits : Optional[AdditionalResource]
        Credits additional resources
    """

    bandwidth: Optional[AdditionalResource] = Field(default=None, alias='bandwidth')
    executions: Optional[AdditionalResource] = Field(default=None, alias='executions')
    member: Optional[AdditionalResource] = Field(default=None, alias='member')
    realtime: Optional[AdditionalResource] = Field(default=None, alias='realtime')
    realtimemessages: Optional[AdditionalResource] = Field(default=None, alias='realtimeMessages')
    realtimebandwidth: Optional[AdditionalResource] = Field(default=None, alias='realtimeBandwidth')
    storage: Optional[AdditionalResource] = Field(default=None, alias='storage')
    users: Optional[AdditionalResource] = Field(default=None, alias='users')
    gbhours: Optional[AdditionalResource] = Field(default=None, alias='GBHours')
    imagetransformations: Optional[AdditionalResource] = Field(default=None, alias='imageTransformations')
    credits: Optional[AdditionalResource] = Field(default=None, alias='credits')
