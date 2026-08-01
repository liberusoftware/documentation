# SAP: Service Management Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-sap-service-management-filament`  
**Matching domain module:** `sap-service-management`  
**Application:** SAP  
**Source feature:** [Service Management](../../features/sap/service-management.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `sap-service-management` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Catalog:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Requests:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Incidents:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Problems:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Changes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Knowledge:** resource/table/form/action or page behavior for this module's authorized workflow.
- **CMDB:** resource/table/form/action or page behavior for this module's authorized workflow.
- **SLA:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Field service:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-sap-service-management-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `catalog`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `requests`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `incidents`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `problems`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `changes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `knowledge`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cmdb`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sla`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `field-service`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `sap-service-management` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
