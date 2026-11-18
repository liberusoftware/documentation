# Accounting Leases React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-leases). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-leases-react-native
**Matching core package:** module-accounting-accounting-leases ([implementation](../core/accounting-leases.md))
**Matching API package:** module-accounting-accounting-leases-api ([contract](../api/accounting-leases.md))

## Implementation plan

This adapter presents Accounting Leases for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Leases API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-leases.md), and [API module](../api/accounting-leases.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-leases`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-leases.md)) |
| Capability React Native module skeleton | [`module-accounting-leases-react-native`](https://github.com/liberusoftware/module-accounting-leases-react-native) (`@liberusoftware/module-accounting-leases-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Lease records** | Progressive mobile list/detail/sheet flow for `lease records` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Payment schedules** | Progressive mobile list/detail/sheet flow for `payment schedules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Right-of-use assets** | Progressive mobile list/detail/sheet flow for `right-of-use assets` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Liabilities** | Progressive mobile list/detail/sheet flow for `liabilities` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Interest/depreciation** | Progressive mobile list/detail/sheet flow for `interest/depreciation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Modifications** | Progressive mobile list/detail/sheet flow for `modifications` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Disclosures (optional)** | Progressive mobile list/detail/sheet flow for `disclosures (optional)` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [LeaseQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Queries/LeaseQuery.php) | `public function leases(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function disclosure(Lease $lease): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDisclosure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/CreateDisclosure.php) | `public function handle(Lease $lease, string $asOfDate): LeaseDisclosure` |
| [CreateLease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/CreateLease.php) | `public function handle(array $attributes): Lease` |
| [GenerateSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/GenerateSchedule.php) | `public function handle(Lease $lease): Lease` |
| [ModifyLease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/ModifyLease.php) | `public function handle(Lease $lease, array $attributes): Lease` |
| [PostPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/PostPayment.php) | `public function handle(LeasePayment $payment): LeasePayment` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Lease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/Lease.php) | `team_id`, `lease_ref`, `name`, `lessor_ref`, `asset_ref`, `commencement_date`, `end_date`, `currency`, `payment_amount`, `payment_frequency`, `interest_rate`, `discount_rate`, `useful_life_months`, `status`, `right_of_use_asset`, `lease_liability`, `accumulated_depreciation`, `metadata` |
| [LeaseDisclosure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeaseDisclosure.php) | `lease_id`, `as_of_date`, `remaining_liability`, `current_liability`, `non_current_liability`, `future_payments`, `notes`, `metadata` |
| [LeaseModification.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeaseModification.php) | `lease_id`, `modification_ref`, `effective_date`, `kind`, `old_term_end`, `new_term_end`, `old_payment_amount`, `new_payment_amount`, `adjustment_amount`, `reason`, `metadata` |
| [LeasePayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeasePayment.php) | `lease_id`, `payment_ref`, `due_date`, `amount`, `principal_amount`, `interest_amount`, `depreciation_amount`, `status`, `posted_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [LeasesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases-api/src/Http/Controllers/LeasesController.php) | `public function index(Request $request, LeaseQuery $query): mixed`<br>`public function store(Request $request, CreateLease $action): LeaseResource`<br>`public function show(Lease $lease): LeaseResource`<br>`public function schedule(Lease $lease, GenerateSchedule $action): LeaseResource`<br>`public function modify(Request $request, Lease $lease, ModifyLease $action): LeaseResource`<br>`public function disclosure(Request $request, Lease $lease, CreateDisclosure $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-leases-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/leases')->group(function (): void {
Route::get('/', [LeasesController::class, 'index'])->name('accounting.leases.list');
Route::post('/', [LeasesController::class, 'store'])->name('accounting.leases.create');
Route::get('/{lease}', [LeasesController::class, 'show'])->name('accounting.leases.show');
Route::post('/{lease}/schedule', [LeasesController::class, 'schedule'])->name('accounting.leases.schedule');
Route::post('/{lease}/modify', [LeasesController::class, 'modify'])->name('accounting.leases.modify');
Route::post('/{lease}/disclosure', [LeasesController::class, 'disclosure'])->name('accounting.leases.disclosure');
```
<!-- layer-implementation-plan:end -->
