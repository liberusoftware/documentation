# Control Panel: Control Core Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-control-panel-control-core-filament`  
**Matching domain module:** `control-panel-control-core`  
**Application:** Control Panel  
**Source feature:** [Control Core](../features/control-core.md)  
**Architecture:** [FILAMENT.md](../CONTROL-PANEL.md) · [MODULES.md](../CONTROL-PANEL.md) · [TESTING.md](../CONTROL-PANEL.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `control-panel-control-core` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Nodes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capabilities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Credentials:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Task engine:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Inventory:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Desired state:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Locks:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Audit:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-control-panel-control-core-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `nodes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capabilities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `credentials`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `task-engine`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `inventory`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `desired-state`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `locks`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `audit`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `control-panel-control-core` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
