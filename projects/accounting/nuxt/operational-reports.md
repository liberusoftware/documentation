# Accounting: Operational Reports Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#operational-reports). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-operational-reports-nuxt`
**Matching domain module:** `accounting-operational-reports`
**Application:** Accounting
**Source feature:** [Operational Reports](../features/operational-reports.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/operational-reports.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-operational-reports` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Receivables/payables:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sales/purchases:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tax:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Bank:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Inventory:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Assets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Expenses:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Projects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payroll:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exception reports:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-operational-reports-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `receivables-payables`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sales-purchases`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tax`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `bank`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `inventory`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `assets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `expenses`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `projects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payroll`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exception-reports`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-operational-reports` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/operational-reports.md)) |
| Capability Nuxt module skeleton | [`module-accounting-operational-reports-nuxt`](https://github.com/liberusoftware/module-accounting-operational-reports-nuxt) (`@liberusoftware/module-accounting-operational-reports-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Receivables/payables** | Expose composable and Vue 3 component for `receivables/payables` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/operational-reports.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Sales/purchases** | Expose composable and Vue 3 component for `sales/purchases` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/operational-reports.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Tax** | Expose composable and Vue 3 component for `tax` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/operational-reports.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Bank** | Expose composable and Vue 3 component for `bank` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/operational-reports.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Inventory** | Expose composable and Vue 3 component for `inventory` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/operational-reports.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Assets** | Expose composable and Vue 3 component for `assets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/operational-reports.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Expenses** | Expose composable and Vue 3 component for `expenses` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/operational-reports.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Projects** | Expose composable and Vue 3 component for `projects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/operational-reports.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Payroll** | Expose composable and Vue 3 component for `payroll` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/operational-reports.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Exception reports** | Expose composable and Vue 3 component for `exception reports` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/operational-reports.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ReportQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Queries/ReportQuery.php) | `public function paginate(?int $teamId = null, ?string $category = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function exceptions(?int $teamId = null): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GenerateReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Actions/GenerateReport.php) | `public function handle(array $attributes, array $rows = [], array $exceptions = []): ReportRun` |
| [PublishReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Actions/PublishReport.php) | `public function handle(ReportRun $run, int $actorId): ReportRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReportAudit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportAudit.php) | `run_id`, `event_type`, `actor_id`, `payload`, `payload_hash`, `created_at` |
| [ReportException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportException.php) | `run_id`, `exception_key`, `severity`, `message`, `source_type`, `source_id`, `status`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [ReportRow.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportRow.php) | `run_id`, `row_key`, `label`, `source_type`, `source_id`, `amount`, `currency`, `state`, `dimensions`, `payload` |
| [ReportRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportRun.php) | `team_id`, `report_key`, `name`, `category`, `period_start`, `period_end`, `currency`, `status`, `filters`, `summary`, `source_hash`, `requested_by`, `published_by`, `published_at`, `failure_message`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [OperationalReportsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports-api/src/Http/Controllers/OperationalReportsController.php) | `public function index(Request $request, ReportQuery $query): mixed`<br>`public function store(Request $request, GenerateReport $action): JsonResponse`<br>`public function show(ReportRun $reportRun): ReportResource`<br>`public function publish(Request $request, ReportRun $reportRun, PublishReport $action): ReportResource`<br>`public function exceptions(Request $request, ReportQuery $query): mixed` |

**Observed route declarations:**

[modules/accounting-operational-reports-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/operational-reports')->group(function (): void {
Route::get('/', [OperationalReportsController::class, 'index'])->name('accounting.operational-reports.list');
Route::post('/', [OperationalReportsController::class, 'store'])->name('accounting.operational-reports.create');
Route::get('/exceptions', [OperationalReportsController::class, 'exceptions'])->name('accounting.operational-reports.exceptions');
Route::get('/{reportRun}', [OperationalReportsController::class, 'show'])->name('accounting.operational-reports.show');
Route::post('/{reportRun}/publish', [OperationalReportsController::class, 'publish'])->name('accounting.operational-reports.publish');
```
<!-- layer-implementation-plan:end -->
