# Accounting: Accounting Time Tracking Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-time-tracking). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-accounting-time-tracking-vue-inertia`
**Matching domain module:** `accounting-time-tracking`
**Application:** Accounting
**Source feature:** [Accounting Time Tracking](../features/accounting-time-tracking.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-time-tracking.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Timesheets:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Timers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Employees/contractors:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Customers/projects/tasks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Billable/cost rates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Approval:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Payroll/invoice export:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Corrections:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-time-tracking-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `timesheets`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `timers`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `employees-contractors`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `customers-projects-tasks`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `billable-cost-rates`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `approval`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `payroll-invoice-export`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `corrections`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-time-tracking` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-accounting-erp-laravel-inertia-vue`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-accounting-time-tracking-vue-inertia`](https://github.com/liberusoftware/module-accounting-time-tracking-vue-inertia) (`@liberusoftware/module-accounting-time-tracking-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/accounting-time-tracking.md) · [Core plan](../core/accounting-time-tracking.md) · [API plan](../api/accounting-time-tracking.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Timesheets** | Render `timesheets` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Timers** | Render `timers` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Employees/contractors** | Render `employees/contractors` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Customers/projects/tasks** | Render `customers/projects/tasks` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Billable/cost rates** | Render `billable/cost rates` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Approval** | Render `approval` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Payroll/invoice export** | Render `payroll/invoice export` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Corrections** | Render `corrections` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveTimeEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/ApproveTimeEntry.php) | `public function handle(TimeEntry $entry): TimeEntry` |
| [CreateTimeEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/CreateTimeEntry.php) | `public function handle(array $attributes): TimeEntry` |
| [StartTimer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/StartTimer.php) | `public function handle(array $attributes): TimeTimer` |
| [StopTimer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/StopTimer.php) | `public function handle(TimeTimer $timer): TimeTimer` |
| [SubmitTimeEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/SubmitTimeEntry.php) | `public function handle(TimeEntry $entry): TimeEntry` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TimeEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Models/TimeEntry.php) | `team_id`, `worker_ref`, `customer_ref`, `project_ref`, `task_ref`, `worked_on`, `hours`, `billable_rate`, `cost_rate`, `currency`, `billable`, `status`, `description`, `metadata` |
| [TimeExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Models/TimeExport.php) | `team_id`, `destination`, `period_start`, `period_end`, `entry_count`, `status`, `exported_at`, `metadata` |
| [TimeTimer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Models/TimeTimer.php) | `team_id`, `worker_ref`, `project_ref`, `started_at`, `stopped_at`, `status` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TimeTrackingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking-api/src/Http/Controllers/TimeTrackingController.php) | `public function entries(Request $request): mixed`<br>`public function createEntry(Request $request, CreateTimeEntry $action): mixed`<br>`public function submit(Request $request, string $entry, SubmitTimeEntry $action): mixed`<br>`public function approve(Request $request, string $entry, ApproveTimeEntry $action): mixed`<br>`public function startTimer(Request $request, StartTimer $action): mixed`<br>`public function stopTimer(Request $request, string $timer, StopTimer $action): mixed` |

**Observed route declarations:**

[modules/accounting-time-tracking-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/time-tracking')->middleware(['auth:sanctum'])->group(function (): void {
Route::get('/entries', [TimeTrackingController::class, 'entries'])->middleware('ability:accounting.time-tracking.read');
Route::post('/entries', [TimeTrackingController::class, 'createEntry'])->middleware('ability:accounting.time-tracking.write');
Route::post('/entries/{entry}/submit', [TimeTrackingController::class, 'submit'])->middleware('ability:accounting.time-tracking.write');
Route::post('/entries/{entry}/approve', [TimeTrackingController::class, 'approve'])->middleware('ability:accounting.time-tracking.approve');
Route::post('/timers/start', [TimeTrackingController::class, 'startTimer'])->middleware('ability:accounting.time-tracking.write');
Route::post('/timers/{timer}/stop', [TimeTrackingController::class, 'stopTimer'])->middleware('ability:accounting.time-tracking.write');
```
<!-- layer-implementation-plan:end -->
