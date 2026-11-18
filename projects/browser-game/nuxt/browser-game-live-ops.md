# Browser Game: Browser Game Live Ops Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#browser-game-live-ops). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-browser-game-browser-game-live-ops-nuxt`
**Matching domain module:** `browser-game-live-ops`
**Application:** Browser Game
**Source feature:** [Browser Game Live Ops](../features/browser-game-live-ops.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/browser-game-live-ops.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `browser-game-live-ops` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Daily activities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Events:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Seasons:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Content schedules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Announcements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Grants:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rollback:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-browser-game-browser-game-live-ops-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `daily-activities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `events`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `seasons`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `content-schedules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `announcements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `grants`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rollback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-live-ops` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-browser-game-nuxt-vue`](https://github.com/liberusoftware/project-browser-game-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/browser-game-live-ops.md)) |
| Capability Nuxt module skeleton | [`module-browser-game-live-ops-nuxt`](https://github.com/liberusoftware/module-browser-game-live-ops-nuxt) (`@liberusoftware/module-browser-game-live-ops-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Daily activities** | Expose composable and Vue 3 component for `daily activities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-live-ops.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Events** | Expose composable and Vue 3 component for `events` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-live-ops.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Seasons** | Expose composable and Vue 3 component for `seasons` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-live-ops.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Content schedules** | Expose composable and Vue 3 component for `content schedules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-live-ops.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Announcements** | Expose composable and Vue 3 component for `announcements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-live-ops.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Grants** | Expose composable and Vue 3 component for `grants` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-live-ops.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Rollback** | Expose composable and Vue 3 component for `rollback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/browser-game-live-ops.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [LiveOpsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-live-ops/src/Queries/LiveOpsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [LiveOpsClaim.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-live-ops/src/Models/LiveOpsClaim.php) | No literal fillable array detected; inspect the model and API schema. |
| [LiveOpsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-live-ops/src/Models/LiveOpsRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [LiveOpsRollback.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-live-ops/src/Models/LiveOpsRollback.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [LiveOpsController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-live-ops-api/src/Http/Controllers/LiveOpsController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function publish(Request $request, LiveOpsRecord $liveOps): JsonResponse`<br>`public function claim(Request $request, LiveOpsRecord $liveOps): JsonResponse`<br>`public function dailyStatus(Request $request, LiveOpsRecord $liveOps): JsonResponse`<br>`public function dailyClaim(Request $request, LiveOpsRecord $liveOps): JsonResponse`<br>`public function rollback(Request $request, LiveOpsRecord $liveOps): JsonResponse`<br>`public function show(Request $request, LiveOpsRecord $liveOps): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-live-ops-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-live-ops-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/live-ops')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [LiveOpsController::class, 'index'])->name('browser-game.live-ops.index');
Route::post('/', [LiveOpsController::class, 'store'])->name('browser-game.live-ops.store');
Route::post('/{liveOps}/publish', [LiveOpsController::class, 'publish'])->name('browser-game.live-ops.publish');
Route::post('/{liveOps}/claim', [LiveOpsController::class, 'claim'])->name('browser-game.live-ops.claim');
Route::get('/daily/{liveOps}/status', [LiveOpsController::class, 'dailyStatus'])->name('browser-game.live-ops.daily.status');
Route::post('/daily/{liveOps}/claim', [LiveOpsController::class, 'dailyClaim'])->name('browser-game.live-ops.daily.claim');
Route::post('/{liveOps}/rollback', [LiveOpsController::class, 'rollback'])->name('browser-game.live-ops.rollback');
Route::get('/{liveOps}', [LiveOpsController::class, 'show'])->name('browser-game.live-ops.show');
```
<!-- layer-implementation-plan:end -->
