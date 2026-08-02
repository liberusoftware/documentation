# Control Panel: OS Adapters Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-control-panel-os-adapters-filament`  
**Matching domain module:** `control-panel-os-adapters`  
**Application:** Control Panel  
**Source feature:** [OS Adapters](../features/os-adapters.md)  
**Architecture:** [FILAMENT.md](../CONTROL-PANEL.md) · [MODULES.md](../CONTROL-PANEL.md) · [TESTING.md](../CONTROL-PANEL.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `control-panel-os-adapters` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Detection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Packages:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Services:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Firewall:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Users:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Filesystems:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Repositories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Support matrix:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-control-panel-os-adapters-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `detection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `packages`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `services`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `firewall`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `users`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `filesystems`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `repositories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `support-matrix`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `control-panel-os-adapters` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
