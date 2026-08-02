# Ecommerce: Point of Sale Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-point-of-sale-filament`  
**Matching domain module:** `ecommerce-point-of-sale`  
**Application:** Ecommerce  
**Source feature:** [Point of Sale](../features/point-of-sale.md)  
**Architecture:** [FILAMENT.md](../ECOMMERCE.md) · [MODULES.md](../ECOMMERCE.md) · [TESTING.md](../ECOMMERCE.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-point-of-sale` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Registers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Carts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Customers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Products:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Taxes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Discounts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tenders:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Receipts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Returns/exchanges:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Holds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Staff actions:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-point-of-sale-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `registers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `carts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `customers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `products`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `taxes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `discounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tenders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `receipts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `returns/exchanges`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `holds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `staff-actions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-point-of-sale` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
