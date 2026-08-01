# CRM: Feedback and Voice of Customer Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-feedback-and-voice-of-customer-filament`  
**Matching domain module:** `crm-feedback-and-voice-of-customer`  
**Application:** CRM  
**Source feature:** [Feedback and Voice of Customer](../../features/crm/feedback-and-voice-of-customer.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-feedback-and-voice-of-customer` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **CSAT:** resource/table/form/action or page behavior for this module's authorized workflow.
- **NPS:** resource/table/form/action or page behavior for this module's authorized workflow.
- **CES:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Custom surveys:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sampling:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Delivery:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Responses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Text analysis:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Alerts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Close-the-loop cases:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Trend reporting:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-feedback-and-voice-of-customer-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `csat`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `nps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `ces`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `custom-surveys`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sampling`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `delivery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `responses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `text-analysis`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `alerts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `close-the-loop-cases`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `trend-reporting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-feedback-and-voice-of-customer` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
