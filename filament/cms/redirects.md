# CMS: Redirects Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-cms-redirects-filament`  
**Matching domain module:** `cms-redirects`  
**Application:** CMS  
**Source feature:** [Redirects](../../features/cms/redirects.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `cms-redirects` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Redirect records:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Imports:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Automatic slug-change redirects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Chains/loops:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Hit counts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Expiry:** resource/table/form/action or page behavior for this module's authorized workflow.
- **404 suggestions:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-cms-redirects-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `redirect-records`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `imports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `automatic-slug-change-redirects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `chains/loops`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `hit-counts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `expiry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `404-suggestions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `cms-redirects` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
