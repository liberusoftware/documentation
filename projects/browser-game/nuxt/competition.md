# Browser Game: Competition Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#competition). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-browser-game-competition-nuxt`
**Matching domain module:** `browser-game-competition`
**Application:** Browser Game
**Source feature:** [Competition](../features/competition.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/competition.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `browser-game-competition` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **PvP modes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Matchmaking:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Seasons:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rankings:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Leaderboards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rewards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Anti-collusion:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-browser-game-competition-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `pvp-modes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `matchmaking`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `seasons`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rankings`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `leaderboards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rewards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `anti-collusion`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-competition` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-browser-game-nuxt-vue`](https://github.com/liberusoftware/project-browser-game-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/competition.md)) |
| Capability Nuxt module skeleton | [`module-browser-game-competition-nuxt`](https://github.com/liberusoftware/module-browser-game-competition-nuxt) (`@liberusoftware/module-browser-game-competition-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **PvP modes** | Expose composable and Vue 3 component for `pvp modes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/competition.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Matchmaking** | Expose composable and Vue 3 component for `matchmaking` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/competition.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Seasons** | Expose composable and Vue 3 component for `seasons` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/competition.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Rankings** | Expose composable and Vue 3 component for `rankings` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/competition.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Leaderboards** | Expose composable and Vue 3 component for `leaderboards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/competition.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Rewards** | Expose composable and Vue 3 component for `rewards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/competition.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Anti-collusion** | Expose composable and Vue 3 component for `anti-collusion` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/competition.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CompetitionQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Queries/CompetitionQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CompetitionEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [CompetitionFlag.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionFlag.php) | No literal fillable array detected; inspect the model and API schema. |
| [CompetitionMatch.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionMatch.php) | No literal fillable array detected; inspect the model and API schema. |
| [CompetitionRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [CompetitionReward.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition/src/Models/CompetitionReward.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CompetitionController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition-api/src/Http/Controllers/CompetitionController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function queue(Request $request, CompetitionRecord $competition): JsonResponse`<br>`public function match(Request $request, CompetitionRecord $competition): JsonResponse`<br>`public function resolve(Request $request, CompetitionMatch $match): JsonResponse`<br>`public function leaderboard(Request $request, CompetitionRecord $competition): JsonResponse`<br>`public function rewards(Request $request, CompetitionRecord $competition): JsonResponse`<br>`public function claimReward(Request $request, CompetitionReward $reward): JsonResponse`<br>`public function flag(Request $request, CompetitionRecord $competition): JsonResponse`<br>`public function show(Request $request, CompetitionRecord $competition): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-competition-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-competition-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/competition')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [CompetitionController::class, 'index'])->name('browser-game.competition.index');
Route::post('/', [CompetitionController::class, 'store'])->name('browser-game.competition.store');
Route::post('/{competition}/queue', [CompetitionController::class, 'queue'])->name('browser-game.competition.queue');
Route::post('/{competition}/matches', [CompetitionController::class, 'match'])->name('browser-game.competition.match');
Route::get('/{competition}/leaderboard', [CompetitionController::class, 'leaderboard'])->name('browser-game.competition.leaderboard');
Route::get('/{competition}/rewards', [CompetitionController::class, 'rewards'])->name('browser-game.competition.rewards');
Route::post('/{competition}/flags', [CompetitionController::class, 'flag'])->name('browser-game.competition.flag');
Route::post('/rewards/{reward}/claim', [CompetitionController::class, 'claimReward'])->name('browser-game.competition.reward.claim');
Route::post('/matches/{match}/resolve', [CompetitionController::class, 'resolve'])->name('browser-game.competition.resolve');
Route::get('/{competition}', [CompetitionController::class, 'show'])->name('browser-game.competition.show');
```
<!-- layer-implementation-plan:end -->
