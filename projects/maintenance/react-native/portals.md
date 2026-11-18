# Portals React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#portals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-portals-react-native
**Matching core package:** module-maintenance-portals ([implementation](../core/portals.md))
**Matching API package:** module-maintenance-portals-api ([contract](../api/portals.md))

## Implementation plan

This adapter presents Portals for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Portals API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/portals.md), and [API module](../api/portals.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `portals`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-maintenance-mobile-react`](https://github.com/liberusoftware/project-maintenance-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/portals.md)) |
| Capability React Native module skeleton | [`module-maintenance-portals-react-native`](https://github.com/liberusoftware/module-maintenance-portals-react-native) (`@liberusoftware/module-maintenance-portals-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Customer requests** | Progressive mobile list/detail/sheet flow for `customer requests` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approvals** | Progressive mobile list/detail/sheet flow for `approvals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Status** | Progressive mobile list/detail/sheet flow for `status` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Engineer schedule/work/offline capture** | Progressive mobile list/detail/sheet flow for `engineer schedule/work/offline capture` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePortalRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals/src/Actions/CreatePortalRecord.php) | `public function handle(int $teamId, array $attributes): PortalRecord` |
| [DeletePortalRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals/src/Actions/DeletePortalRecord.php) | `public function handle(int $teamId, PortalRecord $record): void` |
| [TransitionPortalRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals/src/Actions/TransitionPortalRecord.php) | `public function handle(int $teamId, PortalRecord $record, string $status): PortalRecord` |
| [UpdatePortalRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals/src/Actions/UpdatePortalRecord.php) | `public function handle(int $teamId, PortalRecord $record, array $attributes): PortalRecord` |
| [PortalRecordPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals/src/Policies/PortalRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, PortalRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, PortalRecord $record): bool`<br>`public function delete(object $user, PortalRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PortalRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals/src/Models/PortalRecord.php) | `kind`, `title`, `description`, `status`, `requested_by`, `metadata`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PortalsRecordController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals-api/src/Http/Controllers/PortalsRecordController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreatePortalRecord $create): JsonResponse`<br>`public function show(Request $request, PortalRecord $record): JsonResponse`<br>`public function update(Request $request, PortalRecord $record, UpdatePortalRecord $update): JsonResponse`<br>`public function destroy(Request $request, PortalRecord $record, DeletePortalRecord $delete): JsonResponse`<br>`public function transition(Request $request, PortalRecord $record, TransitionPortalRecord $transition): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-portals-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/portals')->group(function (): void {
Route::get('/', [PortalsRecordController::class, 'index']);
Route::post('/', [PortalsRecordController::class, 'store']);
Route::post('/{record}/transition', [PortalsRecordController::class, 'transition']);
Route::get('/{record}', [PortalsRecordController::class, 'show']);
Route::patch('/{record}', [PortalsRecordController::class, 'update']);
Route::delete('/{record}', [PortalsRecordController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
