# Accounting: Dashboards Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-dashboards-filament`  
**Matching domain module:** `accounting-dashboards`  
**Application:** Accounting  
**Source feature:** [Dashboards](../features/dashboards.md)  
**Architecture:** [FILAMENT.md](../ACCOUNTING.md) · [MODULES.md](../ACCOUNTING.md) · [TESTING.md](../ACCOUNTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-dashboards` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Role-specific KPIs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Widgets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Periods:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dimensions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Targets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Drill-through:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Refresh status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sharing:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-dashboards-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `role-specific-kpis`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `widgets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `periods`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dimensions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `targets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `drill-through`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `refresh-status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sharing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-dashboards` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
