# Change Log

## 22.0.0

* Breaking: removed `Health` service and all health models and enums
* Breaking: removed `Usage` service and `UsageMetric`, `UsageDataPoint`, `UsageEventList`, `UsageGaugeList` models
* Breaking: removed messaging `list_message_logs`, `list_provider_logs`, `list_subscriber_logs`, `list_topic_logs` methods
* Breaking: renamed `tables_db.create` parameter `dedicated_database_id` to `specification`
* Breaking: removed `countryCode` and `countryName` from `ActivityEvent` model
* Added: `Client.set_bearer` for OAuth access token authentication
* Added: `organization` service `get`, `update`, `delete` and membership CRUD methods
* Added: `oauth2` service `create_par`, `list_organizations`, `list_projects` methods
* Added: `resource`, `audience`, `request_uri` OAuth2 parameters; `scope` on `approve`
* Added: `appwrite` OAuth provider, `OAuth2Appwrite` model, `update_o_auth2_appwrite` method
* Added: `Query.vector_dot`, `Query.vector_cosine`, `Query.vector_euclidean` methods
* Added: `apps.update_labels` method and `labels` field on `App` model
* Added: `new_specification` parameter to `backups.create_restoration`
* Added: `type` parameter to `functions` and `sites` `list_specifications`
* Added: `token` parameter to `functions.get_deployment_download`
* Added: `prompt` and `max_age` parameters to `update_o_auth2_oidc`; `default_scopes` to `update_o_auth2_server`
* Added: `BillingPlan`, `Organization`, `Program`, `Oauth2PAR`, `DatabaseStatus`, `BillingPlanGroup` models and enums
* Added: `status` on `Database`, `mode` on `Block`, `onboarding` on `Project`, geolocation fields on `Locale`
* Added: organization, `project.oauth2`, and `stages` key scope enum values
* Fixed: booleans now serialized as `true`/`false` in flattened query parameters
* Fixed: `model_dump` on `Document`, `Row`, `Preferences` now includes dynamic `data`

## 21.0.0

* Added: `apps` service for managing apps and app secrets
* Added: `oauth2` service for the OAuth2 authorization, device, and token flows
* Added: device authorization grant parameters (`verificationUrl`, `userCodeLength`, `userCodeFormat`, `deviceCodeDuration`) to `updateOAuth2Server`
* Added: `emailCanonical`, `emailIsFree`, `emailIsDisposable`, `emailIsCorporate`, and `emailIsCanonical` to the `User` model
* Added: `userAccessedAt` to the `Membership` model
* Added: `PolicyDenyCorporateEmail` and `deny-corporate-email` to `ProjectPolicyId`
* Added: `dedicatedDatabases.execute` to `ProjectKeyScopes`
* Breaking: `usage.listEvents` now takes a required `metrics` array with `resource`, `interval`, and `dimensions` instead of `queries` and `total`
* Breaking: Replaced `UsageEvent` and `UsageGauge` models with `UsageDataPoint` and `UsageMetric`
* Updated: Send an `Accept: application/json` header on all requests


## 20.1.0

* Added: `createSesProvider` and `updateSesProvider` to `messaging`
* Added: `updateOAuth2Server` to `project` for OAuth2 server settings
* Added: `updatePasswordStrengthPolicy` and `PolicyPasswordStrength` to `project`
* Added: `getAuditsDB` health check to `health`
* Added: `password-strength` to `ProjectPolicyId`
* Added: `apps.read` and `apps.write` to `ProjectKeyScopes`


## 20.0.0

* Breaking: Removed `githubImagine` and `googleImagine` from `ProjectOAuthProviderId`
* Breaking: Removed `deno-1.21`, `deno-1.24`, and `deno-1.35` from `Runtime` and `BuildRuntime`
* Breaking: Dropped numeric suffixes from `StatusCode` redirect members
* Added: `Organization` service for managing projects and API keys
* Added: `PolicyDenyAliasedEmail`, `PolicyDenyDisposableEmail`, and `PolicyDenyFreeEmail` policy models
* Added: `deny-aliased-email`, `deny-disposable-email`, and `deny-free-email` to `ProjectPolicyId`
* Replaced: `BrowserTheme`, `HealthQueueName`, `OrganizationKeyScopes`, and `Region` enums
* Added: `dart-3.12` and `flutter-3.44` runtimes
* Added: `ProjectList` model and new attributes on `Function`, `Site`, and `UsageGauge`
* Updated: `functions`, `sites`, `usage`, `health`, and `avatars` services
* Updated: Renamed `updatePresence` to `update` in the `presences` service

## 19.0.0

