# Financial Master Data: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-financial-master-data`.

**Proposed design identifier:** `module-accounting-financial-master-data-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/financial-master-data.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-financial-master-data](../../../modules/source/liberusoftware--module-accounting-financial-master-data.md) |
| API | [liberusoftware/module-accounting-financial-master-data-api](../../../modules/source/liberusoftware--module-accounting-financial-master-data-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Customers | A focused authorized view or workflow section for customers; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Suppliers | A focused authorized view or workflow section for suppliers; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Items/services | A focused authorized view or workflow section for items/services; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Accounts | A focused authorized view or workflow section for accounts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Tax profiles | A focused authorized view or workflow section for tax profiles; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Payment terms | A focused authorized view or workflow section for payment terms; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Addresses | A focused authorized view or workflow section for addresses; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Bank details references | A focused authorized view or workflow section for bank details references; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Lifecycle | A focused authorized view or workflow section for lifecycle; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Deduplication | A focused authorized view or workflow section for deduplication; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [FindDuplicateParties.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Queries/FindDuplicateParties.php) | `public function handle(int $legalEntityId, ?string $type = null): Collection` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [ArchiveParty.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Actions/ArchiveParty.php) | `public function handle(Party $party): Party` |
| [MergeDuplicateParties.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Actions/MergeDuplicateParties.php) | `public function handle(Party $survivor, Party $duplicate): Party` |
| [SaveParty.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Actions/SaveParty.php) | `public function handle(array $attributes, ?Party $party = null): Party` |
| [SaveReferenceData.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Actions/SaveReferenceData.php) | `public function handle(string $modelClass, array $attributes, ?Model $record = null): Model` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Address.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/Address.php) | `party_id`, `kind`, `line_one`, `line_two`, `city`, `region`, `postal_code`, `country_code`, `is_primary`, `metadata` |
| [BankDetailReference.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/BankDetailReference.php) | `party_id`, `label`, `account_name`, `bank_name`, `country_code`, `currency_code`, `masked_account`, `credential_reference`, `is_primary`, `status`, `metadata` |
| [ItemService.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/ItemService.php) | `legal_entity_id`, `sku`, `name`, `description`, `kind`, `unit`, `sales_price`, `purchase_price`, `tax_profile_id`, `status`, `metadata` |
| [Party.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/Party.php) | `legal_entity_id`, `type`, `reference`, `name`, `email`, `phone`, `tax_identifier`, `payment_term_id`, `credit_limit`, `status`, `metadata` |
| [PaymentTerm.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/PaymentTerm.php) | `legal_entity_id`, `code`, `name`, `days`, `status`, `metadata` |
| [TaxProfile.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data/src/Models/TaxProfile.php) | `legal_entity_id`, `code`, `name`, `rate`, `inclusive`, `recoverable`, `status`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-financial-master-data-api/routes/api.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-master-data-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/financial-master-data')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('parties', [PartyController::class, 'index'])->middleware('ability:accounting.master-data.read');
Route::get('parties/{party}', [PartyController::class, 'show'])->middleware('ability:accounting.master-data.read');
Route::post('parties', [PartyController::class, 'store'])->middleware('ability:accounting.master-data.write');
Route::delete('parties/{party}', [PartyController::class, 'destroy'])->middleware('ability:accounting.master-data.write');
Route::get('parties/{party}/'.$detail, [PartyDetailController::class, 'index'])->defaults('detail', $detail)->middleware('ability:accounting.master-data.read');
Route::post('parties/{party}/'.$detail, [PartyDetailController::class, 'store'])->defaults('detail', $detail)->middleware('ability:accounting.master-data.write');
Route::delete('parties/{party}/'.$detail.'/{record}', [PartyDetailController::class, 'destroy'])->defaults('detail', $detail)->middleware('ability:accounting.master-data.write');
Route::get($resource, [ReferenceDataController::class, 'index'])->defaults('resource', $resource)->middleware('ability:accounting.master-data.read');
Route::get($resource.'/{record}', [ReferenceDataController::class, 'show'])->defaults('resource', $resource)->middleware('ability:accounting.master-data.read');
Route::post($resource, [ReferenceDataController::class, 'store'])->defaults('resource', $resource)->middleware('ability:accounting.master-data.write');
Route::delete($resource.'/{record}', [ReferenceDataController::class, 'destroy'])->defaults('resource', $resource)->middleware('ability:accounting.master-data.write');
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
