# Data Processing React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#data-processing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-automation-data-processing-react-native
**Matching core package:** module-automation-data-processing ([implementation](../core/data-processing.md))
**Matching API package:** module-automation-data-processing-api ([contract](../api/data-processing.md))

## Implementation plan

This adapter presents Data Processing for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Data Processing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/data-processing.md), and [API module](../api/data-processing.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `data-processing`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-automation-mobile-react`](https://github.com/liberusoftware/project-automation-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/data-processing.md)) |
| Capability React Native module skeleton | [`module-automation-data-processing-react-native`](https://github.com/liberusoftware/module-automation-data-processing-react-native) (`@liberusoftware/module-automation-data-processing-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Classification** | Progressive mobile list/detail/sheet flow for `classification` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Extraction** | Progressive mobile list/detail/sheet flow for `extraction` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Summarization** | Progressive mobile list/detail/sheet flow for `summarization` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Translation** | Progressive mobile list/detail/sheet flow for `translation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Enrichment** | Progressive mobile list/detail/sheet flow for `enrichment` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Redaction** | Progressive mobile list/detail/sheet flow for `redaction` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Batch processing** | Progressive mobile list/detail/sheet flow for `batch processing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDataProcessingResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing/src/Actions/CreateDataProcessingResource.php) | `public function execute(string $teamId, string $name, array $payload = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): DataProcessingResource` |
| [TransitionDataProcessingResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing/src/Actions/TransitionDataProcessingResource.php) | `public function execute(DataProcessingResource $resource, string $teamId, string $status, array $allowedStatuses = ['draft', 'active', 'paused', 'completed', 'failed', 'cancelled'], ?string $actorId = null, ?string $correlationId = null): DataProcessingResource` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DataProcessingResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing/src/Models/DataProcessingResource.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [DataProcessingResourceController.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing-api/src/Http/Controllers/DataProcessingResourceController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateDataProcessingResource $create): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function update(Request $request, string $id): JsonResponse`<br>`public function destroy(Request $request, string $id): JsonResponse`<br>`public function transition(Request $request, string $id, TransitionDataProcessingResource $transition): JsonResponse` |

**Observed route declarations:**

[modules/module-automation-data-processing-api/routes/api.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-data-processing-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:60,1'])->prefix('api/v1/automation/data-processing')->group(function (): void {
Route::get('/', [DataProcessingResourceController::class, 'index']);
Route::post('/', [DataProcessingResourceController::class, 'store']);
Route::get('/{id}', [DataProcessingResourceController::class, 'show']);
Route::patch('/{id}', [DataProcessingResourceController::class, 'update']);
Route::delete('/{id}', [DataProcessingResourceController::class, 'destroy']);
Route::post('/{id}/transition', [DataProcessingResourceController::class, 'transition']);
```
<!-- layer-implementation-plan:end -->
