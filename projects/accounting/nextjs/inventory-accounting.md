# Inventory Accounting: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-accounting-inventory-accounting`.

**Proposed design identifier:** `module-accounting-inventory-accounting-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/inventory-accounting.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-accounting-inventory-accounting](../../../modules/source/liberusoftware--module-accounting-inventory-accounting.md) |
| API | [liberusoftware/module-accounting-inventory-accounting-api](../../../modules/source/liberusoftware--module-accounting-inventory-accounting-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Perpetual/periodic methods | A focused authorized view or workflow section for perpetual/periodic methods; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Valuation | A focused authorized view or workflow section for valuation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Cost layers | A focused authorized view or workflow section for cost layers; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Cost of sales | A focused authorized view or workflow section for cost of sales; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Landed cost | A focused authorized view or workflow section for landed cost; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Adjustments | A focused authorized view or workflow section for adjustments; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Write-downs | A focused authorized view or workflow section for write-downs; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Subledger reconciliation | A focused authorized view or workflow section for subledger reconciliation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [InventoryQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Queries/InventoryQuery.php) | `public function paginate(?int $teamId = null, ?InventoryStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function valuation(InventoryItem $item): array` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AdjustInventory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/AdjustInventory.php) | `public function handle(InventoryItem $item, array $attributes): InventoryAdjustment` |
| [ApplyLandedCost.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/ApplyLandedCost.php) | `public function handle(InventoryItem $item, array $attributes): LandedCost` |
| [CreateInventoryItem.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/CreateInventoryItem.php) | `public function handle(array $attributes): InventoryItem` |
| [IssueInventory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/IssueInventory.php) | `public function handle(InventoryItem $item, array $attributes): float` |
| [ReceiveInventory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/ReceiveInventory.php) | `public function handle(InventoryItem $item, array $attributes): CostLayer` |
| [ReconcileInventory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/ReconcileInventory.php) | `public function handle(array $attributes, ?InventoryItem $item = null): InventoryReconciliation` |
| [WriteDownInventory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/WriteDownInventory.php) | `public function handle(InventoryItem $item, array $attributes): InventoryWriteDown` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [CostLayer.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/CostLayer.php) | `item_id`, `layer_ref`, `received_at`, `quantity_received`, `quantity_remaining`, `unit_cost`, `total_cost`, `source_ref`, `metadata` |
| [InventoryAdjustment.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryAdjustment.php) | `item_id`, `adjustment_ref`, `quantity_delta`, `value_delta`, `reason`, `actor_ref`, `adjusted_at`, `metadata` |
| [InventoryItem.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryItem.php) | `team_id`, `item_ref`, `description`, `warehouse_ref`, `currency`, `valuation_method`, `status`, `quantity_on_hand`, `inventory_value`, `metadata` |
| [InventoryMovement.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryMovement.php) | `item_id`, `movement_ref`, `movement_type`, `quantity`, `unit_cost`, `total_cost`, `source_ref`, `occurred_at`, `metadata` |
| [InventoryReconciliation.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryReconciliation.php) | `team_id`, `reconciliation_ref`, `period_ref`, `subledger_value`, `general_ledger_value`, `variance`, `status`, `actor_ref`, `reconciled_at`, `metadata` |
| [InventoryWriteDown.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryWriteDown.php) | `item_id`, `write_down_ref`, `amount`, `reason`, `actor_ref`, `written_down_at`, `metadata` |
| [LandedCost.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/LandedCost.php) | `item_id`, `cost_ref`, `amount`, `allocation_basis`, `source_ref`, `allocated_at`, `metadata` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/accounting-inventory-accounting-api/routes/api.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/inventory-accounting')->group(function (): void {
Route::get('/', [InventoryAccountingController::class, 'index'])->name('accounting.inventory-accounting.list');
Route::post('/', [InventoryAccountingController::class, 'store'])->name('accounting.inventory-accounting.create');
Route::get('/{item}', [InventoryAccountingController::class, 'show'])->name('accounting.inventory-accounting.show');
Route::post('/{item}/receipts', [InventoryAccountingController::class, 'receive'])->name('accounting.inventory-accounting.receive');
Route::post('/{item}/issues', [InventoryAccountingController::class, 'issue'])->name('accounting.inventory-accounting.issue');
Route::post('/{item}/adjustments', [InventoryAccountingController::class, 'adjust'])->name('accounting.inventory-accounting.adjust');
Route::post('/{item}/landed-costs', [InventoryAccountingController::class, 'landed'])->name('accounting.inventory-accounting.landed');
Route::post('/{item}/write-downs', [InventoryAccountingController::class, 'writeDown'])->name('accounting.inventory-accounting.write-down');
Route::get('/{item}/valuation', [InventoryAccountingController::class, 'valuation'])->name('accounting.inventory-accounting.valuation');
Route::post('/reconciliations', [InventoryAccountingController::class, 'reconcile'])->name('accounting.inventory-accounting.reconcile');
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
