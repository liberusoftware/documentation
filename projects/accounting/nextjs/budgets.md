# Budgets: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-budgets`.

**Proposed design identifier:** `module-accounting-budgets-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/budgets.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-budgets](../../../modules/source/liberusoftware--module-accounting-budgets.md) |
| API | [liberusoftware/module-accounting-budgets-api](../../../modules/source/liberusoftware--module-accounting-budgets-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Annual/rolling budgets | A focused authorized view or workflow section for annual/rolling budgets; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Accounts/dimensions/projects | A focused authorized view or workflow section for accounts/dimensions/projects; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Imports | A focused authorized view or workflow section for imports; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Versions | A focused authorized view or workflow section for versions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approvals | A focused authorized view or workflow section for approvals; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Phasing | A focused authorized view or workflow section for phasing; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Actual comparison | A focused authorized view or workflow section for actual comparison; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Revisions | A focused authorized view or workflow section for revisions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [BudgetQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Queries/BudgetQuery.php) | `public function paginate(int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddBudgetLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/AddBudgetLine.php) | `public function handle(Budget $budget, array $attributes): BudgetLine` |
| [ApproveBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/ApproveBudget.php) | `public function handle(Budget $budget, int $actorId): Budget` |
| [CreateBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/CreateBudget.php) | `public function handle(array $attributes): Budget` |
| [ReviseBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/ReviseBudget.php) | `public function handle(Budget $budget, array $attributes): Budget` |
| [SubmitBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/SubmitBudget.php) | `public function handle(Budget $budget, int $actorId): Budget` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Budget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Models/Budget.php) | `team_id`, `name`, `period_start`, `period_end`, `currency`, `status`, `version`, `notes`, `metadata`, `submitted_by`, `approved_by`, `approved_at`, `rejected_at` |
| [BudgetLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Models/BudgetLine.php) | `budget_id`, `account_id`, `project_id`, `dimensions`, `planned_amount`, `phases`, `actual_amount`, `notes` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-budgets-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/budgets')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [BudgetsController::class, 'index'])->middleware('ability:accounting.budgets.read');
Route::post('/', [BudgetsController::class, 'store'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/submit', [BudgetsController::class, 'submit'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/lines', [BudgetsController::class, 'addLine'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/approve', [BudgetsController::class, 'approve'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/revise', [BudgetsController::class, 'revise'])->middleware('ability:accounting.budgets.write');
Route::get('/{budget}', [BudgetsController::class, 'show'])->middleware('ability:accounting.budgets.read');
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
