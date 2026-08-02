# CRM: Affiliate Management Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-affiliate-management-filament`  
**Matching domain module:** `crm-affiliate-management`  
**Application:** CRM  
**Source feature:** [Affiliate Management](../features/affiliate-management.md)  
**Architecture:** [FILAMENT.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-affiliate-management` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Affiliates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Applications:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Campaigns:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Clicks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conversions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Commission rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payout approvals/exports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Disputes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Assets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Portal:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-affiliate-management-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `affiliates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `applications`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `campaigns`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `clicks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conversions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `commission-rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payout-approvals/exports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `disputes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `assets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `portal`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-affiliate-management` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
