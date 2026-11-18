# Accounting: Accounting Sales Tax And Gst Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-sales-tax-and-gst). Observed identity: [`liberusoftware/module-accounting-sales-tax-and-gst-filament`](../../../modules/source/liberusoftware--module-accounting-sales-tax-and-gst-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-sales-tax-and-gst-filament`  
**Matching domain module:** `accounting-sales-tax-and-gst`  
**Application:** Accounting  
**Source feature:** [Accounting Sales Tax And Gst](../features/accounting-sales-tax-and-gst.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-sales-tax-and-gst` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Registrations/nexus:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Destination/origin rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Taxable bases:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Liabilities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Adjustments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Return periods:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Calculation adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-sales-tax-and-gst-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `registrations-nexus`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `destination-origin-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `taxable-bases`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `liabilities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `adjustments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `return-periods`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `calculation-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-sales-tax-and-gst` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-sales-tax-and-gst-filament`](https://github.com/liberusoftware/module-accounting-sales-tax-and-gst-filament) (`liberusoftware/accounting-sales-tax-and-gst-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-sales-tax-and-gst.md) · [API plan](../api/accounting-sales-tax-and-gst.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Registrations/nexus** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `registrations/nexus`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Destination/origin rules** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `destination/origin rules`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Taxable bases** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `taxable bases`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Liabilities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `liabilities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Adjustments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `adjustments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Return periods** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `return periods`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Calculation adapters** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `calculation adapters`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [SalesTaxResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst-filament/src/Resources/SalesTaxResource.php) · [ListSalesTax.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst-filament/src/Resources/SalesTaxResource/Pages/ListSalesTax.php) · [SalesTaxAndGstFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst-filament/src/SalesTaxAndGstFilamentPlugin.php) · [SalesTaxAndGstFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst-filament/src/SalesTaxAndGstFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [SalesTaxRecordQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Queries/SalesTaxRecordQuery.php) | `public function paginate(?string $context = null, ?string $type = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateSalesTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Actions/ActivateSalesTaxRecord.php) | `public function handle(SalesTaxRecord $record): SalesTaxRecord` |
| [CloseSalesTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Actions/CloseSalesTaxRecord.php) | `public function handle(SalesTaxRecord $record): SalesTaxRecord` |
| [CreateSalesTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Actions/CreateSalesTaxRecord.php) | `public function handle(array $attributes): SalesTaxRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SalesTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Models/SalesTaxRecord.php) | `context_id`, `type`, `jurisdiction`, `origin`, `destination`, `rate`, `taxable_base`, `liability`, `status`, `period_start`, `period_end`, `metadata` |
<!-- layer-implementation-plan:end -->
