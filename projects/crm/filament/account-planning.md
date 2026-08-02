# CRM: Account Planning Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-account-planning-filament`  
**Matching domain module:** `crm-account-planning`  
**Application:** CRM  
**Source feature:** [Account Planning](../features/account-planning.md)  
**Architecture:** [FILAMENT.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-account-planning` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Account hierarchies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Stakeholders:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Influence maps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Whitespace:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Account plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Objectives:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Risks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Mutual action plans:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Account-based coordination:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-account-planning-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `account-hierarchies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `stakeholders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `influence-maps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `whitespace`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `account-plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `objectives`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `risks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `mutual-action-plans`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `account-based-coordination`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-account-planning` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
