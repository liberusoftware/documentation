# CRM: Crm Service Analytics Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-service-analytics). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-service-analytics-nuxt`
**Matching domain module:** `crm-service-analytics`
**Application:** CRM
**Source feature:** [Crm Service Analytics](../features/crm-service-analytics.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-service-analytics.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-service-analytics` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Volume:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Backlog:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deflection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **First response:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Resolution:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reopen:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transfer:** page/component/composable/API-action behavior for this module's authorized workflow.
- **SLA:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Satisfaction:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quality:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Staffing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cost-to-serve:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-service-analytics-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `volume`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `backlog`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deflection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `first-response`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `resolution`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reopen`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transfer`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sla`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `satisfaction`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quality`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `staffing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cost-to-serve`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-service-analytics` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-service-analytics.md)) |
| Capability Nuxt module skeleton | [`module-crm-service-analytics-nuxt`](https://github.com/liberusoftware/module-crm-service-analytics-nuxt) (`@liberusoftware/module-crm-service-analytics-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Volume** | Expose composable and Vue 3 component for `volume` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-service-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Backlog** | Expose composable and Vue 3 component for `backlog` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-service-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Deflection** | Expose composable and Vue 3 component for `deflection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-service-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **First response** | Expose composable and Vue 3 component for `first response` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-service-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Resolution** | Expose composable and Vue 3 component for `resolution` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-service-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Reopen** | Expose composable and Vue 3 component for `reopen` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-service-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Transfer** | Expose composable and Vue 3 component for `transfer` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-service-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **SLA** | Expose composable and Vue 3 component for `sla` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-service-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Satisfaction** | Expose composable and Vue 3 component for `satisfaction` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-service-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Quality** | Expose composable and Vue 3 component for `quality` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-service-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Staffing** | Expose composable and Vue 3 component for `staffing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-service-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Cost-to-serve** | Expose composable and Vue 3 component for `cost-to-serve` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-service-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AnalyticsQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Queries/AnalyticsQuery.php) | `public function snapshots(int $teamId)`<br>`public function metric(int $teamId, string $metric, $from = null, $to = null)`<br>`public function summary(int $teamId, $from = null, $to = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordMetric.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Actions/RecordMetric.php) | `public function execute(int $teamId, int $actorId, array $data): AnalyticsSnapshot` |
| [RecordServiceMetrics.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Actions/RecordServiceMetrics.php) | `public function execute(int $teamId, int $actorId, array $metrics): int` |
| [AnalyticsAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Services/AnalyticsAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [AnalyticsPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Services/AnalyticsPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AnalyticsAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Models/AnalyticsAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [AnalyticsSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Models/AnalyticsSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AnalyticsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics-api/src/Http/Controllers/AnalyticsController.php) | `public function index(Request $r, AnalyticsQuery $q)`<br>`public function metric(Request $r, string $metric, AnalyticsQuery $q)`<br>`public function summary(Request $r, AnalyticsQuery $q)`<br>`public function store(Request $r, RecordMetric $a)`<br>`public function batch(Request $r, RecordServiceMetrics $a)` |

**Observed route declarations:**

[modules/crm-service-analytics-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/service-analytics')->group(function (): void {
Route::get('/snapshots', [AnalyticsController::class, 'index']);
Route::get('/metrics/{metric}', [AnalyticsController::class, 'metric']);
Route::get('/summary', [AnalyticsController::class, 'summary']);
Route::post('/snapshots', [AnalyticsController::class, 'store']);
Route::post('/snapshots/batch', [AnalyticsController::class, 'batch']);
```
<!-- layer-implementation-plan:end -->
