# Maintenance: Inventory Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#inventory). Observed identity: [`liberusoftware/module-maintenance-inventory-filament`](../../../modules/source/liberusoftware--module-maintenance-inventory-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-maintenance-inventory-filament`  
**Matching domain module:** `maintenance-inventory`  
**Application:** Maintenance  
**Source feature:** [Inventory](../features/inventory.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `maintenance-inventory` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Parts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Warehouses/vans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Stock ledger:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reservations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Issues/returns:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transfers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reorder:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Counts:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-maintenance-inventory-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `parts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `warehouses-vans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `stock-ledger`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reservations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `issues-returns`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transfers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reorder`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `counts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `maintenance-inventory` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-maintenance-inventory-filament`](https://github.com/liberusoftware/module-maintenance-inventory-filament) (`liberusoftware/maintenance-inventory-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/inventory.md) · [API plan](../api/inventory.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Parts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `parts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Warehouses/vans** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `warehouses/vans`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Stock ledger** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `stock ledger`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reservations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reservations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Issues/returns** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `issues/returns`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transfers** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transfers`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reorder** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reorder`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Counts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `counts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [InventoryFilamentPlugin.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory-filament/src/InventoryFilamentPlugin.php) · [InventoryFilamentServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory-filament/src/InventoryFilamentServiceProvider.php) · [StockItemResource.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory-filament/src/Resources/StockItemResource.php) · [CreateStockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory-filament/src/Resources/StockItemResource/Pages/CreateStockItem.php) · [EditStockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory-filament/src/Resources/StockItemResource/Pages/EditStockItem.php) · [ListStockItems.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory-filament/src/Resources/StockItemResource/Pages/ListStockItems.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AdjustStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/AdjustStock.php) | `public function handle(int $teamId, StockItem $item, int $delta, string $reason = 'adjustment', ?int $userId = null, ?string $notes = null): StockItem` |
| [CreateStockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/CreateStockItem.php) | `public function handle(int $teamId, array $attributes): StockItem` |
| [DeleteStockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/DeleteStockItem.php) | `public function handle(int $teamId, StockItem $item): void` |
| [IssueStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/IssueStock.php) | `public function __construct(private readonly AdjustStock $adjustStock)`<br>`public function handle(int $teamId, StockItem $item, int $quantity, ?int $userId = null, ?string $notes = null): StockItem` |
| [ReleaseReservedStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReleaseReservedStock.php) | `public function handle(int $teamId, StockItem $item, int $quantity): StockItem` |
| [ReserveStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReserveStock.php) | `public function handle(int $teamId, StockItem $item, int $quantity): StockItem` |
| [ReturnStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReturnStock.php) | `public function __construct(private readonly AdjustStock $adjustStock)`<br>`public function handle(int $teamId, StockItem $item, int $quantity, ?int $userId = null, ?string $notes = null): StockItem` |
| [UpdateStockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/UpdateStockItem.php) | `public function handle(int $teamId, StockItem $item, array $attributes): StockItem` |
| [StockItemPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Policies/StockItemPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, StockItem $item): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, StockItem $item): bool`<br>`public function delete(object $user, StockItem $item): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [StockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Models/StockItem.php) | `team_id`, `part_number`, `name`, `description`, `category`, `location`, `supplier_name`, `lead_time_days`, `notes`, `quantity`, `reorder_level`, `reorder_quantity`, `unit`, `unit_cost` |
| [StockMovement.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Models/StockMovement.php) | `team_id`, `stock_item_id`, `user_id`, `delta`, `quantity_before`, `quantity_after`, `reason`, `notes` |
<!-- layer-implementation-plan:end -->
