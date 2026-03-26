# Change Log

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
