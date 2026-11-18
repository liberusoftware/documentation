# Accounting: Accounting Cash Flow Forecasting Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-cash-flow-forecasting). Observed identity: [`liberusoftware/module-accounting-cash-flow-forecasting-filament`](../../../modules/source/liberusoftware--module-accounting-cash-flow-forecasting-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-cash-flow-forecasting-filament`  
**Matching domain module:** `accounting-cash-flow-forecasting`  
**Application:** Accounting  
**Source feature:** [Accounting Cash Flow Forecasting](../features/accounting-cash-flow-forecasting.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-cash-flow-forecasting` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Direct forecast:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Opening cash:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Receivable/payable timing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Recurring items:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Scenarios:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Manual assumptions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Variance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Confidence:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-cash-flow-forecasting-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `direct-forecast`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `opening-cash`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `receivable-payable-timing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `recurring-items`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `scenarios`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `manual-assumptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `variance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `confidence`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-cash-flow-forecasting` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-cash-flow-forecasting-filament`](https://github.com/liberusoftware/module-accounting-cash-flow-forecasting-filament) (`liberusoftware/accounting-cash-flow-forecasting-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-cash-flow-forecasting.md) · [API plan](../api/accounting-cash-flow-forecasting.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Direct forecast** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `direct forecast`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Opening cash** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `opening cash`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Receivable/payable timing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `receivable/payable timing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Recurring items** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `recurring items`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Scenarios** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `scenarios`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Manual assumptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `manual assumptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Variance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `variance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Confidence** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `confidence`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CashFlowForecastingFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting-filament/src/CashFlowForecastingFilamentPlugin.php) · [CashFlowForecastingFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting-filament/src/CashFlowForecastingFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CashFlowForecastQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Queries/CashFlowForecastQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddForecastItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/AddForecastItem.php) | `public function receivable(CashFlowForecast $forecast, array $item): CashFlowForecast`<br>`public function payable(CashFlowForecast $forecast, array $item): CashFlowForecast`<br>`public function recurring(CashFlowForecast $forecast, array $item): CashFlowForecast` |
| [CreateCashFlowForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/CreateCashFlowForecast.php) | `public function handle(array $attributes): CashFlowForecast` |
| [SetForecastScenario.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/SetForecastScenario.php) | `public function handle(CashFlowForecast $forecast, array $scenario): CashFlowForecast` |
| [UpdateCashFlowForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/UpdateCashFlowForecast.php) | `public function handle(CashFlowForecast $forecast, array $data): CashFlowForecast` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CashFlowForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Models/CashFlowForecast.php) | `team_id`, `forecast_ref`, `currency`, `starts_on`, `ends_on`, `opening_cash`, `forecast_cash`, `variance`, `confidence`, `receivables`, `payables`, `recurring_items`, `scenarios`, `assumptions` |
<!-- layer-implementation-plan:end -->
