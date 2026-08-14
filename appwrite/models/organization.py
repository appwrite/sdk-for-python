from typing import Any, Dict, List, Optional, Union, cast, Generic, TypeVar, Type
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .preferences import Preferences
from .billing_plan import BillingPlan
from .billing_limits import BillingLimits

T = TypeVar('T')

class Organization(AppwriteModel, Generic[T]):
    """
    Organization

    Attributes
    ----------
    id : str
        Team ID.
    createdat : str
        Team creation date in ISO 8601 format.
    updatedat : str
        Team update date in ISO 8601 format.
    name : str
        Team name.
    total : float
        Total number of team members.
    prefs : Preferences[T]
        Team preferences as a key-value object
    billingbudget : Optional[float]
        Project budget limit. Null when no budget is set.
    budgetalerts : List[Any]
        Project budget limit
    billingplan : str
        Organization&#039;s billing plan ID.
    billingplanid : str
        Organization&#039;s billing plan ID.
    billingplandetails : BillingPlan
        Organization&#039;s billing plan.
    billingemail : str
        Billing email set for the organization.
    billingstartdate : str
        Billing cycle start date.
    billingcurrentinvoicedate : str
        Current invoice cycle start date.
    billingnextinvoicedate : str
        Next invoice cycle start date.
    billingtrialstartdate : Optional[str]
        Start date of trial.
    billingtrialdays : float
        Number of trial days.
    billingaggregationid : str
        Current active aggregation id.
    billinginvoiceid : str
        Current active aggregation id.
    paymentmethodid : str
        Default payment method.
    billingaddressid : Optional[str]
        Default payment method.
    backuppaymentmethodid : Optional[str]
        Backup payment method.
    status : str
        Team status.
    remarks : Optional[str]
        Remarks on team status.
    agreementbaa : Optional[str]
        Organization agreements
    programmanagername : Optional[str]
        Program manager&#039;s name.
    programmanagercalendar : Optional[str]
        Program manager&#039;s calendar link.
    programdiscordchannelname : Optional[str]
        Program&#039;s discord channel name.
    programdiscordchannelurl : Optional[str]
        Program&#039;s discord channel URL.
    billinglimits : Optional[BillingLimits]
        Billing limits reached
    billingplandowngrade : Optional[str]
        Billing plan selected for downgrade.
    billingtaxid : Optional[str]
        Tax Id
    markedfordeletion : bool
        Marked for deletion
    platform : str
        Product with which the organization is associated (appwrite or imagine)
    projects : List[Any]
        Selected projects
    """
    id: str = Field(..., alias='$id')
    createdat: str = Field(..., alias='$createdAt')
    updatedat: str = Field(..., alias='$updatedAt')
    name: str = Field(..., alias='name')
    total: float = Field(..., alias='total')
    prefs: Preferences[T] = Field(..., alias='prefs')
    billingbudget: Optional[float] = Field(default=None, alias='billingBudget')
    budgetalerts: List[Any] = Field(..., alias='budgetAlerts')
    billingplan: str = Field(..., alias='billingPlan')
    billingplanid: str = Field(..., alias='billingPlanId')
    billingplandetails: BillingPlan = Field(..., alias='billingPlanDetails')
    billingemail: str = Field(..., alias='billingEmail')
    billingstartdate: str = Field(..., alias='billingStartDate')
    billingcurrentinvoicedate: str = Field(..., alias='billingCurrentInvoiceDate')
    billingnextinvoicedate: str = Field(..., alias='billingNextInvoiceDate')
    billingtrialstartdate: Optional[str] = Field(default=None, alias='billingTrialStartDate')
    billingtrialdays: float = Field(..., alias='billingTrialDays')
    billingaggregationid: str = Field(..., alias='billingAggregationId')
    billinginvoiceid: str = Field(..., alias='billingInvoiceId')
    paymentmethodid: str = Field(..., alias='paymentMethodId')
    billingaddressid: Optional[str] = Field(default=None, alias='billingAddressId')
    backuppaymentmethodid: Optional[str] = Field(default=None, alias='backupPaymentMethodId')
    status: str = Field(..., alias='status')
    remarks: Optional[str] = Field(default=None, alias='remarks')
    agreementbaa: Optional[str] = Field(default=None, alias='agreementBAA')
    programmanagername: Optional[str] = Field(default=None, alias='programManagerName')
    programmanagercalendar: Optional[str] = Field(default=None, alias='programManagerCalendar')
    programdiscordchannelname: Optional[str] = Field(default=None, alias='programDiscordChannelName')
    programdiscordchannelurl: Optional[str] = Field(default=None, alias='programDiscordChannelUrl')
    billinglimits: Optional[BillingLimits] = Field(default=None, alias='billingLimits')
    billingplandowngrade: Optional[str] = Field(default=None, alias='billingPlanDowngrade')
    billingtaxid: Optional[str] = Field(default=None, alias='billingTaxId')
    markedfordeletion: bool = Field(..., alias='markedForDeletion')
    platform: str = Field(..., alias='platform')
    projects: List[Any] = Field(..., alias='projects')

    @classmethod
    def with_data(cls, data: Dict[str, Any], model_type: Type[T] = dict) -> 'Organization[T]':
        """Create Organization instance with typed data."""
        instance = cls.model_validate(data)
        if 'prefs' in data and data['prefs'] is not None:
            instance.prefs = Preferences.with_data(
                data['prefs'], model_type
            )
        return instance
