# CRM: Crm Revenue Intelligence Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-revenue-intelligence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-revenue-intelligence-nuxt`
**Matching domain module:** `crm-revenue-intelligence`
**Application:** CRM
**Source feature:** [Crm Revenue Intelligence](../features/crm-revenue-intelligence.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-revenue-intelligence.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-revenue-intelligence` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Pipeline inspection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Health/risk:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Engagement gaps:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Opportunity scoring:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Relationship maps:** page/component/composable/API-action behavior for this module's authorized workflow.
- **White-space/next-product suggestions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Anomaly detection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Alerts:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-revenue-intelligence-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `pipeline-inspection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `health-risk`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `engagement-gaps`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `opportunity-scoring`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `relationship-maps`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `white-space-next-product-suggestions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `anomaly-detection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `alerts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-revenue-intelligence` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-revenue-intelligence.md)) |
| Capability Nuxt module skeleton | [`module-crm-revenue-intelligence-nuxt`](https://github.com/liberusoftware/module-crm-revenue-intelligence-nuxt) (`@liberusoftware/module-crm-revenue-intelligence-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Pipeline inspection** | Expose composable and Vue 3 component for `pipeline inspection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-revenue-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Health/risk** | Expose composable and Vue 3 component for `health/risk` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-revenue-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Engagement gaps** | Expose composable and Vue 3 component for `engagement gaps` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-revenue-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Opportunity scoring** | Expose composable and Vue 3 component for `opportunity scoring` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-revenue-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Relationship maps** | Expose composable and Vue 3 component for `relationship maps` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-revenue-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **White-space/next-product suggestions** | Expose composable and Vue 3 component for `white-space/next-product suggestions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-revenue-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Anomaly detection** | Expose composable and Vue 3 component for `anomaly detection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-revenue-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Alerts** | Expose composable and Vue 3 component for `alerts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-revenue-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [RevenueIntelligenceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Queries/RevenueIntelligenceQuery.php) | `public function insights(int $teamId)`<br>`public function alerts(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/CreateAlert.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueIntelligenceAlert` |
| [RecordInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/RecordInsight.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueInsight` |
| [ResolveAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/ResolveAlert.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $alertId): RevenueIntelligenceAlert` |
| [UpdateInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/UpdateInsight.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $insightId, array $input): RevenueInsight` |
| [RevenueIntelligencePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Services/RevenueIntelligencePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RevenueInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Models/RevenueInsight.php) | No literal fillable array detected; inspect the model and API schema. |
| [RevenueIntelligenceAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Models/RevenueIntelligenceAlert.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [RevenueIntelligenceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-api/src/Http/Controllers/RevenueIntelligenceController.php) | `public function insights(Request $r, RevenueIntelligenceQuery $q)`<br>`public function insight(Request $r, RecordInsight $a)`<br>`public function alerts(Request $r, RevenueIntelligenceQuery $q)`<br>`public function alert(Request $r, CreateAlert $a)`<br>`public function resolve(Request $r, int $alert, ResolveAlert $a)` |

**Observed route declarations:**

[modules/crm-revenue-intelligence-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/revenue-intelligence')->group(function (): void {
Route::get('/insights', [RevenueIntelligenceController::class, 'insights']);
Route::post('/insights', [RevenueIntelligenceController::class, 'insight']);
Route::get('/alerts', [RevenueIntelligenceController::class, 'alerts']);
Route::post('/alerts', [RevenueIntelligenceController::class, 'alert']);
Route::post('/alerts/{alert}/resolve', [RevenueIntelligenceController::class, 'resolve']);
```
<!-- layer-implementation-plan:end -->
