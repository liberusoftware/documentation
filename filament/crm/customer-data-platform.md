# CRM: Customer Data Platform Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-customer-data-platform-filament`  
**Matching domain module:** `crm-customer-data-platform`  
**Application:** CRM  
**Source feature:** [Customer Data Platform](../../features/crm/customer-data-platform.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-customer-data-platform` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Source profiles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Identity resolution:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Unified profiles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audience activation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Event ingestion:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Consent-aware calculated attributes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Profile lineage:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-customer-data-platform-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `source-profiles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `identity-resolution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `unified-profiles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audience-activation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `event-ingestion`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `consent-aware-calculated-attributes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `profile-lineage`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-customer-data-platform` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
