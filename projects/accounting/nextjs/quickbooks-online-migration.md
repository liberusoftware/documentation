# QuickBooks Online Migration: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-quickbooks-online-migration`.

**Proposed design identifier:** `module-accounting-quickbooks-online-migration-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/quickbooks-online-migration.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-quickbooks-online-migration](../../../modules/source/liberusoftware--module-accounting-quickbooks-online-migration.md) |
| API | [liberusoftware/module-accounting-quickbooks-online-migration-api](../../../modules/source/liberusoftware--module-accounting-quickbooks-online-migration-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Chart | A focused authorized view or workflow section for chart; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Classes/locations | A focused authorized view or workflow section for classes/locations; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Contacts | A focused authorized view or workflow section for contacts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Items | A focused authorized view or workflow section for items; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Invoices/bills/credits/payments | A focused authorized view or workflow section for invoices/bills/credits/payments; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Journals | A focused authorized view or workflow section for journals; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Bank data | A focused authorized view or workflow section for bank data; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Projects | A focused authorized view or workflow section for projects; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Tax | A focused authorized view or workflow section for tax; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Attachments | A focused authorized view or workflow section for attachments; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Source IDs | A focused authorized view or workflow section for source ids; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [CreateMigrationRun.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Actions/CreateMigrationRun.php) | `public function handle(?int $connectionId, array $metadata = []): QboMigrationRun` |
| [ImportMigrationRecords.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Actions/ImportMigrationRecords.php) | `public function handle(QboMigrationRun $run, array $records): QboMigrationRun` |
| [ReconcileMigration.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Actions/ReconcileMigration.php) | `public function handle(QboMigrationRun $run): QboMigrationRun` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [QboMigrationConnection.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Models/QboMigrationConnection.php) | `team_id`, `realm_id`, `access_token`, `refresh_token`, `token_expires_at`, `status`, `last_synced_at` |
| [QboMigrationRecord.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Models/QboMigrationRecord.php) | `run_id`, `entity_type`, `source_id`, `status`, `payload`, `payload_hash`, `error_message`, `metadata` |
| [QboMigrationRun.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration/src/Models/QboMigrationRun.php) | `connection_id`, `status`, `total_records`, `imported_records`, `failed_records`, `errors`, `metadata`, `started_at`, `finished_at` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-quickbooks-online-migration-api/routes/api.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-quickbooks-online-migration-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/quickbooks-online-migration')->group(function (): void {
Route::get('/', [QboMigrationController::class, 'index']);
Route::post('/', [QboMigrationController::class, 'store']);
Route::get('/{run}', [QboMigrationController::class, 'show']);
Route::post('/{run}/reconcile', [QboMigrationController::class, 'reconcile']);
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
