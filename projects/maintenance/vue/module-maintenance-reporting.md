# Maintenance: Module Maintenance Reporting Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-reporting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-maintenance-module-maintenance-reporting-vue-inertia`
**Matching domain module:** `module-maintenance-reporting`
**Application:** Maintenance
**Source feature:** [Module Maintenance Reporting](../features/module-maintenance-reporting.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-maintenance-reporting.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Backlog:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Response:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **First-time fix:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Downtime:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Cost:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Utilization:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Stock:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **SLA:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Compliance metrics:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-maintenance-module-maintenance-reporting-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `backlog`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `response`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `first-time-fix`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `downtime`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `cost`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `utilization`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `stock`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `sla`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `compliance-metrics`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `module-maintenance-reporting` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-maintenance-laravel-inertia-vue`](https://github.com/liberusoftware/project-maintenance-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-maintenance-reporting-vue-inertia`](https://github.com/liberusoftware/module-maintenance-reporting-vue-inertia) (`@liberusoftware/module-maintenance-reporting-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/module-maintenance-reporting.md) · [Core plan](../core/module-maintenance-reporting.md) · [API plan](../api/module-maintenance-reporting.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Backlog** | Render `backlog` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Response** | Render `response` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **First-time fix** | Render `first-time fix` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Downtime** | Render `downtime` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Cost** | Render `cost` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Utilization** | Render `utilization` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Stock** | Render `stock` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **SLA** | Render `sla` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Compliance metrics** | Render `compliance metrics` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
