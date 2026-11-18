# Accounting: Accounting Multi Currency Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-multi-currency). Observed identity: [`liberusoftware/module-accounting-multi-currency-filament`](../../../modules/source/liberusoftware--module-accounting-multi-currency-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-multi-currency-filament`  
**Matching domain module:** `accounting-multi-currency`  
**Application:** Accounting  
**Source feature:** [Accounting Multi Currency](../features/accounting-multi-currency.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-multi-currency` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Transaction/functional/reporting currencies:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Revaluation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Realized/unrealized gains:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Historical rates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-multi-currency-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `transaction-functional-reporting-currencies`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `revaluation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `realized-unrealized-gains`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `historical-rates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-multi-currency` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-multi-currency-filament`](https://github.com/liberusoftware/module-accounting-multi-currency-filament) (`liberusoftware/accounting-multi-currency-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-multi-currency.md) · [API plan](../api/accounting-multi-currency.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Transaction/functional/reporting currencies** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transaction/functional/reporting currencies`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Revaluation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `revaluation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Realized/unrealized gains** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `realized/unrealized gains`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Historical rates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `historical rates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [MultiCurrencyFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency-filament/src/MultiCurrencyFilamentPlugin.php) · [MultiCurrencyFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency-filament/src/MultiCurrencyFilamentServiceProvider.php) · [ListRevaluations.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency-filament/src/Resources/Pages/ListRevaluations.php) · [RevaluationResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency-filament/src/Resources/RevaluationResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CurrencyQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Queries/CurrencyQuery.php) | `public function rates(?int $teamId = null, ?string $from = null, ?string $to = null, int $perPage = 25): LengthAwarePaginator`<br>`public function revaluations(?int $teamId = null): LengthAwarePaginator`<br>`public function report(RevaluationRun $run): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureCurrency.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Actions/ConfigureCurrency.php) | `public function handle(array $attributes): CurrencyProfile` |
| [CreateRevaluation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Actions/CreateRevaluation.php) | `public function handle(array $attributes, array $positions): RevaluationRun` |
| [RecordExchangeRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Actions/RecordExchangeRate.php) | `public function handle(array $attributes): ExchangeRate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CurrencyProfile.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/CurrencyProfile.php) | `team_id`, `scope_ref`, `currency`, `role`, `is_active`, `metadata` |
| [CurrencyReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/CurrencyReconciliation.php) | `run_id`, `reference_type`, `reference_id`, `expected_gain_loss`, `actual_gain_loss`, `variance`, `status`, `external_ref`, `notes`, `metadata` |
| [ExchangeRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/ExchangeRate.php) | `team_id`, `from_currency`, `to_currency`, `rate_date`, `rate`, `source`, `rate_type`, `is_historical`, `metadata` |
| [RevaluationPosition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/RevaluationPosition.php) | `run_id`, `reference_type`, `reference_id`, `currency`, `foreign_amount`, `book_rate`, `closing_rate`, `book_value`, `closing_value`, `gain_loss`, `gain_status`, `metadata` |
| [RevaluationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/RevaluationRun.php) | `team_id`, `run_ref`, `scope_ref`, `as_of_date`, `functional_currency`, `status`, `source_hash`, `realized_gain`, `realized_loss`, `unrealized_gain`, `unrealized_loss`, `summary`, `failure_message`, `requested_by`, `posted_by`, `posted_at`, `metadata` |
| [Currency.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency-api/src/Models/Currency.php) | `code`, `name`, `symbol`, `is_default` |
<!-- layer-implementation-plan:end -->
