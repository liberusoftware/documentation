# Browser Game: Moderation and Analytics Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#moderation-and-analytics). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-browser-game-moderation-and-analytics-nuxt`
**Matching domain module:** `browser-game-moderation-and-analytics`
**Application:** Browser Game
**Source feature:** [Moderation and Analytics](../features/moderation-and-analytics.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/moderation-and-analytics.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `browser-game-moderation-and-analytics` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Reports:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sanctions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Appeals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Telemetry:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Funnels:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Balance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Economy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fraud:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Health:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-browser-game-moderation-and-analytics-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `reports`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sanctions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `appeals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `telemetry`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `funnels`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `balance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `economy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fraud`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `health`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-moderation-and-analytics` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-browser-game-nuxt-vue`](https://github.com/liberusoftware/project-browser-game-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/moderation-and-analytics.md)) |
| Capability Nuxt module skeleton | [`module-browser-game-moderation-and-analytics-nuxt`](https://github.com/liberusoftware/module-browser-game-moderation-and-analytics-nuxt) (`@liberusoftware/module-browser-game-moderation-and-analytics-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Reports** | Expose composable and Vue 3 component for `reports` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation-and-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Sanctions** | Expose composable and Vue 3 component for `sanctions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation-and-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Appeals** | Expose composable and Vue 3 component for `appeals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation-and-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Telemetry** | Expose composable and Vue 3 component for `telemetry` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation-and-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Funnels** | Expose composable and Vue 3 component for `funnels` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation-and-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Balance** | Expose composable and Vue 3 component for `balance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation-and-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Economy** | Expose composable and Vue 3 component for `economy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation-and-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Fraud** | Expose composable and Vue 3 component for `fraud` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation-and-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Health** | Expose composable and Vue 3 component for `health` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/moderation-and-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ModerationAndAnalyticsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Queries/ModerationAndAnalyticsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ModerationAndAnalyticsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics/src/Models/ModerationAndAnalyticsRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ModerationAndAnalyticsController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-api/src/Http/Controllers/ModerationAndAnalyticsController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function report(Request $request): JsonResponse`<br>`public function sanction(Request $request): JsonResponse`<br>`public function appeal(Request $request): JsonResponse`<br>`public function telemetry(Request $request): JsonResponse`<br>`public function funnel(Request $request): JsonResponse`<br>`public function balance(Request $request): JsonResponse`<br>`public function economy(Request $request): JsonResponse`<br>`public function fraud(Request $request): JsonResponse`<br>`public function health(Request $request): JsonResponse`<br>`public function resolve(Request $request, ModerationAndAnalyticsRecord $moderationAndAnalytics): JsonResponse`<br>`public function show(Request $request, ModerationAndAnalyticsRecord $moderationAndAnalytics): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-moderation-and-analytics-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-moderation-and-analytics-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/moderation-and-analytics')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [ModerationAndAnalyticsController::class, 'index'])->name('browser-game.moderation-and-analytics.index');
Route::post('/', [ModerationAndAnalyticsController::class, 'store'])->name('browser-game.moderation-and-analytics.store');
Route::post('/reports', [ModerationAndAnalyticsController::class, 'report'])->name('browser-game.moderation-and-analytics.reports');
Route::post('/sanctions', [ModerationAndAnalyticsController::class, 'sanction'])->name('browser-game.moderation-and-analytics.sanctions');
Route::post('/appeals', [ModerationAndAnalyticsController::class, 'appeal'])->name('browser-game.moderation-and-analytics.appeals');
Route::post('/telemetry', [ModerationAndAnalyticsController::class, 'telemetry'])->name('browser-game.moderation-and-analytics.telemetry');
Route::post('/funnels', [ModerationAndAnalyticsController::class, 'funnel'])->name('browser-game.moderation-and-analytics.funnels');
Route::post('/balance', [ModerationAndAnalyticsController::class, 'balance'])->name('browser-game.moderation-and-analytics.balance');
Route::post('/economy', [ModerationAndAnalyticsController::class, 'economy'])->name('browser-game.moderation-and-analytics.economy');
Route::post('/fraud', [ModerationAndAnalyticsController::class, 'fraud'])->name('browser-game.moderation-and-analytics.fraud');
Route::post('/health', [ModerationAndAnalyticsController::class, 'health'])->name('browser-game.moderation-and-analytics.health');
Route::post('/{moderationAndAnalytics}/resolve', [ModerationAndAnalyticsController::class, 'resolve'])->name('browser-game.moderation-and-analytics.resolve');
Route::get('/{moderationAndAnalytics}', [ModerationAndAnalyticsController::class, 'show'])->name('browser-game.moderation-and-analytics.show');
```
<!-- layer-implementation-plan:end -->
