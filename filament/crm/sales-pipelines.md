# CRM: Sales Pipelines Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-sales-pipelines-filament`  
**Matching domain module:** `crm-sales-pipelines`  
**Application:** CRM  
**Source feature:** [Sales Pipelines](../../features/crm/sales-pipelines.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-sales-pipelines` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Multiple pipelines:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Stages:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Opportunities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Products:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Values:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Probabilities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Close dates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Competitors:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dependencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Stage history:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rotting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Loss reasons:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-sales-pipelines-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `multiple-pipelines`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `stages`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `opportunities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `products`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `values`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `probabilities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `close-dates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `competitors`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dependencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `stage-history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rotting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `loss-reasons`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-sales-pipelines` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
