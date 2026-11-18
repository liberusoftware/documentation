# Automation Core React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#automation-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-automation-automation-core-react-native
**Matching core package:** module-automation-automation-core ([implementation](../core/automation-core.md))
**Matching API package:** module-automation-automation-core-api ([contract](../api/automation-core.md))

## Implementation plan

This adapter presents Automation Core for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Automation Core API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/automation-core.md), and [API module](../api/automation-core.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `automation-core`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-automation-mobile-react`](https://github.com/liberusoftware/project-automation-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/automation-core.md)) |
| Capability React Native module skeleton | [`module-automation-automation-core-react-native`](https://github.com/liberusoftware/module-automation-automation-core-react-native) (`@liberusoftware/module-automation-automation-core-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Workflow definitions** | Progressive mobile list/detail/sheet flow for `workflow definitions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Versions** | Progressive mobile list/detail/sheet flow for `versions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Triggers** | Progressive mobile list/detail/sheet flow for `triggers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **State** | Progressive mobile list/detail/sheet flow for `state` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Runs** | Progressive mobile list/detail/sheet flow for `runs` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Variables** | Progressive mobile list/detail/sheet flow for `variables` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Schedules** | Progressive mobile list/detail/sheet flow for `schedules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Retries** | Progressive mobile list/detail/sheet flow for `retries` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cancellation** | Progressive mobile list/detail/sheet flow for `cancellation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Compensation** | Progressive mobile list/detail/sheet flow for `compensation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-automation-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CancelWorkflowRun.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/CancelWorkflowRun.php) | `public function execute(WorkflowRunRecord $run, string $teamId, ?string $actorId = null, ?string $correlationId = null): WorkflowRunRecord` |
| [CreateAutomationCoreResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/CreateAutomationCoreResource.php) | `public function execute(string $teamId, string $name, array $payload = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): AutomationCoreResource` |
| [PublishWorkflow.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/PublishWorkflow.php) | `public function execute(AutomationCoreResource $workflow, string $teamId, WorkflowDefinition $definition, ?string $actorId = null, ?string $correlationId = null): WorkflowVersion` |
| [StartWorkflowRun.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/StartWorkflowRun.php) | `public function execute(AutomationCoreResource $workflow, string $teamId, array $variables = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): WorkflowRunRecord` |
| [TransitionAutomationCoreResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Actions/TransitionAutomationCoreResource.php) | `public function execute(AutomationCoreResource $resource, string $teamId, string $status, array $allowedStatuses = ['draft', 'active', 'paused', 'completed', 'failed', 'cancelled'], ?string $actorId = null, ?string $correlationId = null): AutomationCoreResource` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AutomationCoreResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Models/AutomationCoreResource.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkflowRunRecord.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Models/WorkflowRunRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkflowVersion.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core/src/Models/WorkflowVersion.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AutomationCoreResourceController.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core-api/src/Http/Controllers/AutomationCoreResourceController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateAutomationCoreResource $create): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function update(Request $request, string $id): JsonResponse`<br>`public function destroy(Request $request, string $id): JsonResponse`<br>`public function transition(Request $request, string $id, TransitionAutomationCoreResource $transition): JsonResponse`<br>`public function publish(Request $request, string $id, PublishWorkflow $publish): JsonResponse`<br>`public function run(Request $request, string $id, StartWorkflowRun $start): JsonResponse`<br>`public function cancelRun(Request $request, string $id, string $runId, CancelWorkflowRun $cancel): JsonResponse` |

**Observed route declarations:**

[modules/module-automation-automation-core-api/routes/api.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-automation-core-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:60,1'])->prefix('api/v1/automation/automation-core')->group(function (): void {
Route::get('/', [AutomationCoreResourceController::class, 'index']);
Route::post('/', [AutomationCoreResourceController::class, 'store']);
Route::get('/{id}', [AutomationCoreResourceController::class, 'show']);
Route::patch('/{id}', [AutomationCoreResourceController::class, 'update']);
Route::delete('/{id}', [AutomationCoreResourceController::class, 'destroy']);
Route::post('/{id}/transition', [AutomationCoreResourceController::class, 'transition']);
Route::post('/{id}/publish', [AutomationCoreResourceController::class, 'publish']);
Route::post('/{id}/runs', [AutomationCoreResourceController::class, 'run']);
Route::post('/{id}/runs/{runId}/cancel', [AutomationCoreResourceController::class, 'cancelRun']);
```
<!-- layer-implementation-plan:end -->
