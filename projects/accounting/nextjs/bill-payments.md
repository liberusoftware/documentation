# Bill Payments: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-bill-payments`.

**Proposed design identifier:** `module-accounting-bill-payments-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/bill-payments.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-bill-payments](../../../modules/source/liberusoftware--module-accounting-bill-payments.md) |
| API | [liberusoftware/module-accounting-bill-payments-api](../../../modules/source/liberusoftware--module-accounting-bill-payments-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Payment proposals | A focused authorized view or workflow section for payment proposals; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Due-date/discount optimization | A focused authorized view or workflow section for due-date/discount optimization; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Bank details validation | A focused authorized view or workflow section for bank details validation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Maker-checker approval | A focused authorized view or workflow section for maker-checker approval; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Files/APIs | A focused authorized view or workflow section for files/apis; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Remittances | A focused authorized view or workflow section for remittances; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Status | A focused authorized view or workflow section for status; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [BillPaymentOptimizationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Queries/BillPaymentOptimizationQuery.php) | `public function handle(BillPaymentProposal $payment): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ApproveBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/ApproveBillPayment.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [CreateBillPaymentProposal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/CreateBillPaymentProposal.php) | `public function handle(array $attributes): BillPaymentProposal` |
| [MarkBillPaymentPaid.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/MarkBillPaymentPaid.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [RejectBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/RejectBillPayment.php) | `public function handle(BillPaymentProposal $payment, string $reason): BillPaymentProposal` |
| [RequestBillPaymentApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/RequestBillPaymentApproval.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [SubmitBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/SubmitBillPayment.php) | `public function handle(BillPaymentProposal $payment, PaymentProviderAdapter $adapter): BillPaymentProposal` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [BillPaymentProposal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Models/BillPaymentProposal.php) | `team_id`, `supplier_id`, `bill_reference`, `amount`, `currency`, `due_date`, `discount_date`, `discount_rate`, `payment_date`, `bank_details`, `provider`, `provider_connection_id`, `payment_payload`, `idempotency_key`, `status`, `requested_by`, `approved_by`, `approved_at`, `submitted_at`, `paid_at`, `rejected_at`, `failure_code`, `failure_message`, `provider_reference`, `provider_result`, `remittance_reference`, `remittance_sent_at`, `metadata` |
| [Bill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Models/Bill.php) | `vendor_id`, `bill_number`, `bill_date`, `due_date`, `subtotal_amount`, `tax_amount`, `total_amount`, `amount_paid`, `tax_rate_id`, `status`, `payment_status`, `purchase_order_id`, `reference_number`, `notes`, `document_path`, `approved_by`, `approved_at`, `approval_status`, `rejection_reason`, `team_id`, `is_recurring`, `recurrence_frequency`, `recurrence_start`, `recurrence_end`, `last_generated`, `qbo_id`, `qbo_sync_token`, `xero_id`, `sage_id` |
| [BillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Models/BillPayment.php) | `bill_id`, `payment_date`, `amount`, `payment_method`, `reference_number`, `bank_account_id`, `notes` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-bill-payments-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/bill-payments')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [BillPaymentController::class, 'index'])->middleware('ability:accounting.bill-payments.read');
Route::post('/', [BillPaymentController::class, 'store'])->middleware('ability:accounting.bill-payments.write');
Route::get('/{payment}', [BillPaymentController::class, 'show'])->middleware('ability:accounting.bill-payments.read');
Route::get('/{payment}/optimization', [BillPaymentController::class, 'optimization'])->middleware('ability:accounting.bill-payments.read');
Route::post('/{payment}/request-approval', [BillPaymentController::class, 'requestApproval'])->middleware('ability:accounting.bill-payments.write');
Route::post('/{payment}/approve', [BillPaymentController::class, 'approve'])->middleware('ability:accounting.bill-payments.write');
Route::post('/{payment}/reject', [BillPaymentController::class, 'reject'])->middleware('ability:accounting.bill-payments.write');
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
