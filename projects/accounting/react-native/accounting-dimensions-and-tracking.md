# Accounting Dimensions And Tracking React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-dimensions-and-tracking). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-dimensions-and-tracking-react-native
**Matching core package:** module-accounting-accounting-dimensions-and-tracking ([implementation](../core/accounting-dimensions-and-tracking.md))
**Matching API package:** module-accounting-accounting-dimensions-and-tracking-api ([contract](../api/accounting-dimensions-and-tracking.md))

## Implementation plan

This adapter presents Accounting Dimensions And Tracking for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Dimensions And Tracking API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-dimensions-and-tracking.md), and [API module](../api/accounting-dimensions-and-tracking.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-dimensions-and-tracking`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-dimensions-and-tracking.md)) |
| Capability React Native module skeleton | [`module-accounting-dimensions-and-tracking-react-native`](https://github.com/liberusoftware/module-accounting-dimensions-and-tracking-react-native) (`@liberusoftware/module-accounting-dimensions-and-tracking-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Classes/categories** | Progressive mobile list/detail/sheet flow for `classes/categories` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Locations** | Progressive mobile list/detail/sheet flow for `locations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Departments** | Progressive mobile list/detail/sheet flow for `departments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cost/profit centers** | Progressive mobile list/detail/sheet flow for `cost/profit centers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Projects** | Progressive mobile list/detail/sheet flow for `projects` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tags** | Progressive mobile list/detail/sheet flow for `tags` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Validation** | Progressive mobile list/detail/sheet flow for `validation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Allocations** | Progressive mobile list/detail/sheet flow for `allocations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Dimensional balances** | Progressive mobile list/detail/sheet flow for `dimensional balances` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DimensionalBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Queries/DimensionalBalances.php) | `public function handle(?string $key = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateDimensions.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Actions/AllocateDimensions.php) | `public function handle(string $key, string\|int\|float $amount, array $allocations, ?string $currency = null, ?string $actor = null): array` |
| [SaveDimension.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Actions/SaveDimension.php) | `public function handle(array $attributes, ?Dimension $dimension = null): Dimension` |
| [SaveDimensionValue.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Actions/SaveDimensionValue.php) | `public function handle(Dimension $dimension, array $attributes, ?DimensionValue $value = null): DimensionValue` |
| [ValidateDimensions.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Actions/ValidateDimensions.php) | `public function handle(array $values): array` |
| [DimensionsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/src/Policies/DimensionsPolicy.php) | `public function viewAny(?Authenticatable $u): bool`<br>`public function view(?Authenticatable $u, Dimension $d): bool`<br>`public function create(?Authenticatable $u): bool`<br>`public function update(?Authenticatable $u, Dimension $d): bool`<br>`public function delete(?Authenticatable $u, Dimension $d): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Dimension.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Models/Dimension.php) | `code`, `name`, `kind`, `description`, `is_required`, `is_active`, `metadata` |
| [DimensionAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Models/DimensionAllocation.php) | `allocation_key`, `amount`, `currency`, `percentage`, `dimensions`, `created_by` |
| [DimensionValue.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking/src/Models/DimensionValue.php) | `dimension_id`, `code`, `name`, `parent_id`, `is_active`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [DimensionsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/src/Http/Controllers/DimensionsController.php) | `public function index(Request $request)`<br>`public function show(string $dimension): DimensionResource`<br>`public function store(Request $request, SaveDimension $save)`<br>`public function update(Request $request, string $dimension, SaveDimension $save): DimensionResource`<br>`public function values(Request $request, string $dimension, SaveDimensionValue $save)`<br>`public function validateValues(Request $request, ValidateDimensions $validate)`<br>`public function allocate(Request $request, AllocateDimensions $allocate)`<br>`public function balances(Request $request, DimensionalBalances $balances)`<br>`public function destroy(string $dimension): Response` |

**Observed route declarations:**

[modules/accounting-dimensions-and-tracking-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:60,1'])->prefix('api/v1/accounting/dimensions-and-tracking')->group(function (): void {
Route::get('/', [DimensionsController::class, 'index'])->middleware('ability:accounting.dimensions.read');
Route::post('/', [DimensionsController::class, 'store'])->middleware('ability:accounting.dimensions.write');
Route::get('/balances', [DimensionsController::class, 'balances'])->middleware('ability:accounting.dimensions.read');
Route::post('/validate', [DimensionsController::class, 'validateValues'])->middleware('ability:accounting.dimensions.read');
Route::post('/allocate', [DimensionsController::class, 'allocate'])->middleware('ability:accounting.dimensions.write');
Route::get('/{dimension}', [DimensionsController::class, 'show'])->middleware('ability:accounting.dimensions.read');
Route::patch('/{dimension}', [DimensionsController::class, 'update'])->middleware('ability:accounting.dimensions.write');
Route::post('/{dimension}/values', [DimensionsController::class, 'values'])->middleware('ability:accounting.dimensions.write');
Route::delete('/{dimension}', [DimensionsController::class, 'destroy'])->middleware('ability:accounting.dimensions.write');
```
<!-- layer-implementation-plan:end -->
