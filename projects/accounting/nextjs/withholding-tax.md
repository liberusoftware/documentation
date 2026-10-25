# Withholding Tax: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-withholding-tax`.

**Proposed design identifier:** `module-accounting-withholding-tax-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/withholding-tax.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-withholding-tax](../../../modules/source/liberusoftware--module-accounting-withholding-tax.md) |
| API | [liberusoftware/module-accounting-withholding-tax-api](../../../modules/source/liberusoftware--module-accounting-withholding-tax-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Rules | A focused authorized view or workflow section for rules; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Certificates | A focused authorized view or workflow section for certificates; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Supplier/customer deductions | A focused authorized view or workflow section for supplier/customer deductions; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Liabilities | A focused authorized view or workflow section for liabilities; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Remittance | A focused authorized view or workflow section for remittance; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Statements | A focused authorized view or workflow section for statements; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Regional filing adapters | A focused authorized view or workflow section for regional filing adapters; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CalculateWithholdingTax.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/CalculateWithholdingTax.php) | `public function handle(WithholdingTaxRule $rule, array $attributes): WithholdingTaxDeduction` |
| [CreateWithholdingTaxRule.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/CreateWithholdingTaxRule.php) | `public function handle(array $attributes): WithholdingTaxRule` |
| [RemitWithholdingTax.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Actions/RemitWithholdingTax.php) | `public function handle(WithholdingTaxLiability $liability, array $attributes): WithholdingTaxRemittance` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [WithholdingTaxCertificate.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxCertificate.php) | `team_id`, `rule_id`, `party_type`, `party_id`, `certificate_ref`, `valid_from`, `valid_until`, `status`, `metadata` |
| [WithholdingTaxDeduction.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxDeduction.php) | `team_id`, `rule_id`, `party_type`, `party_id`, `source_ref`, `currency`, `gross_amount`, `withheld_amount`, `status`, `metadata` |
| [WithholdingTaxFilingAdapter.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxFilingAdapter.php) | `team_id`, `jurisdiction`, `provider`, `status`, `configuration` |
| [WithholdingTaxLiability.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxLiability.php) | `team_id`, `deduction_id`, `amount`, `due_on`, `status`, `metadata` |
| [WithholdingTaxRemittance.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxRemittance.php) | `team_id`, `liability_id`, `amount`, `remitted_on`, `reference`, `status`, `metadata` |
| [WithholdingTaxRule.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxRule.php) | `team_id`, `code`, `name`, `jurisdiction`, `rate`, `threshold`, `effective_from`, `effective_until`, `status`, `metadata` |
| [WithholdingTaxStatement.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax/src/Models/WithholdingTaxStatement.php) | `team_id`, `jurisdiction`, `period_start`, `period_end`, `total_amount`, `status`, `payload` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-withholding-tax-api/routes/api.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-withholding-tax-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/withholding-tax')->group(function (): void {
Route::middleware('ability:accounting.withholding-tax.read')->group(function (): void {
Route::get('/rules', [WithholdingTaxController::class, 'rules']);
Route::get('/deductions', [WithholdingTaxController::class, 'deductions']);
Route::middleware('ability:accounting.withholding-tax.write')->group(function (): void {
Route::post('/rules', [WithholdingTaxController::class, 'createRule']);
Route::post('/rules/{rule}/deductions', [WithholdingTaxController::class, 'calculate']);
Route::post('/liabilities/{liability}/remit', [WithholdingTaxController::class, 'remit']);
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
