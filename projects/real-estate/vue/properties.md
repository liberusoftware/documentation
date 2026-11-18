# Real Estate: Properties Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#properties). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-real-estate-properties-vue-inertia`
**Matching domain module:** `real-estate-properties`
**Application:** Real Estate
**Source feature:** [Properties](../features/properties.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/properties.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Address/location:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Units:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Characteristics:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tenure:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Utilities:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Features:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Status:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **History:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Keys:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-real-estate-properties-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `address-location`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `units`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `characteristics`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `tenure`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `utilities`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `features`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `status`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `history`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `keys`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-properties` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-real-estate-laravel-inertia-vue`](https://github.com/liberusoftware/project-real-estate-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-real-estate-properties-vue-inertia`](https://github.com/liberusoftware/module-real-estate-properties-vue-inertia) (`@liberusoftware/module-real-estate-properties-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/properties.md) · [Core plan](../core/properties.md) · [API plan](../api/properties.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Address/location** | Render `address/location` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Units** | Render `units` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Characteristics** | Render `characteristics` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Tenure** | Render `tenure` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Utilities** | Render `utilities` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Features** | Render `features` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Status** | Render `status` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **History** | Render `history` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Keys** | Render `keys` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PropertyCategoryPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Policies/PropertyCategoryPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function delete(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function forceDelete(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, PropertyCategory $propertyCategory): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [PropertyPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Policies/PropertyPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Property $property): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Property $property): bool`<br>`public function delete(AuthUser $authUser, Property $property): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Property $property): bool`<br>`public function forceDelete(AuthUser $authUser, Property $property): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Property $property): bool`<br>`public function reorder(AuthUser $authUser): bool` |
| [PropertyTemplatePolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Policies/PropertyTemplatePolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function delete(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function forceDelete(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, PropertyTemplate $propertyTemplate): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommunityEvent.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/CommunityEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [Neighborhood.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/Neighborhood.php) | No literal fillable array detected; inspect the model and API schema. |
| [NeighborhoodReview.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/NeighborhoodReview.php) | No literal fillable array detected; inspect the model and API schema. |
| [Property.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/Property.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyCategory.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyCategory.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyFavorite.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyFavorite.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyHistory.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyHistory.php) | No literal fillable array detected; inspect the model and API schema. |
| [PropertyKey.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties/src/Models/PropertyKey.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CommunityEventController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/CommunityEventController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, CommunityEvent $event): JsonResponse` |
| [PropertyArTourController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyArTourController.php) | `public function config(Property $property, ConfigurePropertyArTour $arTour): JsonResponse`<br>`public function availability(Property $property, ConfigurePropertyArTour $arTour): JsonResponse`<br>`public function enable(Request $request, Property $property, ConfigurePropertyArTour $arTour): JsonResponse`<br>`public function disable(Request $request, Property $property, ConfigurePropertyArTour $arTour): JsonResponse`<br>`public function updateSettings(Request $request, Property $property, ConfigurePropertyArTour $arTour): JsonResponse` |
| [PropertyCategoryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyCategoryController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function update(Request $request, PropertyCategory $category): JsonResponse`<br>`public function destroy(Request $request, PropertyCategory $category): Response` |
| [PropertyController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateProperty $create): JsonResponse`<br>`public function favorite(Request $request, Property $property, TogglePropertyFavorite $toggle): JsonResponse`<br>`public function favorites(Request $request): JsonResponse`<br>`public function removeFavorite(Request $request, Property $property, RemovePropertyFavorite $remove): JsonResponse`<br>`public function similar(Request $request, Property $property): JsonResponse`<br>`public function walkability(Request $request, Property $property, FetchWalkabilityScores $fetch, UpdateProperty $update): JsonResponse`<br>`public function qrCode(Request $request, Property $property, GeneratePropertyQrCode $generate): JsonResponse`<br>`public function share(Request $request, Property $property, SendPropertyToFriend $send): JsonResponse`<br>`public function compare(Request $request): JsonResponse`<br>`public function taxEstimate(Request $request, EstimatePropertyTax $estimate): JsonResponse`<br>`public function show(Request $request, Property $property): JsonResponse`<br>`public function history(Request $request, Property $property): JsonResponse`<br>`public function update(Request $request, Property $property, UpdateProperty $update): JsonResponse`<br>`public function transition(Request $request, Property $property, string $status, TransitionProperty $transition): JsonResponse`<br>`public function unit(Request $request, Property $property, UpsertPropertyUnit $upsert): JsonResponse`<br>`public function key(Request $request, Property $property, RecordPropertyKey $record): JsonResponse`<br>`public function destroy(Request $request, Property $property, DeleteProperty $delete): Response` |
| [PropertyPriceAlertController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyPriceAlertController.php) | `public function index(Request $request, int\|string $property): JsonResponse`<br>`public function store(Request $request, int\|string $property, CreatePriceAlert $create): JsonResponse`<br>`public function update(Request $request, int\|string $alert, UpdatePriceAlert $update): JsonResponse`<br>`public function destroy(Request $request, int\|string $alert, DeletePriceAlert $delete): JsonResponse` |
| [PropertySavedSearchController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertySavedSearchController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, SavePropertySearch $save): JsonResponse`<br>`public function destroy(Request $request, int $savedSearch, DeletePropertySearch $delete): JsonResponse` |
| [PropertyTemplateController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyTemplateController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function update(Request $request, PropertyTemplate $template): JsonResponse`<br>`public function destroy(Request $request, PropertyTemplate $template): Response` |
| [PublicPropertyController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PublicPropertyController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, Property $property): JsonResponse` |

**Observed route declarations:**

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
<!-- layer-implementation-plan:end -->
