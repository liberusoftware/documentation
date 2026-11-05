# Leases: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-leases`.

**Proposed design identifier:** `module-accounting-leases-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/leases.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-leases](../../../modules/source/liberusoftware--module-accounting-leases.md) |
| API | [liberusoftware/module-accounting-leases-api](../../../modules/source/liberusoftware--module-accounting-leases-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Lease records | A focused authorized view or workflow section for lease records; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Payment schedules | A focused authorized view or workflow section for payment schedules; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Right-of-use assets | A focused authorized view or workflow section for right-of-use assets; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Liabilities | A focused authorized view or workflow section for liabilities; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Interest/depreciation | A focused authorized view or workflow section for interest/depreciation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Modifications | A focused authorized view or workflow section for modifications; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Disclosures (optional) | A focused authorized view or workflow section for disclosures (optional); define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [LeaseQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Queries/LeaseQuery.php) | `public function leases(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function disclosure(Lease $lease): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateDisclosure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/CreateDisclosure.php) | `public function handle(Lease $lease, string $asOfDate): LeaseDisclosure` |
| [CreateLease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/CreateLease.php) | `public function handle(array $attributes): Lease` |
| [GenerateSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/GenerateSchedule.php) | `public function handle(Lease $lease): Lease` |
| [ModifyLease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/ModifyLease.php) | `public function handle(Lease $lease, array $attributes): Lease` |
| [PostPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Actions/PostPayment.php) | `public function handle(LeasePayment $payment): LeasePayment` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Lease.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/Lease.php) | `team_id`, `lease_ref`, `name`, `lessor_ref`, `asset_ref`, `commencement_date`, `end_date`, `currency`, `payment_amount`, `payment_frequency`, `interest_rate`, `discount_rate`, `useful_life_months`, `status`, `right_of_use_asset`, `lease_liability`, `accumulated_depreciation`, `metadata` |
| [LeaseDisclosure.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeaseDisclosure.php) | `lease_id`, `as_of_date`, `remaining_liability`, `current_liability`, `non_current_liability`, `future_payments`, `notes`, `metadata` |
| [LeaseModification.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeaseModification.php) | `lease_id`, `modification_ref`, `effective_date`, `kind`, `old_term_end`, `new_term_end`, `old_payment_amount`, `new_payment_amount`, `adjustment_amount`, `reason`, `metadata` |
| [LeasePayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases/src/Models/LeasePayment.php) | `lease_id`, `payment_ref`, `due_date`, `amount`, `principal_amount`, `interest_amount`, `depreciation_amount`, `status`, `posted_at`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-leases-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-leases-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/leases')->group(function (): void {
Route::get('/', [LeasesController::class, 'index'])->name('accounting.leases.list');
Route::post('/', [LeasesController::class, 'store'])->name('accounting.leases.create');
Route::get('/{lease}', [LeasesController::class, 'show'])->name('accounting.leases.show');
Route::post('/{lease}/schedule', [LeasesController::class, 'schedule'])->name('accounting.leases.schedule');
Route::post('/{lease}/modify', [LeasesController::class, 'modify'])->name('accounting.leases.modify');
Route::post('/{lease}/disclosure', [LeasesController::class, 'disclosure'])->name('accounting.leases.disclosure');
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
