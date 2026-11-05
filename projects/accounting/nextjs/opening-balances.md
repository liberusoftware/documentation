# Opening Balances: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-opening-balances`.

**Proposed design identifier:** `module-accounting-opening-balances-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/opening-balances.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-opening-balances](../../../modules/source/liberusoftware--module-accounting-opening-balances.md) |
| API | [liberusoftware/module-accounting-opening-balances-api](../../../modules/source/liberusoftware--module-accounting-opening-balances-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Migration date | A focused authorized view or workflow section for migration date; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Account/customer/supplier/bank/item balances | A focused authorized view or workflow section for account/customer/supplier/bank/item balances; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Outstanding documents | A focused authorized view or workflow section for outstanding documents; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Validation | A focused authorized view or workflow section for validation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Approval | A focused authorized view or workflow section for approval; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Reconciliation | A focused authorized view or workflow section for reconciliation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [OpeningBalanceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Queries/OpeningBalanceQuery.php) | `public function paginate(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ApproveOpeningBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Actions/ApproveOpeningBalances.php) | `public function handle(OpeningBalanceBatch $batch, int $actorId): OpeningBalanceBatch` |
| [CreateOpeningBalanceBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Actions/CreateOpeningBalanceBatch.php) | `public function handle(array $attributes, array $entries): OpeningBalanceBatch` |
| [ReconcileOpeningBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Actions/ReconcileOpeningBalances.php) | `public function handle(OpeningBalanceBatch $batch, array $actuals): OpeningBalanceBatch` |
| [ValidateOpeningBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Actions/ValidateOpeningBalances.php) | `public function handle(OpeningBalanceBatch $batch): OpeningBalanceBatch` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [OpeningBalanceAudit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Models/OpeningBalanceAudit.php) | `batch_id`, `event_type`, `actor_id`, `payload`, `payload_hash`, `created_at` |
| [OpeningBalanceBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Models/OpeningBalanceBatch.php) | `team_id`, `batch_ref`, `migration_date`, `currency`, `status`, `source_hash`, `idempotency_key`, `summary`, `failure_message`, `requested_by`, `approved_by`, `approved_at`, `metadata` |
| [OpeningBalanceEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Models/OpeningBalanceEntry.php) | `batch_id`, `balance_type`, `reference_type`, `reference_id`, `document_ref`, `document_date`, `due_date`, `currency`, `debit_amount`, `credit_amount`, `status`, `description`, `metadata` |
| [OpeningBalanceReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Models/OpeningBalanceReconciliation.php) | `batch_id`, `entry_id`, `expected_amount`, `actual_amount`, `variance`, `status`, `external_ref`, `notes`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-opening-balances-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/opening-balances')->group(function (): void {
Route::get('/', [OpeningBalancesController::class, 'index'])->name('accounting.opening-balances.list');
Route::post('/', [OpeningBalancesController::class, 'store'])->name('accounting.opening-balances.create');
Route::get('/{openingBalance}', [OpeningBalancesController::class, 'show'])->name('accounting.opening-balances.show');
Route::post('/{openingBalance}/validate', [OpeningBalancesController::class, 'validateBatch'])->name('accounting.opening-balances.validate');
Route::post('/{openingBalance}/approve', [OpeningBalancesController::class, 'approve'])->name('accounting.opening-balances.approve');
Route::post('/{openingBalance}/reconcile', [OpeningBalancesController::class, 'reconcile'])->name('accounting.opening-balances.reconcile');
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
