# Social Network: Communities Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-communities-filament`  
**Matching domain module:** `social-network-communities`  
**Application:** Social Network  
**Source feature:** [Communities](../features/communities.md)  
**Architecture:** [FILAMENT.md](../SOCIAL-NETWORK.md) · [MODULES.md](../SOCIAL-NETWORK.md) · [TESTING.md](../SOCIAL-NETWORK.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `social-network-communities` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Groups/pages:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Memberships:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Roles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rules:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Feeds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Files:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Questions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Moderation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-communities-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `groups/pages`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `memberships`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `roles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rules`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `feeds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `files`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `questions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `moderation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `social-network-communities` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
