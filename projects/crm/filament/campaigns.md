# CRM: Campaigns Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-campaigns-filament`  
**Matching domain module:** `crm-campaigns`  
**Application:** CRM  
**Source feature:** [Campaigns](../features/campaigns.md)  
**Architecture:** [FILAMENT.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-campaigns` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Campaign hierarchy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Briefs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Objectives:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Budget:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Assets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Channels:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audience:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Owners:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Calendar:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tasks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Costs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Responses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Influence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **ROI:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-campaigns-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `campaign-hierarchy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `briefs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `objectives`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `budget`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `assets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `channels`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audience`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `owners`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `calendar`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tasks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `costs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `responses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `influence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `roi`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-campaigns` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
