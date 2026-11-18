# Browser Game: Crafting Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crafting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-browser-game-crafting-nuxt`
**Matching domain module:** `browser-game-crafting`
**Application:** Browser Game
**Source feature:** [Crafting](../features/crafting.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crafting.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `browser-game-crafting` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Recipes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Professions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Resources:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quality:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Queues:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Discovery:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Salvage:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Outputs:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-browser-game-crafting-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `recipes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `professions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `resources`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quality`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `queues`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `discovery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `salvage`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `outputs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-crafting` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-browser-game-nuxt-vue`](https://github.com/liberusoftware/project-browser-game-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crafting.md)) |
| Capability Nuxt module skeleton | [`module-browser-game-crafting-nuxt`](https://github.com/liberusoftware/module-browser-game-crafting-nuxt) (`@liberusoftware/module-browser-game-crafting-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Recipes** | Expose composable and Vue 3 component for `recipes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crafting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Professions** | Expose composable and Vue 3 component for `professions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crafting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Resources** | Expose composable and Vue 3 component for `resources` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crafting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Quality** | Expose composable and Vue 3 component for `quality` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crafting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Queues** | Expose composable and Vue 3 component for `queues` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crafting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Discovery** | Expose composable and Vue 3 component for `discovery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crafting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Salvage** | Expose composable and Vue 3 component for `salvage` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crafting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Outputs** | Expose composable and Vue 3 component for `outputs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crafting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CraftingQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Queries/CraftingQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CraftingDiscovery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingDiscovery.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingOutput.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingOutput.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingProfession.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingProfession.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingQueue.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingQueue.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [CraftingResource.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingResource.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CraftingController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting-api/src/Http/Controllers/CraftingController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, CraftingRecord $crafting): JsonResponse`<br>`public function queue(Request $request): JsonResponse`<br>`public function queues(Request $request): JsonResponse`<br>`public function complete(Request $request, CraftingQueue $queue): JsonResponse`<br>`public function cancel(Request $request, CraftingQueue $queue): JsonResponse`<br>`public function salvage(Request $request, CraftingQueue $queue): JsonResponse`<br>`public function discover(Request $request, CraftingRecord $crafting): JsonResponse`<br>`public function professions(Request $request): JsonResponse`<br>`public function resources(Request $request): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-crafting-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/crafting')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [CraftingController::class, 'index'])->name('browser-game.crafting.index');
Route::post('/queue', [CraftingController::class, 'queue'])->name('browser-game.crafting.queue');
Route::get('/queue', [CraftingController::class, 'queues'])->name('browser-game.crafting.queues');
Route::post('/queue/{queue}/complete', [CraftingController::class, 'complete'])->name('browser-game.crafting.queue.complete');
Route::post('/queue/{queue}/cancel', [CraftingController::class, 'cancel'])->name('browser-game.crafting.queue.cancel');
Route::post('/queue/{queue}/salvage', [CraftingController::class, 'salvage'])->name('browser-game.crafting.queue.salvage');
Route::get('/professions', [CraftingController::class, 'professions'])->name('browser-game.crafting.professions');
Route::get('/resources', [CraftingController::class, 'resources'])->name('browser-game.crafting.resources');
Route::post('/{crafting}/discover', [CraftingController::class, 'discover'])->name('browser-game.crafting.discover');
Route::get('/{crafting}', [CraftingController::class, 'show'])->name('browser-game.crafting.show');
```
<!-- layer-implementation-plan:end -->
