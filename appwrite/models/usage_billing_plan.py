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
    member : AdditionalResource
        Member additional resources
    realtime : AdditionalResource
        Realtime additional resources
    realtimemessages : AdditionalResource
        Realtime messages additional resources
    realtimebandwidth : AdditionalResource
        Realtime bandwidth additional resources
    storage : AdditionalResource
        Storage additional resources
    users : AdditionalResource
        User additional resources
    gbhours : AdditionalResource
        GBHour additional resources
    imagetransformations : AdditionalResource
        Image transformation additional resources
    credits : AdditionalResource
        Credits additional resources
    """
    bandwidth: AdditionalResource = Field(..., alias='bandwidth')
    executions: AdditionalResource = Field(..., alias='executions')
    member: AdditionalResource = Field(..., alias='member')
    realtime: AdditionalResource = Field(..., alias='realtime')
    realtimemessages: AdditionalResource = Field(..., alias='realtimeMessages')
    realtimebandwidth: AdditionalResource = Field(..., alias='realtimeBandwidth')
    storage: AdditionalResource = Field(..., alias='storage')
    users: AdditionalResource = Field(..., alias='users')
    gbhours: AdditionalResource = Field(..., alias='GBHours')
    imagetransformations: AdditionalResource = Field(..., alias='imageTransformations')
    credits: AdditionalResource = Field(..., alias='credits')
