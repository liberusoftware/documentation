# Browser Game: Combat Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#combat). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-browser-game-combat-nuxt`
**Matching domain module:** `browser-game-combat`
**Application:** Browser Game
**Source feature:** [Combat](../features/combat.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/combat.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `browser-game-combat` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Turn/action rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Abilities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Effects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cooldowns:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Enemies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Bosses:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Loot:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Logs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Simulation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-browser-game-combat-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `turn-action-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `abilities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `effects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cooldowns`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `enemies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `bosses`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `loot`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `logs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `simulation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-combat` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-browser-game-nuxt-vue`](https://github.com/liberusoftware/project-browser-game-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/combat.md)) |
| Capability Nuxt module skeleton | [`module-browser-game-combat-nuxt`](https://github.com/liberusoftware/module-browser-game-combat-nuxt) (`@liberusoftware/module-browser-game-combat-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Turn/action rules** | Expose composable and Vue 3 component for `turn/action rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/combat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Abilities** | Expose composable and Vue 3 component for `abilities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/combat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Effects** | Expose composable and Vue 3 component for `effects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/combat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Cooldowns** | Expose composable and Vue 3 component for `cooldowns` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/combat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Enemies** | Expose composable and Vue 3 component for `enemies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/combat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Bosses** | Expose composable and Vue 3 component for `bosses` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/combat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Loot** | Expose composable and Vue 3 component for `loot` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/combat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Logs** | Expose composable and Vue 3 component for `logs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/combat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Simulation** | Expose composable and Vue 3 component for `simulation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/combat.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CombatQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Queries/CombatQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CombatPolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Policies/CombatPolicy.php) | `public function view(mixed $user, CombatBattle $battle): bool`<br>`public function act(mixed $user, CombatBattle $battle): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CombatAction.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Models/CombatAction.php) | No literal fillable array detected; inspect the model and API schema. |
| [CombatBattle.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Models/CombatBattle.php) | No literal fillable array detected; inspect the model and API schema. |
| [CombatDefinition.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat/src/Models/CombatDefinition.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CombatController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-api/src/Http/Controllers/CombatController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, CombatBattle $battle): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function action(Request $request, CombatBattle $battle): JsonResponse`<br>`public function definition(Request $request): JsonResponse`<br>`public function simulate(Request $request): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-combat-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-combat-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/combat')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [CombatController::class, 'index'])->name('browser-game.combat.index');
Route::get('/{battle}', [CombatController::class, 'show'])->name('browser-game.combat.show');
Route::post('/', [CombatController::class, 'store'])->name('browser-game.combat.store');
Route::post('/{battle}/actions', [CombatController::class, 'action'])->name('browser-game.combat.action');
Route::post('/definitions', [CombatController::class, 'definition'])->name('browser-game.combat.definition');
Route::post('/simulate', [CombatController::class, 'simulate'])->name('browser-game.combat.simulate');
```
<!-- layer-implementation-plan:end -->
