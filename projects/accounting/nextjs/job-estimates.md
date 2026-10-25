# Job Estimates: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-job-estimates`.

**Proposed design identifier:** `module-accounting-job-estimates-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/job-estimates.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-job-estimates](../../../modules/source/liberusoftware--module-accounting-job-estimates.md) |
| API | [liberusoftware/module-accounting-job-estimates-api](../../../modules/source/liberusoftware--module-accounting-job-estimates-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Cost/revenue estimates | A focused authorized view or workflow section for cost/revenue estimates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Quantities/rates | A focused authorized view or workflow section for quantities/rates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Versions | A focused authorized view or workflow section for versions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approvals | A focused authorized view or workflow section for approvals; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Actual comparison | A focused authorized view or workflow section for actual comparison; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Estimate-at-completion | A focused authorized view or workflow section for estimate-at-completion; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [JobEstimateQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Queries/JobEstimateQuery.php) | `public function paginate(?int $teamId = null, ?EstimateStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function comparison(JobEstimate $estimate): array`<br>`public function estimateAtCompletion(JobEstimate $estimate): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddEstimateLine.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/AddEstimateLine.php) | `public function handle(JobEstimate $estimate, array $attributes): EstimateLine` |
| [CreateEstimate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/CreateEstimate.php) | `public function handle(array $attributes): JobEstimate` |
| [CreateVersion.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/CreateVersion.php) | `public function handle(JobEstimate $estimate, ?string $notes = null): EstimateVersion` |
| [DecideEstimate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/DecideEstimate.php) | `public function handle(JobEstimate $estimate, string $actor, bool $approved, ?string $comment = null): JobEstimate` |
| [RecordActual.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/RecordActual.php) | `public function handle(JobEstimate $estimate, array $attributes): EstimateActual` |
| [SubmitEstimate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Actions/SubmitEstimate.php) | `public function handle(JobEstimate $estimate): JobEstimate` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [EstimateActual.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateActual.php) | `estimate_id`, `version_id`, `line_ref`, `category`, `amount`, `source_ref`, `occurred_at`, `metadata` |
| [EstimateApproval.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateApproval.php) | `estimate_id`, `version_id`, `actor_ref`, `decision`, `comment`, `decided_at`, `metadata` |
| [EstimateLine.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateLine.php) | `estimate_id`, `version_id`, `line_ref`, `line_type`, `category`, `description`, `quantity`, `rate`, `amount`, `actual_amount`, `metadata` |
| [EstimateVersion.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/EstimateVersion.php) | `estimate_id`, `version_no`, `status`, `notes`, `total_cost`, `total_revenue`, `metadata` |
| [JobEstimate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates/src/Models/JobEstimate.php) | `team_id`, `estimate_ref`, `project_ref`, `title`, `currency`, `status`, `version_no`, `total_cost`, `total_revenue`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-job-estimates-api/routes/api.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-job-estimates-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/job-estimates')->group(function (): void {
Route::middleware('ability:accounting.job-estimates.read')->group(function (): void {
Route::get('/', [JobEstimatesController::class, 'index'])->name('accounting.job-estimates.list');
Route::get('/{estimate}/comparison', [JobEstimatesController::class, 'comparison'])->name('accounting.job-estimates.comparison');
Route::get('/{estimate}/eac', [JobEstimatesController::class, 'eac'])->name('accounting.job-estimates.eac');
Route::get('/{estimate}', [JobEstimatesController::class, 'show'])->name('accounting.job-estimates.show');
Route::middleware('ability:accounting.job-estimates.write')->group(function (): void {
Route::post('/', [JobEstimatesController::class, 'store'])->name('accounting.job-estimates.create');
Route::post('/{estimate}/lines', [JobEstimatesController::class, 'line'])->name('accounting.job-estimates.line');
Route::post('/{estimate}/submit', [JobEstimatesController::class, 'submit'])->name('accounting.job-estimates.submit');
Route::post('/{estimate}/decide', [JobEstimatesController::class, 'decide'])->name('accounting.job-estimates.decide');
Route::post('/{estimate}/versions', [JobEstimatesController::class, 'version'])->name('accounting.job-estimates.version');
Route::post('/{estimate}/actuals', [JobEstimatesController::class, 'actual'])->name('accounting.job-estimates.actual');
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
