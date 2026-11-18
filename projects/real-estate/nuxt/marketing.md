# Real Estate: Marketing Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#marketing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-real-estate-marketing-nuxt`
**Matching domain module:** `real-estate-marketing`
**Application:** Real Estate
**Source feature:** [Marketing](../features/marketing.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/marketing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `real-estate-marketing` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Campaigns:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Boards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Brochures:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Portals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Website:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Social/email:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attribution:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Consent:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-real-estate-marketing-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `campaigns`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `boards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `brochures`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `portals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `website`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `social-email`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attribution`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `consent`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-marketing` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-real-estate-nuxt-vue`](https://github.com/liberusoftware/project-real-estate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/marketing.md)) |
| Capability Nuxt module skeleton | [`module-real-estate-marketing-nuxt`](https://github.com/liberusoftware/module-real-estate-marketing-nuxt) (`@liberusoftware/module-real-estate-marketing-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Campaigns** | Expose composable and Vue 3 component for `campaigns` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Boards** | Expose composable and Vue 3 component for `boards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Brochures** | Expose composable and Vue 3 component for `brochures` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Portals** | Expose composable and Vue 3 component for `portals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Website** | Expose composable and Vue 3 component for `website` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Social/email** | Expose composable and Vue 3 component for `social/email` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Attribution** | Expose composable and Vue 3 component for `attribution` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Consent** | Expose composable and Vue 3 component for `consent` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/marketing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MarketingCampaignPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing/src/Policies/MarketingCampaignPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function delete(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function forceDelete(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, MarketingCampaign $marketingCampaign): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MarketingCampaign.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing/src/Models/MarketingCampaign.php) | No literal fillable array detected; inspect the model and API schema. |
| [NewsArticle.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing/src/Models/NewsArticle.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [MarketingCampaignController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing-api/src/Http/Controllers/MarketingCampaignController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateMarketingCampaign $create): JsonResponse`<br>`public function show(Request $request, MarketingCampaign $marketingCampaign): JsonResponse`<br>`public function update(Request $request, MarketingCampaign $marketingCampaign, UpdateMarketingCampaign $update): JsonResponse`<br>`public function transition(Request $request, MarketingCampaign $marketingCampaign, string $status, TransitionMarketingCampaign $transition): JsonResponse`<br>`public function updateSection(Request $request, MarketingCampaign $marketingCampaign, string $section, UpdateMarketingCampaignSection $update): JsonResponse`<br>`public function destroy(Request $request, MarketingCampaign $marketingCampaign, DeleteMarketingCampaign $delete): Response` |
| [NewsArticleController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing-api/src/Http/Controllers/NewsArticleController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, string $slug): JsonResponse`<br>`public function latest(Request $request): JsonResponse`<br>`public function featured(Request $request): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-marketing-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-marketing-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/news')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [NewsArticleController::class, 'index']);
Route::get('/featured', [NewsArticleController::class, 'featured']);
Route::get('/{slug}', [NewsArticleController::class, 'show']);
Route::prefix('api/v1/real-estate/marketing')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [MarketingCampaignController::class, 'index']);
Route::post('/', [MarketingCampaignController::class, 'store']);
Route::get('/{marketingCampaign}', [MarketingCampaignController::class, 'show']);
Route::post('/{marketingCampaign}/transition/{status}', [MarketingCampaignController::class, 'transition']);
Route::patch('/{marketingCampaign}/{section}', [MarketingCampaignController::class, 'updateSection'])->whereIn('section', ['audience', 'content', 'schedule', 'metrics']);
Route::delete('/{marketingCampaign}', [MarketingCampaignController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
