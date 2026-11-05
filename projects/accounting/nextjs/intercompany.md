# Intercompany: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-intercompany`.

**Proposed design identifier:** `module-accounting-intercompany-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/intercompany.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-intercompany](../../../modules/source/liberusoftware--module-accounting-intercompany.md) |
| API | [liberusoftware/module-accounting-intercompany-api](../../../modules/source/liberusoftware--module-accounting-intercompany-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Counterparties | A focused authorized view or workflow section for counterparties; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Trading rules | A focused authorized view or workflow section for trading rules; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Paired transactions | A focused authorized view or workflow section for paired transactions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Confirmations | A focused authorized view or workflow section for confirmations; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Settlement | A focused authorized view or workflow section for settlement; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Differences | A focused authorized view or workflow section for differences; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Transfer-pricing evidence | A focused authorized view or workflow section for transfer-pricing evidence; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Reconciliation | A focused authorized view or workflow section for reconciliation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [IntercompanyQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Queries/IntercompanyQuery.php) | `public function paginate(?int $teamId = null, ?TransactionStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function reconciliationSummary(IntercompanyTransaction $transaction): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddTransferPricingEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/AddTransferPricingEvidence.php) | `public function handle(IntercompanyTransaction $transaction, array $a): TransferPricingEvidence` |
| [ConfigureTradingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/ConfigureTradingRule.php) | `public function handle(IntercompanyCounterparty $counterparty, array $a): TradingRule` |
| [ConfirmTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/ConfirmTransaction.php) | `public function handle(IntercompanyTransaction $transaction, string $entity, bool $confirmed, ?string $comment = null): IntercompanyTransaction` |
| [CreateCounterparty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/CreateCounterparty.php) | `public function handle(array $a): IntercompanyCounterparty` |
| [CreateTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/CreateTransaction.php) | `public function handle(IntercompanyCounterparty $counterparty, array $a): IntercompanyTransaction` |
| [ReconcileIntercompany.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/ReconcileIntercompany.php) | `public function handle(array $a): IntercompanyReconciliation` |
| [RecordDifference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/RecordDifference.php) | `public function handle(IntercompanyTransaction $transaction, array $a): IntercompanyDifference` |
| [SettleTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/SettleTransaction.php) | `public function handle(IntercompanyTransaction $transaction, array $a): IntercompanyTransaction` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [IntercompanyConfirmation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyConfirmation.php) | `transaction_id`, `entity_ref`, `status`, `confirmed_amount`, `comment`, `actor_ref`, `confirmed_at`, `metadata` |
| [IntercompanyCounterparty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyCounterparty.php) | `team_id`, `entity_ref`, `counterparty_ref`, `name`, `default_currency`, `active`, `metadata` |
| [IntercompanyDifference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyDifference.php) | `transaction_id`, `difference_ref`, `amount`, `reason`, `status`, `actor_ref`, `resolved_at`, `metadata` |
| [IntercompanyReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyReconciliation.php) | `team_id`, `reconciliation_ref`, `period_ref`, `entity_ref`, `counterparty_ref`, `transaction_count`, `source_total`, `counterparty_total`, `difference_total`, `status`, `actor_ref`, `reconciled_at`, `metadata` |
| [IntercompanySettlement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanySettlement.php) | `transaction_id`, `settlement_ref`, `amount`, `currency`, `settled_at`, `source_ref`, `metadata` |
| [IntercompanyTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyTransaction.php) | `team_id`, `transaction_ref`, `counterparty_id`, `source_entity_ref`, `target_entity_ref`, `transaction_type`, `description`, `amount`, `currency`, `status`, `transaction_date`, `metadata` |
| [TradingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/TradingRule.php) | `counterparty_id`, `rule_ref`, `description`, `pricing_method`, `markup_percent`, `currency`, `active`, `metadata` |
| [TransferPricingEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/TransferPricingEvidence.php) | `transaction_id`, `evidence_ref`, `kind`, `file_ref`, `description`, `arm_length_value`, `currency`, `captured_at`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-intercompany-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/intercompany')->group(function (): void {
Route::get('/', [IntercompanyController::class, 'index'])->name('accounting.intercompany.list');
Route::post('/counterparties', [IntercompanyController::class, 'counterparty'])->name('accounting.intercompany.counterparty');
Route::post('/counterparties/{counterparty}/rules', [IntercompanyController::class, 'rule'])->name('accounting.intercompany.rule');
Route::post('/counterparties/{counterparty}/transactions', [IntercompanyController::class, 'store'])->name('accounting.intercompany.create');
Route::get('/transactions/{transaction}', [IntercompanyController::class, 'show'])->name('accounting.intercompany.show');
Route::post('/transactions/{transaction}/confirm', [IntercompanyController::class, 'confirm'])->name('accounting.intercompany.confirm');
Route::post('/transactions/{transaction}/settle', [IntercompanyController::class, 'settle'])->name('accounting.intercompany.settle');
Route::post('/transactions/{transaction}/differences', [IntercompanyController::class, 'difference'])->name('accounting.intercompany.difference');
Route::post('/transactions/{transaction}/evidence', [IntercompanyController::class, 'evidence'])->name('accounting.intercompany.evidence');
Route::get('/transactions/{transaction}/summary', [IntercompanyController::class, 'summary'])->name('accounting.intercompany.summary');
Route::post('/reconciliations', [IntercompanyController::class, 'reconcile'])->name('accounting.intercompany.reconcile');
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
