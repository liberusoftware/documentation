# CMS: Content Entities Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-content-entities-filament`  
**Matching domain module:** `cms-content-entities`  
**Application:** CMS  
**Source feature:** [Content Entities](../features/content-entities.md)  
**Architecture:** [FILAMENT.md](../CMS.md) · [MODULES.md](../CMS.md) · [TESTING.md](../CMS.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-content-entities` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Typed entities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bundles/content types:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Authorship:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cloning:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Relationships:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Canonical identifiers:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-content-entities-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `typed-entities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bundles/content-types`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `authorship`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cloning`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `relationships`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `canonical-identifiers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-content-entities` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
