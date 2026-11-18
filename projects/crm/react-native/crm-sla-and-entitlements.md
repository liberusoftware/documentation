# Crm Sla And Entitlements React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-sla-and-entitlements). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-sla-and-entitlements-react-native
**Matching core package:** module-crm-crm-sla-and-entitlements ([implementation](../core/crm-sla-and-entitlements.md))
**Matching API package:** module-crm-crm-sla-and-entitlements-api ([contract](../api/crm-sla-and-entitlements.md))

## Implementation plan

This adapter presents Crm Sla And Entitlements for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Sla And Entitlements API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-sla-and-entitlements.md), and [API module](../api/crm-sla-and-entitlements.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-sla-and-entitlements`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-sla-and-entitlements.md)) |
| Capability React Native module skeleton | [`module-crm-sla-and-entitlements-react-native`](https://github.com/liberusoftware/module-crm-sla-and-entitlements-react-native) (`@liberusoftware/module-crm-sla-and-entitlements-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Service contracts** | Progressive mobile list/detail/sheet flow for `service contracts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Coverage** | Progressive mobile list/detail/sheet flow for `coverage` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Business calendars** | Progressive mobile list/detail/sheet flow for `business calendars` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Response/resolution targets** | Progressive mobile list/detail/sheet flow for `response/resolution targets` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Milestones** | Progressive mobile list/detail/sheet flow for `milestones` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Pauses** | Progressive mobile list/detail/sheet flow for `pauses` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Warnings** | Progressive mobile list/detail/sheet flow for `warnings` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Breaches** | Progressive mobile list/detail/sheet flow for `breaches` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Escalations** | Progressive mobile list/detail/sheet flow for `escalations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Exceptions** | Progressive mobile list/detail/sheet flow for `exceptions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SlaQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Queries/SlaQuery.php) | `public function contracts(int $teamId)`<br>`public function calendars(int $teamId)`<br>`public function entitlements(int $teamId)`<br>`public function cases(int $teamId)`<br>`public function escalations(int $teamId)`<br>`public function exceptions(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCalendar.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/CreateCalendar.php) | `public function execute(int $teamId, int $actorId, array $data): SlaCalendar` |
| [CreateContract.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/CreateContract.php) | `public function execute(int $teamId, int $actorId, array $data): SlaContract` |
| [EvaluateCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/EvaluateCase.php) | `public function execute(int $teamId, int $actorId, int $caseId): array` |
| [OpenCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/OpenCase.php) | `public function execute(int $teamId, int $actorId, array $data): SlaCase` |
| [RequestException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/RequestException.php) | `public function execute(int $teamId, int $actorId, array $data): SlaException` |
| [SetEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/SetEntitlement.php) | `public function execute(int $teamId, int $actorId, array $data): SlaEntitlement` |
| [TransitionCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/TransitionCase.php) | `public function execute(int $teamId, int $actorId, int $caseId, string $transition, array $data = []): SlaCase` |
| [SlaAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Services/SlaAudit.php) | `public function record(int $teamId, ?int $actorId, int $caseId, string $type, array $payload = []): SlaCaseEvent` |
| [SlaPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Services/SlaPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SlaCalendar.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaCalendar.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaCase.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaCaseEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaCaseEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaContract.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaContract.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaEntitlement.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaEscalation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaEscalation.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaException.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [SlaController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-api/src/Http/Controllers/SlaController.php) | `public function contracts(Request $r, SlaQuery $q): JsonResponse`<br>`public function calendars(Request $r, SlaQuery $q): JsonResponse`<br>`public function entitlements(Request $r, SlaQuery $q): JsonResponse`<br>`public function cases(Request $r, SlaQuery $q): JsonResponse`<br>`public function storeContract(Request $r, CreateContract $a): JsonResponse`<br>`public function storeCalendar(Request $r, CreateCalendar $a): JsonResponse`<br>`public function storeEntitlement(Request $r, SetEntitlement $a): JsonResponse`<br>`public function storeCase(Request $r, OpenCase $a): JsonResponse`<br>`public function transition(Request $r, int $case, string $transition, TransitionCase $a): JsonResponse`<br>`public function evaluate(Request $r, int $case, EvaluateCase $a): JsonResponse`<br>`public function exception(Request $r, RequestException $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-sla-and-entitlements-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/sla-and-entitlements')->group(function (): void {
Route::get('/contracts', [SlaController::class, 'contracts']);
Route::post('/contracts', [SlaController::class, 'storeContract']);
Route::get('/calendars', [SlaController::class, 'calendars']);
Route::post('/calendars', [SlaController::class, 'storeCalendar']);
Route::get('/entitlements', [SlaController::class, 'entitlements']);
Route::post('/entitlements', [SlaController::class, 'storeEntitlement']);
Route::get('/cases', [SlaController::class, 'cases']);
Route::post('/cases', [SlaController::class, 'storeCase']);
Route::post('/cases/{case}/{transition}', [SlaController::class, 'transition'])->whereIn('transition', ['responded', 'pause', 'resume', 'resolve', 'close']);
Route::post('/cases/{case}/evaluate', [SlaController::class, 'evaluate']);
Route::post('/exceptions', [SlaController::class, 'exception']);
```
<!-- layer-implementation-plan:end -->
