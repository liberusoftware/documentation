# Browser Game: Browser Game Characters Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-characters). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-browser-game-browser-game-characters-nuxt`
**Matching domain module:** `browser-game-characters`
**Application:** Browser Game
**Source feature:** [Browser Game Characters](../features/browser-game-characters.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/browser-game-characters.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `browser-game-characters` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Creation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Race/class/background:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Statistics:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Skills:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Experience:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Level:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Health:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Respec:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-browser-game-browser-game-characters-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `creation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `race-class-background`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `statistics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `skills`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `experience`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `level`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `health`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `respec`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-characters` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-browser-game-nuxt-vue`](https://github.com/liberusoftware/project-browser-game-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/browser-game-characters.md)) |
| Capability Nuxt module skeleton | [`module-browser-game-characters-nuxt`](https://github.com/liberusoftware/module-browser-game-characters-nuxt) (`@liberusoftware/module-browser-game-characters-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Creation** | Expose composable and Vue 3 component for `creation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-characters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Race/class/background** | Expose composable and Vue 3 component for `race/class/background` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-characters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Statistics** | Expose composable and Vue 3 component for `statistics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-characters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Skills** | Expose composable and Vue 3 component for `skills` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-characters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Experience** | Expose composable and Vue 3 component for `experience` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-characters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Level** | Expose composable and Vue 3 component for `level` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-characters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Health** | Expose composable and Vue 3 component for `health` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-characters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Respec** | Expose composable and Vue 3 component for `respec` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-characters.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CharacterQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Queries/CharacterQuery.php) | `public function forPlayer(string $playerId, ?string $worldId = null): Builder`<br>`public function levelForExperience(int $experience): int` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CharacterPolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Policies/CharacterPolicy.php) | `public function view(?string $actorId, ?string $teamId, GameCharacter $character): bool`<br>`public function manage(?string $actorId, ?string $teamId, GameCharacter $character): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [GameCharacter.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters/src/Models/GameCharacter.php) | `player_id`, `world_id`, `tenant_id`, `team_id`, `name`, `race`, `class`, `background`, `statistics`, `skills`, `experience`, `level`, `health`, `max_health`, `mana`, `max_mana`, `strength`, `defense`, `agility`, `intelligence`, `stat_points`, `available_skill_points`, `respec_count`, `last_operation_key`, `last_battle_at`, `last_action_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CharactersController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters-api/src/Http/Controllers/CharactersController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function update(Request $request, GameCharacter $character): JsonResponse`<br>`public function show(Request $request, GameCharacter $character): JsonResponse`<br>`public function respec(Request $request, GameCharacter $character): JsonResponse`<br>`public function spendStats(Request $request, GameCharacter $character): JsonResponse`<br>`public function skills(Request $request, GameCharacter $character): JsonResponse`<br>`public function experience(Request $request, GameCharacter $character): JsonResponse`<br>`public function vitals(Request $request, GameCharacter $character): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-characters-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-characters-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/characters')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [CharactersController::class, 'index'])->name('browser-game.characters.index');
Route::post('/', [CharactersController::class, 'store'])->name('browser-game.characters.store');
Route::get('/{character}', [CharactersController::class, 'show'])->name('browser-game.characters.show');
Route::patch('/{character}', [CharactersController::class, 'update'])->name('browser-game.characters.update');
Route::post('/{character}/respec', [CharactersController::class, 'respec'])->name('browser-game.characters.respec');
Route::post('/{character}/stats', [CharactersController::class, 'spendStats'])->name('browser-game.characters.stats');
Route::post('/{character}/skills', [CharactersController::class, 'skills'])->name('browser-game.characters.skills');
Route::post('/{character}/experience', [CharactersController::class, 'experience'])->name('browser-game.characters.experience');
Route::post('/{character}/vitals', [CharactersController::class, 'vitals'])->name('browser-game.characters.vitals');
```
<!-- layer-implementation-plan:end -->
