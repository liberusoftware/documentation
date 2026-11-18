# Payroll Journals React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payroll-journals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-payroll-journals-react-native
**Matching core package:** module-accounting-payroll-journals ([implementation](../core/payroll-journals.md))
**Matching API package:** module-accounting-payroll-journals-api ([contract](../api/payroll-journals.md))

## Implementation plan

This adapter presents Payroll Journals for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Payroll Journals API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/payroll-journals.md), and [API module](../api/payroll-journals.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `payroll-journals`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/payroll-journals.md)) |
| Capability React Native module skeleton | [`module-accounting-payroll-journals-react-native`](https://github.com/liberusoftware/module-accounting-payroll-journals-react-native) (`@liberusoftware/module-accounting-payroll-journals-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Gross pay** | Progressive mobile list/detail/sheet flow for `gross pay` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Taxes** | Progressive mobile list/detail/sheet flow for `taxes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Deductions** | Progressive mobile list/detail/sheet flow for `deductions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Benefits** | Progressive mobile list/detail/sheet flow for `benefits` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Employer costs** | Progressive mobile list/detail/sheet flow for `employer costs` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Net pay** | Progressive mobile list/detail/sheet flow for `net pay` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Liabilities** | Progressive mobile list/detail/sheet flow for `liabilities` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Allocation** | Progressive mobile list/detail/sheet flow for `allocation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Posting** | Progressive mobile list/detail/sheet flow for `posting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reversal** | Progressive mobile list/detail/sheet flow for `reversal` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Corrections** | Progressive mobile list/detail/sheet flow for `corrections` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PayrollJournalSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Queries/PayrollJournalSummary.php) | `public function forTeam(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Actions/CreatePayrollJournal.php) | `public function handle(array $attributes): PayrollJournal` |
| [PostPayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Actions/PostPayrollJournal.php) | `public function handle(PayrollJournal $journal): PayrollJournal` |
| [ReversePayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Actions/ReversePayrollJournal.php) | `public function handle(PayrollJournal $journal, string $reversalRef): PayrollJournal` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Models/PayrollJournal.php) | `team_id`, `journal_ref`, `payroll_period_start`, `payroll_period_end`, `currency`, `gross_pay`, `taxes`, `deductions`, `benefits`, `employer_costs`, `net_pay`, `liabilities`, `allocation`, `status`, `posted_at`, `reversed_at`, `reversal_ref`, `correction_ref`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PayrollJournalsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals-api/src/Http/Controllers/PayrollJournalsController.php) | `public function index(Request $request): AnonymousResourceCollection`<br>`public function store(Request $request, CreatePayrollJournal $action): JsonResponse`<br>`public function show(Request $request, PayrollJournal $payrollJournal): PayrollJournalResource`<br>`public function post(Request $request, PayrollJournal $payrollJournal, PostPayrollJournal $action): PayrollJournalResource`<br>`public function reverse(Request $request, PayrollJournal $payrollJournal, ReversePayrollJournal $action): PayrollJournalResource`<br>`public function summary(Request $request, PayrollJournalSummary $query): array` |

**Observed route declarations:**

[modules/accounting-payroll-journals-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/payroll-journals')->group(function (): void {
Route::middleware('ability:accounting.payroll-journals.read')->group(function (): void {
Route::get('/', [PayrollJournalsController::class, 'index']);
Route::get('/summary', [PayrollJournalsController::class, 'summary']);
Route::get('/{payrollJournal}', [PayrollJournalsController::class, 'show']);
Route::middleware('ability:accounting.payroll-journals.write')->group(function (): void {
Route::post('/', [PayrollJournalsController::class, 'store']);
Route::post('/{payrollJournal}/post', [PayrollJournalsController::class, 'post']);
Route::post('/{payrollJournal}/reverse', [PayrollJournalsController::class, 'reverse']);
```
<!-- layer-implementation-plan:end -->
