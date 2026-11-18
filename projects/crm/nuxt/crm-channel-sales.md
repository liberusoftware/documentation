# CRM: Crm Channel Sales Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-channel-sales). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-channel-sales-nuxt`
**Matching domain module:** `crm-channel-sales`
**Application:** CRM
**Source feature:** [Crm Channel Sales](../features/crm-channel-sales.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-channel-sales.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-channel-sales` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Partner opportunities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Shared pipelines:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Referrals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reseller pricing references:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quotes/orders handoff:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Commissions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Forecasts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Partner portal:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-channel-sales-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `partner-opportunities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `shared-pipelines`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `referrals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reseller-pricing-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quotes-orders-handoff`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `commissions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `forecasts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `partner-portal`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-channel-sales` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-channel-sales.md)) |
| Capability Nuxt module skeleton | [`module-crm-channel-sales-nuxt`](https://github.com/liberusoftware/module-crm-channel-sales-nuxt) (`@liberusoftware/module-crm-channel-sales-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Partner opportunities** | Expose composable and Vue 3 component for `partner opportunities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-sales.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Shared pipelines** | Expose composable and Vue 3 component for `shared pipelines` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-sales.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Referrals** | Expose composable and Vue 3 component for `referrals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-sales.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Reseller pricing references** | Expose composable and Vue 3 component for `reseller pricing references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-sales.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Quotes/orders handoff** | Expose composable and Vue 3 component for `quotes/orders handoff` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-sales.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Commissions** | Expose composable and Vue 3 component for `commissions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-sales.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Forecasts** | Expose composable and Vue 3 component for `forecasts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-sales.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Partner portal** | Expose composable and Vue 3 component for `partner portal` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-channel-sales.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ChannelSalesQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Queries/ChannelSalesQuery.php) | `public function opportunities(int $teamId): Builder`<br>`public function forecast(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AdvanceChannelOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Actions/AdvanceChannelOpportunity.php) | `public function execute(int $teamId, int $actorId, ChannelOpportunity $opportunity, string $stage, string $handoffStatus = 'pending'): ChannelEvent` |
| [RegisterChannelOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Actions/RegisterChannelOpportunity.php) | `public function execute(int $teamId, int $ownerId, string $partnerKey, string $opportunityKey, float $amount, float $commissionRate, array $pricingReference = []): ChannelOpportunity` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ChannelEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Models/ChannelEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ChannelOpportunity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales/src/Models/ChannelOpportunity.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ChannelSalesController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales-api/src/Http/Controllers/ChannelSalesController.php) | `public function __construct(private readonly ChannelSalesQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(RegisterChannelOpportunity $a): JsonResponse`<br>`public function advance(ChannelOpportunity $opportunity, AdvanceChannelOpportunity $a): JsonResponse`<br>`public function forecast(): JsonResponse` |

**Observed route declarations:**

[modules/crm-channel-sales-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-channel-sales-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/channel-sales')->group(function (): void {
Route::get('opportunities', [ChannelSalesController::class, 'index']);
Route::post('opportunities', [ChannelSalesController::class, 'store']);
Route::post('opportunities/{opportunity}/advance', [ChannelSalesController::class, 'advance']);
Route::get('forecast', [ChannelSalesController::class, 'forecast']);
```
<!-- layer-implementation-plan:end -->
