# CMS: Drupal Migration Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-drupal-migration-filament`  
**Matching domain module:** `cms-drupal-migration`  
**Application:** CMS  
**Source feature:** [Drupal Migration](../features/drupal-migration.md)  
**Architecture:** [FILAMENT.md](../CMS.md) · [MODULES.md](../CMS.md) · [TESTING.md](../CMS.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-drupal-migration` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Entity/bundle/field data:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Revisions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Moderation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Taxonomy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Media:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Menus:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Views mapping:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Translations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Configuration evidence:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-drupal-migration-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `entity/bundle/field-data`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `revisions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `moderation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `taxonomy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `media`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `menus`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `views-mapping`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `translations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `configuration-evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-drupal-migration` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
