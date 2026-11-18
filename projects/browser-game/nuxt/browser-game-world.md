# Browser Game: Browser Game World Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-world). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-browser-game-browser-game-world-nuxt`
**Matching domain module:** `browser-game-world`
**Application:** Browser Game
**Source feature:** [Browser Game World](../features/browser-game-world.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/browser-game-world.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `browser-game-world` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Regions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Locations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Maps:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Travel:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Encounters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **NPCs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Resources:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Weather:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Unlocks:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-browser-game-browser-game-world-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `regions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `locations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `maps`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `travel`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `encounters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `npcs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `resources`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `weather`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `unlocks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-world` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-browser-game-nuxt-vue`](https://github.com/liberusoftware/project-browser-game-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/browser-game-world.md)) |
| Capability Nuxt module skeleton | [`module-browser-game-world-nuxt`](https://github.com/liberusoftware/module-browser-game-world-nuxt) (`@liberusoftware/module-browser-game-world-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Regions** | Expose composable and Vue 3 component for `regions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-world.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Locations** | Expose composable and Vue 3 component for `locations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-world.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Maps** | Expose composable and Vue 3 component for `maps` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-world.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Travel** | Expose composable and Vue 3 component for `travel` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-world.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Encounters** | Expose composable and Vue 3 component for `encounters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-world.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **NPCs** | Expose composable and Vue 3 component for `npcs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-world.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Resources** | Expose composable and Vue 3 component for `resources` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-world.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Weather** | Expose composable and Vue 3 component for `weather` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-world.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Unlocks** | Expose composable and Vue 3 component for `unlocks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-world.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [WorldQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Queries/WorldQuery.php) | `public function visible(?string $tenantId, ?string $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [WorldPolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Policies/WorldPolicy.php) | `public function view(?string $tenantId, ?string $teamId, WorldEntity $entity): bool`<br>`public function manage(?string $actorId, ?string $tenantId, ?string $teamId, WorldEntity $entity): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorldEntity.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldEntity.php) | `tenant_id`, `team_id`, `world_id`, `kind`, `name`, `slug`, `status`, `attributes`, `coordinates`, `unlock_key` |
| [WorldTravel.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldTravel.php) | `tenant_id`, `team_id`, `actor_id`, `origin_id`, `destination_id`, `idempotency_key`, `metadata` |
| [WorldUnlock.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldUnlock.php) | `tenant_id`, `team_id`, `actor_id`, `entity_id`, `unlock_key`, `status`, `metadata`, `idempotency_key`, `granted_at`, `revoked_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WorldController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-api/src/Http/Controllers/WorldController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function travel(Request $request): JsonResponse`<br>`public function unlock(Request $request, WorldEntity $entity): JsonResponse`<br>`public function revokeUnlock(Request $request, WorldUnlock $unlock): JsonResponse`<br>`public function show(Request $request, WorldEntity $entity): JsonResponse`<br>`public function update(Request $request, WorldEntity $entity): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-world-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/world')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [WorldController::class, 'index'])->name('browser-game.world.index');
Route::post('/', [WorldController::class, 'store'])->name('browser-game.world.store');
Route::post('/travel', [WorldController::class, 'travel'])->name('browser-game.world.travel');
Route::post('/{entity}/unlock', [WorldController::class, 'unlock'])->name('browser-game.world.unlock');
Route::delete('/unlocks/{unlock}', [WorldController::class, 'revokeUnlock'])->name('browser-game.world.unlock.revoke');
Route::patch('/{entity}', [WorldController::class, 'update'])->name('browser-game.world.update');
Route::get('/{entity}', [WorldController::class, 'show'])->name('browser-game.world.show');
```
<!-- layer-implementation-plan:end -->
