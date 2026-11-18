# Browser Game: Browser Game Items Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-items). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-browser-game-browser-game-items-nuxt`
**Matching domain module:** `browser-game-items`
**Application:** Browser Game
**Source feature:** [Browser Game Items](../features/browser-game-items.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/browser-game-items.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `browser-game-items` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Definitions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Inventory:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Equipment:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Durability:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Binding:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Containers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Stack rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provenance:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-browser-game-browser-game-items-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `definitions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `inventory`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `equipment`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `durability`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `binding`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `containers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `stack-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provenance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-items` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-browser-game-nuxt-vue`](https://github.com/liberusoftware/project-browser-game-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/browser-game-items.md)) |
| Capability Nuxt module skeleton | [`module-browser-game-items-nuxt`](https://github.com/liberusoftware/module-browser-game-items-nuxt) (`@liberusoftware/module-browser-game-items-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Definitions** | Expose composable and Vue 3 component for `definitions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Inventory** | Expose composable and Vue 3 component for `inventory` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Equipment** | Expose composable and Vue 3 component for `equipment` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Durability** | Expose composable and Vue 3 component for `durability` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Binding** | Expose composable and Vue 3 component for `binding` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Containers** | Expose composable and Vue 3 component for `containers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Stack rules** | Expose composable and Vue 3 component for `stack rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Provenance** | Expose composable and Vue 3 component for `provenance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ItemsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Queries/ItemsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [InventoryEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Models/InventoryEntry.php) | No literal fillable array detected; inspect the model and API schema. |
| [ItemsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Models/ItemsRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ItemsController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items-api/src/Http/Controllers/ItemsController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, ItemsRecord $items): JsonResponse`<br>`public function inventory(Request $request): JsonResponse`<br>`public function addToInventory(Request $request, ItemsRecord $item): JsonResponse`<br>`public function removeFromInventory(Request $request, ItemsRecord $item): JsonResponse`<br>`public function equip(Request $request, InventoryEntry $entry): JsonResponse`<br>`public function unequip(Request $request, InventoryEntry $entry): JsonResponse`<br>`public function bind(Request $request, InventoryEntry $entry): JsonResponse`<br>`public function durability(Request $request, InventoryEntry $entry): JsonResponse`<br>`public function container(Request $request, InventoryEntry $entry): JsonResponse`<br>`public function provenance(Request $request, InventoryEntry $entry): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-items-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/items')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [ItemsController::class, 'index'])->name('browser-game.items.index');
Route::get('/inventory/me', [ItemsController::class, 'inventory'])->name('browser-game.items.inventory');
Route::post('/inventory/{item}/add', [ItemsController::class, 'addToInventory'])->name('browser-game.items.inventory.add');
Route::post('/inventory/{item}/remove', [ItemsController::class, 'removeFromInventory'])->name('browser-game.items.inventory.remove');
Route::post('/inventory/entries/{entry}/equip', [ItemsController::class, 'equip'])->name('browser-game.items.inventory.equip');
Route::post('/inventory/entries/{entry}/unequip', [ItemsController::class, 'unequip'])->name('browser-game.items.inventory.unequip');
Route::post('/inventory/entries/{entry}/bind', [ItemsController::class, 'bind'])->name('browser-game.items.inventory.bind');
Route::post('/inventory/entries/{entry}/durability', [ItemsController::class, 'durability'])->name('browser-game.items.inventory.durability');
Route::post('/inventory/entries/{entry}/container', [ItemsController::class, 'container'])->name('browser-game.items.inventory.container');
Route::post('/inventory/entries/{entry}/provenance', [ItemsController::class, 'provenance'])->name('browser-game.items.inventory.provenance');
Route::get('/{items}', [ItemsController::class, 'show'])->name('browser-game.items.show');
```
<!-- layer-implementation-plan:end -->
