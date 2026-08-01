# Ecommerce: Shipping Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-shipping-filament`  
**Matching domain module:** `ecommerce-shipping`  
**Application:** Ecommerce  
**Source feature:** [Shipping](../../features/ecommerce/shipping.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-shipping` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Zones:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Methods:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Packages:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Restrictions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Free shipping:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Table rates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Carrier adapters:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Delivery estimates:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-shipping-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `zones`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `methods`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `packages`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `restrictions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `free-shipping`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `table-rates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `carrier-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `delivery-estimates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-shipping` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
