# Browser Game: Browser Game Quests Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-quests). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-browser-game-browser-game-quests-nuxt`
**Matching domain module:** `browser-game-quests`
**Application:** Browser Game
**Source feature:** [Browser Game Quests](../features/browser-game-quests.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/browser-game-quests.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `browser-game-quests` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Storylines:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Objectives:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Prerequisites:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Branching:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dialogue:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rewards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Repeatability:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Progress:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-browser-game-browser-game-quests-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `storylines`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `objectives`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `prerequisites`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `branching`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dialogue`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rewards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `repeatability`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `progress`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-quests` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-browser-game-nuxt-vue`](https://github.com/liberusoftware/project-browser-game-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/browser-game-quests.md)) |
| Capability Nuxt module skeleton | [`module-browser-game-quests-nuxt`](https://github.com/liberusoftware/module-browser-game-quests-nuxt) (`@liberusoftware/module-browser-game-quests-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Storylines** | Expose composable and Vue 3 component for `storylines` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-quests.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Objectives** | Expose composable and Vue 3 component for `objectives` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-quests.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Prerequisites** | Expose composable and Vue 3 component for `prerequisites` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-quests.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Branching** | Expose composable and Vue 3 component for `branching` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-quests.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Dialogue** | Expose composable and Vue 3 component for `dialogue` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-quests.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Rewards** | Expose composable and Vue 3 component for `rewards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-quests.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Repeatability** | Expose composable and Vue 3 component for `repeatability` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-quests.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Progress** | Expose composable and Vue 3 component for `progress` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-quests.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [QuestQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests/src/Queries/QuestQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder`<br>`public function availableFor(string $actorId, ?string $tenantId, ?string $teamId): Builder`<br>`public function activeFor(string $actorId, ?string $tenantId, ?string $teamId): Builder`<br>`public function completedFor(string $actorId, ?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Quest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests/src/Models/Quest.php) | No literal fillable array detected; inspect the model and API schema. |
| [QuestProgress.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests/src/Models/QuestProgress.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [QuestsController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests-api/src/Http/Controllers/QuestsController.php) | `public function index(Request $request): JsonResponse`<br>`public function available(Request $request): JsonResponse`<br>`public function active(Request $request): JsonResponse`<br>`public function completed(Request $request): JsonResponse`<br>`public function show(Request $request, Quest $quest): JsonResponse`<br>`public function progress(Request $request, Quest $quest): JsonResponse`<br>`public function accept(Request $request, Quest $quest): JsonResponse`<br>`public function complete(Request $request, Quest $quest): JsonResponse`<br>`public function abandon(Request $request, Quest $quest): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-quests-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-quests-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/quests')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [QuestsController::class, 'index'])->name('browser-game.quests.index');
Route::get('/available', [QuestsController::class, 'available'])->name('browser-game.quests.available');
Route::get('/active', [QuestsController::class, 'active'])->name('browser-game.quests.active');
Route::get('/completed', [QuestsController::class, 'completed'])->name('browser-game.quests.completed');
Route::post('/{quest}/accept', [QuestsController::class, 'accept'])->name('browser-game.quests.accept');
Route::post('/{quest}/complete', [QuestsController::class, 'complete'])->name('browser-game.quests.complete');
Route::post('/{quest}/abandon', [QuestsController::class, 'abandon'])->name('browser-game.quests.abandon');
Route::get('/{quest}', [QuestsController::class, 'show'])->name('browser-game.quests.show');
Route::post('/{quest}/progress', [QuestsController::class, 'progress'])->name('browser-game.quests.progress');
```
<!-- layer-implementation-plan:end -->
