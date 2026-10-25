# KPI and Goals: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-kpi-and-goals`.

**Proposed design identifier:** `module-accounting-kpi-and-goals-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/kpi-and-goals.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-kpi-and-goals](../../../modules/source/liberusoftware--module-accounting-kpi-and-goals.md) |
| API | [liberusoftware/module-accounting-kpi-and-goals-api](../../../modules/source/liberusoftware--module-accounting-kpi-and-goals-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Governed metrics | A focused authorized view or workflow section for governed metrics; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Targets | A focused authorized view or workflow section for targets; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Owners | A focused authorized view or workflow section for owners; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Thresholds | A focused authorized view or workflow section for thresholds; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Periods | A focused authorized view or workflow section for periods; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Alerts | A focused authorized view or workflow section for alerts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Commentary | A focused authorized view or workflow section for commentary; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| History | A focused authorized view or workflow section for history; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [KpiQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Queries/KpiQuery.php) | `public function goals(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function progress(KpiGoal $goal): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddCommentary.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/AddCommentary.php) | `public function handle(KpiGoal $goal, string $actor, string $body, ?string $period = null): KpiCommentary` |
| [CreateGoal.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/CreateGoal.php) | `public function handle(KpiMetric $metric, array $attributes): KpiGoal` |
| [CreateMetric.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/CreateMetric.php) | `public function handle(array $attributes): KpiMetric` |
| [RecordMeasurement.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/RecordMeasurement.php) | `public function handle(KpiGoal $goal, array $attributes): KpiMeasurement` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [KpiAlert.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiAlert.php) | `team_id`, `goal_id`, `measurement_id`, `severity`, `status`, `message`, `triggered_at`, `acknowledged_by`, `resolved_at`, `metadata` |
| [KpiCommentary.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiCommentary.php) | `goal_id`, `actor_ref`, `body`, `period_ref`, `metadata` |
| [KpiGoal.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiGoal.php) | `team_id`, `metric_id`, `goal_ref`, `name`, `owner_ref`, `period_start`, `period_end`, `baseline`, `target`, `warning_threshold`, `critical_threshold`, `status`, `metadata` |
| [KpiMeasurement.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiMeasurement.php) | `team_id`, `metric_id`, `goal_id`, `period_ref`, `measured_on`, `value`, `progress`, `source_ref`, `metadata` |
| [KpiMetric.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiMetric.php) | `team_id`, `metric_ref`, `name`, `description`, `unit`, `direction`, `source_contract`, `formula`, `owner_ref`, `active`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-kpi-and-goals-api/routes/api.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/kpi-and-goals')->group(function (): void {
Route::get('/goals', [KpiController::class, 'index'])->name('accounting.kpi-and-goals.list');
Route::post('/metrics', [KpiController::class, 'metric'])->name('accounting.kpi-and-goals.metric');
Route::post('/metrics/{metric}/goals', [KpiController::class, 'goal'])->name('accounting.kpi-and-goals.goal');
Route::get('/goals/{goal}', [KpiController::class, 'show'])->name('accounting.kpi-and-goals.show');
Route::post('/goals/{goal}/measurements', [KpiController::class, 'measurement'])->name('accounting.kpi-and-goals.measurement');
Route::post('/goals/{goal}/commentary', [KpiController::class, 'commentary'])->name('accounting.kpi-and-goals.commentary');
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