* Breaking: Renamed `AuthMethod` enum to `ProjectAuthMethodId`
* Breaking: Renamed `EmailTemplateType` to `ProjectEmailTemplateId` and `EmailTemplateLocale` to `ProjectEmailTemplateLocale`
* Breaking: Renamed `ServiceId` to `ProjectServiceId`, `ProtocolId` to `ProjectProtocolId`, `Secure` to `ProjectSMTPSecure`, `ProjectPolicy` to `ProjectPolicyId`
* Breaking: Replaced `Scopes` enum with `ProjectKeyScopes` for project key endpoints
* Breaking: Removed `update_deny_canonical_email_policy`; replaced with `update_deny_aliased_email_policy`, `update_deny_disposable_email_policy`, and `update_deny_free_email_policy`
* Breaking: Removed `AuthProvider` model; use new `ProjectOAuthProviderId` enum instead
* Added: `Project.get` method to fetch current project details
* Added: `Advisor`, `Presences`, and `Usage` services
* Added: `Insight`, `Presence`, `Report`, `UsageEvent`, and `UsageGauge` models with list variants
* Added: `ProjectAuthMethod`, `ProjectProtocol`, and `ProjectService` models
* Added: `ProjectOAuthProviderId` and `ProjectOAuth2GooglePrompt` enums
* Updated: `Project`, `Database`, and `OAuth2Google` model schemas
* Updated: `X-Appwrite-Response-Format` header to `1.9.5`

## 18.1.0

* Added: Introduced `bigint` create/update APIs for legacy Databases attributes
* Added: Introduced `bigint` create/update APIs for `TablesDB` columns
* Updated: Extended key-list query filters with `key`, `resourceType`, `resourceId`, and `secret`

## 18.0.0

* [BREAKING] Renamed Webhook model fields: `security` → `tls`, `httpUser` → `authUsername`, `httpPass` → `authPassword`, `signatureKey` → `secret`
* [BREAKING] Renamed Webhook service parameters to match: `security` → `tls`, `httpUser` → `authUsername`, `httpPass` → `authPassword`
* [BREAKING] Renamed `Webhooks.update_signature()` to `Webhooks.update_secret()` with new optional `secret` parameter
* Added `Client.get_headers()` method to retrieve request headers
* Added `secret` parameter to Webhook create and update methods
* Added `x` OAuth provider to `OAuthProvider` enum
* Added `userType` field to `Log` model
* Added `purge` parameter to `update_collection` and `update_table` for cache invalidation
* Added Project service: platform CRUD, key CRUD, protocol/service status management
* Added new models: `Key`, `KeyList`, `Project`, `DevKey`, `MockNumber`, `AuthProvider`, `PlatformAndroid`, `PlatformApple`, `PlatformLinux`, `PlatformList`, `PlatformWeb`, `PlatformWindows`, `BillingLimits`, `Block`
* Added new enums: `PlatformType`, `ProtocolId`, `ServiceId`
* Updated `BuildRuntime`, `Runtime` enums with `dart-3.11` and `flutter-3.41`
* Updated `Scopes` enum with `keys_read`, `keys_write`, `platforms_read`, `platforms_write`
* Updated `X-Appwrite-Response-Format` header to `1.9.1`
* Updated TTL description for list caching in Databases and TablesDB
* Simplified `_parse_response()` by removing `union_models` parameter

## 17.0.0

* [BREAKING] Changed `$sequence` type from `float` to `str` for `Row` and `Document` models
* [BREAKING] Renamed `IndexType` enum: split into `DatabasesIndexType` (with new `SPATIAL` value) and `TablesDBIndexType`
* [BREAKING] Replaced `specification` parameter with `build_specification` and `runtime_specification` in `functions.create()`, `functions.update()`, `sites.create()`, `sites.update()`
* Added new `Project` service with full CRUD for project-level environment variables
* Added new `Webhooks` service with full CRUD for project webhooks (including `update_signature`)
* Added `Webhook` and `WebhookList` models
* Added `users.update_impersonator()` method for enabling/disabling user impersonation
* Added impersonation support: `set_impersonate_user_id()`, `set_impersonate_user_email()`, `set_impersonate_user_phone()` on `Client`
* Added `impersonator` and `impersonatoruserid` optional fields to `User` model
* Added `deployment_retention` parameter to Functions and Sites create/update
* Added `start_command` parameter to Sites create/update
* Added `Documentsdb`, `Vectorsdb` values to `BackupServices` and `DatabaseType` enums
* Added `WebhooksRead`, `WebhooksWrite`, `ProjectRead`, `ProjectWrite` scopes
* Removed `get_queue_billing_project_aggregation`, `get_queue_billing_team_aggregation`, `get_queue_priority_builds`, `get_queue_region_manager`, `get_queue_threats` from `Health` service
* Updated `Log` model field descriptions to clarify impersonation behavior
* Updated `X-Appwrite-Response-Format` header to `1.9.0`

## 16.0.0

