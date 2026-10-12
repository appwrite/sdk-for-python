from typing import Any, Dict, List, Optional, Union, cast
from pydantic import Field, PrivateAttr, model_validator

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
    members : Optional[float]
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
    activitylogs : Optional[float]
        Activity log days
    usagelogs : float
        Usage history days
    usagelogsintervals : Optional[List[Any]]
        Usage log time intervals allowed for this plan (e.g. 15m, 1h, 1d).
    usageaggregateonlymetrics : Optional[List[Any]]
        Metrics this plan only records as a total. They cannot be broken down by dimension or filtered, because the stored events cover a fraction of the real traffic.
    projectinactivitydays : float
        Number of days of console inactivity before a project is paused. 0 means pausing is disabled.
    alertlimit : float
        Alert threshold percentage
    usage : Optional[UsageBillingPlan]
        Additional resources. Null when the plan does not support usage billing.
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
    eligiblecountries : Optional[List[Any]]
        ISO country codes eligible for this regional plan. Empty means no restriction.
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
    supportsdedicateddatabases : bool
        Does plan support dedicated databases.
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
    backupsenabled : Optional[bool]
        Does plan support backup policies.
    usageperproject : bool
        Whether usage addons are calculated per project.
    supportedaddons : BillingPlanSupportedAddons
        Supported addons for this plan
    backuppolicies : Optional[float]
        How many policies does plan support
    deploymentsize : float
        Maximum function and site deployment size in MB
    buildsize : float
        Maximum function and site deployment size in MB
    functionsintervalminimum : float
        Shortest function schedule interval allowed, in minutes. 0 allows every interval.
    databasesallowencrypt : bool
        Does the plan support encrypted string attributes or not.
    limits : Optional[BillingPlanLimits]
        Plan specific limits
    group : BillingPlanGroup
        Group of this billing plan for variants
    program : Optional[Program]
        Details of the program this plan is a part of.
    databasecomputecredit : float
        Included monthly dedicated-database compute credit in USD. Resets each billing cycle with no roll-over.
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
    members: Optional[float] = Field(default=None, alias='members')
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
    activitylogs: Optional[float] = Field(default=None, alias='activityLogs')
    usagelogs: float = Field(..., alias='usageLogs')
    usagelogsintervals: Optional[List[Any]] = Field(default=None, alias='usageLogsIntervals')
    usageaggregateonlymetrics: Optional[List[Any]] = Field(default=None, alias='usageAggregateOnlyMetrics')
    projectinactivitydays: float = Field(..., alias='projectInactivityDays')
    alertlimit: float = Field(..., alias='alertLimit')
    usage: Optional[UsageBillingPlan] = Field(default=None, alias='usage')
    addons: BillingPlanAddon = Field(..., alias='addons')
    budgetcapenabled: bool = Field(..., alias='budgetCapEnabled')
    customsmtp: bool = Field(..., alias='customSmtp')
    emailbranding: bool = Field(..., alias='emailBranding')
    requirespaymentmethod: bool = Field(..., alias='requiresPaymentMethod')
    requiresbillingaddress: bool = Field(..., alias='requiresBillingAddress')
    eligiblecountries: Optional[List[Any]] = Field(default=None, alias='eligibleCountries')
    isavailable: bool = Field(..., alias='isAvailable')
    selfservice: bool = Field(..., alias='selfService')
    premiumsupport: bool = Field(..., alias='premiumSupport')
    budgeting: bool = Field(..., alias='budgeting')
    supportsmocknumbers: bool = Field(..., alias='supportsMockNumbers')
    supportsorganizationroles: bool = Field(..., alias='supportsOrganizationRoles')
    supportscredits: bool = Field(..., alias='supportsCredits')
    supportsdedicateddatabases: bool = Field(..., alias='supportsDedicatedDatabases')
    supportsdisposableemailvalidation: bool = Field(..., alias='supportsDisposableEmailValidation')
    supportscanonicalemailvalidation: bool = Field(..., alias='supportsCanonicalEmailValidation')
    supportsfreeemailvalidation: bool = Field(..., alias='supportsFreeEmailValidation')
    supportscorporateemailvalidation: bool = Field(..., alias='supportsCorporateEmailValidation')
    supportsprojectspecificroles: bool = Field(..., alias='supportsProjectSpecificRoles')
    backupsenabled: Optional[bool] = Field(default=None, alias='backupsEnabled')
    usageperproject: bool = Field(..., alias='usagePerProject')
    supportedaddons: BillingPlanSupportedAddons = Field(..., alias='supportedAddons')
    backuppolicies: Optional[float] = Field(default=None, alias='backupPolicies')
    deploymentsize: float = Field(..., alias='deploymentSize')
    buildsize: float = Field(..., alias='buildSize')
    functionsintervalminimum: float = Field(..., alias='functionsIntervalMinimum')
    databasesallowencrypt: bool = Field(..., alias='databasesAllowEncrypt')
    limits: Optional[BillingPlanLimits] = Field(default=None, alias='limits')
    group: BillingPlanGroup = Field(..., alias='group')
    program: Optional[Program] = Field(default=None, alias='program')
    databasecomputecredit: float = Field(..., alias='databaseComputeCredit')
    dedicateddatabases: Optional[BillingPlanDedicatedDatabaseLimits] = Field(default=None, alias='dedicatedDatabases')

    @model_validator(mode='before')
    @classmethod
    def _apply_defaults(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data

        data = dict(data)
        if '$id' not in data and 'id' not in data:
            data['$id'] = ''
        if 'name' not in data:
            data['name'] = ''
        if 'desc' not in data:
            data['desc'] = ''
        if 'order' not in data:
            data['order'] = 0
        if 'price' not in data:
            data['price'] = 0
        if 'trial' not in data:
            data['trial'] = 0
        if 'bandwidth' not in data:
            data['bandwidth'] = 0
        if 'storage' not in data:
            data['storage'] = 0
        if 'imageTransformations' not in data and 'imagetransformations' not in data:
            data['imageTransformations'] = 0
        if 'screenshotsGenerated' not in data and 'screenshotsgenerated' not in data:
            data['screenshotsGenerated'] = 0
        if 'webhooks' not in data:
            data['webhooks'] = 0
        if 'wafRules' not in data and 'wafrules' not in data:
            data['wafRules'] = 0
        if 'projects' not in data:
            data['projects'] = 0
        if 'platforms' not in data:
            data['platforms'] = 0
        if 'users' not in data:
            data['users'] = 0
        if 'teams' not in data:
            data['teams'] = 0
        if 'databases' not in data:
            data['databases'] = 0
        if 'databasesReads' not in data and 'databasesreads' not in data:
            data['databasesReads'] = 0
        if 'databasesWrites' not in data and 'databaseswrites' not in data:
            data['databasesWrites'] = 0
        if 'databasesBatchSize' not in data and 'databasesbatchsize' not in data:
            data['databasesBatchSize'] = 0
        if 'buckets' not in data:
            data['buckets'] = 0
        if 'fileSize' not in data and 'filesize' not in data:
            data['fileSize'] = 0
        if 'functions' not in data:
            data['functions'] = 0
        if 'sites' not in data:
            data['sites'] = 0
        if 'executions' not in data:
            data['executions'] = 0
        if 'executionsRetentionCount' not in data and 'executionsretentioncount' not in data:
            data['executionsRetentionCount'] = 1000
        if 'GBHours' not in data and 'gbhours' not in data:
            data['GBHours'] = 0
        if 'realtime' not in data:
            data['realtime'] = 0
        if 'realtimeMessages' not in data and 'realtimemessages' not in data:
            data['realtimeMessages'] = 0
        if 'messages' not in data:
            data['messages'] = 0
        if 'topics' not in data:
            data['topics'] = 0
        if 'authPhone' not in data and 'authphone' not in data:
            data['authPhone'] = 0
        if 'domains' not in data:
            data['domains'] = 0
        if 'usageLogs' not in data and 'usagelogs' not in data:
            data['usageLogs'] = 0
        if 'projectInactivityDays' not in data and 'projectinactivitydays' not in data:
            data['projectInactivityDays'] = 0
        if 'alertLimit' not in data and 'alertlimit' not in data:
            data['alertLimit'] = 80
        if 'budgetCapEnabled' not in data and 'budgetcapenabled' not in data:
            data['budgetCapEnabled'] = False
        if 'customSmtp' not in data and 'customsmtp' not in data:
            data['customSmtp'] = False
        if 'emailBranding' not in data and 'emailbranding' not in data:
            data['emailBranding'] = False
        if 'requiresPaymentMethod' not in data and 'requirespaymentmethod' not in data:
            data['requiresPaymentMethod'] = True
        if 'requiresBillingAddress' not in data and 'requiresbillingaddress' not in data:
            data['requiresBillingAddress'] = False
        if 'isAvailable' not in data and 'isavailable' not in data:
            data['isAvailable'] = True
        if 'selfService' not in data and 'selfservice' not in data:
            data['selfService'] = True
        if 'premiumSupport' not in data and 'premiumsupport' not in data:
            data['premiumSupport'] = True
        if 'budgeting' not in data:
            data['budgeting'] = True
        if 'supportsMockNumbers' not in data and 'supportsmocknumbers' not in data:
            data['supportsMockNumbers'] = True
        if 'supportsOrganizationRoles' not in data and 'supportsorganizationroles' not in data:
            data['supportsOrganizationRoles'] = True
        if 'supportsCredits' not in data and 'supportscredits' not in data:
            data['supportsCredits'] = False
        if 'supportsDedicatedDatabases' not in data and 'supportsdedicateddatabases' not in data:
            data['supportsDedicatedDatabases'] = False
        if 'supportsDisposableEmailValidation' not in data and 'supportsdisposableemailvalidation' not in data:
            data['supportsDisposableEmailValidation'] = False
        if 'supportsCanonicalEmailValidation' not in data and 'supportscanonicalemailvalidation' not in data:
            data['supportsCanonicalEmailValidation'] = False
        if 'supportsFreeEmailValidation' not in data and 'supportsfreeemailvalidation' not in data:
            data['supportsFreeEmailValidation'] = False
        if 'supportsCorporateEmailValidation' not in data and 'supportscorporateemailvalidation' not in data:
            data['supportsCorporateEmailValidation'] = False
        if 'supportsProjectSpecificRoles' not in data and 'supportsprojectspecificroles' not in data:
            data['supportsProjectSpecificRoles'] = False
        if 'usagePerProject' not in data and 'usageperproject' not in data:
            data['usagePerProject'] = True
        if 'deploymentSize' not in data and 'deploymentsize' not in data:
            data['deploymentSize'] = 0
        if 'buildSize' not in data and 'buildsize' not in data:
            data['buildSize'] = 0
        if 'functionsIntervalMinimum' not in data and 'functionsintervalminimum' not in data:
            data['functionsIntervalMinimum'] = 0
        if 'databasesAllowEncrypt' not in data and 'databasesallowencrypt' not in data:
            data['databasesAllowEncrypt'] = False
        if 'databaseComputeCredit' not in data and 'databasecomputecredit' not in data:
            data['databaseComputeCredit'] = 0
        return data
