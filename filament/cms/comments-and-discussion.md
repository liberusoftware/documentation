# CMS: Comments and Discussion Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-comments-and-discussion-filament`  
**Matching domain module:** `cms-comments-and-discussion`  
**Application:** CMS  
**Source feature:** [Comments and Discussion](../../features/cms/comments-and-discussion.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-comments-and-discussion` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Threaded comments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Guest/member policy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Moderation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Subscriptions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Mentions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Spam control:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Editing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Retention:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-comments-and-discussion-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `threaded-comments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `guest/member-policy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `moderation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `subscriptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `mentions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `spam-control`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `editing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `retention`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-comments-and-discussion` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
