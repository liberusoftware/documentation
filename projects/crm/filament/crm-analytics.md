# CRM: CRM Analytics Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-analytics-filament`  
**Matching domain module:** `crm-analytics`  
**Application:** CRM  
**Source feature:** [CRM Analytics](../features/crm-analytics.md)  
**Architecture:** [FILAMENT.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-analytics` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Governed datasets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dashboards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Pivots:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Funnels:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cohorts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Goals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Row-level access:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Metric lineage:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-analytics-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `governed-datasets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dashboards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `pivots`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `funnels`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cohorts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `goals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `row-level-access`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `metric-lineage`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-analytics` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
