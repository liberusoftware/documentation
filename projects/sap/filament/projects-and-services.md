# SAP: Projects and Services Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-sap-projects-and-services-filament`  
**Matching domain module:** `sap-projects-and-services`  
**Application:** SAP  
**Source feature:** [Projects and Services](../features/projects-and-services.md)  
**Architecture:** [FILAMENT.md](../SAP.md) · [MODULES.md](../SAP.md) · [TESTING.md](../SAP.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `sap-projects-and-services` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Portfolios:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Projects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Resources:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Skills:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Time:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Expenses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Milestones:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Risks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Delivery:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Profitability:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-sap-projects-and-services-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `portfolios`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `projects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `resources`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `skills`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `time`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `expenses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `milestones`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `risks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `delivery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `profitability`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `sap-projects-and-services` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
