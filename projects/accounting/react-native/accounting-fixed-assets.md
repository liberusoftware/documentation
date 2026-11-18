# Accounting Fixed Assets React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-fixed-assets). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-fixed-assets-react-native
**Matching core package:** module-accounting-accounting-fixed-assets ([implementation](../core/accounting-fixed-assets.md))
**Matching API package:** module-accounting-accounting-fixed-assets-api ([contract](../api/accounting-fixed-assets.md))

## Implementation plan

This adapter presents Accounting Fixed Assets for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Fixed Assets API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-fixed-assets.md), and [API module](../api/accounting-fixed-assets.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-fixed-assets`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-fixed-assets.md)) |
| Capability React Native module skeleton | [`module-accounting-fixed-assets-react-native`](https://github.com/liberusoftware/module-accounting-fixed-assets-react-native) (`@liberusoftware/module-accounting-fixed-assets-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Asset register** | Progressive mobile list/detail/sheet flow for `asset register` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Categories** | Progressive mobile list/detail/sheet flow for `categories` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Acquisition** | Progressive mobile list/detail/sheet flow for `acquisition` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Capitalization** | Progressive mobile list/detail/sheet flow for `capitalization` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Components** | Progressive mobile list/detail/sheet flow for `components` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Locations/custodians** | Progressive mobile list/detail/sheet flow for `locations/custodians` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Books** | Progressive mobile list/detail/sheet flow for `books` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Supporting documents** | Progressive mobile list/detail/sheet flow for `supporting documents` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AssetQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Queries/AssetQuery.php) | `public function paginate(?int $teamId = null, ?AssetStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function registerSummary(Asset $asset): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AcquireAsset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AcquireAsset.php) | `public function handle(AssetCategory $category, array $attributes): Asset` |
| [AddAssetComponent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AddAssetComponent.php) | `public function handle(Asset $asset, array $attributes): AssetComponent` |
| [AddAssetDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AddAssetDocument.php) | `public function handle(Asset $asset, array $attributes): AssetDocument` |
| [ArchiveAsset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/ArchiveAsset.php) | `public function handle(Asset $asset): Asset` |
| [AssignAssetCustodian.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AssignAssetCustodian.php) | `public function handle(Asset $asset, AssetCustodian $custodian): Asset` |
| [AssignAssetLocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AssignAssetLocation.php) | `public function handle(Asset $asset, AssetLocation $location): Asset` |
| [CapitalizeAsset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CapitalizeAsset.php) | `public function handle(Asset $asset, string $bookReference): Asset` |
| [CreateCategory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CreateCategory.php) | `public function handle(array $attributes): AssetCategory` |
| [CreateCustodian.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CreateCustodian.php) | `public function handle(array $attributes): AssetCustodian` |
| [CreateLocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CreateLocation.php) | `public function handle(array $attributes): AssetLocation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Asset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/Asset.php) | `team_id`, `asset_ref`, `name`, `category_id`, `status`, `acquired_on`, `capitalized_on`, `cost`, `salvage_value`, `net_book_value`, `currency`, `location_id`, `custodian_id`, `location_ref`, `custodian_ref`, `metadata` |
| [AssetBook.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetBook.php) | `asset_id`, `book_ref`, `cost`, `accumulated_depreciation`, `net_book_value`, `last_depreciated_on`, `metadata` |
| [AssetCategory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetCategory.php) | `team_id`, `category_ref`, `name`, `asset_account_ref`, `depreciation_account_ref`, `useful_life_months`, `depreciation_method`, `metadata` |
| [AssetComponent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetComponent.php) | `asset_id`, `component_ref`, `name`, `cost`, `useful_life_months`, `metadata` |
| [AssetCustodian.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetCustodian.php) | `team_id`, `custodian_ref`, `name`, `email`, `metadata` |
| [AssetDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetDocument.php) | `asset_id`, `document_ref`, `kind`, `file_ref`, `description`, `checksum`, `attached_by`, `attached_at`, `metadata` |
| [AssetLocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetLocation.php) | `team_id`, `location_ref`, `name`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [FixedAssetsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets-api/src/Http/Controllers/FixedAssetsController.php) | `public function __construct(private readonly AssetQuery $query)`<br>`public function index(Request $request): AnonymousResourceCollection`<br>`public function show(Request $request, Asset $asset): AssetResource`<br>`public function store(Request $request, AcquireAsset $action): AssetResource`<br>`public function category(Request $request, CreateCategory $action): JsonResponse`<br>`public function location(Request $request, CreateLocation $action): JsonResponse`<br>`public function custodian(Request $request, CreateCustodian $action): JsonResponse`<br>`public function update(Request $request, Asset $asset, UpdateAsset $action): AssetResource`<br>`public function delete(Request $request, Asset $asset, ArchiveAsset $action): JsonResponse`<br>`public function capitalize(Request $request, Asset $asset, CapitalizeAsset $action): AssetResource`<br>`public function dispose(Request $request, Asset $asset, DisposeAsset $action): AssetResource`<br>`public function document(Request $request, Asset $asset, AddAssetDocument $action): AssetResource`<br>`public function component(Request $request, Asset $asset, AddAssetComponent $action): AssetResource`<br>`public function assignLocation(Request $request, Asset $asset, AssignAssetLocation $action): AssetResource`<br>`public function assignCustodian(Request $request, Asset $asset, AssignAssetCustodian $action): AssetResource`<br>`public function summary(Request $request, Asset $asset): JsonResponse` |

**Observed route declarations:**

[modules/accounting-fixed-assets-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])
Route::middleware('ability:accounting.fixed-assets.read')->group(function (): void {
Route::get('/', [FixedAssetsController::class, 'index'])->name('accounting.fixed-assets.list');
Route::get('/{asset}', [FixedAssetsController::class, 'show'])->name('accounting.fixed-assets.show');
Route::get('/{asset}/summary', [FixedAssetsController::class, 'summary'])->name('accounting.fixed-assets.summary');
Route::middleware('ability:accounting.fixed-assets.write')->group(function (): void {
Route::post('/', [FixedAssetsController::class, 'store'])->name('accounting.fixed-assets.create');
Route::post('/categories', [FixedAssetsController::class, 'category'])->name('accounting.fixed-assets.categories.create');
Route::post('/locations', [FixedAssetsController::class, 'location'])->name('accounting.fixed-assets.locations.create');
Route::post('/custodians', [FixedAssetsController::class, 'custodian'])->name('accounting.fixed-assets.custodians.create');
Route::patch('/{asset}', [FixedAssetsController::class, 'update'])->name('accounting.fixed-assets.update');
Route::delete('/{asset}', [FixedAssetsController::class, 'delete'])->name('accounting.fixed-assets.archive');
Route::post('/{asset}/capitalize', [FixedAssetsController::class, 'capitalize'])->name('accounting.fixed-assets.capitalize');
Route::post('/{asset}/dispose', [FixedAssetsController::class, 'dispose'])->name('accounting.fixed-assets.dispose');
Route::post('/{asset}/components', [FixedAssetsController::class, 'component'])->name('accounting.fixed-assets.components.create');
Route::post('/{asset}/location', [FixedAssetsController::class, 'assignLocation'])->name('accounting.fixed-assets.location.assign');
Route::post('/{asset}/custodian', [FixedAssetsController::class, 'assignCustodian'])->name('accounting.fixed-assets.custodian.assign');
Route::post('/{asset}/documents', [FixedAssetsController::class, 'document'])->name('accounting.fixed-assets.documents.create');
```
<!-- layer-implementation-plan:end -->
