# Ecommerce: Companies Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-ecommerce-companies-filament`  
**Matching domain module:** `ecommerce-companies`  
**Application:** Ecommerce  
**Source feature:** [Companies](../features/companies.md)  
**Architecture:** [FILAMENT.md](../ECOMMERCE.md) · [MODULES.md](../ECOMMERCE.md) · [TESTING.md](../ECOMMERCE.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `ecommerce-companies` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Company accounts/locations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contacts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Roles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Buyers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvers:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sales reps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax/exemption:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payment terms:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Addresses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-ecommerce-companies-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `company-accounts/locations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contacts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `roles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `buyers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvers`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sales-reps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax/exemption`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payment-terms`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `addresses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `ecommerce-companies` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
