# Accounting: Financial Statements Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#financial-statements). Observed identity: [`liberusoftware/module-accounting-financial-statements-filament`](../../../modules/source/liberusoftware--module-accounting-financial-statements-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-financial-statements-filament`  
**Matching domain module:** `accounting-financial-statements`  
**Application:** Accounting  
**Source feature:** [Financial Statements](../features/financial-statements.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-financial-statements` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Profit and loss:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Balance sheet:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cash flow:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Changes in equity:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Comparative periods:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Dimensions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Drill-through:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-financial-statements-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `profit-and-loss`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `balance-sheet`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cash-flow`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `changes-in-equity`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `comparative-periods`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `dimensions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `drill-through`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-financial-statements` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-financial-statements-filament`](https://github.com/liberusoftware/module-accounting-financial-statements-filament) (`liberusoftware/accounting-financial-statements-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/financial-statements.md) · [API plan](../api/financial-statements.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Profit and loss** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `profit and loss`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Balance sheet** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `balance sheet`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cash flow** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cash flow`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Changes in equity** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `changes in equity`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Comparative periods** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `comparative periods`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Dimensions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `dimensions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Drill-through** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drill-through`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [FinancialStatementsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-filament/src/FinancialStatementsFilamentPlugin.php) · [FinancialStatementsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-filament/src/FinancialStatementsFilamentServiceProvider.php) · [FinancialStatements.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-filament/src/Pages/FinancialStatements.php).

| Observed core query | Public method signatures |
| --- | --- |
| [StatementQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/src/Queries/StatementQuery.php) | `public function profitAndLoss(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function balanceSheet(int $bookId, string $asOf, ?array $dimensions = null): array`<br>`public function cashFlow(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function changesInEquity(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function comparative(int $bookId, string $start, string $end, string $compareStart, string $compareEnd, ?array $dimensions = null): array`<br>`public function drillThrough(int $bookId, int $accountId, string $start, string $end, ?array $dimensions = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [FinancialStatementsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-api/src/Policies/FinancialStatementsPolicy.php) | `public function view(?Authenticatable $user): bool` |
<!-- layer-implementation-plan:end -->
