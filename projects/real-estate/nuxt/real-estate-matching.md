# Real Estate: Real Estate Matching Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-matching). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-real-estate-real-estate-matching-nuxt`
**Matching domain module:** `real-estate-matching`
**Application:** Real Estate
**Source feature:** [Real Estate Matching](../features/real-estate-matching.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/real-estate-matching.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `real-estate-matching` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Applicant requirements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Affordability:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preferences:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Scoring:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Alerts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Feedback:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exclusions:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-real-estate-real-estate-matching-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `applicant-requirements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `affordability`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preferences`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `scoring`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `alerts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `feedback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exclusions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-matching` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-real-estate-nuxt-vue`](https://github.com/liberusoftware/project-real-estate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-matching.md)) |
| Capability Nuxt module skeleton | [`module-real-estate-matching-nuxt`](https://github.com/liberusoftware/module-real-estate-matching-nuxt) (`@liberusoftware/module-real-estate-matching-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Applicant requirements** | Expose composable and Vue 3 component for `applicant requirements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-matching.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Affordability** | Expose composable and Vue 3 component for `affordability` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-matching.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Preferences** | Expose composable and Vue 3 component for `preferences` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-matching.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Scoring** | Expose composable and Vue 3 component for `scoring` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-matching.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Alerts** | Expose composable and Vue 3 component for `alerts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-matching.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Feedback** | Expose composable and Vue 3 component for `feedback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-matching.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Exclusions** | Expose composable and Vue 3 component for `exclusions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-matching.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MatchProfilePolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-matching/src/Policies/MatchProfilePolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function delete(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function forceDelete(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, MatchProfile $matchProfile): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MatchProfile.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-matching/src/Models/MatchProfile.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [MatchProfileController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-matching-api/src/Http/Controllers/MatchProfileController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateMatchProfile $create): JsonResponse`<br>`public function show(Request $request, MatchProfile $matchProfile): JsonResponse`<br>`public function update(Request $request, MatchProfile $matchProfile, UpdateMatchProfile $update): JsonResponse`<br>`public function updateSection(Request $request, MatchProfile $matchProfile, string $section, UpdateMatchProfileSection $update): JsonResponse`<br>`public function calculateScore(Request $request, CalculateMatchScore $calculate): JsonResponse`<br>`public function recommendProperties(Request $request, RankPropertyRecommendations $rank): JsonResponse`<br>`public function destroy(Request $request, MatchProfile $matchProfile, DeleteMatchProfile $delete): Response` |

**Observed route declarations:**

[modules/real-estate-matching-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-matching-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/matching')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [MatchProfileController::class, 'index'])->name('real-estate.matching.index');
Route::post('/', [MatchProfileController::class, 'store'])->name('real-estate.matching.store');
Route::post('/calculate-score', [MatchProfileController::class, 'calculateScore'])->name('real-estate.matching.calculate-score');
Route::post('/recommend-properties', [MatchProfileController::class, 'recommendProperties'])->name('real-estate.matching.recommend-properties');
Route::get('/{matchProfile}', [MatchProfileController::class, 'show'])->name('real-estate.matching.show');
Route::patch('/{matchProfile}/{section}', [MatchProfileController::class, 'updateSection'])->whereIn('section', ['requirements', 'affordability', 'preferences', 'scoring', 'alerts', 'feedback', 'exclusions'])->name('real-estate.matching.section');
Route::delete('/{matchProfile}', [MatchProfileController::class, 'destroy'])->name('real-estate.matching.destroy');
```
<!-- layer-implementation-plan:end -->
