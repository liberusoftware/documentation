# Accounting Year End React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-year-end). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-year-end-react-native
**Matching core package:** module-accounting-accounting-year-end ([implementation](../core/accounting-year-end.md))
**Matching API package:** module-accounting-accounting-year-end-api ([contract](../api/accounting-year-end.md))

## Implementation plan

This adapter presents Accounting Year End for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Year End API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-year-end.md), and [API module](../api/accounting-year-end.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-year-end`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-year-end.md)) |
| Capability React Native module skeleton | [`module-accounting-year-end-react-native`](https://github.com/liberusoftware/module-accounting-year-end-react-native) (`@liberusoftware/module-accounting-year-end-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Final adjustments** | Progressive mobile list/detail/sheet flow for `final adjustments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Retained earnings/roll-forward** | Progressive mobile list/detail/sheet flow for `retained earnings/roll-forward` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Opening balances** | Progressive mobile list/detail/sheet flow for `opening balances` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Statutory/tax handoff** | Progressive mobile list/detail/sheet flow for `statutory/tax handoff` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Lock** | Progressive mobile list/detail/sheet flow for `lock` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Archive** | Progressive mobile list/detail/sheet flow for `archive` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Evidence** | Progressive mobile list/detail/sheet flow for `evidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [YearEndQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Queries/YearEndQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddYearEndAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/AddYearEndAdjustment.php) | `public function handle(YearEndPeriod $period, array $attributes): YearEndAdjustment` |
| [ArchiveYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/ArchiveYearEnd.php) | `public function handle(YearEndPeriod $period): YearEndPeriod` |
| [CloseYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CloseYearEnd.php) | `public function handle(YearEndClose $close, string $closingEntryRef): YearEndClose` |
| [CreateYearEndClose.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CreateYearEndClose.php) | `public function handle(array $attributes): YearEndClose` |
| [CreateYearEndPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CreateYearEndPeriod.php) | `public function handle(array $attributes): YearEndPeriod` |
| [LockYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/LockYearEnd.php) | `public function handle(YearEndPeriod $period, int $actor): YearEndPeriod` |
| [ReopenYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/ReopenYearEnd.php) | `public function handle(YearEndClose $close): YearEndClose` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [YearEndAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndAdjustment.php) | `period_id`, `team_id`, `adjustment_ref`, `amount`, `description`, `journal_ref`, `status`, `evidence` |
| [YearEndClose.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndClose.php) | `team_id`, `fiscal_year`, `period_end`, `retained_earnings_account_ref`, `net_income`, `status`, `closed_at`, `locked_at`, `closing_entry_ref`, `metadata` |
| [YearEndPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndPeriod.php) | `team_id`, `period_ref`, `period_end`, `status`, `retained_earnings`, `opening_balances`, `statutory_handoff`, `evidence`, `locked_by`, `locked_at`, `archived_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [YearEndController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end-api/src/Http/Controllers/YearEndController.php) | `public function index(YearEndQuery $query): JsonResponse`<br>`public function store(Request $request, CreateYearEndPeriod $action): JsonResponse`<br>`public function adjustment(Request $request, string $period, AddYearEndAdjustment $action): JsonResponse`<br>`public function lock(Request $request, string $period, LockYearEnd $action): JsonResponse`<br>`public function archive(Request $request, string $period, ArchiveYearEnd $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-year-end-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/year-end')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.year-end.read')->get('/', [YearEndController::class, 'index']);
Route::middleware('ability:accounting.year-end.write')->group(function (): void {
Route::post('/', [YearEndController::class, 'store']);
Route::post('/{period}/adjustments', [YearEndController::class, 'adjustment']);
Route::post('/{period}/lock', [YearEndController::class, 'lock']);
Route::post('/{period}/archive', [YearEndController::class, 'archive']);
```
<!-- layer-implementation-plan:end -->
