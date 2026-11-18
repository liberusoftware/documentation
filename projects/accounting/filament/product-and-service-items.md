# Accounting: Product and Service Items Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#product-and-service-items). Observed identity: [`liberusoftware/module-accounting-product-and-service-items-filament`](../../../modules/source/liberusoftware--module-accounting-product-and-service-items-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-product-and-service-items-filament`  
**Matching domain module:** `accounting-product-and-service-items`  
**Application:** Accounting  
**Source feature:** [Product and Service Items](../features/product-and-service-items.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-product-and-service-items` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Items/services:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Codes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Purchase/sales descriptions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Accounts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax defaults:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Units:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Costs/prices:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ecommerce references:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-product-and-service-items-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `items-services`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `codes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `purchase-sales-descriptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `accounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax-defaults`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `units`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `costs-prices`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ecommerce-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-product-and-service-items` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-product-and-service-items-filament`](https://github.com/liberusoftware/module-accounting-product-and-service-items-filament) (`liberusoftware/accounting-product-and-service-items-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/product-and-service-items.md) · [API plan](../api/product-and-service-items.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Items/services** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `items/services`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Codes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `codes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Purchase/sales descriptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `purchase/sales descriptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Accounts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `accounts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tax defaults** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax defaults`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Units** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `units`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Costs/prices** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `costs/prices`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Ecommerce references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `ecommerce references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ProductAndServiceItemsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items-filament/src/ProductAndServiceItemsFilamentPlugin.php) · [ProductAndServiceItemsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items-filament/src/ProductAndServiceItemsFilamentServiceProvider.php) · [AccountingItemResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items-filament/src/Resources/AccountingItemResource.php) · [ListAccountingItems.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items-filament/src/Resources/AccountingItemResource/Pages/ListAccountingItems.php).

| Observed core query | Public method signatures |
| --- | --- |
| [FindAccountingItems.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items/src/Queries/FindAccountingItems.php) | `public function search(?string $term = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SaveAccountingItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items/src/Actions/SaveAccountingItem.php) | `public function handle(array $attributes): AccountingItem` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountingItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items/src/Models/AccountingItem.php) | `team_id`, `code`, `name`, `kind`, `purchase_description`, `sales_description`, `sales_account_ref`, `purchase_account_ref`, `tax_default_ref`, `unit`, `purchase_price`, `sales_price`, `currency`, `status`, `ecommerce_refs`, `metadata` |
<!-- layer-implementation-plan:end -->
