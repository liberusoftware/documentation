# Accounting: Forecasts Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#forecasts). Observed identity: [`liberusoftware/module-accounting-forecasts-filament`](../../../modules/source/liberusoftware--module-accounting-forecasts-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-forecasts-filament`  
**Matching domain module:** `accounting-forecasts`  
**Application:** Accounting  
**Source feature:** [Forecasts](../features/forecasts.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-forecasts` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Driver/manual forecasts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Scenarios:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rolling periods:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Actual replacement:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Assumptions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Variance:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-forecasts-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `driver-manual-forecasts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `scenarios`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rolling-periods`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `actual-replacement`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `assumptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `variance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-forecasts` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-forecasts-filament`](https://github.com/liberusoftware/module-accounting-forecasts-filament) (`liberusoftware/accounting-forecasts-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/forecasts.md) · [API plan](../api/forecasts.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Driver/manual forecasts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `driver/manual forecasts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Scenarios** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `scenarios`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rolling periods** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rolling periods`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Actual replacement** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `actual replacement`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Assumptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `assumptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Variance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `variance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ForecastsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts-filament/src/ForecastsFilamentPlugin.php) · [ForecastsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts-filament/src/ForecastsFilamentServiceProvider.php) · [ForecastResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts-filament/src/Resources/ForecastResource.php) · [ListForecasts.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts-filament/src/Resources/Pages/ListForecasts.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ForecastQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Queries/ForecastQuery.php) | `public function paginate(?int $teamId = null, ?ForecastStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function variance(Forecast $forecast): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddForecastAssumption.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/AddForecastAssumption.php) | `public function handle(Forecast $forecast, array $attributes): ForecastAssumption` |
| [AddForecastLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/AddForecastLine.php) | `public function handle(Forecast $forecast, array $a): ForecastLine` |
| [CreateForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/CreateForecast.php) | `public function handle(array $a): Forecast` |
| [CreateForecastPeriods.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/CreateForecastPeriods.php) | `public function handle(Forecast $forecast, ?string $startsOn = null): array` |
| [DecideForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/DecideForecast.php) | `public function handle(Forecast $forecast, string $actor, bool $approved, ?string $comment = null): Forecast` |
| [ReplaceActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/ReplaceActual.php) | `public function handle(Forecast $forecast, array $a): ForecastActual` |
| [SubmitForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/SubmitForecast.php) | `public function handle(Forecast $forecast): Forecast` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Forecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/Forecast.php) | `team_id`, `forecast_ref`, `name`, `currency`, `method`, `status`, `base_period`, `horizon_periods`, `scenario_ref`, `metadata` |
| [ForecastActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastActual.php) | `forecast_id`, `line_id`, `period_ref`, `actual_value`, `source_ref`, `replaced_at`, `metadata` |
| [ForecastApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastApproval.php) | `forecast_id`, `actor_ref`, `approved`, `comment`, `decided_at`, `metadata` |
| [ForecastAssumption.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastAssumption.php) | `forecast_id`, `assumption_ref`, `name`, `value`, `unit`, `source`, `effective_from`, `effective_to`, `metadata` |
| [ForecastLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastLine.php) | `forecast_id`, `period_ref`, `account_ref`, `dimension_ref`, `description`, `driver_ref`, `forecast_value`, `actual_value`, `variance_value`, `metadata` |
| [ForecastPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastPeriod.php) | `forecast_id`, `period_ref`, `starts_on`, `ends_on`, `status`, `is_rolling`, `metadata` |
<!-- layer-implementation-plan:end -->
