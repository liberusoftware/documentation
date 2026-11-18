# Accounting Projects And Jobs React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-projects-and-jobs). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-projects-and-jobs-react-native
**Matching core package:** module-accounting-accounting-projects-and-jobs ([implementation](../core/accounting-projects-and-jobs.md))
**Matching API package:** module-accounting-accounting-projects-and-jobs-api ([contract](../api/accounting-projects-and-jobs.md))

## Implementation plan

This adapter presents Accounting Projects And Jobs for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Projects And Jobs API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-projects-and-jobs.md), and [API module](../api/accounting-projects-and-jobs.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-projects-and-jobs`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-projects-and-jobs.md)) |
| Capability React Native module skeleton | [`module-accounting-projects-and-jobs-react-native`](https://github.com/liberusoftware/module-accounting-projects-and-jobs-react-native) (`@liberusoftware/module-accounting-projects-and-jobs-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Customers** | Progressive mobile list/detail/sheet flow for `customers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Project/job hierarchy** | Progressive mobile list/detail/sheet flow for `project/job hierarchy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Status** | Progressive mobile list/detail/sheet flow for `status` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Dates** | Progressive mobile list/detail/sheet flow for `dates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Managers** | Progressive mobile list/detail/sheet flow for `managers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Budgets** | Progressive mobile list/detail/sheet flow for `budgets` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Dimensions** | Progressive mobile list/detail/sheet flow for `dimensions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Source links** | Progressive mobile list/detail/sheet flow for `source links` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Lifecycle** | Progressive mobile list/detail/sheet flow for `lifecycle` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateProjectJob.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Actions/CreateProjectJob.php) | `public function handle(array $attributes): ProjectJob` |
| [TransitionProject.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Actions/TransitionProject.php) | `public function handle(ProjectJob $project, ProjectStatus $status): ProjectJob` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProjectCustomer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Models/ProjectCustomer.php) | `team_id`, `customer_ref`, `name`, `status`, `metadata` |
| [ProjectJob.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Models/ProjectJob.php) | `team_id`, `customer_id`, `parent_id`, `name`, `code`, `description`, `start_date`, `end_date`, `status`, `manager_ref`, `budget_amount`, `budget_currency`, `dimensions`, `source_links`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProjectsAndJobsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs-api/src/Http/Controllers/ProjectsAndJobsController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateProjectJob $action): mixed`<br>`public function show(Request $request, ProjectJob $project): ProjectJob`<br>`public function transition(Request $request, ProjectJob $project, TransitionProject $action): ProjectJob` |

**Observed route declarations:**

[modules/accounting-projects-and-jobs-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/projects-and-jobs')->group(function (): void {
Route::middleware('ability:accounting.projects-and-jobs.read')->group(function (): void {
Route::get('/', [ProjectsAndJobsController::class, 'index']);
Route::get('/{project}', [ProjectsAndJobsController::class, 'show']);
Route::middleware('ability:accounting.projects-and-jobs.write')->group(function (): void {
Route::post('/', [ProjectsAndJobsController::class, 'store']);
Route::post('/{project}/transition', [ProjectsAndJobsController::class, 'transition']);
```
<!-- layer-implementation-plan:end -->
