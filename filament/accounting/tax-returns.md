# Accounting: Tax Returns Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-tax-returns-filament`  
**Matching domain module:** `accounting-tax-returns`  
**Application:** Accounting  
**Source feature:** [Tax Returns](../../features/accounting/tax-returns.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-tax-returns` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Return preparation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Source reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Diagnostics:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Review:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Submission adapter:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Receipt/status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payment:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Amendments:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-tax-returns-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `return-preparation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `source-reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `diagnostics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `review`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `submission-adapter`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `receipt/status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payment`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `amendments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-tax-returns` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
