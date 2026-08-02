# Accounting: Deposits and Clearing Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-deposits-and-clearing-filament`  
**Matching domain module:** `accounting-deposits-and-clearing`  
**Application:** Accounting  
**Source feature:** [Deposits and Clearing](../features/deposits-and-clearing.md)  
**Architecture:** [FILAMENT.md](../ACCOUNTING.md) · [MODULES.md](../ACCOUNTING.md) · [TESTING.md](../ACCOUNTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-deposits-and-clearing` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Undeposited funds:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Grouped deposits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payment-provider clearing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fees:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payouts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Timing differences:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-deposits-and-clearing-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `undeposited-funds`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `grouped-deposits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payment-provider-clearing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fees`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payouts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `timing-differences`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-deposits-and-clearing` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
