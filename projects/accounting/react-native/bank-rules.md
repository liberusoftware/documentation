# Bank Rules React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#bank-rules). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-bank-rules-react-native
**Matching core package:** module-accounting-bank-rules ([implementation](../core/bank-rules.md))
**Matching API package:** module-accounting-bank-rules-api ([contract](../api/bank-rules.md))

## Implementation plan

This adapter presents Bank Rules for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Bank Rules API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/bank-rules.md), and [API module](../api/bank-rules.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `bank-rules`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/bank-rules.md)) |
| Capability React Native module skeleton | [`module-accounting-bank-rules-react-native`](https://github.com/liberusoftware/module-accounting-bank-rules-react-native) (`@liberusoftware/module-accounting-bank-rules-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Payee/text/amount/account conditions** | Progressive mobile list/detail/sheet flow for `payee/text/amount/account conditions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Split/category/tax/dimension actions** | Progressive mobile list/detail/sheet flow for `split/category/tax/dimension actions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Priority** | Progressive mobile list/detail/sheet flow for `priority` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Suggestions/automation** | Progressive mobile list/detail/sheet flow for `suggestions/automation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Testing** | Progressive mobile list/detail/sheet flow for `testing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **History** | Progressive mobile list/detail/sheet flow for `history` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [BankRuleQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Queries/BankRuleQuery.php) | `public function forTeam(int $teamId): Builder`<br>`public function matching(int $teamId, array $transaction): array`<br>`public function matches(array $conditions, array $transaction): bool` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordBankRuleDecision.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Actions/RecordBankRuleDecision.php) | `public function handle(BankRule $rule, string $transactionReference, bool $matched, string $outcome, array $actionsApplied = [], ?string $actorReference = null): BankRuleHistory` |
| [SaveBankRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Actions/SaveBankRule.php) | `public function handle(array $attributes, ?BankRule $rule = null): BankRule` |
| [TestBankRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Actions/TestBankRule.php) | `public function __construct(private readonly BankRuleQuery $query)`<br>`public function handle(BankRule $rule, array $transaction): array` |
| [BankRulesPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules-api/src/Policies/BankRulesPolicy.php) | `public function viewAny($user): bool`<br>`public function view($user, BankRule $rule): bool`<br>`public function create($user): bool`<br>`public function update($user, BankRule $rule): bool`<br>`public function delete($user, BankRule $rule): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BankRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Models/BankRule.php) | `team_id`, `name`, `priority`, `enabled`, `conditions`, `actions`, `automation_mode`, `metadata` |
| [BankRuleHistory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules/src/Models/BankRuleHistory.php) | `team_id`, `rule_id`, `transaction_reference`, `outcome`, `matched`, `actions_applied`, `actor_reference`, `created_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [BankRuleController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules-api/src/Http/Controllers/BankRuleController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, SaveBankRule $action): BankRuleResource`<br>`public function show(string $rule): BankRuleResource`<br>`public function update(Request $request, string $rule, SaveBankRule $action): BankRuleResource`<br>`public function destroy(string $rule): mixed`<br>`public function test(Request $request, string $rule, TestBankRule $action): mixed`<br>`public function history(string $rule): mixed` |

**Observed route declarations:**

[modules/accounting-bank-rules-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-rules-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/bank-rules')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [BankRuleController::class, 'index'])->middleware('ability:accounting.bank-rules.read');
Route::post('/', [BankRuleController::class, 'store'])->middleware('ability:accounting.bank-rules.write');
Route::get('/{rule}', [BankRuleController::class, 'show'])->middleware('ability:accounting.bank-rules.read');
Route::patch('/{rule}', [BankRuleController::class, 'update'])->middleware('ability:accounting.bank-rules.write');
Route::delete('/{rule}', [BankRuleController::class, 'destroy'])->middleware('ability:accounting.bank-rules.write');
Route::post('/{rule}/test', [BankRuleController::class, 'test'])->middleware('ability:accounting.bank-rules.read');
Route::get('/{rule}/history', [BankRuleController::class, 'history'])->middleware('ability:accounting.bank-rules.read');
```
<!-- layer-implementation-plan:end -->
