# CRM: Templates and Snapshots Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-templates-and-snapshots-filament`  
**Matching domain module:** `crm-templates-and-snapshots`  
**Application:** CRM  
**Source feature:** [Templates and Snapshots](../../features/crm/templates-and-snapshots.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-templates-and-snapshots` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Versioned bundles of fields:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Pipelines:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Workflows:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Forms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Funnels:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Calendars:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dashboards:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Settings with preview:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Protected sharing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Install:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Update:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rollback:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-templates-and-snapshots-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `versioned-bundles-of-fields`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `pipelines`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `workflows`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `forms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `funnels`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `calendars`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dashboards`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `settings-with-preview`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `protected-sharing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `install`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `update`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rollback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-templates-and-snapshots` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
