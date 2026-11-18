# Real Estate: Real Estate Vr Design Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-vr-design). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-real-estate-real-estate-vr-design-vue-inertia`
**Matching domain module:** `real-estate-vr-design`
**Application:** Real Estate
**Source feature:** [Real Estate Vr Design](../features/real-estate-vr-design.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/real-estate-vr-design.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Design styles:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Furniture placement:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Room layouts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Materials and lighting:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Public templates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Thumbnail uploads:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **VR exports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-real-estate-real-estate-vr-design-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `design-styles`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `furniture-placement`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `room-layouts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `materials-and-lighting`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `public-templates`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `thumbnail-uploads`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `vr-exports`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `real-estate-vr-design` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-real-estate-laravel-inertia-vue`](https://github.com/liberusoftware/project-real-estate-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-real-estate-vr-design-vue-inertia`](https://github.com/liberusoftware/module-real-estate-vr-design-vue-inertia) (`@liberusoftware/module-real-estate-vr-design-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/real-estate-vr-design.md) · [Core plan](../core/real-estate-vr-design.md) · [API plan](../api/real-estate-vr-design.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Design styles** | Render `design styles` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Furniture placement** | Render `furniture placement` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Room layouts** | Render `room layouts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Materials and lighting** | Render `materials and lighting` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Public templates** | Render `public templates` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Thumbnail uploads** | Render `thumbnail uploads` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **VR exports** | Render `vr exports` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
