# Real Estate: Real Estate Offers Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-offers). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-real-estate-real-estate-offers-nuxt`
**Matching domain module:** `real-estate-offers`
**Application:** Real Estate
**Source feature:** [Real Estate Offers](../features/real-estate-offers.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/real-estate-offers.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `real-estate-offers` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Terms:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Qualification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Negotiation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Proof:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Decision history:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Accepted-offer controls:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-real-estate-real-estate-offers-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `terms`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `qualification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `negotiation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `proof`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `decision-history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `accepted-offer-controls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-offers` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-real-estate-nuxt-vue`](https://github.com/liberusoftware/project-real-estate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-offers.md)) |
| Capability Nuxt module skeleton | [`module-real-estate-offers-nuxt`](https://github.com/liberusoftware/module-real-estate-offers-nuxt) (`@liberusoftware/module-real-estate-offers-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Terms** | Expose composable and Vue 3 component for `terms` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-offers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Qualification** | Expose composable and Vue 3 component for `qualification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-offers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Negotiation** | Expose composable and Vue 3 component for `negotiation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-offers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Proof** | Expose composable and Vue 3 component for `proof` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-offers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Decision history** | Expose composable and Vue 3 component for `decision history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-offers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Accepted-offer controls** | Expose composable and Vue 3 component for `accepted-offer controls` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-offers.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [OfferPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers/src/Policies/OfferPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Offer $offer): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Offer $offer): bool`<br>`public function delete(AuthUser $authUser, Offer $offer): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Offer $offer): bool`<br>`public function forceDelete(AuthUser $authUser, Offer $offer): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Offer $offer): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Offer.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers/src/Models/Offer.php) | No literal fillable array detected; inspect the model and API schema. |
| [OfferEvent.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers/src/Models/OfferEvent.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [OfferController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers-api/src/Http/Controllers/OfferController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateOffer $create): JsonResponse`<br>`public function show(Request $request, Offer $offer): JsonResponse`<br>`public function update(Request $request, Offer $offer, UpdateOffer $update): JsonResponse`<br>`public function destroy(Request $request, Offer $offer, DeleteOffer $delete): Response`<br>`public function transition(Request $request, Offer $offer, string $status, TransitionOffer $transition): JsonResponse`<br>`public function proof(Request $request, Offer $offer, RecordOfferProof $record): JsonResponse`<br>`public function timeline(Request $request, Offer $offer): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-offers-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-offers-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/offers')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [OfferController::class, 'index'])->name('real-estate.offers.index');
Route::post('/', [OfferController::class, 'store'])->name('real-estate.offers.store');
Route::post('/{offer}/transition/{status}', [OfferController::class, 'transition'])->name('real-estate.offers.transition');
Route::post('/{offer}/proof', [OfferController::class, 'proof'])->name('real-estate.offers.proof');
Route::get('/{offer}/timeline', [OfferController::class, 'timeline'])->name('real-estate.offers.timeline');
Route::get('/{offer}', [OfferController::class, 'show'])->name('real-estate.offers.show');
Route::delete('/{offer}', [OfferController::class, 'destroy'])->name('real-estate.offers.destroy');
```
<!-- layer-implementation-plan:end -->
