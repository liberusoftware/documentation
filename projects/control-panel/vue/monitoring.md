# Control Panel: Monitoring Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#monitoring). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-control-panel-monitoring-vue-inertia`
**Matching domain module:** `control-panel-monitoring`
**Application:** Control Panel
**Source feature:** [Monitoring](../features/monitoring.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/monitoring.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Metrics:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Logs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Uptime:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Capacity:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Alerts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Incidents:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Maintenance windows:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Status:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-control-panel-monitoring-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `metrics`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `logs`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `uptime`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `capacity`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `alerts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `incidents`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `maintenance-windows`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `status`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `control-panel-monitoring` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-control-panel-laravel-inertia-vue`](https://github.com/liberusoftware/project-control-panel-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-control-panel-monitoring-vue-inertia`](https://github.com/liberusoftware/module-control-panel-monitoring-vue-inertia) (`@liberusoftware/module-control-panel-monitoring-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/monitoring.md) · [Core plan](../core/monitoring.md) · [API plan](../api/monitoring.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Metrics** | Render `metrics` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Logs** | Render `logs` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Uptime** | Render `uptime` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Capacity** | Render `capacity` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Alerts** | Render `alerts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Incidents** | Render `incidents` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Maintenance windows** | Render `maintenance windows` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Status** | Render `status` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
