# CRM: Revenue Lifecycle Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-lifecycle). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-revenue-lifecycle-nuxt`
**Matching domain module:** `crm-revenue-lifecycle`
**Application:** CRM
**Source feature:** [Revenue Lifecycle](../features/revenue-lifecycle.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/revenue-lifecycle.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-revenue-lifecycle` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Opportunity-to-order orchestration:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Assets/installed products:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Entitlements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Renewals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Upgrades:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Downgrades:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cancellation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Usage signals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fallout queues:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-revenue-lifecycle-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `opportunity-to-order-orchestration`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `assets-installed-products`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `entitlements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `renewals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `upgrades`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `downgrades`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cancellation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `usage-signals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fallout-queues`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-revenue-lifecycle` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/revenue-lifecycle.md)) |
| Capability Nuxt module skeleton | [`module-crm-revenue-lifecycle-nuxt`](https://github.com/liberusoftware/module-crm-revenue-lifecycle-nuxt) (`@liberusoftware/module-crm-revenue-lifecycle-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Opportunity-to-order orchestration** | Expose composable and Vue 3 component for `opportunity-to-order orchestration` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-lifecycle.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Assets/installed products** | Expose composable and Vue 3 component for `assets/installed products` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-lifecycle.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Entitlements** | Expose composable and Vue 3 component for `entitlements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-lifecycle.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Renewals** | Expose composable and Vue 3 component for `renewals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-lifecycle.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Upgrades** | Expose composable and Vue 3 component for `upgrades` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-lifecycle.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Downgrades** | Expose composable and Vue 3 component for `downgrades` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-lifecycle.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Cancellation** | Expose composable and Vue 3 component for `cancellation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-lifecycle.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Usage signals** | Expose composable and Vue 3 component for `usage signals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-lifecycle.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Fallout queues** | Expose composable and Vue 3 component for `fallout queues` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/revenue-lifecycle.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [RevenueQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Queries/RevenueQuery.php) | `public function assets(int $teamId)`<br>`public function orders(int $teamId)`<br>`public function fallout(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateOrder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/CreateOrder.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueOrder` |
| [ManageAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/ManageAsset.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueAsset` |
| [RecordUsageSignal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/RecordUsageSignal.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $assetId, array $input): RevenueAsset` |
| [ResolveFallout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Actions/ResolveFallout.php) | `public function __construct(private readonly RevenuePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $falloutId, array $input): RevenueFallout` |
| [RevenuePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Services/RevenuePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RevenueAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueAsset.php) | No literal fillable array detected; inspect the model and API schema. |
| [RevenueFallout.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueFallout.php) | No literal fillable array detected; inspect the model and API schema. |
| [RevenueOrder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle/src/Models/RevenueOrder.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [RevenueLifecycleController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle-api/src/Http/Controllers/RevenueLifecycleController.php) | `public function assets(Request $request, RevenueQuery $query)`<br>`public function asset(Request $request, ManageAsset $action)`<br>`public function order(Request $request, CreateOrder $action)`<br>`public function usage(Request $request, int $asset, RecordUsageSignal $action)`<br>`public function fallout(Request $request, RevenueQuery $query)`<br>`public function resolveFallout(Request $request, int $fallout, ResolveFallout $action)` |

**Observed route declarations:**

[modules/crm-revenue-lifecycle-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-lifecycle-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/revenue-lifecycle')->group(function (): void {
Route::get('/assets', [RevenueLifecycleController::class, 'assets']);
Route::post('/assets', [RevenueLifecycleController::class, 'asset']);
Route::post('/assets/{asset}/usage', [RevenueLifecycleController::class, 'usage']);
Route::post('/orders', [RevenueLifecycleController::class, 'order']);
Route::get('/fallout', [RevenueLifecycleController::class, 'fallout']);
Route::post('/fallout/{fallout}/resolve', [RevenueLifecycleController::class, 'resolveFallout']);
```
<!-- layer-implementation-plan:end -->
