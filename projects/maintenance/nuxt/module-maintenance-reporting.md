# Maintenance: Module Maintenance Reporting Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-reporting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-module-maintenance-reporting-nuxt`
**Matching domain module:** `module-maintenance-reporting`
**Application:** Maintenance
**Source feature:** [Module Maintenance Reporting](../features/module-maintenance-reporting.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-maintenance-reporting.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-maintenance-reporting` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Backlog:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Response:** page/component/composable/API-action behavior for this module's authorized workflow.
- **First-time fix:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Downtime:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cost:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Utilization:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Stock:** page/component/composable/API-action behavior for this module's authorized workflow.
- **SLA:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Compliance metrics:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-module-maintenance-reporting-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `backlog`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `response`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `first-time-fix`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `downtime`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cost`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `utilization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `stock`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sla`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `compliance-metrics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-maintenance-reporting` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-maintenance-reporting.md)) |
| Capability Nuxt module skeleton | [`module-maintenance-reporting-nuxt`](https://github.com/liberusoftware/module-maintenance-reporting-nuxt) (`@liberusoftware/module-maintenance-reporting-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Backlog** | Expose composable and Vue 3 component for `backlog` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Response** | Expose composable and Vue 3 component for `response` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **First-time fix** | Expose composable and Vue 3 component for `first-time fix` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Downtime** | Expose composable and Vue 3 component for `downtime` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Cost** | Expose composable and Vue 3 component for `cost` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Utilization** | Expose composable and Vue 3 component for `utilization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Stock** | Expose composable and Vue 3 component for `stock` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **SLA** | Expose composable and Vue 3 component for `sla` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Compliance metrics** | Expose composable and Vue 3 component for `compliance metrics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [BuildReportSummary.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Queries/BuildReportSummary.php) | `public function handle(int $teamId, ?CarbonInterface $start = null, ?CarbonInterface $end = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/CreateReportRecord.php) | `public function handle(int $teamId, array $attributes): ReportRecord` |
| [DeleteReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/DeleteReportRecord.php) | `public function handle(int $teamId, ReportRecord $record): void` |
| [PublishReport.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/PublishReport.php) | `public function execute(int $teamId, ReportRecord $record): ReportRecord` |
| [UpdateReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/UpdateReportRecord.php) | `public function handle(int $teamId, ReportRecord $record, array $attributes): ReportRecord` |
| [ReportRecordPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Policies/ReportRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, ReportRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, ReportRecord $record): bool`<br>`public function delete(object $user, ReportRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReportKind.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Models/ReportKind.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Models/ReportRecord.php) | `kind`, `title`, `description`, `metric_value`, `period_start`, `period_end`, `status`, `metadata`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReportingRecordController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting-api/src/Http/Controllers/ReportingRecordController.php) | `public function index(Request $request): JsonResponse`<br>`public function summary(Request $request, BuildReportSummary $summary): JsonResponse`<br>`public function store(Request $request, CreateReportRecord $create): JsonResponse`<br>`public function publish(Request $request, ReportRecord $record, PublishReport $publish): JsonResponse`<br>`public function show(Request $request, ReportRecord $record): JsonResponse`<br>`public function update(Request $request, ReportRecord $record, UpdateReportRecord $update): JsonResponse`<br>`public function destroy(Request $request, ReportRecord $record, DeleteReportRecord $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-reporting-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/reporting')->group(function (): void {
Route::get('/', [ReportingRecordController::class, 'index']);
Route::get('/summary', [ReportingRecordController::class, 'summary']);
Route::post('/', [ReportingRecordController::class, 'store']);
Route::get('/{record}', [ReportingRecordController::class, 'show']);
Route::patch('/{record}', [ReportingRecordController::class, 'update']);
Route::post('/{record}/publish', [ReportingRecordController::class, 'publish']);
Route::delete('/{record}', [ReportingRecordController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
