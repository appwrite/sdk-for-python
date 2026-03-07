# Change Log

## 15.3.0

* Added `ActivityEvent` and `ActivityEventList` models to the public API
* Updated README with `uv add appwrite` example

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
