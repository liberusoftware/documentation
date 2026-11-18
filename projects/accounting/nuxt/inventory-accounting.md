# Accounting: Inventory Accounting Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#inventory-accounting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-inventory-accounting-nuxt`
**Matching domain module:** `accounting-inventory-accounting`
**Application:** Accounting
**Source feature:** [Inventory Accounting](../features/inventory-accounting.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/inventory-accounting.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-inventory-accounting` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Perpetual/periodic methods:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Valuation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cost layers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cost of sales:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Landed cost:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Adjustments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Write-downs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Subledger reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-inventory-accounting-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `perpetual-periodic-methods`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `valuation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cost-layers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cost-of-sales`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `landed-cost`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `adjustments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `write-downs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `subledger-reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-inventory-accounting` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/inventory-accounting.md)) |
| Capability Nuxt module skeleton | [`module-accounting-inventory-accounting-nuxt`](https://github.com/liberusoftware/module-accounting-inventory-accounting-nuxt) (`@liberusoftware/module-accounting-inventory-accounting-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Perpetual/periodic methods** | Expose composable and Vue 3 component for `perpetual/periodic methods` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/inventory-accounting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Valuation** | Expose composable and Vue 3 component for `valuation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/inventory-accounting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Cost layers** | Expose composable and Vue 3 component for `cost layers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/inventory-accounting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Cost of sales** | Expose composable and Vue 3 component for `cost of sales` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/inventory-accounting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Landed cost** | Expose composable and Vue 3 component for `landed cost` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/inventory-accounting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Adjustments** | Expose composable and Vue 3 component for `adjustments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/inventory-accounting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Write-downs** | Expose composable and Vue 3 component for `write-downs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/inventory-accounting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Subledger reconciliation** | Expose composable and Vue 3 component for `subledger reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/inventory-accounting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [InventoryQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Queries/InventoryQuery.php) | `public function paginate(?int $teamId = null, ?InventoryStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function valuation(InventoryItem $item): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AdjustInventory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/AdjustInventory.php) | `public function handle(InventoryItem $item, array $attributes): InventoryAdjustment` |
| [ApplyLandedCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/ApplyLandedCost.php) | `public function handle(InventoryItem $item, array $attributes): LandedCost` |
| [CreateInventoryItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/CreateInventoryItem.php) | `public function handle(array $attributes): InventoryItem` |
| [IssueInventory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/IssueInventory.php) | `public function handle(InventoryItem $item, array $attributes): float` |
| [ReceiveInventory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/ReceiveInventory.php) | `public function handle(InventoryItem $item, array $attributes): CostLayer` |
| [ReconcileInventory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/ReconcileInventory.php) | `public function handle(array $attributes, ?InventoryItem $item = null): InventoryReconciliation` |
| [WriteDownInventory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/WriteDownInventory.php) | `public function handle(InventoryItem $item, array $attributes): InventoryWriteDown` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CostLayer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/CostLayer.php) | `item_id`, `layer_ref`, `received_at`, `quantity_received`, `quantity_remaining`, `unit_cost`, `total_cost`, `source_ref`, `metadata` |
| [InventoryAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryAdjustment.php) | `item_id`, `adjustment_ref`, `quantity_delta`, `value_delta`, `reason`, `actor_ref`, `adjusted_at`, `metadata` |
| [InventoryItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryItem.php) | `team_id`, `item_ref`, `description`, `warehouse_ref`, `currency`, `valuation_method`, `status`, `quantity_on_hand`, `inventory_value`, `metadata` |
| [InventoryMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryMovement.php) | `item_id`, `movement_ref`, `movement_type`, `quantity`, `unit_cost`, `total_cost`, `source_ref`, `occurred_at`, `metadata` |
| [InventoryReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryReconciliation.php) | `team_id`, `reconciliation_ref`, `period_ref`, `subledger_value`, `general_ledger_value`, `variance`, `status`, `actor_ref`, `reconciled_at`, `metadata` |
| [InventoryWriteDown.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryWriteDown.php) | `item_id`, `write_down_ref`, `amount`, `reason`, `actor_ref`, `written_down_at`, `metadata` |
| [LandedCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/LandedCost.php) | `item_id`, `cost_ref`, `amount`, `allocation_basis`, `source_ref`, `allocated_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [InventoryAccountingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting-api/src/Http/Controllers/InventoryAccountingController.php) | `public function __construct(private readonly InventoryQuery $query)`<br>`public function index(Request $request): InventoryItemResource`<br>`public function store(Request $request, CreateInventoryItem $action): InventoryItemResource`<br>`public function show(InventoryItem $item): InventoryItemResource`<br>`public function receive(Request $request, InventoryItem $item, ReceiveInventory $action): InventoryItemResource`<br>`public function issue(Request $request, InventoryItem $item, IssueInventory $action): JsonResponse`<br>`public function adjust(Request $request, InventoryItem $item, AdjustInventory $action): InventoryItemResource`<br>`public function landed(Request $request, InventoryItem $item, ApplyLandedCost $action): InventoryItemResource`<br>`public function writeDown(Request $request, InventoryItem $item, WriteDownInventory $action): InventoryItemResource`<br>`public function valuation(InventoryItem $item, InventoryQuery $query): JsonResponse`<br>`public function reconcile(Request $request, ReconcileInventory $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-inventory-accounting-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting-api/routes/api.php)

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
<!-- layer-implementation-plan:end -->
