# CRM: Communities Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-communities-filament`  
**Matching domain module:** `crm-communities`  
**Application:** CRM  
**Source feature:** [Communities](../../features/crm/communities.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-communities` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customer/partner groups:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Spaces:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Memberships:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Posts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Comments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Events:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Moderation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Gamification:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Knowledge links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **CRM profile activity:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-communities-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `customer/partner-groups`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `spaces`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `memberships`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `posts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `comments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `events`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `moderation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `gamification`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `knowledge-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `crm-profile-activity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-communities` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
