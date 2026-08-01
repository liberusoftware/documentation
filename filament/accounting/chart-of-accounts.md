# Accounting: Chart of Accounts Filament

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-chart-of-accounts-filament`  
**Matching domain module:** `accounting-chart-of-accounts`  
**Application:** Accounting  
**Source feature:** [Chart of Accounts](../../features/accounting/chart-of-accounts.md)  
**Architecture:** [FILAMENT.md](../../FILAMENT.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-chart-of-accounts` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Account types:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Codes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Hierarchies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Control accounts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Normal balances:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Templates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Restrictions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Localization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Lifecycle:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-chart-of-accounts-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `account-types`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `codes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `hierarchies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `control-accounts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `normal-balances`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `templates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `restrictions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `localization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `lifecycle`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-chart-of-accounts` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
