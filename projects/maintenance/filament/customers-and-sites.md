# Maintenance: Customers and Sites Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-maintenance-customers-and-sites-filament`  
**Matching domain module:** `maintenance-customers-and-sites`  
**Application:** Maintenance  
**Source feature:** [Customers and Sites](../features/customers-and-sites.md)  
**Architecture:** [FILAMENT.md](../MAINTENANCE.md) · [MODULES.md](../MAINTENANCE.md) · [TESTING.md](../MAINTENANCE.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `maintenance-customers-and-sites` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contacts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sites:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Locations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Access details:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Hazards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Service windows:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-maintenance-customers-and-sites-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `customers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contacts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sites`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `locations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `access-details`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `hazards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `service-windows`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `maintenance-customers-and-sites` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
