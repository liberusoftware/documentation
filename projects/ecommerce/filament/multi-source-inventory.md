# Ecommerce: Multi-Source Inventory Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-multi-source-inventory-filament`  
**Matching domain module:** `ecommerce-multi-source-inventory`  
**Application:** Ecommerce  
**Source feature:** [Multi-Source Inventory](../features/multi-source-inventory.md)  
**Architecture:** [FILAMENT.md](../ECOMMERCE.md) · [MODULES.md](../ECOMMERCE.md) · [TESTING.md](../ECOMMERCE.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-multi-source-inventory` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Sources/warehouses/stores/drop shippers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Stocks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Channel assignment:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Aggregated salable quantity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Priority/distance rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source health:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-multi-source-inventory-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `sources/warehouses/stores/drop-shippers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `stocks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `channel-assignment`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `aggregated-salable-quantity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `priority/distance-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-health`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-multi-source-inventory` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
