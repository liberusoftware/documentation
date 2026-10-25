# Inventory: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-maintenance-inventory`.

**Proposed design identifier:** `module-maintenance-inventory-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/inventory.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-maintenance-inventory](../../../modules/source/liberusoftware--module-maintenance-inventory.md) |
| API | [liberusoftware/module-maintenance-inventory-api](../../../modules/source/liberusoftware--module-maintenance-inventory-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Parts | A focused authorized view or workflow section for parts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Warehouses/vans | A focused authorized view or workflow section for warehouses/vans; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Stock ledger | A focused authorized view or workflow section for stock ledger; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Reservations | A focused authorized view or workflow section for reservations; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Issues/returns | A focused authorized view or workflow section for issues/returns; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Transfers | A focused authorized view or workflow section for transfers; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Reorder | A focused authorized view or workflow section for reorder; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Counts | A focused authorized view or workflow section for counts; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AdjustStock.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/AdjustStock.php) | `public function handle(int $teamId, StockItem $item, int $delta, string $reason = 'adjustment', ?int $userId = null, ?string $notes = null): StockItem` |
| [CreateStockItem.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/CreateStockItem.php) | `public function handle(int $teamId, array $attributes): StockItem` |
| [DeleteStockItem.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/DeleteStockItem.php) | `public function handle(int $teamId, StockItem $item): void` |
| [IssueStock.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/IssueStock.php) | `public function handle(int $teamId, StockItem $item, int $quantity, ?int $userId = null, ?string $notes = null): StockItem` |
| [ReleaseReservedStock.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReleaseReservedStock.php) | `public function handle(int $teamId, StockItem $item, int $quantity): StockItem` |
| [ReserveStock.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReserveStock.php) | `public function handle(int $teamId, StockItem $item, int $quantity): StockItem` |
| [ReturnStock.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReturnStock.php) | `public function handle(int $teamId, StockItem $item, int $quantity, ?int $userId = null, ?string $notes = null): StockItem` |
| [UpdateStockItem.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/UpdateStockItem.php) | `public function handle(int $teamId, StockItem $item, array $attributes): StockItem` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [StockItem.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Models/StockItem.php) | `team_id`, `part_number`, `name`, `description`, `category`, `location`, `supplier_name`, `lead_time_days`, `notes`, `quantity`, `reorder_level`, `reorder_quantity`, `unit`, `unit_cost` |
| [StockMovement.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Models/StockMovement.php) | `team_id`, `stock_item_id`, `user_id`, `delta`, `quantity_before`, `quantity_after`, `reason`, `notes` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/module-maintenance-inventory-api/routes/api.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/inventory')->group(function (): void {
Route::get('/', [StockItemController::class, 'index']);
Route::post('/', [StockItemController::class, 'store']);
Route::get('/{stockItem}', [StockItemController::class, 'show']);
Route::patch('/{stockItem}', [StockItemController::class, 'update']);
Route::delete('/{stockItem}', [StockItemController::class, 'destroy']);
Route::post('/{stockItem}/adjust', [StockItemController::class, 'adjust']);
Route::post('/{stockItem}/reserve', [StockItemController::class, 'reserve']);
Route::post('/{stockItem}/release', [StockItemController::class, 'release']);
Route::post('/{stockItem}/issue', [StockItemController::class, 'issue']);
Route::post('/{stockItem}/return', [StockItemController::class, 'return']);
Route::get('/{stockItem}/movements', [StockItemController::class, 'movements']);
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
