# Management Reporting: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-management-reporting`.

**Proposed design identifier:** `module-accounting-management-reporting-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/management-reporting.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-management-reporting](../../../modules/source/liberusoftware--module-accounting-management-reporting.md) |
| API | [liberusoftware/module-accounting-management-reporting-api](../../../modules/source/liberusoftware--module-accounting-management-reporting-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Report packs | A focused authorized view or workflow section for report packs; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Narratives | A focused authorized view or workflow section for narratives; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Charts | A focused authorized view or workflow section for charts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Schedules | A focused authorized view or workflow section for schedules; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Review | A focused authorized view or workflow section for review; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approval | A focused authorized view or workflow section for approval; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| PDF/spreadsheet delivery | A focused authorized view or workflow section for pdf/spreadsheet delivery; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Archive | A focused authorized view or workflow section for archive; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ReportQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Queries/ReportQuery.php) | `public function packs(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function summary(ReportPack $report): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddReportContent.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/AddReportContent.php) | `public function narrative(ReportPack $report, array $attributes): ReportNarrative`<br>`public function chart(ReportPack $report, array $attributes): ReportChart` |
| [ArchiveReport.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/ArchiveReport.php) | `public function handle(ReportPack $report): ReportPack` |
| [CreateReportPack.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/CreateReportPack.php) | `public function handle(array $attributes): ReportPack` |
| [DeliverReport.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/DeliverReport.php) | `public function handle(ReportPack $report, string $format, array $attributes = []): ReportDelivery` |
| [ReviewReport.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/ReviewReport.php) | `public function handle(ReportPack $report, string $actor, string $decision, ?string $comment = null): ReportPack` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [ReportChart.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportChart.php) | `report_pack_id`, `chart_ref`, `title`, `chart_type`, `data_source`, `series`, `options`, `metadata` |
| [ReportDelivery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportDelivery.php) | `report_pack_id`, `format`, `file_ref`, `status`, `recipients`, `checksum`, `delivered_at`, `failure_message`, `metadata` |
| [ReportNarrative.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportNarrative.php) | `report_pack_id`, `section_ref`, `title`, `body`, `author_ref`, `version`, `metadata` |
| [ReportPack.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportPack.php) | `team_id`, `report_ref`, `name`, `period_start`, `period_end`, `currency`, `status`, `version`, `owner_ref`, `approved_by`, `approved_at`, `delivered_at`, `archived_at`, `metadata` |
| [ReportReview.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportReview.php) | `report_pack_id`, `actor_ref`, `decision`, `comment`, `reviewed_at`, `metadata` |
| [ReportSchedule.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportSchedule.php) | `report_pack_id`, `frequency`, `timezone`, `recipients`, `next_run_at`, `active`, `last_run_at`, `failure_message`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-management-reporting-api/routes/api.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/management-reporting')->group(function (): void {
Route::get('/packs', [ManagementReportingController::class, 'index'])->name('accounting.management-reporting.list');
Route::post('/packs', [ManagementReportingController::class, 'store'])->name('accounting.management-reporting.create');
Route::get('/packs/{reportPack}', [ManagementReportingController::class, 'show'])->name('accounting.management-reporting.show');
Route::post('/packs/{reportPack}/review', [ManagementReportingController::class, 'review'])->name('accounting.management-reporting.review');
Route::post('/packs/{reportPack}/deliver', [ManagementReportingController::class, 'deliver'])->name('accounting.management-reporting.deliver');
Route::post('/packs/{reportPack}/archive', [ManagementReportingController::class, 'archive'])->name('accounting.management-reporting.archive');
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
