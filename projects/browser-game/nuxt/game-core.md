# Browser Game: Game Core Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#game-core). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-browser-game-game-core-nuxt`
**Matching domain module:** `browser-game-game-core`
**Application:** Browser Game
**Source feature:** [Game Core](../features/game-core.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/game-core.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `browser-game-game-core` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Worlds/shards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Game clock:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rulesets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Content versions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Feature flags:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Maintenance state:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-browser-game-game-core-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `worlds-shards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `game-clock`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rulesets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `content-versions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `feature-flags`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `maintenance-state`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-game-core` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-browser-game-nuxt-vue`](https://github.com/liberusoftware/project-browser-game-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/game-core.md)) |
| Capability Nuxt module skeleton | [`module-browser-game-game-core-nuxt`](https://github.com/liberusoftware/module-browser-game-game-core-nuxt) (`@liberusoftware/module-browser-game-game-core-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Worlds/shards** | Expose composable and Vue 3 component for `worlds/shards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/game-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Game clock** | Expose composable and Vue 3 component for `game clock` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/game-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Rulesets** | Expose composable and Vue 3 component for `rulesets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/game-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Content versions** | Expose composable and Vue 3 component for `content versions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/game-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Feature flags** | Expose composable and Vue 3 component for `feature flags` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/game-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Maintenance state** | Expose composable and Vue 3 component for `maintenance state` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/game-core.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [GameCoreOverview.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Queries/GameCoreOverview.php) | `public function forWorld(GameCoreContext $context, string $worldId): array`<br>`public function enabledFlags(?string $worldId = null): Collection`<br>`public function isEnabled(GameCoreContext $context, ?GameWorld $world, string $key, array $attributes = []): bool`<br>`public function enabledFor(GameCoreContext $context, ?GameWorld $world, array $attributes = []): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GameCoreContext.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Contracts/GameCoreContext.php) | `public function actorId(): ?string`<br>`public function tenantId(): ?string`<br>`public function teamId(): ?string` |
| [GameCorePolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Policies/GameCorePolicy.php) | `public function view(GameCoreContext $context, GameWorld $world): bool`<br>`public function manage(GameCoreContext $context, GameWorld $world): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [GameClock.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameClock.php) | `world_id`, `current_at`, `speed`, `paused`, `updated_by` |
| [GameContentVersion.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameContentVersion.php) | `world_id`, `version`, `status`, `content_hash`, `manifest`, `published_at`, `published_by` |
| [GameFeatureFlag.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameFeatureFlag.php) | `world_id`, `key`, `enabled`, `rollout_percentage`, `constraints`, `changed_by` |
| [GameMaintenanceState.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameMaintenanceState.php) | `world_id`, `status`, `message`, `starts_at`, `ends_at`, `changed_by` |
| [GameRuleset.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameRuleset.php) | `world_id`, `version`, `status`, `rules`, `published_at`, `published_by` |
| [GameWorld.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core/src/Models/GameWorld.php) | `tenant_id`, `team_id`, `name`, `slug`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [GameCoreController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-api/src/Http/Controllers/GameCoreController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, string $world): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function update(Request $request, GameWorld $world): JsonResponse`<br>`public function clock(Request $request, GameWorld $world): JsonResponse`<br>`public function ruleset(Request $request, GameWorld $world): JsonResponse`<br>`public function content(Request $request, GameWorld $world): JsonResponse`<br>`public function flag(Request $request, GameWorld $world, string $key): JsonResponse`<br>`public function evaluateFlag(Request $request, GameWorld $world, string $key): JsonResponse`<br>`public function maintenance(Request $request, GameWorld $world): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-game-core-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-game-core-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/game-core')
Route::get('/', [GameCoreController::class, 'index'])->name('browser-game.game-core.index');
Route::post('/', [GameCoreController::class, 'store'])->name('browser-game.game-core.store');
Route::get('/{world}', [GameCoreController::class, 'show'])->name('browser-game.game-core.show');
Route::patch('/{world}', [GameCoreController::class, 'update'])->name('browser-game.game-core.update');
Route::put('/{world}/clock', [GameCoreController::class, 'clock'])->name('browser-game.game-core.clock');
Route::post('/{world}/rulesets', [GameCoreController::class, 'ruleset'])->name('browser-game.game-core.ruleset');
Route::post('/{world}/content-versions', [GameCoreController::class, 'content'])->name('browser-game.game-core.content');
Route::put('/{world}/feature-flags/{key}', [GameCoreController::class, 'flag'])->name('browser-game.game-core.flag');
Route::get('/{world}/feature-flags/{key}', [GameCoreController::class, 'evaluateFlag'])->name('browser-game.game-core.flag.evaluate');
Route::put('/{world}/maintenance', [GameCoreController::class, 'maintenance'])->name('browser-game.game-core.maintenance');
```
<!-- layer-implementation-plan:end -->
