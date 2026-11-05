# liberusoftware/module-accounting-cash-flow-forecasting: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Accounting cash-flow forecasting domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-cash-flow-forecasting](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-cash-flow-forecasting`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-cash-flow-forecasting` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-cash-flow-forecasting` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\CashFlowForecasting\\CashFlowForecastingServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\CashFlowForecasting\\CashFlowForecastingServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/module.json).

**Declared capabilities:** accounting.cash-flow-forecasting

**Declared features:** Direct forecast, Opening cash, Receivable and payable timing, Recurring items, Scenarios and assumptions, Variance and confidence

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\CashFlowForecasting\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AddForecastItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/AddForecastItem.php) | `public function receivable(CashFlowForecast $forecast, array $item): CashFlowForecast`<br>`public function payable(CashFlowForecast $forecast, array $item): CashFlowForecast`<br>`public function recurring(CashFlowForecast $forecast, array $item): CashFlowForecast` |
| [src/Actions/CreateCashFlowForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/CreateCashFlowForecast.php) | `public function handle(array $attributes): CashFlowForecast` |
| [src/Actions/SetForecastScenario.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/SetForecastScenario.php) | `public function handle(CashFlowForecast $forecast, array $scenario): CashFlowForecast` |
| [src/Actions/UpdateCashFlowForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/UpdateCashFlowForecast.php) | `public function handle(CashFlowForecast $forecast, array $data): CashFlowForecast` |
| [src/Queries/CashFlowForecastQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Queries/CashFlowForecastQuery.php) | `public function forTeam(int $teamId): Collection` |

Other non-legacy PHP sources: [src/CashFlowForecastingServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/CashFlowForecastingServiceProvider.php) · [src/Exceptions/InvalidCashFlowForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Exceptions/InvalidCashFlowForecast.php) · [src/Models/CashFlowForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Models/CashFlowForecast.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_29_000029_create_accounting_cash_flow_forecasts_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/database/migrations/2026_08_29_000029_create_accounting_cash_flow_forecasts_table.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
