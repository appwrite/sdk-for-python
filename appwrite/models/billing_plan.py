from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr

from .base_model import AppwriteModel
from .usage_billing_plan import UsageBillingPlan
from .billing_plan_addon import BillingPlanAddon
from .billing_plan_supported_addons import BillingPlanSupportedAddons
from .billing_plan_limits import BillingPlanLimits
from ..enums.billing_plan_group import BillingPlanGroup
from .program import Program
from .billing_plan_dedicated_database_limits import BillingPlanDedicatedDatabaseLimits

class BillingPlan(AppwriteModel):
    """
    billingPlan

    Attributes
    ----------
    id : str
        Plan ID.
    name : str
        Plan name
    desc : str
        Plan description
    order : float
        Plan order
    price : float
        Price
    trial : float
        Trial days
    bandwidth : float
        Bandwidth
    storage : float
        Storage
    imagetransformations : float
        Image Transformations
    screenshotsgenerated : float
        Screenshots generated
    members : float
        Members
    webhooks : float
        Webhooks
    wafrules : float
        Maximum WAF rules per project
    projects : float
        Projects
    platforms : float
        Platforms
    users : float
        Users
    teams : float
        Teams
    databases : float
        Databases
    databasesreads : float
        Database reads per month
    databaseswrites : float
        Database writes per month
    databasesbatchsize : float
        Database batch size limit
    buckets : float
        Buckets
    filesize : float
        File size
    functions : float
        Functions
    sites : float
        Sites
    executions : float
        Function executions
    executionsretentioncount : float
        Rolling max executions retained per function/site
    gbhours : float
        GB hours for functions
    realtime : float
        Realtime connections
    realtimemessages : float
        Realtime messages
    messages : float
        Messages per month
    topics : float
        Topics for messaging
    authphone : float
        SMS authentications per month
    domains : float
        Custom domains
    activitylogs : float
        Activity log days
    usagelogs : float
        Usage history days
    usagelogsintervals : Optional[List[Any]]
        Usage log time intervals allowed for this plan (e.g. 15m, 1h, 1d).
    projectinactivitydays : float
        Number of days of console inactivity before a project is paused. 0 means pausing is disabled.
    alertlimit : float
        Alert threshold percentage
    usage : UsageBillingPlan
        Additional resources
    addons : BillingPlanAddon
        Addons
    budgetcapenabled : bool
        Budget cap enabled or disabled.
    customsmtp : bool
        Custom SMTP
    emailbranding : bool
        Appwrite branding in email
    requirespaymentmethod : bool
        Does plan require payment method
    requiresbillingaddress : bool
        Does plan require billing address
    isavailable : bool
        Is the billing plan available
    selfservice : bool
        Can user change the plan themselves
    premiumsupport : bool
        Does plan enable premium support
    budgeting : bool
        Does plan support budget cap
    supportsmocknumbers : bool
        Does plan support mock numbers
    supportsorganizationroles : bool
        Does plan support organization roles
    supportscredits : bool
        Does plan support credit
    supportsdisposableemailvalidation : bool
        Does plan support blocking disposable email addresses.
    supportscanonicalemailvalidation : bool
        Does plan support requiring canonical email addresses.
    supportsfreeemailvalidation : bool
        Does plan support blocking free email addresses.
    supportscorporateemailvalidation : bool
        Does plan support restricting sign-ups to corporate email addresses only.
    supportsprojectspecificroles : bool
        Does plan support project-specific member roles.
    backupsenabled : bool
        Does plan support backup policies.
    usageperproject : bool
        Whether usage addons are calculated per project.
    supportedaddons : BillingPlanSupportedAddons
        Supported addons for this plan
    backuppolicies : float
        How many policies does plan support
    deploymentsize : float
        Maximum function and site deployment size in MB
    buildsize : float
        Maximum function and site deployment size in MB
    databasesallowencrypt : bool
        Does the plan support encrypted string attributes or not.
    limits : Optional[BillingPlanLimits]
        Plan specific limits
    group : BillingPlanGroup
        Group of this billing plan for variants
    program : Optional[Program]
        Details of the program this plan is a part of.
    dedicateddatabases : Optional[BillingPlanDedicatedDatabaseLimits]
        Dedicated database limits available to this plan.
    """
    id: str = Field(..., alias='$id')
    name: str = Field(..., alias='name')
    desc: str = Field(..., alias='desc')
    order: float = Field(..., alias='order')
    price: float = Field(..., alias='price')
    trial: float = Field(..., alias='trial')
    bandwidth: float = Field(..., alias='bandwidth')
    storage: float = Field(..., alias='storage')
    imagetransformations: float = Field(..., alias='imageTransformations')
    screenshotsgenerated: float = Field(..., alias='screenshotsGenerated')
    members: float = Field(..., alias='members')
    webhooks: float = Field(..., alias='webhooks')
    wafrules: float = Field(..., alias='wafRules')
    projects: float = Field(..., alias='projects')
    platforms: float = Field(..., alias='platforms')
    users: float = Field(..., alias='users')
    teams: float = Field(..., alias='teams')
    databases: float = Field(..., alias='databases')
    databasesreads: float = Field(..., alias='databasesReads')
    databaseswrites: float = Field(..., alias='databasesWrites')
    databasesbatchsize: float = Field(..., alias='databasesBatchSize')
    buckets: float = Field(..., alias='buckets')
    filesize: float = Field(..., alias='fileSize')
    functions: float = Field(..., alias='functions')
    sites: float = Field(..., alias='sites')
    executions: float = Field(..., alias='executions')
    executionsretentioncount: float = Field(..., alias='executionsRetentionCount')
    gbhours: float = Field(..., alias='GBHours')
    realtime: float = Field(..., alias='realtime')
    realtimemessages: float = Field(..., alias='realtimeMessages')
    messages: float = Field(..., alias='messages')
    topics: float = Field(..., alias='topics')
    authphone: float = Field(..., alias='authPhone')
    domains: float = Field(..., alias='domains')
    activitylogs: float = Field(..., alias='activityLogs')
    usagelogs: float = Field(..., alias='usageLogs')
    usagelogsintervals: Optional[List[Any]] = Field(default=None, alias='usageLogsIntervals')
    projectinactivitydays: float = Field(..., alias='projectInactivityDays')
    alertlimit: float = Field(..., alias='alertLimit')
    usage: UsageBillingPlan = Field(..., alias='usage')
    addons: BillingPlanAddon = Field(..., alias='addons')
    budgetcapenabled: bool = Field(..., alias='budgetCapEnabled')
    customsmtp: bool = Field(..., alias='customSmtp')
    emailbranding: bool = Field(..., alias='emailBranding')
    requirespaymentmethod: bool = Field(..., alias='requiresPaymentMethod')
    requiresbillingaddress: bool = Field(..., alias='requiresBillingAddress')
    isavailable: bool = Field(..., alias='isAvailable')
    selfservice: bool = Field(..., alias='selfService')
    premiumsupport: bool = Field(..., alias='premiumSupport')
    budgeting: bool = Field(..., alias='budgeting')
    supportsmocknumbers: bool = Field(..., alias='supportsMockNumbers')
    supportsorganizationroles: bool = Field(..., alias='supportsOrganizationRoles')
    supportscredits: bool = Field(..., alias='supportsCredits')
    supportsdisposableemailvalidation: bool = Field(..., alias='supportsDisposableEmailValidation')
    supportscanonicalemailvalidation: bool = Field(..., alias='supportsCanonicalEmailValidation')
    supportsfreeemailvalidation: bool = Field(..., alias='supportsFreeEmailValidation')
    supportscorporateemailvalidation: bool = Field(..., alias='supportsCorporateEmailValidation')
    supportsprojectspecificroles: bool = Field(..., alias='supportsProjectSpecificRoles')
    backupsenabled: bool = Field(..., alias='backupsEnabled')
    usageperproject: bool = Field(..., alias='usagePerProject')
    supportedaddons: BillingPlanSupportedAddons = Field(..., alias='supportedAddons')
    backuppolicies: float = Field(..., alias='backupPolicies')
    deploymentsize: float = Field(..., alias='deploymentSize')
    buildsize: float = Field(..., alias='buildSize')
    databasesallowencrypt: bool = Field(..., alias='databasesAllowEncrypt')
    limits: Optional[BillingPlanLimits] = Field(default=None, alias='limits')
    group: BillingPlanGroup = Field(..., alias='group')
    program: Optional[Program] = Field(default=None, alias='program')
    dedicateddatabases: Optional[BillingPlanDedicatedDatabaseLimits] = Field(default=None, alias='dedicatedDatabases')
