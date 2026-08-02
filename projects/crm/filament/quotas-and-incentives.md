# CRM: Quotas and Incentives Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-quotas-and-incentives-filament`  
**Matching domain module:** `crm-quotas-and-incentives`  
**Application:** CRM  
**Source feature:** [Quotas and Incentives](../features/quotas-and-incentives.md)  
**Architecture:** [FILAMENT.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-quotas-and-incentives` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Quotas:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Ramps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Crediting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Splits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Territories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attainment:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Commission plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Accelerators:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Adjustments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Disputes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payroll/export adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-quotas-and-incentives-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `quotas`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ramps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `crediting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `splits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `territories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attainment`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `commission-plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `accelerators`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `adjustments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `disputes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payroll/export-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-quotas-and-incentives` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
