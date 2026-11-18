# Billing: Module Billing Reporting Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-reporting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-module-billing-reporting-nuxt`
**Matching domain module:** `module-billing-reporting`
**Application:** Billing
**Source feature:** [Module Billing Reporting](../features/module-billing-reporting.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-billing-reporting.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-billing-reporting` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **MRR/ARR:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Churn:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Aging:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Revenue:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tax:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Usage:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provisioning:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Collection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider metrics:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-module-billing-reporting-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `mrr-arr`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `churn`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `aging`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `revenue`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tax`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `usage`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provisioning`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `collection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provider-metrics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-billing-reporting` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-reporting.md)) |
| Capability Nuxt module skeleton | [`module-billing-reporting-nuxt`](https://github.com/liberusoftware/module-billing-reporting-nuxt) (`@liberusoftware/module-billing-reporting-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **MRR/ARR** | Expose composable and Vue 3 component for `mrr/arr` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Churn** | Expose composable and Vue 3 component for `churn` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Aging** | Expose composable and Vue 3 component for `aging` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Revenue** | Expose composable and Vue 3 component for `revenue` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Tax** | Expose composable and Vue 3 component for `tax` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Usage** | Expose composable and Vue 3 component for `usage` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Provisioning** | Expose composable and Vue 3 component for `provisioning` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Collection** | Expose composable and Vue 3 component for `collection` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Provider metrics** | Expose composable and Vue 3 component for `provider metrics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-billing-reporting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListMetricSnapshots.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Queries/ListMetricSnapshots.php) | `public function execute(int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListReportingMetrics.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Queries/ListReportingMetrics.php) | `public function execute(int $teamId, ?string $metric = null, int $perPage = 25): LengthAwarePaginator` |
| [ListReportingRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Queries/ListReportingRecords.php) | `public function handle(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CalculateReportingMetric.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/CalculateReportingMetric.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(int $teamId, string $metric, CarbonImmutable $periodStart, CarbonImmutable $periodEnd, ?string $currency = null): array` |
| [CreateMetricSnapshot.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/CreateMetricSnapshot.php) | `public function handle(int $teamId, array $attributes): MetricSnapshot` |
| [ExportReportingMetrics.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/ExportReportingMetrics.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(int $teamId, ?string $metric = null): string` |
| [GenerateCustomerBillingSummary.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/GenerateCustomerBillingSummary.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(int $teamId, int $customerId, ?string $currency = null): array` |
| [RecordReportingMetric.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/RecordReportingMetric.php) | `public function execute(int $teamId, array $attributes): ReportingMetric` |
| [MetricSnapshotPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Policies/MetricSnapshotPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, MetricSnapshot $record): bool`<br>`public function update(?Authenticatable $user, MetricSnapshot $record): bool` |
| [ReportingMetricPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Policies/ReportingMetricPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MetricSnapshot.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Models/MetricSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReportingMetric.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Models/ReportingMetric.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReportingController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-api/src/Http/Controllers/ReportingController.php) | `public function metrics(Request $request, ListReportingMetrics $metrics): JsonResponse`<br>`public function exportMetrics(Request $request, ExportReportingMetrics $export): Response`<br>`public function recordMetric(Request $request, RecordReportingMetric $record): JsonResponse`<br>`public function calculateMetric(Request $request, CalculateReportingMetric $calculate, RecordReportingMetric $record): JsonResponse`<br>`public function snapshots(Request $request, ListMetricSnapshots $snapshots): JsonResponse`<br>`public function customerSummary(Request $request, GenerateCustomerBillingSummary $summary, int $customer): JsonResponse`<br>`public function createSnapshot(Request $request, CreateMetricSnapshot $create): JsonResponse`<br>`public function snapshot(Request $request, int $record): JsonResponse` |
| [ReportingMetricController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-api/src/Http/Controllers/ReportingMetricController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, RecordReportingMetric $record): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-reporting-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.reporting.read'])->prefix('api/v1/billing/reporting/metrics')->group(function (): void {
Route::get('/', [ReportingController::class, 'metrics'])->name('billing.reporting.metrics.index');
Route::get('/export', [ReportingController::class, 'exportMetrics'])->name('billing.reporting.metrics.export');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.reporting.write', 'idempotency'])->prefix('api/v1/billing/reporting/metrics')->group(function (): void {
Route::post('/', [ReportingController::class, 'recordMetric'])->name('billing.reporting.metrics.store');
Route::post('/calculate', [ReportingController::class, 'calculateMetric'])->name('billing.reporting.metrics.calculate');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.reporting.read'])->prefix('api/v1/billing/reporting')->group(function (): void {
Route::get('/customers/{customer}/summary', [ReportingController::class, 'customerSummary'])->whereNumber('customer')->name('billing.reporting.customers.summary');
Route::get('/', [ReportingController::class, 'snapshots'])->name('billing.reporting.snapshots.index');
Route::get('/{record}', [ReportingController::class, 'snapshot'])->whereNumber('record')->name('billing.reporting.snapshots.show');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.reporting.write', 'idempotency'])->prefix('api/v1/billing/reporting')->group(function (): void {
Route::post('/snapshots', [ReportingController::class, 'createSnapshot'])->name('billing.reporting.snapshots.store');
```
<!-- layer-implementation-plan:end -->
