# Real Estate Valuations Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-valuations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-valuations-flutter
**Matching core package:** module-real-estate-real-estate-valuations ([implementation](../core/real-estate-valuations.md))
**Matching API package:** module-real-estate-real-estate-valuations-api ([contract](../api/real-estate-valuations.md))

## Implementation plan

This adapter presents Real Estate Valuations for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Valuations API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/real-estate-valuations.md), and [API module](../api/real-estate-valuations.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `real-estate-valuations`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-real-estate-mobile-flutter`](https://github.com/liberusoftware/project-real-estate-mobile-flutter) | [`module-real-estate-valuations-flutter`](https://github.com/liberusoftware/module-real-estate-valuations-flutter) (`module_real_estate_valuations_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-real-estate-dart-mobile`](https://github.com/liberusoftware/project-real-estate-dart-mobile) | [`module-real-estate-valuations-dart-mobile`](https://github.com/liberusoftware/module-real-estate-valuations-dart-mobile) (`module_real_estate_valuations_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-real-estate-dart-desktop`](https://github.com/liberusoftware/project-real-estate-dart-desktop) | [`module-real-estate-valuations-dart-desktop`](https://github.com/liberusoftware/module-real-estate-valuations-dart-desktop) (`module_real_estate_valuations_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | [API plan](../api/real-estate-valuations.md) · [Core plan](../core/real-estate-valuations.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Appraisals** | Adaptive mobile cards/sheets for `appraisals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `appraisals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Comparables** | Adaptive mobile cards/sheets for `comparables` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `comparables` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Pricing** | Adaptive mobile cards/sheets for `pricing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `pricing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Fees** | Adaptive mobile cards/sheets for `fees` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `fees` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Recommendations** | Adaptive mobile cards/sheets for `recommendations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `recommendations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Follow-up** | Adaptive mobile cards/sheets for `follow-up` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `follow-up` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Conversion** | Adaptive mobile cards/sheets for `conversion` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `conversion` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
