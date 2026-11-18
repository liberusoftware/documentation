# Accounting Close Management React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-close-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-close-management-react-native
**Matching core package:** module-accounting-accounting-close-management ([implementation](../core/accounting-close-management.md))
**Matching API package:** module-accounting-accounting-close-management-api ([contract](../api/accounting-close-management.md))

## Implementation plan

This adapter presents Accounting Close Management for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Close Management API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-close-management.md), and [API module](../api/accounting-close-management.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-close-management`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-close-management.md)) |
| Capability React Native module skeleton | [`module-accounting-close-management-react-native`](https://github.com/liberusoftware/module-accounting-close-management-react-native) (`@liberusoftware/module-accounting-close-management-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Checklist** | Progressive mobile list/detail/sheet flow for `checklist` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Owners** | Progressive mobile list/detail/sheet flow for `owners` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Dependencies** | Progressive mobile list/detail/sheet flow for `dependencies` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Due dates** | Progressive mobile list/detail/sheet flow for `due dates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Evidence** | Progressive mobile list/detail/sheet flow for `evidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliations** | Progressive mobile list/detail/sheet flow for `reconciliations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Adjustments** | Progressive mobile list/detail/sheet flow for `adjustments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Review** | Progressive mobile list/detail/sheet flow for `review` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Certification** | Progressive mobile list/detail/sheet flow for `certification` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Lock** | Progressive mobile list/detail/sheet flow for `lock` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reopen** | Progressive mobile list/detail/sheet flow for `reopen` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CloseCycleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Queries/CloseCycleQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CertifyCloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/CertifyCloseCycle.php) | `public function handle(CloseCycle $cycle, array $certification): CloseCycle` |
| [CreateCloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/CreateCloseCycle.php) | `public function handle(array $attributes): CloseCycle` |
| [LockCloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/LockCloseCycle.php) | `public function handle(CloseCycle $cycle): CloseCycle` |
| [RecordCloseEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/RecordCloseEvidence.php) | `public function handle(CloseCycle $cycle, array $evidence): CloseCycle` |
| [ReopenCloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/ReopenCloseCycle.php) | `public function handle(CloseCycle $cycle, string $reason): CloseCycle` |
| [UpdateCloseChecklist.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Actions/UpdateCloseChecklist.php) | `public function handle(CloseCycle $cycle, array $checklist): CloseCycle` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CloseCycle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management/src/Models/CloseCycle.php) | `team_id`, `cycle_ref`, `period`, `due_date`, `status`, `checklist`, `owners`, `dependencies`, `evidence`, `reconciliations`, `adjustments`, `review`, `certification` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CloseCyclesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management-api/src/Http/Controllers/CloseCyclesController.php) | `public function index(CloseCycleQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCloseCycle $action): JsonResponse`<br>`public function checklist(Request $request, string $cycle, UpdateCloseChecklist $action): JsonResponse`<br>`public function evidence(Request $request, string $cycle, RecordCloseEvidence $action): JsonResponse`<br>`public function certify(Request $request, string $cycle, CertifyCloseCycle $action): JsonResponse`<br>`public function lock(string $cycle, LockCloseCycle $action): JsonResponse`<br>`public function reopen(Request $request, string $cycle, ReopenCloseCycle $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-close-management-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-close-management-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/close-management')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.close-management.read')->get('/', [CloseCyclesController::class, 'index']);
Route::middleware('ability:accounting.close-management.write')->group(function (): void {
Route::post('/', [CloseCyclesController::class, 'store']);
Route::post('/{cycle}/checklist', [CloseCyclesController::class, 'checklist']);
Route::post('/{cycle}/evidence', [CloseCyclesController::class, 'evidence']);
Route::post('/{cycle}/certify', [CloseCyclesController::class, 'certify']);
Route::post('/{cycle}/lock', [CloseCyclesController::class, 'lock']);
Route::post('/{cycle}/reopen', [CloseCyclesController::class, 'reopen']);
```
<!-- layer-implementation-plan:end -->
