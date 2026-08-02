# Ecommerce: Catalog Staging Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-catalog-staging-filament`  
**Matching domain module:** `ecommerce-catalog-staging`  
**Application:** Ecommerce  
**Source feature:** [Catalog Staging](../features/catalog-staging.md)  
**Architecture:** [FILAMENT.md](../ECOMMERCE.md) · [MODULES.md](../ECOMMERCE.md) · [TESTING.md](../ECOMMERCE.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-catalog-staging` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Draft/effective catalog changes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Grouped campaigns:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Preview:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Schedules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conflicts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Atomic activation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rollback:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-catalog-staging-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `draft/effective-catalog-changes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `grouped-campaigns`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `preview`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `schedules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conflicts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `atomic-activation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rollback`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-catalog-staging` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
