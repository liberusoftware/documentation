# CRM: Contracts Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-contracts-filament`  
**Matching domain module:** `crm-contracts`  
**Application:** CRM  
**Source feature:** [Contracts](../features/contracts.md)  
**Architecture:** [FILAMENT.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-contracts` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Parties:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Terms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Clauses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Obligations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Versions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Negotiation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Signatures:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Amendments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Renewals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Notices:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Repository links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Compliance dates:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-contracts-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `parties`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `terms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `clauses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `obligations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `versions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `negotiation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `signatures`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `amendments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `renewals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `notices`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `repository-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `compliance-dates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-contracts` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
