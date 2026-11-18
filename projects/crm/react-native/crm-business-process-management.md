# Crm Business Process Management React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-business-process-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-business-process-management-react-native
**Matching core package:** module-crm-crm-business-process-management ([implementation](../core/crm-business-process-management.md))
**Matching API package:** module-crm-crm-business-process-management-api ([contract](../api/crm-business-process-management.md))

## Implementation plan

This adapter presents Crm Business Process Management for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Business Process Management API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-business-process-management.md), and [API module](../api/crm-business-process-management.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-business-process-management`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-business-process-management.md)) |
| Capability React Native module skeleton | [`module-crm-business-process-management-react-native`](https://github.com/liberusoftware/module-crm-business-process-management-react-native) (`@liberusoftware/module-crm-business-process-management-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Guided stages** | Progressive mobile list/detail/sheet flow for `guided stages` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Required steps/data** | Progressive mobile list/detail/sheet flow for `required steps/data` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approvals** | Progressive mobile list/detail/sheet flow for `approvals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Validations** | Progressive mobile list/detail/sheet flow for `validations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Service processes** | Progressive mobile list/detail/sheet flow for `service processes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Exception routing** | Progressive mobile list/detail/sheet flow for `exception routing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Process versioning** | Progressive mobile list/detail/sheet flow for `process versioning` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProcessQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Queries/ProcessQuery.php) | `public function processes(int $teamId): Builder`<br>`public function runs(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AdvanceProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/AdvanceProcess.php) | `public function execute(int $teamId, int $actorId, ProcessRun $run, array $context = []): ProcessRun` |
| [CreateProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/CreateProcess.php) | `public function execute(int $teamId, int $ownerId, array $input): Process` |
| [PublishProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/PublishProcess.php) | `public function execute(int $teamId, int $actorId, Process $process): Process` |
| [StartProcess.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Actions/StartProcess.php) | `public function execute(int $teamId, int $actorId, Process $process, array $context = []): ProcessRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Process.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/Process.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProcessEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/ProcessEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProcessRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management/src/Models/ProcessRun.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [BusinessProcessesController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management-api/src/Http/Controllers/BusinessProcessesController.php) | `public function __construct(private readonly ProcessQuery $query)`<br>`public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateProcess $action): JsonResponse`<br>`public function publish(Request $request, Process $process, PublishProcess $action): JsonResponse`<br>`public function start(Request $request, Process $process, StartProcess $action): JsonResponse`<br>`public function advance(Request $request, ProcessRun $run, AdvanceProcess $action): JsonResponse`<br>`public function runs(Request $request): JsonResponse` |

**Observed route declarations:**

[modules/crm-business-process-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-business-process-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/business-process-management')->group(function (): void {
Route::get('/', [BusinessProcessesController::class, 'index']);
Route::post('/', [BusinessProcessesController::class, 'store']);
Route::post('{process}/publish', [BusinessProcessesController::class, 'publish']);
Route::post('{process}/runs', [BusinessProcessesController::class, 'start']);
Route::post('runs/{run}/advance', [BusinessProcessesController::class, 'advance']);
Route::get('runs', [BusinessProcessesController::class, 'runs']);
```
<!-- layer-implementation-plan:end -->
