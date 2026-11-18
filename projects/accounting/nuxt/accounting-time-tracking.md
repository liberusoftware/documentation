# Accounting: Accounting Time Tracking Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-time-tracking). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-time-tracking-nuxt`
**Matching domain module:** `accounting-time-tracking`
**Application:** Accounting
**Source feature:** [Accounting Time Tracking](../features/accounting-time-tracking.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-time-tracking.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-time-tracking` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Timesheets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Timers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Employees/contractors:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Customers/projects/tasks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Billable/cost rates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payroll/invoice export:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Corrections:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-time-tracking-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `timesheets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `timers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `employees-contractors`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `customers-projects-tasks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `billable-cost-rates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payroll-invoice-export`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `corrections`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-time-tracking` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-time-tracking.md)) |
| Capability Nuxt module skeleton | [`module-accounting-time-tracking-nuxt`](https://github.com/liberusoftware/module-accounting-time-tracking-nuxt) (`@liberusoftware/module-accounting-time-tracking-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Timesheets** | Expose composable and Vue 3 component for `timesheets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-time-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Timers** | Expose composable and Vue 3 component for `timers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-time-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Employees/contractors** | Expose composable and Vue 3 component for `employees/contractors` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-time-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Customers/projects/tasks** | Expose composable and Vue 3 component for `customers/projects/tasks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-time-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Billable/cost rates** | Expose composable and Vue 3 component for `billable/cost rates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-time-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approval** | Expose composable and Vue 3 component for `approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-time-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Payroll/invoice export** | Expose composable and Vue 3 component for `payroll/invoice export` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-time-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Corrections** | Expose composable and Vue 3 component for `corrections` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-time-tracking.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

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
