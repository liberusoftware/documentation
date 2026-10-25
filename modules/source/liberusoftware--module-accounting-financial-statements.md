# liberusoftware/module-accounting-financial-statements: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Profit and loss, balance sheet, cash flow, equity, comparative, dimensional, and drill-through statements.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-financial-statements](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-financial-statements`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-financial-statements` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-financial-statements` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\FinancialStatements\\FinancialStatementsServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\FinancialStatements\\FinancialStatementsServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/module.json).

**Declared capabilities:** accounting.financial-statements

**Declared features:** Profit and loss, Balance sheet, Cash flow, Changes in equity, Comparative periods, Dimensions, Drill-through

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-accounting-chart-of-accounts` | `^1.0` |
| `liberusoftware/module-accounting-core` | `^1.0` |
| `liberusoftware/module-accounting-general-ledger` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\FinancialStatements\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-accounting-chart-of-accounts": "^1.0", "liberusoftware/module-accounting-core": "^1.0", "liberusoftware/module-accounting-general-ledger": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/StatementQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/src/Queries/StatementQuery.php) | `public function profitAndLoss(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function balanceSheet(int $bookId, string $asOf, ?array $dimensions = null): array`<br>`public function cashFlow(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function changesInEquity(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function comparative(int $bookId, string $start, string $end, string $compareStart, string $compareEnd, ?array $dimensions = null): array`<br>`public function drillThrough(int $bookId, int $accountId, string $start, string $end, ?array $dimensions = null): array` |

Other non-legacy PHP sources: [src/Enums/StatementType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/src/Enums/StatementType.php) · [src/Exceptions/InvalidStatementRequest.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/src/Exceptions/InvalidStatementRequest.php) · [src/FinancialStatementsServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/src/FinancialStatementsServiceProvider.php).

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

[src/Enums/StatementType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/src/Enums/StatementType.php): `ProfitAndLoss = 'profit_and_loss'`, `BalanceSheet = 'balance_sheet'`, `CashFlow = 'cash_flow'`, `ChangesInEquity = 'changes_in_equity'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
