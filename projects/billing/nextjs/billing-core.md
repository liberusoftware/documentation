# Billing Core: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-billing-billing-core`.

**Proposed design identifier:** `module-billing-billing-core-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/billing-core.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-billing-billing-core](../../../modules/source/liberusoftware--module-billing-billing-core.md) |
| API | [liberusoftware/module-billing-core-api](../../../modules/source/liberusoftware--module-billing-core-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Accounts | A focused authorized view or workflow section for accounts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Contacts | A focused authorized view or workflow section for contacts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Currencies | A focused authorized view or workflow section for currencies; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Tax profiles | A focused authorized view or workflow section for tax profiles; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Sequences | A focused authorized view or workflow section for sequences; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Terms | A focused authorized view or workflow section for terms; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Billing settings | A focused authorized view or workflow section for billing settings; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ListBillingAccounts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Queries/ListBillingAccounts.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListBillingRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Queries/ListBillingRecords.php) | `public function execute(string $modelClass, ?int $teamId, int $perPage = 25): LengthAwarePaginator` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CalculateTax.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CalculateTax.php) | `public function execute(int $teamId, float $amount, ?string $jurisdiction = null, ?int $customerId = null): array` |
| [ConvertCurrency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/ConvertCurrency.php) | `public function execute(int $teamId, float $amount, string $from, string $to): array` |
| [CreateBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CreateBillingAccount.php) | `public function execute(array $attributes): BillingAccount` |
| [CreateBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/CreateBillingRecord.php) | `public function execute(string $modelClass, array $attributes): Model` |
| [DeleteBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/DeleteBillingAccount.php) | `public function execute(BillingAccount $account): void` |
| [DeleteBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/DeleteBillingRecord.php) | `public function execute(Model $record, string $recordType): void` |
| [TransitionBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/TransitionBillingAccount.php) | `public function execute(BillingAccount $account, BillingAccountStatus $status): BillingAccount` |
| [UpdateBillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/UpdateBillingAccount.php) | `public function execute(BillingAccount $account, array $attributes): BillingAccount` |
| [UpdateBillingRecord.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Actions/UpdateBillingRecord.php) | `public function execute(Model $record, array $attributes): Model` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [BillingAccount.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingAccount.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingContact.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingContact.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingCurrency.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingCurrency.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingSequence.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingSetting.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingSetting.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTaxExemption.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTaxExemption.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTaxProfile.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTaxProfile.php) | No literal fillable array detected; inspect the model and API schema. |
| [BillingTerm.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/billing-core/src/Models/BillingTerm.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/module-billing-core-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-core-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.billing-core.read'])
Route::get('/', [BillingAccountController::class, 'index'])->name('accounts.index');
Route::post('/currencies/convert', [BillingCoreRecordController::class, 'convertCurrency'])->name('currencies.convert');
Route::post('/tax/calculate', [BillingCoreRecordController::class, 'calculateTax'])->name('tax.calculate');
Route::get('/{type}', [BillingCoreRecordController::class, 'index'])->whereIn('type', ['contacts', 'currencies', 'tax-profiles', 'tax-exemptions', 'sequences', 'terms', 'settings'])->name('records.index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.billing-core.write', 'idempotency'])
Route::post('/', [BillingAccountController::class, 'store'])->name('accounts.store');
Route::patch('/{account}', [BillingAccountController::class, 'update'])->whereNumber('account')->name('accounts.update');
Route::delete('/{account}', [BillingAccountController::class, 'destroy'])->whereNumber('account')->name('accounts.destroy');
Route::patch('/{account}/status', [BillingAccountController::class, 'transition'])->whereNumber('account')->name('accounts.status');
Route::post('/{type}', [BillingCoreRecordController::class, 'store'])->whereIn('type', ['contacts', 'currencies', 'tax-profiles', 'tax-exemptions', 'sequences', 'terms', 'settings'])->name('records.store');
Route::patch('/{type}/{record}', [BillingCoreRecordController::class, 'update'])->whereIn('type', ['contacts', 'currencies', 'tax-profiles', 'tax-exemptions', 'sequences', 'terms', 'settings'])->name('records.update');
Route::delete('/{type}/{record}', [BillingCoreRecordController::class, 'destroy'])->whereIn('type', ['contacts', 'currencies', 'tax-profiles', 'tax-exemptions', 'sequences', 'terms', 'settings'])->name('records.destroy');
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
