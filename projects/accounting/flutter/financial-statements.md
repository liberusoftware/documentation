# Financial Statements Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#financial-statements). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-financial-statements-flutter
**Matching core package:** module-accounting-financial-statements ([implementation](../core/financial-statements.md))
**Matching API package:** module-accounting-financial-statements-api ([contract](../api/financial-statements.md))

## Implementation plan

This adapter presents Financial Statements for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Financial Statements API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/financial-statements.md), and [API module](../api/financial-statements.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `financial-statements`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-financial-statements-flutter`](https://github.com/liberusoftware/module-accounting-financial-statements-flutter) (`module_accounting_financial_statements_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-financial-statements-dart-mobile`](https://github.com/liberusoftware/module-accounting-financial-statements-dart-mobile) (`module_accounting_financial_statements_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-financial-statements-dart-desktop`](https://github.com/liberusoftware/module-accounting-financial-statements-dart-desktop) (`module_accounting_financial_statements_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/financial-statements.md) · [Core plan](../core/financial-statements.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Profit and loss** | Adaptive mobile cards/sheets for `profit and loss` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `profit and loss` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Balance sheet** | Adaptive mobile cards/sheets for `balance sheet` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `balance sheet` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Cash flow** | Adaptive mobile cards/sheets for `cash flow` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `cash flow` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Changes in equity** | Adaptive mobile cards/sheets for `changes in equity` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `changes in equity` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Comparative periods** | Adaptive mobile cards/sheets for `comparative periods` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `comparative periods` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Dimensions** | Adaptive mobile cards/sheets for `dimensions` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `dimensions` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Drill-through** | Adaptive mobile cards/sheets for `drill-through` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `drill-through` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [StatementQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/src/Queries/StatementQuery.php) | `public function profitAndLoss(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function balanceSheet(int $bookId, string $asOf, ?array $dimensions = null): array`<br>`public function cashFlow(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function changesInEquity(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function comparative(int $bookId, string $start, string $end, string $compareStart, string $compareEnd, ?array $dimensions = null): array`<br>`public function drillThrough(int $bookId, int $accountId, string $start, string $end, ?array $dimensions = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [FinancialStatementsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-api/src/Policies/FinancialStatementsPolicy.php) | `public function view(?Authenticatable $user): bool` |

| Observed API controller | Handler signatures |
| --- | --- |
| [FinancialStatementsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-api/src/Http/Controllers/FinancialStatementsController.php) | `public function profitAndLoss(Request $request, StatementQuery $query): JsonResponse`<br>`public function balanceSheet(Request $request, StatementQuery $query): JsonResponse`<br>`public function cashFlow(Request $request, StatementQuery $query): JsonResponse`<br>`public function equity(Request $request, StatementQuery $query): JsonResponse`<br>`public function comparative(Request $request, StatementQuery $query): JsonResponse`<br>`public function drillThrough(Request $request, StatementQuery $query): JsonResponse` |

**Observed route declarations:**

[modules/accounting-financial-statements-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'ability:accounting.financial-statements.read'])
Route::get('/profit-and-loss', [FinancialStatementsController::class, 'profitAndLoss'])->name('accounting.financial-statements.profit-and-loss');
Route::get('/balance-sheet', [FinancialStatementsController::class, 'balanceSheet'])->name('accounting.financial-statements.balance-sheet');
Route::get('/cash-flow', [FinancialStatementsController::class, 'cashFlow'])->name('accounting.financial-statements.cash-flow');
Route::get('/changes-in-equity', [FinancialStatementsController::class, 'equity'])->name('accounting.financial-statements.changes-in-equity');
Route::get('/comparative', [FinancialStatementsController::class, 'comparative'])->name('accounting.financial-statements.comparative');
Route::get('/drill-through', [FinancialStatementsController::class, 'drillThrough'])->name('accounting.financial-statements.drill-through');
```
<!-- layer-implementation-plan:end -->
