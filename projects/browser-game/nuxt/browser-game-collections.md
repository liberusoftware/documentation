# Browser Game: Browser Game Collections Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-collections). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-browser-game-browser-game-collections-nuxt`
**Matching domain module:** `browser-game-collections`
**Application:** Browser Game
**Source feature:** [Browser Game Collections](../features/browser-game-collections.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/browser-game-collections.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `browser-game-collections` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Achievements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Titles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reputation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Pets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Mounts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Housing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cosmetics:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Collection progress:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-browser-game-browser-game-collections-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `achievements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `titles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reputation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `pets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `mounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `housing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cosmetics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `collection-progress`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-collections` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-browser-game-nuxt-vue`](https://github.com/liberusoftware/project-browser-game-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/browser-game-collections.md)) |
| Capability Nuxt module skeleton | [`module-browser-game-collections-nuxt`](https://github.com/liberusoftware/module-browser-game-collections-nuxt) (`@liberusoftware/module-browser-game-collections-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Achievements** | Expose composable and Vue 3 component for `achievements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Titles** | Expose composable and Vue 3 component for `titles` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Reputation** | Expose composable and Vue 3 component for `reputation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Pets** | Expose composable and Vue 3 component for `pets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Mounts** | Expose composable and Vue 3 component for `mounts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Housing** | Expose composable and Vue 3 component for `housing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Cosmetics** | Expose composable and Vue 3 component for `cosmetics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Collection progress** | Expose composable and Vue 3 component for `collection progress` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-collections.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CollectionsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Queries/CollectionsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder`<br>`public function availableAchievements(?string $tenantId, ?string $teamId): Builder`<br>`public function forActor(string $actorId, ?string $tenantId, ?string $teamId): Builder`<br>`public function unlockedForActor(string $actorId, ?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CollectionEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Models/CollectionEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [CollectionProgress.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Models/CollectionProgress.php) | No literal fillable array detected; inspect the model and API schema. |
| [CollectionsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Models/CollectionsRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CollectionsController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections-api/src/Http/Controllers/CollectionsController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function achievements(Request $request): JsonResponse`<br>`public function unlockedAchievements(Request $request): JsonResponse`<br>`public function show(Request $request, CollectionsRecord $collections): JsonResponse`<br>`public function progress(Request $request): JsonResponse`<br>`public function record(Request $request, CollectionsRecord $collections): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-collections-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/collections')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [CollectionsController::class, 'index'])->name('browser-game.collections.index');
Route::post('/', [CollectionsController::class, 'store'])->name('browser-game.collections.store');
Route::get('/achievements', [CollectionsController::class, 'achievements'])->name('browser-game.collections.achievements');
Route::get('/achievements/unlocked', [CollectionsController::class, 'unlockedAchievements'])->name('browser-game.collections.achievements.unlocked');
Route::get('/progress', [CollectionsController::class, 'progress'])->name('browser-game.collections.progress.index');
Route::post('/{collections}/progress', [CollectionsController::class, 'record'])->name('browser-game.collections.progress');
Route::get('/{collections}', [CollectionsController::class, 'show'])->name('browser-game.collections.show');
```
<!-- layer-implementation-plan:end -->
