# Accounting: Sage Accounting Migration Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-sage-accounting-migration-filament`  
**Matching domain module:** `accounting-sage-accounting-migration`  
**Application:** Accounting  
**Source feature:** [Sage Accounting Migration](../../features/accounting/sage-accounting-migration.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-sage-accounting-migration` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Chart/analysis types:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Contacts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Products:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sales/purchases:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bank:** resource/table/form/action or page behavior for this module's authorized workflow.
- **VAT/CIS evidence:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Currencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Budgets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Attachments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source IDs:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-sage-accounting-migration-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `chart/analysis-types`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `contacts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `products`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sales/purchases`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bank`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `vat/cis-evidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `currencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `budgets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `attachments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-ids`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-sage-accounting-migration` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
