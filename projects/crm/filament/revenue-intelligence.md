# CRM: Revenue Intelligence Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-revenue-intelligence-filament`  
**Matching domain module:** `crm-revenue-intelligence`  
**Application:** CRM  
**Source feature:** [Revenue Intelligence](../features/revenue-intelligence.md)  
**Architecture:** [FILAMENT.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-revenue-intelligence` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Pipeline inspection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Health/risk:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Engagement gaps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Opportunity scoring:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Relationship maps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **White-space/next-product suggestions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Anomaly detection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Alerts:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-revenue-intelligence-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `pipeline-inspection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `health/risk`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `engagement-gaps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `opportunity-scoring`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `relationship-maps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `white-space/next-product-suggestions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `anomaly-detection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `alerts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-revenue-intelligence` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
