# Real Estate: Real Estate Vr Design Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-vr-design). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-real-estate-real-estate-vr-design-nuxt`
**Matching domain module:** `real-estate-vr-design`
**Application:** Real Estate
**Source feature:** [Real Estate Vr Design](../features/real-estate-vr-design.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/real-estate-vr-design.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `real-estate-vr-design` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Design styles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Furniture placement:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Room layouts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Materials and lighting:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Public templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Thumbnail uploads:** page/component/composable/API-action behavior for this module's authorized workflow.
- **VR exports:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-real-estate-real-estate-vr-design-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `design-styles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `furniture-placement`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `room-layouts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `materials-and-lighting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `public-templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `thumbnail-uploads`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `vr-exports`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-vr-design` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-real-estate-nuxt-vue`](https://github.com/liberusoftware/project-real-estate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-vr-design.md)) |
| Capability Nuxt module skeleton | [`module-real-estate-vr-design-nuxt`](https://github.com/liberusoftware/module-real-estate-vr-design-nuxt) (`@liberusoftware/module-real-estate-vr-design-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Design styles** | Expose composable and Vue 3 component for `design styles` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-vr-design.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Furniture placement** | Expose composable and Vue 3 component for `furniture placement` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-vr-design.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Room layouts** | Expose composable and Vue 3 component for `room layouts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-vr-design.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Materials and lighting** | Expose composable and Vue 3 component for `materials and lighting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-vr-design.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Public templates** | Expose composable and Vue 3 component for `public templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-vr-design.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Thumbnail uploads** | Expose composable and Vue 3 component for `thumbnail uploads` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-vr-design.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **VR exports** | Expose composable and Vue 3 component for `vr exports` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-vr-design.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |

### Observed domain and transport source evidence

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [VrDesign.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-vr-design/src/Models/VrDesign.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [VrDesignController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-vr-design-api/src/Http/Controllers/VrDesignController.php) | `public function styles(VrDesignService $service): JsonResponse`<br>`public function furnitureCategories(VrDesignService $service): JsonResponse`<br>`public function roomTypes(VrDesignService $service): JsonResponse`<br>`public function devices(VrDesignService $service): JsonResponse`<br>`public function templates(Request $request, VrDesignService $service): JsonResponse`<br>`public function indexForProperty(Request $request, VrDesignService $service, int\|string $propertyId): JsonResponse`<br>`public function store(Request $request, VrDesignService $service, int\|string $propertyId): JsonResponse`<br>`public function show(Request $request, VrDesignService $service, int\|string $designId): JsonResponse`<br>`public function update(Request $request, VrDesignService $service, int\|string $designId): JsonResponse`<br>`public function destroy(Request $request, VrDesignService $service, int\|string $designId): JsonResponse`<br>`public function addFurniture(Request $request, VrDesignService $service, int\|string $designId): JsonResponse`<br>`public function removeFurniture(Request $request, VrDesignService $service, int\|string $designId, string $furnitureId): JsonResponse`<br>`public function cloneDesign(Request $request, VrDesignService $service, int\|string $designId): JsonResponse`<br>`public function uploadThumbnail(Request $request, VrDesignService $service, int\|string $designId): JsonResponse`<br>`public function export(Request $request, VrDesignService $service, int\|string $designId): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-vr-design-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-vr-design-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/vr-design')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/styles', [VrDesignController::class, 'styles'])->name('real-estate.vr-design.styles');
Route::get('/furniture-categories', [VrDesignController::class, 'furnitureCategories'])->name('real-estate.vr-design.furniture-categories');
Route::get('/room-types', [VrDesignController::class, 'roomTypes'])->name('real-estate.vr-design.room-types');
Route::get('/devices', [VrDesignController::class, 'devices'])->name('real-estate.vr-design.devices');
Route::get('/templates', [VrDesignController::class, 'templates'])->name('real-estate.vr-design.templates');
Route::get('/properties/{propertyId}/designs', [VrDesignController::class, 'indexForProperty'])->name('real-estate.vr-design.property.index');
Route::post('/properties/{propertyId}/designs', [VrDesignController::class, 'store'])->name('real-estate.vr-design.property.store');
Route::get('/designs/{designId}', [VrDesignController::class, 'show'])->name('real-estate.vr-design.show');
Route::delete('/designs/{designId}', [VrDesignController::class, 'destroy'])->name('real-estate.vr-design.destroy');
Route::post('/designs/{designId}/furniture', [VrDesignController::class, 'addFurniture'])->name('real-estate.vr-design.furniture.add');
Route::delete('/designs/{designId}/furniture/{furnitureId}', [VrDesignController::class, 'removeFurniture'])->name('real-estate.vr-design.furniture.remove');
Route::post('/designs/{designId}/clone', [VrDesignController::class, 'cloneDesign'])->name('real-estate.vr-design.clone');
Route::post('/designs/{designId}/thumbnail', [VrDesignController::class, 'uploadThumbnail'])->name('real-estate.vr-design.thumbnail');
Route::get('/designs/{designId}/export', [VrDesignController::class, 'export'])->name('real-estate.vr-design.export');
```
<!-- layer-implementation-plan:end -->
