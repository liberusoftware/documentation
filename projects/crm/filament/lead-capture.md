# CRM: Lead Capture Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-lead-capture-filament`  
**Matching domain module:** `crm-lead-capture`  
**Application:** CRM  
**Source feature:** [Lead Capture](../features/lead-capture.md)  
**Architecture:** [FILAMENT.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-lead-capture` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Leads inbox:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Manual/import/API capture:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Forms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Surveys:** resource/table/form/action or page behavior for this module's authorized workflow.
- **QR codes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Chat:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Calls:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Advertisements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Events:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Referrals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source metadata:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-lead-capture-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `leads-inbox`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `manual/import/api-capture`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `forms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `surveys`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `qr-codes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `chat`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `calls`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `advertisements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `referrals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-metadata`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-lead-capture` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
