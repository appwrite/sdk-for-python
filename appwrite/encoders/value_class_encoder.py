import json
from ..models.base_model import AppwriteModel
from ..enums.authenticator_type import AuthenticatorType
from ..enums.authentication_factor import AuthenticationFactor
from ..enums.o_auth_provider import OAuthProvider
from ..enums.browser import Browser
from ..enums.credit_card import CreditCard
from ..enums.flag import Flag
from ..enums.browser_theme import BrowserTheme
from ..enums.timezone import Timezone
from ..enums.browser_permission import BrowserPermission
from ..enums.image_format import ImageFormat
from ..enums.backup_services import BackupServices
from ..enums.relationship_type import RelationshipType
from ..enums.relation_mutate import RelationMutate
from ..enums.databases_index_type import DatabasesIndexType
from ..enums.order_by import OrderBy
from ..enums.runtime import Runtime
from ..enums.project_key_scopes import ProjectKeyScopes
from ..enums.template_reference_type import TemplateReferenceType
from ..enums.vcs_reference_type import VCSReferenceType
from ..enums.deployment_download_type import DeploymentDownloadType
from ..enums.execution_method import ExecutionMethod
from ..enums.message_priority import MessagePriority
from ..enums.smtp_encryption import SmtpEncryption
from ..enums.organization_key_scopes import OrganizationKeyScopes
from ..enums.region import Region
from ..enums.project_auth_method_id import ProjectAuthMethodId
from ..enums.project_o_auth2_google_prompt import ProjectOAuth2GooglePrompt
from ..enums.project_o_auth2_oidc_prompt import ProjectOAuth2OidcPrompt
from ..enums.project_o_auth_provider_id import ProjectOAuthProviderId
from ..enums.project_policy_id import ProjectPolicyId
from ..enums.project_protocol_id import ProjectProtocolId
from ..enums.project_service_id import ProjectServiceId
from ..enums.project_smtp_secure import ProjectSMTPSecure
from ..enums.project_email_template_id import ProjectEmailTemplateId
from ..enums.project_email_template_locale import ProjectEmailTemplateLocale
from ..enums.status_code import StatusCode
from ..enums.proxy_resource_type import ProxyResourceType
from ..enums.framework import Framework
from ..enums.build_runtime import BuildRuntime
from ..enums.adapter import Adapter
from ..enums.compression import Compression
from ..enums.image_gravity import ImageGravity
from ..enums.tables_db_index_type import TablesDBIndexType
from ..enums.password_hash import PasswordHash
from ..enums.messaging_provider_type import MessagingProviderType
from ..enums.database_type import DatabaseType
from ..enums.database_status import DatabaseStatus
from ..enums.attribute_status import AttributeStatus
from ..enums.column_status import ColumnStatus
from ..enums.index_status import IndexStatus
from ..enums.deployment_status import DeploymentStatus
from ..enums.execution_trigger import ExecutionTrigger
from ..enums.execution_status import ExecutionStatus
from ..enums.o_auth2_google_prompt import OAuth2GooglePrompt
from ..enums.o_auth2_oidc_prompt import OAuth2OidcPrompt
from ..enums.platform_type import PlatformType
from ..enums.proxy_rule_deployment_resource_type import ProxyRuleDeploymentResourceType
from ..enums.proxy_rule_status import ProxyRuleStatus
from ..enums.message_status import MessageStatus
from ..enums.billing_plan_group import BillingPlanGroup

class ValueClassEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, AppwriteModel):
            return o.to_dict()

        if isinstance(o, AuthenticatorType):
            return o.value

        if isinstance(o, AuthenticationFactor):
            return o.value

        if isinstance(o, OAuthProvider):
            return o.value

        if isinstance(o, Browser):
            return o.value

        if isinstance(o, CreditCard):
            return o.value

        if isinstance(o, Flag):
            return o.value

        if isinstance(o, BrowserTheme):
            return o.value

        if isinstance(o, Timezone):
            return o.value

        if isinstance(o, BrowserPermission):
            return o.value

        if isinstance(o, ImageFormat):
            return o.value

        if isinstance(o, BackupServices):
            return o.value

        if isinstance(o, RelationshipType):
            return o.value

        if isinstance(o, RelationMutate):
            return o.value

        if isinstance(o, DatabasesIndexType):
            return o.value

        if isinstance(o, OrderBy):
            return o.value

        if isinstance(o, Runtime):
            return o.value

        if isinstance(o, ProjectKeyScopes):
            return o.value

        if isinstance(o, TemplateReferenceType):
            return o.value

        if isinstance(o, VCSReferenceType):
            return o.value

        if isinstance(o, DeploymentDownloadType):
            return o.value

        if isinstance(o, ExecutionMethod):
            return o.value

        if isinstance(o, MessagePriority):
            return o.value

        if isinstance(o, SmtpEncryption):
            return o.value

        if isinstance(o, OrganizationKeyScopes):
            return o.value

        if isinstance(o, Region):
            return o.value

        if isinstance(o, ProjectAuthMethodId):
            return o.value

        if isinstance(o, ProjectOAuth2GooglePrompt):
            return o.value

        if isinstance(o, ProjectOAuth2OidcPrompt):
            return o.value

        if isinstance(o, ProjectOAuthProviderId):
            return o.value

        if isinstance(o, ProjectPolicyId):
            return o.value

        if isinstance(o, ProjectProtocolId):
            return o.value

        if isinstance(o, ProjectServiceId):
            return o.value

        if isinstance(o, ProjectSMTPSecure):
            return o.value

        if isinstance(o, ProjectEmailTemplateId):
            return o.value

        if isinstance(o, ProjectEmailTemplateLocale):
            return o.value

        if isinstance(o, StatusCode):
            return o.value

        if isinstance(o, ProxyResourceType):
            return o.value

        if isinstance(o, Framework):
            return o.value

        if isinstance(o, BuildRuntime):
            return o.value

        if isinstance(o, Adapter):
            return o.value

        if isinstance(o, Compression):
            return o.value

        if isinstance(o, ImageGravity):
            return o.value

        if isinstance(o, TablesDBIndexType):
            return o.value

        if isinstance(o, PasswordHash):
            return o.value

        if isinstance(o, MessagingProviderType):
            return o.value

        if isinstance(o, DatabaseType):
            return o.value

        if isinstance(o, DatabaseStatus):
            return o.value

        if isinstance(o, AttributeStatus):
            return o.value

        if isinstance(o, ColumnStatus):
            return o.value

        if isinstance(o, IndexStatus):
            return o.value

        if isinstance(o, DeploymentStatus):
            return o.value

        if isinstance(o, ExecutionTrigger):
            return o.value

        if isinstance(o, ExecutionStatus):
            return o.value

        if isinstance(o, OAuth2GooglePrompt):
            return o.value

        if isinstance(o, OAuth2OidcPrompt):
            return o.value

        if isinstance(o, PlatformType):
            return o.value

        if isinstance(o, ProxyRuleDeploymentResourceType):
            return o.value

        if isinstance(o, ProxyRuleStatus):
            return o.value

        if isinstance(o, MessageStatus):
            return o.value

        if isinstance(o, BillingPlanGroup):
            return o.value

        return super().default(o)
