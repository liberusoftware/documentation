# Accounting Branch And Location Accounting React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-branch-and-location-accounting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-branch-and-location-accounting-react-native
**Matching core package:** module-accounting-accounting-branch-and-location-accounting ([implementation](../core/accounting-branch-and-location-accounting.md))
**Matching API package:** module-accounting-accounting-branch-and-location-accounting-api ([contract](../api/accounting-branch-and-location-accounting.md))

## Implementation plan

This adapter presents Accounting Branch And Location Accounting for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Branch And Location Accounting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-branch-and-location-accounting.md), and [API module](../api/accounting-branch-and-location-accounting.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-branch-and-location-accounting`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-branch-and-location-accounting.md)) |
| Capability React Native module skeleton | [`module-accounting-branch-and-location-accounting-react-native`](https://github.com/liberusoftware/module-accounting-branch-and-location-accounting-react-native) (`@liberusoftware/module-accounting-branch-and-location-accounting-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Branch/location dimensions or books** | Progressive mobile list/detail/sheet flow for `branch/location dimensions or books` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Local sequences/tax** | Progressive mobile list/detail/sheet flow for `local sequences/tax` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Allocations** | Progressive mobile list/detail/sheet flow for `allocations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Performance** | Progressive mobile list/detail/sheet flow for `performance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Statutory requirements** | Progressive mobile list/detail/sheet flow for `statutory requirements` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [BranchQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Queries/BranchQuery.php) | `public function forTeam(int $teamId, ?string $status = null): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateBranchValue.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Actions/AllocateBranchValue.php) | `public function handle(Branch $branch, float $amount): array` |
| [CreateBranch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Actions/CreateBranch.php) | `public function handle(array $attributes): Branch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Branch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting/src/Models/Branch.php) | `team_id`, `code`, `name`, `location`, `local_tax_code`, `sequence_prefix`, `allocation_rule`, `performance_target`, `statutory_reference`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [BranchController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting-api/src/Http/Controllers/BranchController.php) | `public function index(Request $request, BranchQuery $query): mixed`<br>`public function store(Request $request, CreateBranch $action): mixed`<br>`public function allocate(Request $request, string $branch, AllocateBranchValue $action): mixed` |

**Observed route declarations:**

[modules/accounting-branch-and-location-accounting-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-branch-and-location-accounting-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/branches')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [BranchController::class, 'index'])->middleware('ability:accounting.branch-and-location-accounting.read');
Route::post('/', [BranchController::class, 'store'])->middleware('ability:accounting.branch-and-location-accounting.write');
Route::post('/{branch}/allocate', [BranchController::class, 'allocate'])->middleware('ability:accounting.branch-and-location-accounting.write');
```
<!-- layer-implementation-plan:end -->
