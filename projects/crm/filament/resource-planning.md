# CRM: Resource Planning Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-resource-planning-filament`  
**Matching domain module:** `crm-resource-planning`  
**Application:** CRM  
**Source feature:** [Resource Planning](../features/resource-planning.md)  
**Architecture:** [FILAMENT.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-resource-planning` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Skills:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capacity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Allocation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Utilization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tentative/confirmed bookings:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conflicts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Staffing forecasts:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-resource-planning-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `skills`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capacity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `allocation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `utilization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tentative/confirmed-bookings`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conflicts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `staffing-forecasts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-resource-planning` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
