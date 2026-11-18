# Real Estate Valuations React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-valuations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-valuations-react-native
**Matching core package:** module-real-estate-real-estate-valuations ([implementation](../core/real-estate-valuations.md))
**Matching API package:** module-real-estate-real-estate-valuations-api ([contract](../api/real-estate-valuations.md))

## Implementation plan

This adapter presents Real Estate Valuations for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Valuations API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/real-estate-valuations.md), and [API module](../api/real-estate-valuations.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `real-estate-valuations`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-real-estate-mobile-react`](https://github.com/liberusoftware/project-real-estate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-valuations.md)) |
| Capability React Native module skeleton | [`module-real-estate-valuations-react-native`](https://github.com/liberusoftware/module-real-estate-valuations-react-native) (`@liberusoftware/module-real-estate-valuations-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Appraisals** | Progressive mobile list/detail/sheet flow for `appraisals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Comparables** | Progressive mobile list/detail/sheet flow for `comparables` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Pricing** | Progressive mobile list/detail/sheet flow for `pricing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Fees** | Progressive mobile list/detail/sheet flow for `fees` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Recommendations** | Progressive mobile list/detail/sheet flow for `recommendations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Follow-up** | Progressive mobile list/detail/sheet flow for `follow-up` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Conversion** | Progressive mobile list/detail/sheet flow for `conversion` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ValuationPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Policies/ValuationPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Valuation $valuation): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Valuation $valuation): bool`<br>`public function delete(AuthUser $authUser, Valuation $valuation): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Valuation $valuation): bool`<br>`public function forceDelete(AuthUser $authUser, Valuation $valuation): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Valuation $valuation): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Valuation.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations/src/Models/Valuation.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ValuationController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations-api/src/Http/Controllers/ValuationController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateValuation $create): JsonResponse`<br>`public function calculateNeuralProperty(Request $request, GenerateNeuralPropertyValuation $generate): JsonResponse`<br>`public function show(Request $request, Valuation $valuation): JsonResponse`<br>`public function update(Request $request, Valuation $valuation, UpdateValuation $update): JsonResponse`<br>`public function destroy(Request $request, Valuation $valuation, DeleteValuation $delete): Response`<br>`public function schedule(Request $request, Valuation $valuation, ScheduleValuation $schedule): JsonResponse`<br>`public function complete(Request $request, Valuation $valuation, CompleteValuation $complete): JsonResponse`<br>`public function convert(Request $request, Valuation $valuation, ConvertValuation $convert): JsonResponse`<br>`public function comparables(Request $request, Valuation $valuation, CalculateComparables $calculate): JsonResponse`<br>`public function calculateHome(Request $request, CalculateHomeValuation $calculate): JsonResponse`<br>`public function calculateProperty(Request $request, GeneratePropertyValuation $calculate): JsonResponse`<br>`public function calculateMortgage(Request $request, CalculateMortgage $calculate): JsonResponse`<br>`public function calculateRentalYield(Request $request, CalculateRentalYield $calculate): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-valuations-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/valuations')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [ValuationController::class, 'index'])->name('real-estate.valuations.index');
Route::post('/', [ValuationController::class, 'store'])->name('real-estate.valuations.store');
Route::post('/calculate-home', [ValuationController::class, 'calculateHome'])->name('real-estate.valuations.calculate-home');
Route::post('/calculate-property', [ValuationController::class, 'calculateProperty'])->name('real-estate.valuations.calculate-property');
Route::post('/calculate-neural-property', [ValuationController::class, 'calculateNeuralProperty'])->name('real-estate.valuations.calculate-neural-property');
Route::post('/calculate-mortgage', [ValuationController::class, 'calculateMortgage'])->name('real-estate.valuations.calculate-mortgage');
Route::post('/calculate-rental-yield', [ValuationController::class, 'calculateRentalYield'])->name('real-estate.valuations.calculate-rental-yield');
Route::get('/{valuation}', [ValuationController::class, 'show'])->name('real-estate.valuations.show');
Route::delete('/{valuation}', [ValuationController::class, 'destroy'])->name('real-estate.valuations.destroy');
Route::post('/{valuation}/schedule', [ValuationController::class, 'schedule'])->name('real-estate.valuations.schedule');
Route::post('/{valuation}/complete', [ValuationController::class, 'complete'])->name('real-estate.valuations.complete');
Route::post('/{valuation}/convert', [ValuationController::class, 'convert'])->name('real-estate.valuations.convert');
Route::post('/{valuation}/comparables', [ValuationController::class, 'comparables'])->name('real-estate.valuations.comparables');
```
<!-- layer-implementation-plan:end -->
