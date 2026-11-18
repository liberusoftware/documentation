# Crm Data Operations React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-data-operations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-data-operations-react-native
**Matching core package:** module-crm-crm-data-operations ([implementation](../core/crm-data-operations.md))
**Matching API package:** module-crm-crm-data-operations-api ([contract](../api/crm-data-operations.md))

## Implementation plan

This adapter presents Crm Data Operations for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Data Operations API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-data-operations.md), and [API module](../api/crm-data-operations.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-data-operations`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-data-operations.md)) |
| Capability React Native module skeleton | [`module-crm-data-operations-react-native`](https://github.com/liberusoftware/module-crm-data-operations-react-native) (`@liberusoftware/module-crm-data-operations-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Imports/exports** | Progressive mobile list/detail/sheet flow for `imports/exports` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Field mapping** | Progressive mobile list/detail/sheet flow for `field mapping` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Normalization** | Progressive mobile list/detail/sheet flow for `normalization` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Enrichment orchestration** | Progressive mobile list/detail/sheet flow for `enrichment orchestration` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Duplicate detection/merge** | Progressive mobile list/detail/sheet flow for `duplicate detection/merge` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Formatting** | Progressive mobile list/detail/sheet flow for `formatting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quality rules** | Progressive mobile list/detail/sheet flow for `quality rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Schedules** | Progressive mobile list/detail/sheet flow for `schedules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Exception queues** | Progressive mobile list/detail/sheet flow for `exception queues` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Actions/CreateDataOperation.php) | `public function execute(int $teamId, ?int $actorId, array $attributes, array $mappings = []): DataOperation` |
| [ResolveException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Actions/ResolveException.php) | `public function execute(OperationException $exception, int $actorId): OperationException` |
| [TransitionDataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Actions/TransitionDataOperation.php) | `public function execute(DataOperation $operation, string $status, ?string $reason = null): DataOperation` |
| [DataOperationService.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Services/DataOperationService.php) | `public function mapAndNormalize(array $row, array $mapping): array`<br>`public function duplicateConfidence(array $left, array $right, array $fields): float` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DataOperation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/DataOperation.php) | `team_id`, `actor_id`, `kind`, `status`, `source`, `target`, `options`, `total_rows`, `processed_rows`, `failed_rows`, `failure_reason`, `started_at`, `completed_at` |
| [DuplicateMatch.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/DuplicateMatch.php) | `team_id`, `operation_id`, `left_record_id`, `right_record_id`, `confidence`, `status` |
| [FieldMapping.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/FieldMapping.php) | `operation_id`, `source_field`, `target_field`, `transform`, `required` |
| [OperationException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/OperationException.php) | `team_id`, `operation_id`, `row_number`, `payload`, `reason`, `status`, `resolved_by`, `resolved_at` |
| [OperationRule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/OperationRule.php) | `team_id`, `name`, `kind`, `definition`, `active` |
| [OperationSchedule.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations/src/Models/OperationSchedule.php) | `team_id`, `operation_id`, `cron`, `timezone`, `active`, `next_run_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [DataOperationController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations-api/src/Http/Controllers/DataOperationController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateDataOperation $create): JsonResponse`<br>`public function show(Request $request, int $operation): JsonResponse`<br>`public function update(Request $request, int $operation): JsonResponse`<br>`public function transition(Request $request, int $operation, TransitionDataOperation $transition): JsonResponse` |

**Observed route declarations:**

[modules/crm-data-operations-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-data-operations-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/data-operations')->group(function (): void {
Route::get('/', [DataOperationController::class, 'index']);
Route::post('/', [DataOperationController::class, 'store']);
Route::get('/{operation}', [DataOperationController::class, 'show']);
Route::patch('/{operation}', [DataOperationController::class, 'update']);
Route::post('/{operation}/transition', [DataOperationController::class, 'transition'])->middleware('throttle:api');
```
<!-- layer-implementation-plan:end -->
