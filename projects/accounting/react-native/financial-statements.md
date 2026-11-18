# Financial Statements React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#financial-statements). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-financial-statements-react-native
**Matching core package:** module-accounting-financial-statements ([implementation](../core/financial-statements.md))
**Matching API package:** module-accounting-financial-statements-api ([contract](../api/financial-statements.md))

## Implementation plan

This adapter presents Financial Statements for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Financial Statements API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/financial-statements.md), and [API module](../api/financial-statements.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `financial-statements`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/financial-statements.md)) |
| Capability React Native module skeleton | [`module-accounting-financial-statements-react-native`](https://github.com/liberusoftware/module-accounting-financial-statements-react-native) (`@liberusoftware/module-accounting-financial-statements-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Profit and loss** | Progressive mobile list/detail/sheet flow for `profit and loss` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Balance sheet** | Progressive mobile list/detail/sheet flow for `balance sheet` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cash flow** | Progressive mobile list/detail/sheet flow for `cash flow` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Changes in equity** | Progressive mobile list/detail/sheet flow for `changes in equity` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Comparative periods** | Progressive mobile list/detail/sheet flow for `comparative periods` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Dimensions** | Progressive mobile list/detail/sheet flow for `dimensions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Drill-through** | Progressive mobile list/detail/sheet flow for `drill-through` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
