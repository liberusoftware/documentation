# Financial Statements: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-financial-statements`.

**Proposed design identifier:** `module-accounting-financial-statements-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/financial-statements.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-financial-statements](../../../modules/source/liberusoftware--module-accounting-financial-statements.md) |
| API | [liberusoftware/module-accounting-financial-statements-api](../../../modules/source/liberusoftware--module-accounting-financial-statements-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Profit and loss | A focused authorized view or workflow section for profit and loss; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Balance sheet | A focused authorized view or workflow section for balance sheet; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Cash flow | A focused authorized view or workflow section for cash flow; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Changes in equity | A focused authorized view or workflow section for changes in equity; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Comparative periods | A focused authorized view or workflow section for comparative periods; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Dimensions | A focused authorized view or workflow section for dimensions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Drill-through | A focused authorized view or workflow section for drill-through; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [StatementQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/src/Queries/StatementQuery.php) | `public function profitAndLoss(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function balanceSheet(int $bookId, string $asOf, ?array $dimensions = null): array`<br>`public function cashFlow(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function changesInEquity(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function comparative(int $bookId, string $start, string $end, string $compareStart, string $compareEnd, ?array $dimensions = null): array`<br>`public function drillThrough(int $bookId, int $accountId, string $start, string $end, ?array $dimensions = null): array` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-financial-statements-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'ability:accounting.financial-statements.read'])
Route::get('/profit-and-loss', [FinancialStatementsController::class, 'profitAndLoss'])->name('accounting.financial-statements.profit-and-loss');
Route::get('/balance-sheet', [FinancialStatementsController::class, 'balanceSheet'])->name('accounting.financial-statements.balance-sheet');
Route::get('/cash-flow', [FinancialStatementsController::class, 'cashFlow'])->name('accounting.financial-statements.cash-flow');
Route::get('/changes-in-equity', [FinancialStatementsController::class, 'equity'])->name('accounting.financial-statements.changes-in-equity');
Route::get('/comparative', [FinancialStatementsController::class, 'comparative'])->name('accounting.financial-statements.comparative');
Route::get('/drill-through', [FinancialStatementsController::class, 'drillThrough'])->name('accounting.financial-statements.drill-through');
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
