# Cash Coding React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cash-coding). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-cash-coding-react-native
**Matching core package:** module-accounting-cash-coding ([implementation](../core/cash-coding.md))
**Matching API package:** module-accounting-cash-coding-api ([contract](../api/cash-coding.md))

## Implementation plan

This adapter presents Cash Coding for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Cash Coding API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/cash-coding.md), and [API module](../api/cash-coding.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `cash-coding`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cash-coding.md)) |
| Capability React Native module skeleton | [`module-accounting-cash-coding-react-native`](https://github.com/liberusoftware/module-accounting-cash-coding-react-native) (`@liberusoftware/module-accounting-cash-coding-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **High-volume statement coding** | Progressive mobile list/detail/sheet flow for `high-volume statement coding` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Bulk rules** | Progressive mobile list/detail/sheet flow for `bulk rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tax/dimensions** | Progressive mobile list/detail/sheet flow for `tax/dimensions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Payee creation policy** | Progressive mobile list/detail/sheet flow for `payee creation policy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Review** | Progressive mobile list/detail/sheet flow for `review` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Posting** | Progressive mobile list/detail/sheet flow for `posting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Undo constraints** | Progressive mobile list/detail/sheet flow for `undo constraints` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CashCodingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Queries/CashCodingQuery.php) | `public function forTeam(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCashCodingBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Actions/CreateCashCodingBatch.php) | `public function handle(array $attributes): CashCodingBatch` |
| [TransitionCashCodingBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Actions/TransitionCashCodingBatch.php) | `public function review(CashCodingBatch $batch, ?int $actor = null): CashCodingBatch`<br>`public function post(CashCodingBatch $batch, ?int $actor = null): CashCodingBatch`<br>`public function undo(CashCodingBatch $batch, string $reason): CashCodingBatch` |
| [CashCodingPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding-api/src/Policies/CashCodingPolicy.php) | `public function viewAny($user): bool`<br>`public function view($user, CashCodingBatch $batch): bool`<br>`public function create($user): bool`<br>`public function update($user, CashCodingBatch $batch): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CashCodingBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding/src/Models/CashCodingBatch.php) | `team_id`, `reference`, `status`, `lines`, `payee_creation_policy`, `total_amount`, `currency`, `created_by`, `reviewed_by`, `posted_by`, `undo_reason`, `posted_at`, `undone_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CashCodingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding-api/src/Http/Controllers/CashCodingController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateCashCodingBatch $action): CashCodingResource`<br>`public function show(string $batch): CashCodingResource`<br>`public function review(string $batch, TransitionCashCodingBatch $action): CashCodingResource`<br>`public function post(string $batch, TransitionCashCodingBatch $action): CashCodingResource`<br>`public function undo(Request $request, string $batch, TransitionCashCodingBatch $action): CashCodingResource` |

**Observed route declarations:**

[modules/accounting-cash-coding-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-coding-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/cash-coding')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [CashCodingController::class, 'index'])->middleware('ability:accounting.cash-coding.read');
Route::post('/', [CashCodingController::class, 'store'])->middleware('ability:accounting.cash-coding.write');
Route::get('/{batch}', [CashCodingController::class, 'show'])->middleware('ability:accounting.cash-coding.read');
Route::post('/{batch}/review', [CashCodingController::class, 'review'])->middleware('ability:accounting.cash-coding.write');
Route::post('/{batch}/post', [CashCodingController::class, 'post'])->middleware('ability:accounting.cash-coding.write');
Route::post('/{batch}/undo', [CashCodingController::class, 'undo'])->middleware('ability:accounting.cash-coding.write');
```
<!-- layer-implementation-plan:end -->
