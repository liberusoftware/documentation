# Control Panel: Monitoring Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#monitoring). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-control-panel-monitoring-nuxt`
**Matching domain module:** `control-panel-monitoring`
**Application:** Control Panel
**Source feature:** [Monitoring](../features/monitoring.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/monitoring.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `control-panel-monitoring` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Metrics:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Logs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Uptime:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Capacity:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Alerts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Incidents:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Maintenance windows:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Status:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-control-panel-monitoring-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `metrics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `logs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `uptime`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `capacity`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `alerts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `incidents`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `maintenance-windows`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `status`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `control-panel-monitoring` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/monitoring.md)) |
| Capability Nuxt module skeleton | [`module-control-panel-monitoring-nuxt`](https://github.com/liberusoftware/module-control-panel-monitoring-nuxt) (`@liberusoftware/module-control-panel-monitoring-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Metrics** | Expose composable and Vue 3 component for `metrics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/monitoring.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Logs** | Expose composable and Vue 3 component for `logs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/monitoring.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Uptime** | Expose composable and Vue 3 component for `uptime` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/monitoring.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Capacity** | Expose composable and Vue 3 component for `capacity` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/monitoring.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Alerts** | Expose composable and Vue 3 component for `alerts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/monitoring.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Incidents** | Expose composable and Vue 3 component for `incidents` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/monitoring.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Maintenance windows** | Expose composable and Vue 3 component for `maintenance windows` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/monitoring.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Status** | Expose composable and Vue 3 component for `status` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/monitoring.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListMonitors.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Queries/ListMonitors.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CancelMaintenanceWindow.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/CancelMaintenanceWindow.php) | `public function execute(MaintenanceWindow $window): MaintenanceWindow` |
| [DeleteMaintenanceWindow.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/DeleteMaintenanceWindow.php) | `public function execute(MaintenanceWindow $window): void` |
| [RecordMonitoringEvent.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/RecordMonitoringEvent.php) | `public function execute(array $a): MonitoringEvent` |
| [RecordMonitoringResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/RecordMonitoringResource.php) | `public function execute(array $a): Model` |
| [RegisterMonitor.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/RegisterMonitor.php) | `public function execute(array $attributes): Monitor` |
| [ResolveMonitoringEvent.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/ResolveMonitoringEvent.php) | `public function execute(MonitoringEvent $event): MonitoringEvent` |
| [UpdateMaintenanceWindow.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/UpdateMaintenanceWindow.php) | `public function execute(MaintenanceWindow $window, array $attributes): MaintenanceWindow` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AlertRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/AlertRule.php) | `id`, `team_id`, `name`, `condition`, `threshold`, `channels`, `active` |
| [CapacitySnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/CapacitySnapshot.php) | `id`, `team_id`, `resource`, `used`, `available`, `unit`, `captured_at`, `details` |
| [Incident.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/Incident.php) | `id`, `team_id`, `title`, `severity`, `status`, `summary`, `started_at`, `resolved_at`, `metadata` |
| [LogEntry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/LogEntry.php) | `id`, `team_id`, `source`, `level`, `message`, `context`, `logged_at` |
| [MaintenanceWindow.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/MaintenanceWindow.php) | `id`, `team_id`, `name`, `starts_at`, `ends_at`, `scope`, `status`, `details` |
| [MetricSample.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/MetricSample.php) | `id`, `team_id`, `monitor_id`, `name`, `value`, `unit`, `dimensions`, `sampled_at` |
| [Monitor.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/Monitor.php) | `team_id`, `subject_type`, `subject_id`, `name`, `status`, `last_checked_at`, `metrics` |
| [MonitoringEvent.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/MonitoringEvent.php) | `id`, `team_id`, `monitor_id`, `kind`, `status`, `payload`, `starts_at`, `ends_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MonitorController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-api/src/Http/Controllers/MonitorController.php) | `public function index(Request $request, ListMonitors $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, RegisterMonitor $register): JsonResponse`<br>`public function event(Request $request, RecordMonitoringEvent $record): JsonResponse`<br>`public function record(Request $request, RecordMonitoringResource $record): JsonResponse`<br>`public function resolveEvent(Request $request, string $id, ResolveMonitoringEvent $resolve): JsonResponse`<br>`public function cancelMaintenance(Request $request, MaintenanceWindow $window, CancelMaintenanceWindow $cancel): JsonResponse`<br>`public function deleteMaintenance(Request $request, string $id, DeleteMaintenanceWindow $delete): JsonResponse`<br>`public function updateMaintenance(Request $request, string $id, UpdateMaintenanceWindow $update): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-monitoring-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/monitoring')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [MonitorController::class, 'index'])->name('control-panel.monitoring.index');
Route::post('/', [MonitorController::class, 'store'])->name('control-panel.monitoring.store');
Route::post('/events', [MonitorController::class, 'event'])->name('control-panel.monitoring.events.store');
Route::post('/events/{event}/resolve', [MonitorController::class, 'resolveEvent'])->name('control-panel.monitoring.events.resolve');
Route::post('/resources', [MonitorController::class, 'record'])->name('control-panel.monitoring.resources.store');
Route::post('/maintenance/{window}/cancel', [MonitorController::class, 'cancelMaintenance'])->name('control-panel.monitoring.maintenance.cancel');
Route::delete('/maintenance/{window}', [MonitorController::class, 'deleteMaintenance'])->name('control-panel.monitoring.maintenance.delete');
Route::patch('/maintenance/{window}', [MonitorController::class, 'updateMaintenance'])->name('control-panel.monitoring.maintenance.update');
Route::get('{monitor}', [MonitorController::class, 'show'])->name('control-panel.monitoring.show');
```
<!-- layer-implementation-plan:end -->
