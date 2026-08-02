# CRM: Landing Pages and Funnels Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-landing-pages-and-funnels-filament`  
**Matching domain module:** `crm-landing-pages-and-funnels`  
**Application:** CRM  
**Source feature:** [Landing Pages and Funnels](../features/landing-pages-and-funnels.md)  
**Architecture:** [FILAMENT.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-landing-pages-and-funnels` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Multi-step funnels:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Landing/thank-you pages:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Domains:** resource/table/form/action or page behavior for this module's authorized workflow.
- **SEO metadata:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Personalization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Forms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Order links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Preview:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Publish:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Conversion tracking:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-landing-pages-and-funnels-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `multi-step-funnels`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `landing/thank-you-pages`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `domains`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `seo-metadata`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `personalization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `forms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `order-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `preview`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `publish`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `conversion-tracking`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-landing-pages-and-funnels` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
