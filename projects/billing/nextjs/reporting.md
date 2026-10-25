# Reporting: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-billing-reporting`.

**Proposed design identifier:** `module-billing-reporting-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/reporting.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-billing-reporting](../../../modules/source/liberusoftware--module-billing-reporting.md) |
| API | [liberusoftware/module-billing-reporting-api](../../../modules/source/liberusoftware--module-billing-reporting-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| MRR/ARR | A focused authorized view or workflow section for mrr/arr; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Churn | A focused authorized view or workflow section for churn; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Aging | A focused authorized view or workflow section for aging; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Revenue | A focused authorized view or workflow section for revenue; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Tax | A focused authorized view or workflow section for tax; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Usage | A focused authorized view or workflow section for usage; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Provisioning | A focused authorized view or workflow section for provisioning; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Collection | A focused authorized view or workflow section for collection; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Provider metrics | A focused authorized view or workflow section for provider metrics; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ListMetricSnapshots.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Queries/ListMetricSnapshots.php) | `public function execute(int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListReportingMetrics.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Queries/ListReportingMetrics.php) | `public function execute(int $teamId, ?string $metric = null, int $perPage = 25): LengthAwarePaginator` |
| [ListReportingRecords.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Queries/ListReportingRecords.php) | `public function handle(int $teamId): Collection` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CalculateReportingMetric.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/CalculateReportingMetric.php) | `public function execute(int $teamId, string $metric, CarbonImmutable $periodStart, CarbonImmutable $periodEnd, ?string $currency = null): array` |
| [CreateMetricSnapshot.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/CreateMetricSnapshot.php) | `public function handle(int $teamId, array $attributes): MetricSnapshot` |
| [ExportReportingMetrics.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/ExportReportingMetrics.php) | `public function execute(int $teamId, ?string $metric = null): string` |
| [GenerateCustomerBillingSummary.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/GenerateCustomerBillingSummary.php) | `public function execute(int $teamId, int $customerId, ?string $currency = null): array` |
| [RecordReportingMetric.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/RecordReportingMetric.php) | `public function execute(int $teamId, array $attributes): ReportingMetric` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [MetricSnapshot.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Models/MetricSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReportingMetric.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Models/ReportingMetric.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/module-billing-reporting-api/routes/api.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-api/routes/api.php)

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

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
