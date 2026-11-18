# Commercial React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#commercial). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-commercial-react-native
**Matching core package:** module-maintenance-commercial ([implementation](../core/commercial.md))
**Matching API package:** module-maintenance-commercial-api ([contract](../api/commercial.md))

## Implementation plan

This adapter presents Commercial for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Commercial API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/commercial.md), and [API module](../api/commercial.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `commercial`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-maintenance-mobile-react`](https://github.com/liberusoftware/project-maintenance-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/commercial.md)) |
| Capability React Native module skeleton | [`module-maintenance-commercial-react-native`](https://github.com/liberusoftware/module-maintenance-commercial-react-native) (`@liberusoftware/module-maintenance-commercial-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Quotes** | Progressive mobile list/detail/sheet flow for `quotes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Contracts** | Progressive mobile list/detail/sheet flow for `contracts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Covered assets/services** | Progressive mobile list/detail/sheet flow for `covered assets/services` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rates** | Progressive mobile list/detail/sheet flow for `rates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Renewals** | Progressive mobile list/detail/sheet flow for `renewals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **SLA** | Progressive mobile list/detail/sheet flow for `sla` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Billable lines** | Progressive mobile list/detail/sheet flow for `billable lines` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Actions/CreateCommercialRecord.php) | `public function handle(int $teamId, array $attributes): CommercialRecord` |
| [DeleteCommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Actions/DeleteCommercialRecord.php) | `public function handle(int $teamId, CommercialRecord $record): void` |
| [TransitionCommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Actions/TransitionCommercialRecord.php) | `public function handle(int $teamId, CommercialRecord $record, string $status): CommercialRecord` |
| [UpdateCommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Actions/UpdateCommercialRecord.php) | `public function handle(int $teamId, CommercialRecord $record, array $attributes): CommercialRecord` |
| [CommercialRecordPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Policies/CommercialRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, CommercialRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, CommercialRecord $record): bool`<br>`public function delete(object $user, CommercialRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommercialRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial/src/Models/CommercialRecord.php) | `kind`, `title`, `description`, `amount`, `currency`, `status`, `metadata`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CommercialRecordController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial-api/src/Http/Controllers/CommercialRecordController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateCommercialRecord $create): JsonResponse`<br>`public function show(Request $request, CommercialRecord $record): JsonResponse`<br>`public function update(Request $request, CommercialRecord $record, UpdateCommercialRecord $update): JsonResponse`<br>`public function destroy(Request $request, CommercialRecord $record, DeleteCommercialRecord $delete): JsonResponse`<br>`public function transition(Request $request, CommercialRecord $record, TransitionCommercialRecord $transition): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-commercial-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-commercial-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/commercial')->group(function (): void {
Route::get('/', [CommercialRecordController::class, 'index']);
Route::post('/', [CommercialRecordController::class, 'store']);
Route::post('/{record}/transition', [CommercialRecordController::class, 'transition']);
Route::get('/{record}', [CommercialRecordController::class, 'show']);
Route::patch('/{record}', [CommercialRecordController::class, 'update']);
Route::delete('/{record}', [CommercialRecordController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
