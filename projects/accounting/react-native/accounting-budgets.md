# Accounting Budgets React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-budgets). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-budgets-react-native
**Matching core package:** module-accounting-accounting-budgets ([implementation](../core/accounting-budgets.md))
**Matching API package:** module-accounting-accounting-budgets-api ([contract](../api/accounting-budgets.md))

## Implementation plan

This adapter presents Accounting Budgets for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Budgets API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-budgets.md), and [API module](../api/accounting-budgets.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-budgets`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-budgets.md)) |
| Capability React Native module skeleton | [`module-accounting-budgets-react-native`](https://github.com/liberusoftware/module-accounting-budgets-react-native) (`@liberusoftware/module-accounting-budgets-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Annual/rolling budgets** | Progressive mobile list/detail/sheet flow for `annual/rolling budgets` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Accounts/dimensions/projects** | Progressive mobile list/detail/sheet flow for `accounts/dimensions/projects` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Imports** | Progressive mobile list/detail/sheet flow for `imports` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Versions** | Progressive mobile list/detail/sheet flow for `versions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approvals** | Progressive mobile list/detail/sheet flow for `approvals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Phasing** | Progressive mobile list/detail/sheet flow for `phasing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Actual comparison** | Progressive mobile list/detail/sheet flow for `actual comparison` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Revisions** | Progressive mobile list/detail/sheet flow for `revisions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [BudgetQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Queries/BudgetQuery.php) | `public function paginate(int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddBudgetLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/AddBudgetLine.php) | `public function handle(Budget $budget, array $attributes): BudgetLine` |
| [ApproveBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/ApproveBudget.php) | `public function handle(Budget $budget, int $actorId): Budget` |
| [CreateBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/CreateBudget.php) | `public function handle(array $attributes): Budget` |
| [ReviseBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/ReviseBudget.php) | `public function handle(Budget $budget, array $attributes): Budget` |
| [SubmitBudget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Actions/SubmitBudget.php) | `public function handle(Budget $budget, int $actorId): Budget` |
| [BudgetsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-api/src/Policies/BudgetsPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function create(?object $user): bool`<br>`public function update(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Budget.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Models/Budget.php) | `team_id`, `name`, `period_start`, `period_end`, `currency`, `status`, `version`, `notes`, `metadata`, `submitted_by`, `approved_by`, `approved_at`, `rejected_at` |
| [BudgetLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets/src/Models/BudgetLine.php) | `budget_id`, `account_id`, `project_id`, `dimensions`, `planned_amount`, `phases`, `actual_amount`, `notes` |

| Observed API controller | Handler signatures |
| --- | --- |
| [BudgetsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-api/src/Http/Controllers/BudgetsController.php) | `public function index(Request $request, BudgetQuery $query): mixed`<br>`public function store(Request $request, CreateBudget $action): BudgetResource`<br>`public function show(Request $request, Budget $budget): BudgetResource`<br>`public function addLine(Request $request, Budget $budget, AddBudgetLine $action): BudgetResource`<br>`public function submit(Request $request, Budget $budget, SubmitBudget $action): BudgetResource`<br>`public function approve(Request $request, Budget $budget, ApproveBudget $action): BudgetResource`<br>`public function revise(Request $request, Budget $budget, ReviseBudget $action): BudgetResource` |

**Observed route declarations:**

[modules/accounting-budgets-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-budgets-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/budgets')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [BudgetsController::class, 'index'])->middleware('ability:accounting.budgets.read');
Route::post('/', [BudgetsController::class, 'store'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/submit', [BudgetsController::class, 'submit'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/lines', [BudgetsController::class, 'addLine'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/approve', [BudgetsController::class, 'approve'])->middleware('ability:accounting.budgets.write');
Route::post('/{budget}/revise', [BudgetsController::class, 'revise'])->middleware('ability:accounting.budgets.write');
Route::get('/{budget}', [BudgetsController::class, 'show'])->middleware('ability:accounting.budgets.read');
```
<!-- layer-implementation-plan:end -->
