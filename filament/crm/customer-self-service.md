# CRM: Customer Self-Service Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-customer-self-service-filament`  
**Matching domain module:** `crm-customer-self-service`  
**Application:** CRM  
**Source feature:** [Customer Self-Service](../../features/crm/customer-self-service.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-customer-self-service` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customer portal:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Case submission/status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Knowledge search:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Community links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Appointments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Documents:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Invoices/orders references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Profile:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Preferences:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-customer-self-service-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `customer-portal`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `case-submission/status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `knowledge-search`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `community-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `appointments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `documents`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `invoices/orders-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `profile`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `preferences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-customer-self-service` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
