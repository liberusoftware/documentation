# Fixed Assets: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-fixed-assets`.

**Proposed design identifier:** `module-accounting-fixed-assets-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/fixed-assets.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-fixed-assets](../../../modules/source/liberusoftware--module-accounting-fixed-assets.md) |
| API | [liberusoftware/module-accounting-fixed-assets-api](../../../modules/source/liberusoftware--module-accounting-fixed-assets-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Asset register | A focused authorized view or workflow section for asset register; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Categories | A focused authorized view or workflow section for categories; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Acquisition | A focused authorized view or workflow section for acquisition; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Capitalization | A focused authorized view or workflow section for capitalization; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Components | A focused authorized view or workflow section for components; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Locations/custodians | A focused authorized view or workflow section for locations/custodians; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Books | A focused authorized view or workflow section for books; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Supporting documents | A focused authorized view or workflow section for supporting documents; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [AssetQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Queries/AssetQuery.php) | `public function paginate(?int $teamId = null, ?AssetStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function registerSummary(Asset $asset): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AcquireAsset.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AcquireAsset.php) | `public function handle(AssetCategory $category, array $attributes): Asset` |
| [AddAssetComponent.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AddAssetComponent.php) | `public function handle(Asset $asset, array $attributes): AssetComponent` |
| [AddAssetDocument.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AddAssetDocument.php) | `public function handle(Asset $asset, array $attributes): AssetDocument` |
| [ArchiveAsset.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/ArchiveAsset.php) | `public function handle(Asset $asset): Asset` |
| [AssignAssetCustodian.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AssignAssetCustodian.php) | `public function handle(Asset $asset, AssetCustodian $custodian): Asset` |
| [AssignAssetLocation.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AssignAssetLocation.php) | `public function handle(Asset $asset, AssetLocation $location): Asset` |
| [CapitalizeAsset.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CapitalizeAsset.php) | `public function handle(Asset $asset, string $bookReference): Asset` |
| [CreateCategory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CreateCategory.php) | `public function handle(array $attributes): AssetCategory` |
| [CreateCustodian.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CreateCustodian.php) | `public function handle(array $attributes): AssetCustodian` |
| [CreateLocation.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CreateLocation.php) | `public function handle(array $attributes): AssetLocation` |
| [DisposeAsset.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/DisposeAsset.php) | `public function handle(Asset $asset, string $reason): Asset` |
| [UpdateAsset.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/UpdateAsset.php) | `public function handle(Asset $asset, array $attributes): Asset` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Asset.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/Asset.php) | `team_id`, `asset_ref`, `name`, `category_id`, `status`, `acquired_on`, `capitalized_on`, `cost`, `salvage_value`, `net_book_value`, `currency`, `location_id`, `custodian_id`, `location_ref`, `custodian_ref`, `metadata` |
| [AssetBook.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetBook.php) | `asset_id`, `book_ref`, `cost`, `accumulated_depreciation`, `net_book_value`, `last_depreciated_on`, `metadata` |
| [AssetCategory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetCategory.php) | `team_id`, `category_ref`, `name`, `asset_account_ref`, `depreciation_account_ref`, `useful_life_months`, `depreciation_method`, `metadata` |
| [AssetComponent.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetComponent.php) | `asset_id`, `component_ref`, `name`, `cost`, `useful_life_months`, `metadata` |
| [AssetCustodian.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetCustodian.php) | `team_id`, `custodian_ref`, `name`, `email`, `metadata` |
| [AssetDocument.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetDocument.php) | `asset_id`, `document_ref`, `kind`, `file_ref`, `description`, `checksum`, `attached_by`, `attached_at`, `metadata` |
| [AssetLocation.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetLocation.php) | `team_id`, `location_ref`, `name`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-fixed-assets-api/routes/api.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets-api/routes/api.php)

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

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
