# Properties: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter over a published capability skeleton, not a certified npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/real-estate-properties`.<br>
**Matching domain module:** `properties`

**Proposed design identifier:** `module-real-estate-properties-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope, skeleton repositories, and backend ownership

The [domain specification](../features/properties.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Next.js host skeleton | [`project-real-estate-next-react`](https://github.com/liberusoftware/project-real-estate-next-react) | Application App Router shell, session/BFF boundary, layout, and route composition ([template](https://github.com/liberusoftware/project-boilerplate-next-react) · [wayfinder](../../wayfinders/next-react.md) · [runbook](../../../guides/presentation/NEXTJS.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Product HTTP composition root publishing versioned `/api/v1` contracts ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/properties.md)) |
| Capability Next.js module skeleton | [module-real-estate-properties-nextjs](https://github.com/liberusoftware/module-real-estate-properties-nextjs) (`@liberusoftware/module-real-estate-properties-nextjs`) | Reusable React Server/Client component and typed DTO adapter ([foundation](https://github.com/liberusoftware/module-boilerplate-nextjs) · [catalog](../../../modules/skeletons/next-react.md)) |

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/real-estate-properties](../../../modules/source/liberusoftware--real-estate-properties.md) |
| API | [liberusoftware/real-estate-properties-api](../../../modules/source/liberusoftware--real-estate-properties-api.md) |

## Module surfaces and component contracts

| Capability / feature aspect | Next.js Server & Client Component boundary | API transport, caching & recovery contract |
| --- | --- | --- |
| **Address/location** | Server Component loads authorized `address/location` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-real-estate-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Units** | Server Component loads authorized `units` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-real-estate-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Characteristics** | Server Component loads authorized `characteristics` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-real-estate-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Tenure** | Server Component loads authorized `tenure` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-real-estate-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Utilities** | Server Component loads authorized `utilities` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-real-estate-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Features** | Server Component loads authorized `features` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-real-estate-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Status** | Server Component loads authorized `status` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-real-estate-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **History** | Server Component loads authorized `history` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-real-estate-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |
| **Keys** | Server Component loads authorized `keys` read model; Client Component (`'use client'`) manages interactive filters, forms, focus, and keyboard state. | Consume reviewed `project-real-estate-laravel-api` DTOs with `cache: 'no-store'` default; map 401/403/409/412/422/429 and preserve safe drafts on validation or conflict. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [PropertyCategoryPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Policies/PropertyCategoryPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function delete(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function forceDelete(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [PropertyPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Policies/PropertyPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Property $property): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Property $property): bool`<br>`public function delete(AuthUser $authUser, Property $property): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Property $property): bool`<br>`public function forceDelete(AuthUser $authUser, Property $property): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Property $property): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [PropertyTemplatePolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Policies/PropertyTemplatePolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function delete(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function forceDelete(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function reorder(AuthUser $authUser): bool` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [CommunityEvent.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/CommunityEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [Neighborhood.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/Neighborhood.php) | No literal fillable array detected; inspect the model and API schema. |
| [NeighborhoodReview.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/NeighborhoodReview.php) | No literal fillable array detected; inspect the model and API schema. |
| [Property.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/Property.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyCategory.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyCategory.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyFavorite.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyFavorite.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyHistory.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyHistory.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyKey.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyKey.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyPriceAlert.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyPriceAlert.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyReview.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyReview.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertySavedSearch.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertySavedSearch.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyTemplate.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyTemplate.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyUnit.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyUnit.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/real-estate-properties-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/routes/api.php)

```php
Route::prefix('api/v1/public/properties')->middleware(['api', 'throttle:api'])->group(function (): void {
Route::get('/', [PublicPropertyController::class, 'index'])->name('public.properties.index');
Route::get('/{property}', [PublicPropertyController::class, 'show'])->name('public.properties.show');
Route::prefix('api/v1/real-estate/properties/{property}/ar-tour')->middleware(['api', 'throttle:api'])->group(function (): void {
Route::get('/config', [PropertyArTourController::class, 'config'])->name('real-estate.properties.ar-tour.config');
Route::get('/availability', [PropertyArTourController::class, 'availability'])->name('real-estate.properties.ar-tour.availability');
Route::prefix('api/v1/real-estate/properties/{property}/ar-tour')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/enable', [PropertyArTourController::class, 'enable'])->name('real-estate.properties.ar-tour.enable');
Route::post('/disable', [PropertyArTourController::class, 'disable'])->name('real-estate.properties.ar-tour.disable');
Route::prefix('api/v1/real-estate/property-saved-searches')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [PropertySavedSearchController::class, 'index'])->name('real-estate.property-saved-searches.index');
Route::post('/', [PropertySavedSearchController::class, 'store'])->name('real-estate.property-saved-searches.store');
Route::delete('/{savedSearch}', [PropertySavedSearchController::class, 'destroy'])->name('real-estate.property-saved-searches.destroy');
Route::prefix('api/v1/real-estate/community-events')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [CommunityEventController::class, 'index'])->name('real-estate.community-events.index');
Route::get('/{event}', [CommunityEventController::class, 'show'])->name('real-estate.community-events.show');
Route::prefix('api/v1/real-estate/properties')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [PropertyController::class, 'index'])->name('real-estate.properties.index');
Route::post('/', [PropertyController::class, 'store'])->name('real-estate.properties.store');
Route::get('/compare', [PropertyController::class, 'compare'])->name('real-estate.properties.compare');
Route::post('/tax-estimate', [PropertyController::class, 'taxEstimate'])->name('real-estate.properties.tax-estimate');
Route::get('/favorites', [PropertyController::class, 'favorites'])->name('real-estate.properties.favorites');
Route::post('/{property}/transition/{status}', [PropertyController::class, 'transition'])->name('real-estate.properties.transition');
Route::post('/{property}/favorite', [PropertyController::class, 'favorite'])->name('real-estate.properties.favorite');
Route::delete('/favorites/{property}', [PropertyController::class, 'removeFavorite'])->name('real-estate.properties.favorite-remove');
Route::get('/{property}/similar', [PropertyController::class, 'similar'])->name('real-estate.properties.similar');
Route::post('/{property}/walkability', [PropertyController::class, 'walkability'])->name('real-estate.properties.walkability');
Route::get('/{property}/qr-code', [PropertyController::class, 'qrCode'])->name('real-estate.properties.qr-code');
Route::post('/{property}/share', [PropertyController::class, 'share'])->name('real-estate.properties.share');
Route::get('/{property}/history', [PropertyController::class, 'history'])->name('real-estate.properties.history');
Route::put('/{property}/units', [PropertyController::class, 'unit'])->name('real-estate.properties.units');
Route::post('/{property}/keys', [PropertyController::class, 'key'])->name('real-estate.properties.keys');
Route::get('/{property}', [PropertyController::class, 'show'])->name('real-estate.properties.show');
Route::delete('/{property}', [PropertyController::class, 'destroy'])->name('real-estate.properties.destroy');
Route::prefix('api/v1/real-estate/properties/{property}/price-alerts')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [PropertyPriceAlertController::class, 'index'])->name('real-estate.properties.price-alerts.index');
Route::post('/', [PropertyPriceAlertController::class, 'store'])->name('real-estate.properties.price-alerts.store');
Route::prefix('api/v1/real-estate/price-alerts')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::delete('/{alert}', [PropertyPriceAlertController::class, 'destroy'])->name('real-estate.price-alerts.destroy');
Route::prefix('api/v1/real-estate/property-categories')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [PropertyCategoryController::class, 'index'])->name('real-estate.property-categories.index');
Route::post('/', [PropertyCategoryController::class, 'store'])->name('real-estate.property-categories.store');
Route::delete('/{category}', [PropertyCategoryController::class, 'destroy'])->name('real-estate.property-categories.destroy');
Route::prefix('api/v1/real-estate/property-templates')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [PropertyTemplateController::class, 'index'])->name('real-estate.property-templates.index');
Route::post('/', [PropertyTemplateController::class, 'store'])->name('real-estate.property-templates.store');
Route::delete('/{template}', [PropertyTemplateController::class, 'destroy'])->name('real-estate.property-templates.destroy');
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
