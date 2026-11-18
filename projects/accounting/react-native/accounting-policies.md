# Accounting Policies React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-policies). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-policies-react-native
**Matching core package:** module-accounting-accounting-policies ([implementation](../core/accounting-policies.md))
**Matching API package:** module-accounting-accounting-policies-api ([contract](../api/accounting-policies.md))

## Implementation plan

This adapter presents Accounting Policies for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Policies API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-policies.md), and [API module](../api/accounting-policies.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-policies`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-policies.md)) |
| Capability React Native module skeleton | [`module-accounting-policies-react-native`](https://github.com/liberusoftware/module-accounting-policies-react-native) (`@liberusoftware/module-accounting-policies-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Effective-dated recognition** | Progressive mobile list/detail/sheet flow for `effective-dated recognition` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Capitalization** | Progressive mobile list/detail/sheet flow for `capitalization` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Depreciation** | Progressive mobile list/detail/sheet flow for `depreciation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **FX** | Progressive mobile list/detail/sheet flow for `fx` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tax** | Progressive mobile list/detail/sheet flow for `tax` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Rounding** | Progressive mobile list/detail/sheet flow for `rounding` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Write-off** | Progressive mobile list/detail/sheet flow for `write-off` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Materiality** | Progressive mobile list/detail/sheet flow for `materiality` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approval rules** | Progressive mobile list/detail/sheet flow for `approval rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PolicyRuleForDate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies/src/Queries/PolicyRuleForDate.php) | `public function handle(int\|string $bookId, PolicyCategory\|string $category, string $key, \DateTimeInterface\|string $date): ?PolicyRule` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SavePolicyRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies/src/Actions/SavePolicyRule.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(?PolicyRule $rule, array $attributes): PolicyRule` |
| [AccountingPoliciesPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies-api/src/Policies/AccountingPoliciesPolicy.php) | `public function viewAny(?Authenticatable $u): bool`<br>`public function view(?Authenticatable $u, PolicyRule $rule): bool`<br>`public function create(?Authenticatable $u): bool`<br>`public function update(?Authenticatable $u, PolicyRule $rule): bool`<br>`public function delete(?Authenticatable $u, PolicyRule $rule): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PolicyRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies/src/Models/PolicyRule.php) | `book_id`, `category`, `key`, `value`, `effective_from`, `effective_until`, `is_active`, `approved_by`, `approved_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PolicyRuleController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies-api/src/Http/Controllers/PolicyRuleController.php) | `public function index(Request $request)`<br>`public function show(string $rule): PolicyRuleResource`<br>`public function store(Request $request, SavePolicyRule $save)`<br>`public function update(Request $request, string $rule, SavePolicyRule $save): PolicyRuleResource`<br>`public function resolve(Request $request, PolicyRuleForDate $resolve)`<br>`public function destroy(string $rule): Response` |

**Observed route declarations:**

[modules/accounting-policies-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-policies-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/accounting-policies')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('policies', [PolicyRuleController::class, 'index'])->middleware('ability:accounting.policies.read');
Route::get('policies/{rule}', [PolicyRuleController::class, 'show'])->middleware('ability:accounting.policies.read');
Route::post('policies', [PolicyRuleController::class, 'store'])->middleware('ability:accounting.policies.write');
Route::get('resolve', [PolicyRuleController::class, 'resolve'])->middleware('ability:accounting.policies.read');
Route::delete('policies/{rule}', [PolicyRuleController::class, 'destroy'])->middleware('ability:accounting.policies.write');
```
<!-- layer-implementation-plan:end -->
