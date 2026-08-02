# CRM: Telephony Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-telephony-filament`  
**Matching domain module:** `crm-telephony`  
**Application:** CRM  
**Source feature:** [Telephony](../features/telephony.md)  
**Architecture:** [FILAMENT.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-telephony` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Numbers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Caller ID:** resource/table/form/action or page behavior for this module's authorized workflow.
- **IVR:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Queues:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Business hours:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Skills:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recording:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Voicemail:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transfers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dispositions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Click-to-call:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Call logging:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider adapters:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-telephony-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `numbers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `caller-id`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ivr`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `queues`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `business-hours`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `skills`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recording`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `voicemail`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transfers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dispositions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `click-to-call`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `call-logging`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-adapters`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-telephony` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
