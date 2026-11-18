# Accounting: Fixed Assets Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#fixed-assets). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-fixed-assets-nuxt`
**Matching domain module:** `accounting-fixed-assets`
**Application:** Accounting
**Source feature:** [Fixed Assets](../features/fixed-assets.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/fixed-assets.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-fixed-assets` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Asset register:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Categories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Acquisition:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Capitalization:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Components:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Locations/custodians:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Books:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Supporting documents:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-fixed-assets-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `asset-register`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `categories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `acquisition`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `capitalization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `components`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `locations-custodians`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `books`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `supporting-documents`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-fixed-assets` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/fixed-assets.md)) |
| Capability Nuxt module skeleton | [`module-accounting-fixed-assets-nuxt`](https://github.com/liberusoftware/module-accounting-fixed-assets-nuxt) (`@liberusoftware/module-accounting-fixed-assets-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Asset register** | Expose composable and Vue 3 component for `asset register` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/fixed-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Categories** | Expose composable and Vue 3 component for `categories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/fixed-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Acquisition** | Expose composable and Vue 3 component for `acquisition` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/fixed-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Capitalization** | Expose composable and Vue 3 component for `capitalization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/fixed-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Components** | Expose composable and Vue 3 component for `components` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/fixed-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Locations/custodians** | Expose composable and Vue 3 component for `locations/custodians` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/fixed-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Books** | Expose composable and Vue 3 component for `books` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/fixed-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Supporting documents** | Expose composable and Vue 3 component for `supporting documents` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/fixed-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

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