* Breaking change: All service methods now return typed Pydantic models instead of `Dict[str, Any]`
* Breaking change: Models with dynamic fields (e.g., `Row`, `Document`) now store user-defined data in a typed `.data` property instead of direct attribute access
* Breaking change: Added `pydantic>=2,<3` as a required dependency
* Breaking change: Minimum Python version raised from 3.5 to 3.9
* Added `AppwriteModel` base class (Pydantic `BaseModel`) for all response models with `from_dict()` and `to_dict()` helpers
* Added 130+ typed model classes under `appwrite/models/` (e.g., `Database`, `Collection`, `Document`, `User`, `Session`, `File`, `Bucket`, etc.)
* Added Generic[T] support for models with dynamic fields (e.g., `Row`, `Document`) - pass `model_type=YourModel` to methods like `get_row()` or `list_rows()` for type-safe access to user-defined data via `result.data.field_name`
* Updated README with `uv add appwrite` installation example
* Updated all doc examples to use typed response models (e.g., `result: TemplateFunctionList = functions.list_templates(...)`)

## 15.3.0

* Added get_console_pausing health endpoint
* Added ttl parameter to list_documents and list_rows for cached responses
* Added optional activate parameter to Sites.create_deployment
* Updated docs and examples to reflect TTL usage and activation
* Updated query filtering docs in Messaging service

## 15.2.0

* Extended BuildRuntime and Runtime enums with new runtime versions (e.g., node-23/24/25, php-8.4, ruby-3.4/4.0, python-3.13/3.14, python-ml-3.13, deno-2.5/2.6, dotnet-10, java-25, swift-6.2, kotlin-2.3, bun-1.2/1.3, go-1.24/1.25/1.26).
* Added new permission scopes: schedules.read, schedules.write, and events.read.
* Added contains_any and contains_all filter helpers to the Query API (plus enhanced contains with docstrings).
* Added optional encrypt parameter to all string attribute creation methods (e.g., longtext, mediumtext, text, varchar) in Databases to support encryption at rest.
* Updated README to reflect Appwrite server compatibility version 1.8.x.
* Backward-compatible enhancements: no breaking changes.

## 15.1.0

* Add `dart-3.10` and `flutter-3.38` to `BuildRuntime` and `Runtime` enums
* Fix `Roles` enum removed from Teams service; `roles` parameter now accepts `list[str]`
* Add support for the new `Backups` service

## 15.0.0

* Add array-based enum parameters (e.g., `permissions: list[BrowserPermission]`).
* Breaking change: `Output` enum has been removed; use `ImageFormat` instead.
* Add `getQueueAudits` support to `Health` service.
* Add longtext/mediumtext/text/varchar attribute and column helpers to `Databases` and `TablesDB` services.

## 14.1.0

* Added ability to create columns and indexes synchronously while creating a table

## 14.0.0

* Rename `VCSDeploymentType` enum to `VCSReferenceType`
* Change `create_template_deployment` method signature: replace `version` parameter with `type` (TemplateReferenceType) and `reference` parameters
* Add `get_screenshot` method to `Avatars` service
* Add `Theme`, `Timezone` and `Output` enums
* Add support for dart39 and flutter335 runtimes

## 13.6.1

* Fix passing of `None` to nullable parameters

## 13.6.0

* Add `total` parameter to list queries allowing skipping counting rows in a table for improved performance
* Add `Operator` class for atomic modification of rows via update, bulk update, upsert, and bulk upsert operations

## 13.5.0

* Add `create_resend_provider` and `update_resend_provider` methods to `Messaging` service
* Improve deprecation warnings
* Fix adding `Optional[]` to optional parameters
* Fix passing of `None` to nullable parameters

## 13.4.1

* Add transaction support for Databases and TablesDB

## 13.3.0

* Deprecate `createVerification` method in `Account` service
* Add `createEmailVerification` method in `Account` service

## 11.1.0

* Add `incrementDocumentAttribute` and `decrementDocumentAttribute` support to `Databases` service
* Add `dart38` and `flutter332` support to runtime models
* Add `gif` support to `ImageFormat` enum
* Add `upsertDocument` support to `Databases` service

## 11.0.0

* Add `<REGION>` to doc examples due to the new multi region endpoints
* Add doc examples and methods for bulk api transactions: `createDocuments`, `deleteDocuments` etc.
* Add doc examples, class and methods for new `Sites` service
* Add doc examples, class and methods for new `Tokens` service
* Add enums for `BuildRuntime `, `Adapter`, `Framework`, `DeploymentDownloadType` and `VCSDeploymentType`
* Update enum for `runtimes` with Pythonml312, Dart219, Flutter327 and Flutter329
* Add `token` param to `getFilePreview` and `getFileView` for File tokens usage
* Add `queries` and `search` params to `listMemberships` method
* Remove `search` param from `listExecutions` method

## 10.0.0

* Fix requests failing by removing `Content-Type` header from `GET` and `HEAD` requests

## 9.0.3

* Update sdk to use Numpy-style docstrings
